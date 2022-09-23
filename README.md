
# OCI Instance Tool
![Oracle](https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

Generate automated instance requests to Oracles Cloud Interface. 

Inspired by chacuavip10's [oci_auto](https://github.com/chacuavip10/oci_auto) and supported by these awesome open sourced libraries: [questionary](https://github.com/tmbo/questionary) , [rich_](https://github.com/Textualize/rich) , and [requests](https://github.com/psf/requests).

# Table of Contents
- [OCI Instance Tool](#oci-instance-tool)
- [Table of Contents](#table-of-contents)
- [A Tale of Two Wheels and Why I Reinvented It](#a-tale-of-two-wheels)
- [Pre·req·ui·sites](#prerequisites)
    - <details><summary>Python Libraries</summary>

        - [OCI CLI](#oci-cli)
        - [requests](#requests)
        - [rich](#rich)
        - [questionary](#questionary)
    </details>

    - <details><summary>Notification Options</summary>

        - [IFTTT](#ifttt)
        - [Telegram](#telegram)
    </details>

    - [Generating Config and Saving PEM Key](#generating-config-and-saving-pem-key)  
- [Using OCI Instance Tool](#using-oci-insatnce-tool)
- [License](#license)
- [Demo](#demo)       


# A Tale of Two Wheels
## A Perfectly Good Wheel
Oracle's cloud offers a really enticing free tier of virtual machine options that boast a mighty *up to* 4 OCPU's and 24 GBs of cloud hosted resources. The difficulty is, these free tier VM's are hard to come by and while Oracle regularly adds more, they never announce before hand. So, claiming these resources when they come avalible can feel like winning the lottery and submitting these requests manually is an absolute chore.

While scouring the web for solutions to this problem I can accross chacuavip10's [oci_auto](https://github.com/chacuavip10/oci_auto). This great little tool, with a little setup, lets you grab a curl command from your browsers netwrok tools and automatically submits new instance requests on your behalf on an interval. Whle this tool totally suffices and accomplishes what I was looking for, it had a few security flaws I had a hard time with. Mainly, the script stores things like file paths, ssh keys, and other sensitive information in the script and requires the user to edit the source code itself with these parameters. 

In addition, you had to manually pull instance parameters from the curl command. Again, great tool and totally suffices, but I'm like reeeeeally lazy when it comes to this stuff so I set out to improve on this concept and reduce the number of steps.

## Two Wheels Make a Bike
This tool is a total redesign of it's inspiration. The tool itself accepts JSON as an input and will automatically parse the instance values from the original POST request that failed in OCI. For bonus points I made file paths agnostic, threw in some styling, added an additional notification channel, and made the experience feel a little more like an adventure. 

In the words of the great why the lucky stiff
> No. Please don’t puzzle over it. You don’t need to do anything with the onion. Set the onion aside and let *it* do something *with* you.

Except OCI Instance Tool is the onion and you are... well you know, you.

Also 
> I wonder where he went with all those balloons. That crazy dog must have looked like a party with legs.

Wise words indeed.

[Back to top](#oci-instance-tool)
# Pre·req·ui·sites

This tool was written in Windows for Windows. I'm actually not sure how this would function in other CLI's, but if you want to give it a go or fork the project and make a couple changes, be my guest.

You'll need to install the [OCI CLI](https://github.com/oracle/oci-cli), [requests](https://github.com/psf/requests), [rich_](https://github.com/Textualize/rich), and [questionary](https://github.com/tmbo/questionary).

## OCI CLI
``` 
python pip install oci
```
## requests
```
python pip install requests
```
## rich
```
python pip install rich
```
## questionary
```
python pip install questionary
```
## Generating Config and Saving PEM Key

This artricle by Tri Ngyuen [How to create a free Oracle VPS with Python script (Out of capacity)?](https://www.hintdesk.com/2022/01/15/how-to-create-a-free-oracle-vps-with-python-script-out-of-capacity/) is a great resource for creating API Keys and generating these files.

[Back to top](#oci-instance-tool)

## IFTTT
Its probably handy to have your maker url handy in a txt document or something. Setting this up is actually very straight-forward. Create a ***Webhook*** applet that accepts ***web requests***. Once the applet is created you can grab your maker url containing the applet name and key you'll need. Should look somthing like
```
https://maker.ifttt.com/trigger/{applet}/with/key/{your_key}
```
Be sure the url does not contain `\json\` as a parameter. The following values will accompany your web request:
1. value1 = `instance_display_name`
2. value2 = `domian`
3. value3 = `{ocpus}` ocpus and `{memory_in_gbs}` GB of memory

[Back to top](#oci-instance-tool)

## Telegram
In order to use Telegram you'll need your `Bot ID` and your `Chat ID` handy.

[Back to top](#oci-instance-tool)

# Using OCI Insatnce Tool
To run the tool, in cmd, navigate to the folder containing `OCI_Instance_Tool.py`. For an easier experience the folder should also contain your config file and your PEM key file. However, as long as your config file contains the path to your PEM file, this isn't at all necessary. 

Run:
```
python OCI_Instance_Tool.py
```

Once started, the tool will ask you a few questions and as long as you have your ducks in a row this part should be easy.

* Paste POST data output
* Confirm Instance Configuartion is correct
* Enter the filepath to your config file 
    * *you can use `[tab]` to navigate your folders in the cli*
* Notification preference and notification preference settings

And you're off. The tool will first validate you have enough free resources left in your account and no exisiting instances with the same display name, package your instance request, and start trying to claim instamces on your behalf. 

[Back to top](#oci-instance-tool)

## Demo

The demo folder can be referenced for file content, structure, and usage. It contains a demo version of the `OCI Instance Tool`, an example `POST` request json file, and an example `PEM Key` file. Since you'll be generating actual requests to Oracle that contains your sensiticve information, using the demo to get a feel for the adventure could be helpful.

# License

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)

Do whatever you want with this, just don't use it to DDOS Oracle, pls.
<hr>
<hr>

[Back to top](#oci-instance-tool)