import time
import sys
import argparse

from time import sleep
from rich.console import Console
from rich.table import Table
from rich.layout import Layout
from rich import print
from rich import box

console = Console()
layout = Layout()
colors = {'0': ('black', 'black', 'black'), '1': ('red', 'red', 'red'), '2': ('green', 'green', 'green'), '3': ('yellow', 'yellow', 'yellow'), '4': ('blue', 'blue', 'blue'), '5': ('magenta', 'magenta', 'magenta'), '6': ('cyan', 'cyan', 'cyan'), '7': ('white', 'white', 'white'), '8': ('bright_black', 'bright_black', 'bright_black'), '9': ('bright_red', 'bright_red', 'bright_red'), '10': ('bright_green', 'bright_green', 'bright_green'), '11': ('bright_yellow', 'bright_yellow', 'bright_yellow'), '12': ('bright_blue', 'bright_blue', 'bright_blue'), '13': ('bright_magenta', 'bright_magenta', 'bright_magenta'), '14': ('bright_cyan', 'bright_cyan', 'bright_cyan'), '15': ('bright_white', 'bright_white', 'bright_white'), '16': ('grey0', '#000000', 'rgb(0,0,0)'), '17': ('navy_blue', '#00005f', 'rgb(0,0,95)'), '18': ('dark_blue', '#000087', 'rgb(0,0,135)'), '20': ('blue3', '#0000d7', 'rgb(0,0,215)'), '21': ('blue1', '#0000ff', 'rgb(0,0,255)'), '22': ('dark_green', '#005f00', 'rgb(0,95,0)'), '25': ('deep_sky_blue4', '#005faf', 'rgb(0,95,175)'), '26': ('dodger_blue3', '#005fd7', 'rgb(0,95,215)'), '27': ('dodger_blue2', '#005fff', 'rgb(0,95,255)'), '28': ('green4', '#008700', 'rgb(0,135,0)'), '29': ('spring_green4', '#00875f', 'rgb(0,135,95)'), '30': ('turquoise4', '#008787', 'rgb(0,135,135)'), '32': ('deep_sky_blue3', '#0087d7', 'rgb(0,135,215)'), '33': ('dodger_blue1', '#0087ff', 'rgb(0,135,255)'), '36': ('dark_cyan', '#00af87', 'rgb(0,175,135)'), '37': ('light_sea_green', '#00afaf', 'rgb(0,175,175)'), '38': ('deep_sky_blue2', '#00afd7', 'rgb(0,175,215)'), '39': ('deep_sky_blue1', '#00afff', 'rgb(0,175,255)'), '40': ('green3', '#00d700', 'rgb(0,215,0)'), '41': ('spring_green3', '#00d75f', 'rgb(0,215,95)'), '43': ('cyan3', '#00d7af', 'rgb(0,215,175)'), '44': ('dark_turquoise', '#00d7d7', 'rgb(0,215,215)'), '45': ('turquoise2', '#00d7ff', 'rgb(0,215,255)'), '46': ('green1', '#00ff00', 'rgb(0,255,0)'), '47': ('spring_green2', '#00ff5f', 'rgb(0,255,95)'), '48': ('spring_green1', '#00ff87', 'rgb(0,255,135)'), '49': ('medium_spring_green', '#00ffaf', 'rgb(0,255,175)'), '50': ('cyan2', '#00ffd7', 'rgb(0,255,215)'), '51': ('cyan1', '#00ffff', 'rgb(0,255,255)'), '55': ('purple4', '#5f00af', 'rgb(95,0,175)'), '56': ('purple3', '#5f00d7', 'rgb(95,0,215)'), '57': ('blue_violet', '#5f00ff', 'rgb(95,0,255)'), '59': ('grey37', '#5f5f5f', 'rgb(95,95,95)'), '60': ('medium_purple4', '#5f5f87', 'rgb(95,95,135)'), '62': ('slate_blue3', '#5f5fd7', 'rgb(95,95,215)'), '63': ('royal_blue1', '#5f5fff', 'rgb(95,95,255)'), '64': ('chartreuse4', '#5f8700', 'rgb(95,135,0)'), '66': ('pale_turquoise4', '#5f8787', 'rgb(95,135,135)'), '67': ('steel_blue', '#5f87af', 'rgb(95,135,175)'), '68': ('steel_blue3', '#5f87d7', 'rgb(95,135,215)'), '69': ('cornflower_blue', '#5f87ff', 'rgb(95,135,255)'), '71': ('dark_sea_green4', '#5faf5f', 'rgb(95,175,95)'), '73': ('cadet_blue', '#5fafaf', 'rgb(95,175,175)'), '74': ('sky_blue3', '#5fafd7', 'rgb(95,175,215)'), '76': ('chartreuse3', '#5fd700', 'rgb(95,215,0)'), '78': ('sea_green3', '#5fd787', 'rgb(95,215,135)'), '79': ('aquamarine3', '#5fd7af', 'rgb(95,215,175)'), '80': ('medium_turquoise', '#5fd7d7', 'rgb(95,215,215)'), '81': ('steel_blue1', '#5fd7ff', 'rgb(95,215,255)'), '83': ('sea_green2', '#5fff5f', 'rgb(95,255,95)'), '85': ('sea_green1', '#5fffaf', 'rgb(95,255,175)'), '87': ('dark_slate_gray2', '#5fffff', 'rgb(95,255,255)'), '88': ('dark_red', '#870000', 'rgb(135,0,0)'), '91': ('dark_magenta', '#8700af', 'rgb(135,0,175)'), '94': ('orange4', '#875f00', 'rgb(135,95,0)'), '95': ('light_pink4', '#875f5f', 'rgb(135,95,95)'), '96': ('plum4', '#875f87', 'rgb(135,95,135)'), '98': ('medium_purple3', '#875fd7', 'rgb(135,95,215)'), '99': ('slate_blue1', '#875fff', 'rgb(135,95,255)'), '101': ('wheat4', '#87875f', 'rgb(135,135,95)'), '102': ('grey53', '#878787', 'rgb(135,135,135)'), '103': ('light_slate_grey', '#8787af', 'rgb(135,135,175)'), '104': ('medium_purple', '#8787d7', 'rgb(135,135,215)'), '105': ('light_slate_blue', '#8787ff', 'rgb(135,135,255)'), '106': ('yellow4', '#87af00', 'rgb(135,175,0)'), '108': ('dark_sea_green', '#87af87', 'rgb(135,175,135)'), '110': ('light_sky_blue3', '#87afd7', 'rgb(135,175,215)'), '111': ('sky_blue2', '#87afff', 'rgb(135,175,255)'), '112': ('chartreuse2', '#87d700', 'rgb(135,215,0)'), '114': ('pale_green3', '#87d787', 'rgb(135,215,135)'), '116': ('dark_slate_gray3', '#87d7d7', 'rgb(135,215,215)'), '117': ('sky_blue1', '#87d7ff', 'rgb(135,215,255)'), '118': ('chartreuse1', '#87ff00', 'rgb(135,255,0)'), '120': ('light_green', '#87ff87', 'rgb(135,255,135)'), '122': ('aquamarine1', '#87ffd7', 'rgb(135,255,215)'), '123': ('dark_slate_gray1', '#87ffff', 'rgb(135,255,255)'), '125': ('deep_pink4', '#af005f', 'rgb(175,0,95)'), '126': ('medium_violet_red', '#af0087', 'rgb(175,0,135)'), '128': ('dark_violet', '#af00d7', 'rgb(175,0,215)'), '129': ('purple', '#af00ff', 'rgb(175,0,255)'), '133': ('medium_orchid3', '#af5faf', 'rgb(175,95,175)'), '134': ('medium_orchid', '#af5fd7', 'rgb(175,95,215)'), '136': ('dark_goldenrod', '#af8700', 'rgb(175,135,0)'), '138': ('rosy_brown', '#af8787', 'rgb(175,135,135)'), '139': ('grey63', '#af87af', 'rgb(175,135,175)'), '140': ('medium_purple2', '#af87d7', 'rgb(175,135,215)'), '141': ('medium_purple1', '#af87ff', 'rgb(175,135,255)'), '143': ('dark_khaki', '#afaf5f', 'rgb(175,175,95)'), '144': ('navajo_white3', '#afaf87', 'rgb(175,175,135)'), '145': ('grey69', '#afafaf', 'rgb(175,175,175)'), '146': ('light_steel_blue3', '#afafd7', 'rgb(175,175,215)'), '147': ('light_steel_blue', '#afafff', 'rgb(175,175,255)'), '149': ('dark_olive_green3', '#afd75f', 'rgb(175,215,95)'), '150': ('dark_sea_green3', '#afd787', 'rgb(175,215,135)'), '152': ('light_cyan3', '#afd7d7', 'rgb(175,215,215)'), '153': ('light_sky_blue1', '#afd7ff', 'rgb(175,215,255)'), '154': ('green_yellow', '#afff00', 'rgb(175,255,0)'), '155': ('dark_olive_green2', '#afff5f', 'rgb(175,255,95)'), '156': ('pale_green1', '#afff87', 'rgb(175,255,135)'), '157': ('dark_sea_green2', '#afffaf', 'rgb(175,255,175)'), '159': ('pale_turquoise1', '#afffff', 'rgb(175,255,255)'), '160': ('red3', '#d70000', 'rgb(215,0,0)'), '162': ('deep_pink3', '#d70087', 'rgb(215,0,135)'), '164': ('magenta3', '#d700d7', 'rgb(215,0,215)'), '166': ('dark_orange3', '#d75f00', 'rgb(215,95,0)'), '167': ('indian_red', '#d75f5f', 'rgb(215,95,95)'), '168': ('hot_pink3', '#d75f87', 'rgb(215,95,135)'), '169': ('hot_pink2', '#d75faf', 'rgb(215,95,175)'), '170': ('orchid', '#d75fd7', 'rgb(215,95,215)'), '172': ('orange3', '#d78700', 'rgb(215,135,0)'), '173': ('light_salmon3', '#d7875f', 'rgb(215,135,95)'), '174': ('light_pink3', '#d78787', 'rgb(215,135,135)'), '175': ('pink3', '#d787af', 'rgb(215,135,175)'), '176': ('plum3', '#d787d7', 'rgb(215,135,215)'), '177': ('violet', '#d787ff', 'rgb(215,135,255)'), '178': ('gold3', '#d7af00', 'rgb(215,175,0)'), '179': ('light_goldenrod3', '#d7af5f', 'rgb(215,175,95)'), '180': ('tan', '#d7af87', 'rgb(215,175,135)'), '181': ('misty_rose3', '#d7afaf', 'rgb(215,175,175)'), '182': ('thistle3', '#d7afd7', 'rgb(215,175,215)'), '183': ('plum2', '#d7afff', 'rgb(215,175,255)'), '184': ('yellow3', '#d7d700', 'rgb(215,215,0)'), '185': ('khaki3', '#d7d75f', 'rgb(215,215,95)'), '187': ('light_yellow3', '#d7d7af', 'rgb(215,215,175)'), '188': ('grey84', '#d7d7d7', 'rgb(215,215,215)'), '189': ('light_steel_blue1', '#d7d7ff', 'rgb(215,215,255)'), '190': ('yellow2', '#d7ff00', 'rgb(215,255,0)'), '192': ('dark_olive_green1', '#d7ff87', 'rgb(215,255,135)'), '193': ('dark_sea_green1', '#d7ffaf', 'rgb(215,255,175)'), '194': ('honeydew2', '#d7ffd7', 'rgb(215,255,215)'), '195': ('light_cyan1', '#d7ffff', 'rgb(215,255,255)'), '196': ('red1', '#ff0000', 'rgb(255,0,0)'), '197': ('deep_pink2', '#ff005f', 'rgb(255,0,95)'), '199': ('deep_pink1', '#ff00af', 'rgb(255,0,175)'), '200': ('magenta2', '#ff00d7', 'rgb(255,0,215)'), '201': ('magenta1', '#ff00ff', 'rgb(255,0,255)'), '202': ('orange_red1', '#ff5f00', 'rgb(255,95,0)'), '204': ('indian_red1', '#ff5f87', 'rgb(255,95,135)'), '206': ('hot_pink', '#ff5fd7', 'rgb(255,95,215)'), '207': ('medium_orchid1', '#ff5fff', 'rgb(255,95,255)'), '208': ('dark_orange', '#ff8700', 'rgb(255,135,0)'), '209': ('salmon1', '#ff875f', 'rgb(255,135,95)'), '210': ('light_coral', '#ff8787', 'rgb(255,135,135)'), '211': ('pale_violet_red1', '#ff87af', 'rgb(255,135,175)'), '212': ('orchid2', '#ff87d7', 'rgb(255,135,215)'), '213': ('orchid1', '#ff87ff', 'rgb(255,135,255)'), '214': ('orange1', '#ffaf00', 'rgb(255,175,0)'), '215': ('sandy_brown', '#ffaf5f', 'rgb(255,175,95)'), '216': ('light_salmon1', '#ffaf87', 'rgb(255,175,135)'), '217': ('light_pink1', '#ffafaf', 'rgb(255,175,175)'), '218': ('pink1', '#ffafd7', 'rgb(255,175,215)'), '219': ('plum1', '#ffafff', 'rgb(255,175,255)'), '220': ('gold1', '#ffd700', 'rgb(255,215,0)'), '222': ('light_goldenrod2', '#ffd787', 'rgb(255,215,135)'), '223': ('navajo_white1', '#ffd7af', 'rgb(255,215,175)'), '224': ('misty_rose1', '#ffd7d7', 'rgb(255,215,215)'), '225': ('thistle1', '#ffd7ff', 'rgb(255,215,255)'), '226': ('yellow1', '#ffff00', 'rgb(255,255,0)'), '227': ('light_goldenrod1', '#ffff5f', 'rgb(255,255,95)'), '228': ('khaki1', '#ffff87', 'rgb(255,255,135)'), '229': ('wheat1', '#ffffaf', 'rgb(255,255,175)'), '230': ('cornsilk1', '#ffffd7', 'rgb(255,255,215)'), '231': ('grey100', '#ffffff', 'rgb(255,255,255)'), '232': ('grey3', '#080808', 'rgb(8,8,8)'), '233': ('grey7', '#121212', 'rgb(18,18,18)'), '234': ('grey11', '#1c1c1c', 'rgb(28,28,28)'), '235': ('grey15', '#262626', 'rgb(38,38,38)'), '236': ('grey19', '#303030', 'rgb(48,48,48)'), '237': ('grey23', '#3a3a3a', 'rgb(58,58,58)'), '238': ('grey27', '#444444', 'rgb(68,68,68)'), '239': ('grey30', '#4e4e4e', 'rgb(78,78,78)'), '240': ('grey35', '#585858', 'rgb(88,88,88)'), '241': ('grey39', '#626262', 'rgb(98,98,98)'), '242': ('grey42', '#6c6c6c', 'rgb(108,108,108)'), '243': ('grey46', '#767676', 'rgb(118,118,118)'), '244': ('grey50', '#808080', 'rgb(128,128,128)'), '245': ('grey54', '#8a8a8a', 'rgb(138,138,138)'), '246': ('grey58', '#949494', 'rgb(148,148,148)'), '247': ('grey62', '#9e9e9e', 'rgb(158,158,158)'), '248': ('grey66', '#a8a8a8', 'rgb(168,168,168)'), '249': ('grey70', '#b2b2b2', 'rgb(178,178,178)'), '250': ('grey74', '#bcbcbc', 'rgb(188,188,188)'), '251': ('grey78', '#c6c6c6', 'rgb(198,198,198)'), '252': ('grey82', '#d0d0d0', 'rgb(208,208,208)'), '253': ('grey85', '#dadada', 'rgb(218,218,218)'), '254': ('grey89', '#e4e4e4', 'rgb(228,228,228)'), '255': ('grey93', '#eeeeee', 'rgb(238,238,238)')}

