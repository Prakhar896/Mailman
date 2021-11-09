import requests
author = input("Enter your name: ")
subject = input("Enter the subject of the mail: ")
message = input("Enter the message of the mail: ")
additionalContent = input("Enter additional content, if none, type nil: ")

data = {
    "author": author,
    "subject": subject,
    "message": message,
    "additionalContent": additionalContent
}

url = input("Enter Mailman service send URL: ")

result = requests.post(url, json=data)

try:
    result.raise_for_status()
    print("Mail sent successfully!")
except requests.exceptions.HTTPError as err:
    print("Error: " + str(err))