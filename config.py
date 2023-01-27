import os, json, sys
from dotenv import load_dotenv
load_dotenv()

url = ""
if 'WEBHOOK_URL' in os.environ:
    url = os.environ['WEBHOOK_URL']
else:
    print("No WEBHOOK_URL variable is set in the .env file. Aborting.")
    sys.exit(1)

mailToken = "nil"
if 'MailToken' in os.environ:
    mailToken = os.environ['MailToken']