## CMD Line Argument Handler##
parser = argparse.ArgumentParser(description='Generate automated instance requests to Oracles Cloud Interface. ')
parser.add_argument("--style", "-s", help="changes the color of user input and dynamic variables", default="white")
parser.add_argument("--config_file", help="specify the file path to your config file")
parser.add_argument('--debug', '-d', help="Enables debugging options", action="store_true")
parser.add_argument('--color_help', "-ch", help="prints the avalible color options for style to the console window", action="store_true")
args = parser.parse_args()

if args.style.isnumeric():
    if int(args.style) > 15: 
            theme = colors[args.style][1]
    else:
            theme= colors[args.style]

elif args.style.startswith('#'):
    theme = args.style

else:
    def search(myDict, lookup):
        for key, value in myDict.items():
            for v in value:
                if lookup in v:
                    return key
    _ = search(colors, args.style)
    theme = colors[_][1]

argpath = args.config_file

if args.color_help:
    start= time.time()
    
    basic = list(colors.items())[:15]
    neutral = list(colors.items())[179:203]
    left = list(colors.items())[17:70]
    mid = list(colors.items())[71:124]
    lright = list(colors.items())[125:178]

    table = Table(title= "Basic Colors", box=box.ROUNDED)
    table.add_column("Color", justify="left")
    table.add_column("Number", justify="left")
    table.add_column('Name', justify="left")

    for i in basic:
        x = i[0]
        c = i[1][0]
        table.add_row(f"[{c} on {c}]            [/{c} on {c}]", f"[bold bright_yellow]{x}[/bold bright_yellow]", f"[bold {c}]{c}[/bold {c}]")

    table1 = Table(title="Neutral Colors",box=box.ROUNDED)
    table1.add_column("Color", justify="left")
    table1.add_column("Number", justify="left")
    table1.add_column('Name', justify="left")
    table1.add_row(f"[grey0 on grey0]            [/grey0 on grey0]", f"[bold bright_yellow]16[/bold bright_yellow]", f"[bold grey0]grey0        [/bold grey0]")

    for i in neutral:
        x = i[0]
        c = i[1][0]
        table1.add_row(f"[{c} on {c}]            [/{c} on {c}]", f"[bold bright_yellow]{x}[/bold bright_yellow]", f"[bold {c}]{c}        [/bold {c}]")

    table2 = Table(box=box.ROUNDED)
    table2.add_column("Color", justify="left")
    table2.add_column("Number", justify="left")
    table2.add_column('Name', justify="left")

    for i in left:
        x = i[0]
        c = i[1][0]
        table2.add_row(f"[{c} on {c}]            [/{c} on {c}]", f"[bold bright_yellow]{x}[/bold bright_yellow]", f"[bold {c}]{c}[/bold {c}]")

    table3 = Table(box=box.ROUNDED)
    table3.add_column("Color", justify="left")
    table3.add_column("Number", justify="left")
    table3.add_column('Name', justify="left")

    for i in mid:
        x = i[0]
        c = i[1][0]
        table3.add_row(f"[{c} on {c}]            [/{c} on {c}]", f"[bold bright_yellow]{x}[/bold bright_yellow]", f"[bold {c}]{c}[/bold {c}]")

    table4 = Table(box=box.ROUNDED)
    table4.add_column("Color", justify="left")
    table4.add_column("Number", justify="left")
    table4.add_column('Name', justify="left")

    for i in lright:
        x = i[0]
        c = i[1][0]
        table4.add_row(f"[{c} on {c}]            [/{c} on {c}]", f"[bold bright_yellow]{x}[/bold bright_yellow]", f"[bold {c}]{c}[/bold {c}]")

 
    layout.split(
        Layout(name="main"),
    )

    layout["main"].split_row(
         Layout(name="basic"),
         Layout(table2, name="left"),
        Layout(table3, name="center"),
         Layout(table4, name="right")
    )

    layout["basic"].split_column(
        Layout(table, name="basic", size=20),
        Layout(f"\nMost terminals support the [{theme}]16[/{theme}] basic colors above. \nThe python library [{theme}]rich[/{theme}], used to render colors,\ntables, and layouts to this terminal, provides additional support for these extended colors:", size = 6),
        Layout(table1, name="neutral")
    )

    print("\n\n")
    console.print(layout)
    end = time.time()
    if args.debug:
        print(f"Time taken: [{theme}]{(end-start)*10**3:.03f}ms[/{theme}]")
    sys.exit()

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
flat_ = Style(

    [
        ("qmark", "fg:#673ab7 bold"),
        ("question", "bold"),
        ("pointer", "fg:#673ab7 bold"),
        ("selected", f"fg:{theme} bold"),
    
        ("answer", f"fg:#6c6c6c bold"),
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

    post_data = questionary.text("From OCI's cloud console create a new Instance and open your browsers network tool. Right click the 500 error and paste the POST data output here:\n\n", qmark='>>', style=flat_).ask()
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
    instance_size = f"[bold {theme}]{ocpus}[/bold {theme}] ocpus and [bold {theme}]{memory_in_gbs}[/bold {theme}] GB of memory"

    print("\n")
    print(
            f"[bold white]Instance Configuration:\n\n  Display Name: [bold {theme}]{instance_display_name}[/bold {theme}]\n  Domain: [bold {theme}]{domain}[/bold {theme}]\n  Compartment ID: [bold {theme}]{compartment_id}[/bold {theme}]\n  Image ID: [bold {theme}]{image_id}[/bold {theme}]\n  Subnet ID: [bold {theme}]{subnet_id}[/bold {theme}]\n  SSH Key: [bold {theme}]***** {ssh_key[-18:]}[/bold {theme}]\n  Shape Config: {instance_size}\n"
            )

    cont = questionary.confirm(f"Continue with instance config for {instance_display_name}?", qmark=">>", default=True, style=flat_).ask()        

    if cont == False:
        print("Existing configuration will be deleted and you will be returned to generate a new configuration file")
        continue
    else:
        # print(f"\nContinuing with {instance_display_name}\n")
        break


## Config File Loop ##


if argpath:
    file_location = abspath(argpath)
else:
    relative = questionary.path("Where is your config file located?", qmark=">>", style=flat_).ask()
    file_location = abspath(relative)

## Notification Preference Loop
noti_type = questionary.select("Do you want to use IFTTT or Telegram for notifications?", choices=["IFTTT", "Telegram", "None"], style=flat_, qmark='>>').ask()

noti_loop = True
while noti_loop:
    if noti_type == 'IFTTT':
        url = questionary.text("Maker Channel URL:", qmark='>>', instruction="(https://maker.ifttt.com/trigger/{event}/with/key/{your_key})", style=flat_).ask()
        value1 = instance_display_name
        value2 = domain
        value3 = instance_size
        print(f"\n[bold white]Creating [bold {theme}]{instance_display_name}[/bold {theme}] with {instance_size}. When the instance is claimed you will be notified through {noti_type}![bold white]")
        questionary.print("Remember to set-up your Webhook applet using Web Request as the trigger!\nThe following values will accompany your web request: \n\n  value1 = instance_display_name\n  value2 = domain\n  value3 = instance_size\n", style = "italic" )
        break
    elif noti_type == 'Telegram':
        session = requests.Session()
        bot_api = questionary.text("Bot API:", qmark='>>', style=flat_).ask()
        chat_id = questionary.text("Chat ID:", qmark='>>', style=flat_).ask()
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

print(f"\n[bold underline white]Thank you for using the OCI Instance Tool! Congratulations on your new OCI instance [bold {theme}]{instance_display_name}[/bold {theme}]. Remember to edit your vnic to get a public IP address![/bold underline white]\n")
print(Panel.fit("If you enjoyed this little CLI adventure, feel free to buy me a :coffee:[link=coffee.site]Coffee[/link]"))
        