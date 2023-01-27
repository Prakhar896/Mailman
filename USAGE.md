# Using Mailman for yourself

This project is completely clone-friendly but there are a few steps you need to take to set it up for yourself.

## Table of Contents

- [Requirements](#requirements)
- [Activator](#activator)
    - [How It Works](#how-it-works)
    - [What I Can Do With Activator](#what-i-can-do-with-activator)
- [User notice for updating to `1.0.3` and above](#user-notice-for-updating-to-103-and-above)
- [Steps to setting it up](#steps-to-setting-it-up)
- [Running It](#setting-up-the-webhook)

## Requirements
Here are some of the requirements for this project:

1) Any operating system (Windows, macOS, etc.)
2) Python >= V3.8.9, click [here to download](https://python.org)
3) The following external libraries that you will need to install using `pip`:
    - Flask: `pip install flask`
    - markdown: `pip install markdown`

And that's it!

## Activator

<img src="https://github.com/Prakhar896/ActivatorDocs/blob/main/activatorLogo.png?raw=true" alt="Activator Logo" width="350px">

[Activator](https://github.com/Prakhar896/ActivatorDocs) is a product activation service that activates copies. It also provides users a unified dashboard to manage all of your activated copies across several products that conform to Activator's DRM (Digital Rights Management) process. Mailman is one of these products.

### How It Works

Any copy of Mailman will first need to be activated with Activator. You do not have to do anything on your part; upon boot, if not activated, Mailman will locate the latest Activator server and will activate itself. A `licensekey.txt` file will be downloaded that will contain the license key for the copy. This file will be used to verify the copy's authenticity.

**DO NOT** delete the `licensekey.txt` file. If you do, the copy will be deactivated and will need to be activated again.

Every 14 days, the copy will automatically trigger a license key verification request (KVR) to ensure that the copy is still activated. If the copy is not activated, it will be deactivated and will need to be activated again. (Run the copy code again.)

### What I Can Do With Activator

During copy activation, the activation script generates unique identifiers for the computer it is being run on (called HSN) and for the copy itself (called CSN).

These identifiers are submitted to Activator servers. If an account with the same HSN is found, the CSN is added to the account. If no account is found, a new account is created with the HSN and CSN.

> NOTE: None of your private computer information is divulged in the activation process.

Then, you can log in to Activator using the link provided in the `licensekey.txt` file. You will be able to see all of your activated copies and their CSNs. You can also manage your account, link other HSN accounts as aliases and much more.

> For more information about Activator, see its [documentation](https://github.com/Prakhar896/ActivatorDocs)

## User notice for updating to `1.0.3` and above

In Mailman version `1.0.3`, the way you configure Mailman has been changed.

When you first update, the `config.py` file that previously contained your Discord Webhook URL and Mail Token  (if you added an authorisation layer, it would be the token you set) will be replaced with new code that loads these variables from a `.env` file.

This is done to make it easier for you to update Mailman in the future. You will no longer have to worry about overwriting your configuration file.

What you need to do:

- **Step 1:** Create a new file in the same folder as `main.py` and name it `.env`.
- **Step 2:** In the `.env` file, create a variable called `WEBHOOK_URL` and set it to the Discord Webhook URL you want to receive messages at. For e.g `WEBHOOK_URL=https://discord.com` (no spaces)
- **Step 3:** In the same file, if you want to have a mail token authorisation layer to only receive messages from people you give your token to, set `MailToken` to the token you want to use. For e.g `MailToken=er9g81`. If not, this variable will default to `nil` during boot (no authorisation required).

The setting up documentation below has also been updated for new users of Mailman.

I hope this improves your experience with the product!


## Steps to setting it up
1) Go to Discord and into any server and channel
2) Go to the channel settings > Integrations > Webhooks > Create webhook (name it whatever you like) and copy the webhook URL
3) Clone this [GitHub repository](https://github.com/Prakhar896/Mailman)
4) Open up the cloned folder in any editor (my preference is [VS Code](https://code.visualstudio.com))
5) Create a new file and name it `.env`
6) In said file, create a variable called `WEBHOOK_URL` and set it to the webhook URL you just copied. For e.g `WEBHOOK_URL=https://discord.com` (no spaces)
7) In the same file, if you wish to add a authorisation layer such that only people you give your mail token to can send you messages, you can create a variable called `MailToken` and set it to anything you want. (e.g `MailToken=er9g81`). If not, this variable will default to `nil` (no authorisation required). 

And done! The project is setup and ready to go!

## Running it
If you are on VSC and have the Python extension you can just click the Play button on the top-right and the project will run and a web server will be created.

If not, open up your command prompt (Windows, for macOS its Terminal) and cd (change directory) into the cloned folder. Then type `python main.py`. You should see the output say `Serving Flask app "main" (lazy loading)`

Do note that this will run Mailman locally on your computer and will stop running if your computer goes to sleep. For running it 24/7, you can look for ways to host it on [replit](https://replit.com) for 24 hours without charge using [UptimeRobot](https://uptimerobot.com)