# Using Mailman for yourself

This project is completely clone-friendly but there are a few steps you need to take to set it up for yourself.

## Requirements
Here are some of the requirements for this project:

1) Any operating system (Windows, macOS, etc.)
2) Python >= V3.8.9, click [here to download](https://python.org)
3) The following external libraries that you will need to install using `pip`:
    - Flask: `pip install flask`
    - markdown: `pip install markdown`

And that's it!

## Steps to setting it up
1) Go to Discord and into any server and channel
2) Go to the channel settings > Integrations > Webhooks > Create webhook (name it whatever you like) and copy the webhook URL
3) Clone this [GitHub repository](https://github.com/Prakhar896/Mailman)
4) Open up the cloned folder in any editor (my preference is [VS Code](https://code.visualstudio.com))
5) Create a new file and name it `webhookURL.py`
6) In said file, create a variable called `url` and set it to the webhook URL you just copied. For e.g `url = https://discord.com`

And done! The project is setup and ready to go!

## Running it
If you are on VSC and have the Python extension you can just click the Play button on the top-right and the project will run and a web server will be created.

If not, open up your command prompt (Windows, for macOS its Terminal) and cd (change directory) into the cloned folder. Then type `python main.py`. You should see the output say `Serving Flask app "main" (lazy loading)`

Do note that this will run Mailman locally on your computer and will stop running if your computer goes to sleep. For running it 24/7, you can look for ways to host it on [replit](https://replit.com) for 24 hours without charge using [UptimeRobot](https://uptimerobot.com)