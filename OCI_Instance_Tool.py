import time
from time import sleep

from rich.console import Console

## init Rich Console ##
console = Console(no_color = True, log_path = False)

loading = True
while loading:
    with console.status(f"", spinner='bouncingBall', spinner_style="bold white") as status:
        sleep(.16)
        status.update("Importing literally time itself...")
        from rich import print
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
        import sys
        sleep(.16)
        status.update("Importing oci...")
        import oci

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
print(Panel.fit("\n[bold white]OCI Instance Tool_[i]beta[/i][/bold white][italic] A fork of [link=https://github.com/chacuavip10]chavuavip10's[/link] oci_auto[/italic]\n"
    'Licensed with the [link=https://github.com/tmbo/questionary/blob/master/LICENSE]MIT License[/link]\n'
    "Made with :heart: by [italic]Cory Stanfield[/italic]"))
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

## Resource Validation Loop ##    
val = True
while val:
    with console.status(f"[bold white]Connecting to OCI to validate resources...[/bold white] ", spinner='bouncingBall', spinner_style="bold white") as status:

        # Loading config file
        status.update("[bold white]Loading OCI config and initializing service client...[/bold white]")
        config = oci.config.from_file(f"{file_location}")

        # Initialize service client
        to_launch_instance = oci.core.ComputeClient(config)

        # Check current existing instance(s) in account

        current_instance = to_launch_instance.list_instances(compartment_id=compartment_id)
        response = current_instance.data
        total_ocpus = total_memory = _A1_Flex = 0
        instance_names = []

        if response:
            status.update(f"[bold white]Validating resources...[/bold white] Found {len(response)} exisiting resource(s)")
            sleep(2)
            for instance in response:
                status.update(f"[bold white]Validating resources...[/bold white] {instance.display_name} - {instance.shape} - {int(instance.shape_config.ocpus)} ocpu(s) - {instance.shape_config.memory_in_gbs} GB(s) | State: {instance.lifecycle_state}")
                instance_names.append(instance.display_name)
                if instance.shape == "VM.Standard.A1.Flex" and instance.lifecycle_state not in ("TERMINATING", "TERMINATED"):
                    _A1_Flex += 1
                    total_ocpus += int(instance.shape_config.ocpus)
                    total_memory += int(instance.shape_config.memory_in_gbs)

        else:
            status.update(f"[bold white]Validating resources...[/bold white] No instances found!")
            sleep(2)
        
        # Pre-check to verify total resource of current VM.Standard.A1.Flex (max 4 ocpus/24GB ram)
        status.update("[bold white]Counting availible resources...[/bold white]")
        sleep(2)
        if total_ocpus + ocpus > 4 or total_memory + memory_in_gbs > 24:
            print("[bold red]Total number of requested resources exceeds availible free resources[/bold red]")
            sys.exit()

        # Check for duplicate display name
        if instance_display_name in instance_names:
            print(f"Duplicate display name [bold cyan]{instance_display_name}[/bold cyan] found in existing resources")
            sys.exit()

        status.update(f"[bold white]Counting availible resources...[/bold white] Resource validation succeeded!")
        sleep(2)
        status.update("[bold white]Packaging OCI request...[/bold white]")
        sleep(2)

        # Instance-detail
        instance_detail = oci.core.models.LaunchInstanceDetails(
            metadata={
                "ssh_authorized_keys": ssh_key
            },
            availability_domain=domain,
            shape='VM.Standard.A1.Flex',
            compartment_id=compartment_id,
            display_name=instance_display_name,
            source_details=oci.core.models.InstanceSourceViaImageDetails(
                source_type="image", image_id=image_id),
            create_vnic_details=oci.core.models.CreateVnicDetails(
                assign_public_ip=False, subnet_id=subnet_id, assign_private_dns_record=True),
            agent_config=oci.core.models.LaunchInstanceAgentConfigDetails(
                is_monitoring_disabled=False,
                is_management_disabled=False,
                plugins_config=[oci.core.models.InstanceAgentPluginConfigDetails(
                    name='Vulnerability Scanning', desired_state='DISABLED'), oci.core.models.InstanceAgentPluginConfigDetails(name='Compute Instance Monitoring', desired_state='ENABLED'), oci.core.models.InstanceAgentPluginConfigDetails(name='Bastion', desired_state='DISABLED')]
            ),
            defined_tags={},
            freeform_tags={},
            instance_options=oci.core.models.InstanceOptions(
                are_legacy_imds_endpoints_disabled=False),
            availability_config=oci.core.models.LaunchInstanceAvailabilityConfigDetails(
                recovery_action="RESTORE_INSTANCE"),
            shape_config=oci.core.models.LaunchInstanceShapeConfigDetails(
                ocpus=ocpus, memory_in_gbs=memory_in_gbs)
        )
        
        #initiate notification parameters
        status.update(f"[bold white]Cleaning up a few things...[/bold white]")
        sleep(2)
        requests.session()


    break    
console.log("[bold white]Resource validation and instance request package succeeded! You can minimize this window and grab a :coffee: this could take a little while. Days, this can taske days.[/bold white]\n")

## Main Loop ##
wait_s_for_retry = 30
t = wait_s_for_retry
tries = 0  
to_try = True
while to_try:
    with console.status(f"[bold white]Claiming Instance...[/bold white]", spinner='bouncingBall', spinner_style="bold white") as status:

        def countdown(t):

            while t:
                status.update(f"[bold white]Failed: Retrying in {t}...[/bold white] Latest Response: {e}")
                time.sleep(1)
                t-=1
                if t == 0:
                    break
            t = wait_s_for_retry

        try:
            to_launch_instance.launch_instance(instance_detail)
            to_try = False
            # post to IFTTT
            requests.post(f"{url}?value1={value1}&value2={value2}&value3={value3}")
            session.close()
        except oci.exceptions.ServiceError as e:
            if e.status == 500:
                # Out of host capacity.
                e = "(500) Out of host capacity"
                tries = tries+1
                countdown(int(t))
            elif e.status == 429:
                # TooManyRequests
                e= "(429) Too many requests"
                tries = tries+1
                countdown(int(t))
            elif e.status == 404:
                e ="(404) Not authorized"
                tries = tries+1
                countdown(int(t))    
            else:
                e = "Unexpected error: See logs for more"
                tries = tries+1
                countdown(int(t))
            #time.sleep(wait_s_for_retry)
        except Exception as e:
            e = "Unexpected error: See logs for more"
            tries = tries+1
            countdown(int(t))
            #time.sleep(wait_s_for_retry)
        except KeyboardInterrupt:
            session.close()
            sys.exit()

print(f"\n[bold underline white]Thank you for using the OCI Instance Tool! Congratulations on your new OCI instance [bold cyan]{instance_display_name}[/bold cyan]. Remember to edit your vnic to get a public IP address![/bold underline white]\n")
print(Panel.fit("If you enjoyed this little CLI adventure, feel free to buy me a :coffee:[link=coffee.site]Coffee[/link]"))
        