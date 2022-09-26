import time
import sys
from time import sleep

from rich.console import Console
from rich import print

## init Rich Console ##
console = Console(no_color = True, log_path = False)

from sys import version_info
pv = version_info

loading = True
while loading:
    with console.status(f"", spinner='bouncingBall', spinner_style="bold white") as status:
        status.update("Validating Python version...")
        sleep(2)
        if pv[0] < 3:
            print("[bold red]OCI Instance Tool requires Python 3+!")
            sys.exit()
        else:
            status.update("Validation Pass!")
            sleep(1)
        sleep(.16)
        status.update("Importing literally time itself...")
        sleep(.16)
        status.update("Importing requests...")
        import requests
        sleep(.16)
        status.update("Importing pathlib...")
        import pathlib
        sleep(.16)
        status.update("Importing json...")
        import json
        sleep(.16)
        status.update("Importing questionary...")
        import questionary
        status.update("Importing os...")
        import os
        sleep(.16)
        #status.update("Importing oci...")
        #import oci

        status.update("From pathlib importing path...")
        from pathlib import Path
        sleep(.16)
        status.update("From time importing sandman...")
        status.update("From rich importing panel...")
        from rich.panel import Panel
        sleep(.16)
        status.update("From questionary importing style...")
        from questionary import Style
        sleep(.16)
        status.update("from pathlib importing path...")
        from pathlib import Path
        sleep(.16)
        status.update("from getpass importing getpass...")
        from getpass import getpass
        sleep(.16)
        status.update("From os importing abspath...")
        from os.path import abspath
        sleep(.16)
        status.update("Initializing OCI Instance Tool")
        sleep(2)
    break

## Questionary Style ##
flat_cyan = Style(

    [
        ("qmark", "fg:#673ab7 bold"),
        ("question", "bold"),
        ("pointer", "fg:#673ab7 bold"),
        ("selected", "fg:#2196f3 bold"),
        ("answer", "fg:#2196f3 bold"),
    ]
)


## Welcome Message ##
print(Panel.fit("[bold white]Fork: [/bold white][italic][link=https://github.com/chacuavip10]chavuavip10's[/link] oci_auto[/italic]\n"
    '[bold white]Licensed:[/bold white] [i][link=https://github.com/tmbo/questionary/blob/master/LICENSE]MIT License[/i][/link]\n'
    '[bold white]Made:[/bold white] [i]:heart: [link=https://github.com/Wulf-Steppen?tab=repositories]Wülf-Stëppen[/italic][/link]', title="[bold white]OCI Instance Tool[/bold white]", title_align="left", subtitle="[i][bold white]beta[/bold white]_v.01[/i]", subtitle_align='right'))
print("\n[bold underline white]Welcome to the OCI Instance Tool. This tool transforms POST data into instance configuration values that can be used to automate host creation requests to OCI.[/bold underline white]\n")

