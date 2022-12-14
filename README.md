![Oracle](https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)



# OCI Instance Tool

<image src="./assets/banner_logo.png">


Generate automated instance requests to Oracles Cloud Interface. 

Inspired by chacuavip10's [oci_auto](https://github.com/chacuavip10/oci_auto) and supported by these awesome open sourced libraries: [questionary](https://github.com/tmbo/questionary) , [rich](https://github.com/Textualize/rich) , and [requests](https://github.com/psf/requests).

App logo brought to you by an AI who did it's (their?) best.

# Table of Contents
- [OCI Instance Tool](#oci-instance-tool)
- [Table of Contents](#table-of-contents)
- [A Tale of Two Wheels and Why I Reinvented It](#a-tale-of-two-wheels)
- [Pre·req·ui·sites](#prerequisites)
    - <details><summary>Python Libraries</summary>

        - [OCI](#oci)
        - [requests](#requests)
        - [rich](#rich)
        - [questionary](#questionary)
    </details>

    - <details><summary>Notification Options</summary>

        - [IFTTT](#ifttt)
        - [Telegram](#telegram)
    </details>

    - [Creating a Configuration File and Generating an API Key](#creating-a-configuration-file-and-generating-an-api-key)  
- [Using OCI Instance Tool](#using-oci-insatnce-tool)
- [Command Line Arguments](#command-line-arguements)
- [License](#license)
- [Demo](#demo)       


# A Tale of Two Wheels
## A Perfectly Good Wheel
Oracle's cloud offers a really enticing free tier of virtual machine options that boast a mighty *up to* 4 OCPU's and 24 GBs of cloud hosted resources. The difficulty is, these free tier VM's are hard to come by and while Oracle regularly adds more, they never announce before hand. So, claiming these resources when they come available can feel like winning the lottery and submitting these requests manually is an absolute chore.

While scouring the web for solutions to this problem I can across chacuavip10's [oci_auto](https://github.com/chacuavip10/oci_auto). This great little tool, with a little setup, lets you grab a curl command from your browsers network tools and automatically submits new instance requests on your behalf on an interval. While this tool totally suffices and accomplishes what I was looking for, it had a few security flaws I had a hard time with. Mainly, the script stores things like file paths, ssh keys, and other sensitive information in the script and requires the user to edit the source code itself with these parameters. 

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

**Python 3+ is required** and the script will terminate if a lower version is installed.

This tool was written in Windows for Windows. I'm actually not sure how this would function in other CLI's, but if you want to give it a go or fork the project and make a couple changes, be my guest.

You'll need to install the [OCI SDK](https://github.com/oracle/oci-python-sdk), [requests](https://github.com/psf/requests), [rich](https://github.com/Textualize/rich), and [questionary](https://github.com/tmbo/questionary). This can be done [from requirements](#from-requirements) or installed [individually](#python-libraries).

#

## From Requirements

From the root of OCI Instance Tool's directory
```
pip install -r requirements.txt
```
**-OR-**

To upgrade exisiting packages to their required version:
```
pip install --upgrade -r requirements.txt
```

#

## Python Libraries

### **OCI Python SDK**
``` 
python pip install oci
```
### **requests**
```
python pip install requests
```
### **rich**
```
python pip install rich
```
### **questionary**
```
python pip install questionary
```

#
## Creating a Configuration File and Generating an API Key

OCI Instance Tool will need to authenticate and communicate with your Oracle cloud account. Luckily, creating this config file and generating the API key is only a few steps. Oracle recommends [changing the file permissions](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm#two) so only you can view it. 

From OCI's Cloud Console navigate to **`User Settings`**, 
Under **`Resources`**, select **`API Keys`**:

Select **`Add API Key`**
-  Tick `Generate API Key Pair` and then `Download Private Key` (example key provided in demo)
- Click `Add` and save the contents of the text area to a file (example config file provided in demo)
- `Edit` the `[key_file]` line of the config file from the last step with the filepath to your `Private Key`

```
key_file=oci_private_key.pem
```


[Back to top](#oci-instance-tool)

#

## Notification Options

### **IFTTT**
Its probably handy to have your maker url ready in a txt document or something. Setting this up is actually very straight-forward. Create a ***Webhook*** applet that accepts ***web requests***. Once the applet is created you can grab your maker url containing the applet name and key you'll need. Should look somthing like:
```
https://maker.ifttt.com/trigger/{applet}/with/key/{your_key}
```
Be sure the url does not contain `\json\` as a parameter. The following values will accompany your web request:
1. value1 = `instance_display_name`
2. value2 = `domian`
3. value3 = `{ocpus}` ocpus and `{memory_in_gbs}` GB of memory

[Back to top](#oci-instance-tool)

#

### **Telegram**
In order to use Telegram you'll need your `Bot ID` and your `Chat ID` handy. You can follow this tutorial by Man Hay Hong for a more in depth guide [How to create a Telegram Bot](https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e)

- Search `@BotFather` and send a `/start` message
- Send another `/newbot` message
- Save the APIK token, this is your `Bot ID`
- Start a chat with your new bot `/start` and navigate to
```
https://api.telegram.org/bot<yourtoken>/getUpdates
```
- In the json blob is `"id"`, this is your `Chat ID`

[Back to top](#oci-instance-tool)



# Using OCI Insatnce Tool
To run the tool, in cmd, navigate to the folder containing `OCI_Instance_Tool.py`. For an easier experience the folder should also contain your config file and your PEM key file. However, as long as your config file contains the path to your PEM file, this isn't at all necessary. 

Run:
```
python OCI_Instance_Tool.py
```

<span style="color:grey">*Options*: {-h,-s,--config_file,-d,-ch}</span>

The tool will first import all of the required libraries. While this mostly depends on your PC, OCI will take a while to import. Be patient, it isn't stuck.

1. Paste POST data output here:
    * This question only accepts `{json}` and will reject all other text.
2. Confirm the configuration parser correctly identified your request parameters
    * `Display Name`
    * `Domain`
    * `Compartment ID`
    * `Image ID`
    * `Subnet ID`
    * `SSH Key`
    * `Shape Config`
3. ***Optional:*** Enter the filepath to your config file 
    * *You can use `[tab]` to navigate your folders in the cli*
    * Or use `--config_file {path to your file}` at runtime to skip this question
4. Notification preference and notification preference settings
    * Indicate your notification preference
    * This will generate a folloup question asking for your **IFTTT** `Maker URL` or your **Telegram** `Chat Id` and `Bot ID`
5. Once these questions have been answered **OCI Instance Tool** will validate there are no exisiting resources with duplicate display names or configurations that will exceed your free tier resource limits.    

OCI Instance tool will then attempt to claim your instance every thirty seconds until it succeedes. This can take a very, very long time depending on domain availibility. . 

[Back to top](#oci-instance-tool)

## Command Line Arguements
OCI Instance Tool accepts the following arguments at runtime

### Help
```
--help, h 
```

Shows the help page with availible arguments

### Style
```
--Style, -s
```

changes the color scheme of the tool (ex. `-s 155` or `--style dark_olive_green2` would produce <span style="color:#afff5f">colored text!</span>)

### Config_File
```
--config_file
```

Allows you to specify your config file path at runtime. The config location question is an interactive file tree element. This may save time navigating complicated file structures.

### Debug
```
--debug, -d
```
Enables application debug options. This is in development and currently only outputs a runtime when building the color help page

### Color Help
```
--color_help, -ch
```

This is the color help page. This will produce all the availible colors that can be referenced by style using name or number. Rich supports TrueColors and colors not listed here will need to be referenced by their hex code. (beta, expect bugs)

<image src="./assets/rich colors.png">

[Back to top](#oci-instance-tool)

#

## Demo

The demo folder can be referenced for file content, structure, and usage. It contains a demo version of the `OCI Instance Tool`, an example `POST` request json file, and an example `PEM Key` file. Since you'll be generating actual requests to Oracle that contains your sensiticve information, using the demo to get a feel for the adventure could be helpful.

In the `Demo` folder, open `post_example.json` and copy the contents. **It's important this all stays on one line**.

Run: 

```
python OCI_Instance_Tool_Demo.py
```

When promtped, paste the contents of `post_example.json` and hit `[enter]`. 

[Back to top](#oci-instance-tool)

# License

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./License)

Do whatever you want with this, just don't use it to DDOS Oracle, pls.
<hr>
<hr>

[Back to top](#oci-instance-tool)