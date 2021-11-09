import requests
author = input("Enter your name: ")
subject = input("Enter the subject of the mail: ")
message = input("Enter the message of the mail: ")
additionalContent = input("Enter additional content, if none, type nil: ")
mailToken = input("Enter recipient mail token (if recipient does not have auth layer, type nil): ")

data = {
    "from": author,
    "subject": subject,
    "message": message,
    "additionalContent": additionalContent
}

if mailToken != "nil":
    data['mailToken'] = mailToken

url = input("Enter Mailman service send URL: ")

result = requests.post(url, json=data, headers={"Content-Type": "application/json"})

try:
    result.raise_for_status()
    print("Mail sent successfully!")
except requests.exceptions.HTTPError as err:
    print("Error: " + str(err))