## POST Parser Loop
config_loop = True
while config_loop:
    
    instance_display_name = 'displayName'
    compartment_id = 'compartmentId'
    domain = "availabilityDomain"
    image_id = "imageId"
    subnet_id = 'subnetId'
    fssh_key = 'ssh_authorized_keys'
    ocpus = 'ocpus'
    memory_in_gbs = 'memoryInGBs'

    post_data = questionary.text("From OCI's cloud console create a new Instance and open your browsers network tool. Right click the 500 error and paste the POST data output here:\n\n", qmark='>>', style=flat_cyan).ask()
    script_settings = json.loads(post_data)

    if instance_display_name in script_settings:
            instance_display_name = script_settings[instance_display_name]
    else:
         raise SyntaxError(f"JSON missing {instance_display_name}; validate web request intercept")    
    if domain in script_settings:
            domain = script_settings[domain]
    else:
         raise SyntaxError(f"JSON missing {domain}; validate web request intercept")        
    if compartment_id in script_settings:
            compartment_id = script_settings[compartment_id]
    else:
         raise SyntaxError(f"JSON missing {compartment_id}; validate web request intercept")        
    if image_id in script_settings['sourceDetails']:
        image_id = script_settings['sourceDetails'][image_id]
    else:
         raise SyntaxError(f"JSON missing {image_id}; validate web request intercept")    
    if subnet_id in script_settings['createVnicDetails']:
        subnet_id = script_settings['createVnicDetails'][subnet_id]
    else:
         raise SyntaxError(f"JSON missing {subnet_id}; validate web request intercept")    
    if fssh_key in script_settings['metadata']:
        ssh_key = script_settings['metadata'][fssh_key]
    else:
         raise SyntaxError(f"JSON missing {fssh_key}; validate web request intercept")
    if ocpus in script_settings['shapeConfig']:
        ocpus = script_settings['shapeConfig'][ocpus]
    else:
        ocpus = 4
    if memory_in_gbs in script_settings['shapeConfig']:
        memory_in_gbs = script_settings['shapeConfig'][memory_in_gbs]
    else:        
        memory_in_gbs = ocpus*6
    instance_size = f"[bold cyan]{ocpus}[/bold cyan] ocpus and [bold cyan]{memory_in_gbs}[/bold cyan] GB of memory"

    print("\n")
    print(
            f"[bold white]Instance Configuration:\n\n  Display Name: [bold cyan]{instance_display_name}[/bold cyan]\n  Domain: [bold cyan]{domain}[/bold cyan]\n  Compartment ID: [bold cyan]{compartment_id}[/bold cyan]\n  Image ID: [bold cyan]{image_id}[/bold cyan]\n  Subnet ID: [bold cyan]{subnet_id}[/bold cyan]\n  SSH Key: [bold cyan]***** {ssh_key[-18:]}[/bold cyan]\n  Shape Config: {instance_size}\n"
            )

    cont = questionary.confirm(f"Continue with instance config for {instance_display_name}?", qmark=">>", default=True, style=flat_cyan).ask()        

    if cont == False:
        print("Existing configuration will be deleted and you will be returned to generate a new configuration file")
        continue
    else:
        # print(f"\nContinuing with {instance_display_name}\n")
        break


## Config File Loop ## 
relative = questionary.path("Where is your config file located?", qmark=">>", style=flat_cyan).ask()
file_location = abspath(relative)

## Notification Preference Loop
noti_type = questionary.select("Do you want to use IFTTT or Telegram for notifications?", choices=["IFTTT", "Telegram", "None"], style=flat_cyan, qmark='>>').ask()

noti_loop = True
while noti_loop:
    if noti_type == 'IFTTT':
        url = questionary.text("Maker Channel URL:", qmark='>>', instruction="(https://maker.ifttt.com/trigger/{event}/with/key/{your_key})", style=flat_cyan).ask()
        value1 = instance_display_name
        value2 = domain
        value3 = instance_size
        print(f"\n[bold white]Creating [bold cyan]{instance_display_name}[/bold cyan] with {instance_size}. When the instance is claimed you will be notified through {noti_type}![bold white]")
        questionary.print("Remember to set-up your Webhook applet using Web Request as the trigger!\nThe following values will accompany your web request: \n\n  value1 = instance_display_name\n  value2 = domain\n  value3 = instance_size\n", style = "italic" )
        break
    elif noti_type == 'Telegram':
        session = requests.Session()
        bot_api = questionary.text("Bot API:", qmark='>>', style=flat_cyan).ask()
        chat_id = questionary.text("Chat ID:", qmark='>>', style=flat_cyan).ask()
        print(f"Creating {instance_display_name} with {instance_size}. When the instance is claimed you will be notified through {noti_type}!")
        break
    else:
        print(f"Creating {instance_display_name} with {instance_size}")
        break


## Main Loop ##
tries = 0  
task1 = True
while task1:
    with console.status(f"[bold white]Claiming Instance...[/bold white]", spinner='bouncingBall', spinner_style="bold white") as status:
        sleep(5)
        status.update(f"[bold white]Claiming Instance...[/bold white] Latest Response: (500) Out of host capacity")
        tries = tries+1
        sleep(5) 
        status.update(f"[bold white]Claiming Instance...[/bold white] Latest Response: (429) Too many requests", spinner='bouncingBall', spinner_style="bold white")
        tries = tries+1    
        sleep(5)
        console.log(f"[bold white]Instance claimed![/bold white] after {tries} tries")
        break

print(f"\n[bold underline white]Thank you for using the OCI Instance Tool! Congratulations on your new OCI instance [bold cyan]{instance_display_name}[/bold cyan]. Remember to edit your vnic to get a public IP address![/bold underline white]\n")
print(Panel.fit("If you enjoyed this little CLI adventure, feel free to buy me a :coffee:[link=coffee.site]Coffee[/link]"))
        