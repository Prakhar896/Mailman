from flask import Flask, request, jsonify
from config import *
from activation import *
import requests
from datetime import datetime
import mdConverter

app = Flask(__name__)

def fileContent(fileName):
    with open(fileName, 'r') as f:
        f_content = f.read()
        return f_content

def sendWebhookMessage(data):
    dataToSend = {
        'username': 'Mailman'
    }
    # Get current date and time
    now = datetime.now()
    if data["additionalContent"] != "nil":
        dataToSend['content'] = '```ADDITIONAL CONTENT\n---------------\n' + data["additionalContent"] + '```'

    dataToSend["embeds"] = [
        {
            "title": "New Message: " + data["subject"],
            "description": data["message"],
            "color": 15105570,
            "footer": {
                "text": "Message from " + data["from"] + " | " + now.strftime("%Y-%m-%d %H:%M:%S")
            }
        }
    ]

    result = requests.post(url, json=dataToSend)

    try:
        result.raise_for_status()
    except requests.execeptions.HTTPError as e:
        print(e)

@app.route('/')
def index():
    return fileContent('homepage.html')

@app.route('/about')
def about():
    return mdConverter.convert(fileContent('README.md'))

@app.route('/send', methods=['POST'])
def send():
    if request.headers['Content-Type'] != 'application/json':
        return jsonify({'error': 'Invalid content type'}), 400
    for field in ["from", "subject", "message", "additionalContent"]:
        if field not in request.json:
            return jsonify({'error': 'Missing field: ' + field}), 400
    if mailToken != "nil":
        if not 'mailToken' in request.json:
          return jsonify({'error': 'No mail token parameter present when authorisation layer is active. Authorisation for mail failed.'}), 400
        if request.json['mailToken'] != mailToken:
            return jsonify({'error': 'Invalid mail token. Authorisation for mail failed.'}), 400

    sendWebhookMessage(request.json)
    return jsonify({'success': 'Message sent'}), 200

## Service assets
@app.route('/assets/copyright')
def copyright():
    return fileContent('copyright.js')


if __name__ == "__main__":
    # Check activation
    activationCheck = checkForActivation()
    if activationCheck == True:
        print("Mailman is activated!")
    elif activationCheck == False:
        print("MAIN: Mailman is not activated! Triggering copy activation now...")
        print()
        version = None
        if not os.path.isfile(os.path.join(os.getcwd(), 'version.txt')):
            version = input("Pleae enter the version of Mailman you are using: ")
            print()
        else:
            version = open('version.txt', 'r').read()
        try:
            initActivation("djr3x6wd", version)
        except Exception as e:
            print("MAIN: Error occurred in copy activation. Error: {}".format(e))
            print("Aborting boot...")
            sys.exit(1)
    else:
        print("MAIN: This copy's license key needs to be re-verified. Triggering key verification request...")
        print()
        version = None
        if not os.path.isfile(os.path.join(os.getcwd(), 'version.txt')):
            version = input("Pleae enter the version of Mailman you are using: ")
            print()
        else:
            version = open('version.txt', 'r').read()
        try:
            makeKVR("djr3x6wd", version)
        except Exception as e:
            print("MAIN: Error occurred in verifying license key. Error: {}".format(e))
            print("Aborting boot...")
            sys.exit(1)
        

    app.run(host="0.0.0.0", port=8000)