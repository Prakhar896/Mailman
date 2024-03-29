# Mailman

Mailman is a project that basically just forwards data it receives in a URL POST Request to a Discord Webhook link and act as a sort of message conveyer.

**NOTICE:** If you are updating Mailman from versions `1.0`, `1.0.1` or `1.0.2` to `1.0.3` or later; you will need to re-configure Mailman to function properly as the configuration procedure has changed in 1.0.3 and above. See [`USAGE.md`](USAGE.md) for more information.

Say for example I wanted to send a message to someone and then I would send a POST request to their Mailman service and they would get the message.
(Yes this is very unconventional and yes I do know Whatsapp, even Discord for that matter, do exist, but I was bored...)

Each POST request should have just one header of `Content-Type` which should be set to `application/json`.

The body of the post request has 4 elements:

1) `from`: This is the name of the author of the message and is compulsory. For e.g `John Appleseed`
2) `subject`: Pretty self-explanatory - the subject of your message.
3) `message`: The main content of your message. This is compulsory and can be however long as you like.
4) `additionalContent`: This is any additional content, such as code or anything else that you would like to add to your message. This is optional, but it does have to be set to `nil` if you are not adding this component.
5) `mailToken`: This is an optional parameter but is required if the person you are sending the message to you has an authorsation layer. Without their mail token, you will not be able to send them a message. If a `mailToken` is required, set this parameter to whatever it is. If it is incorrect, the response will tell you that it is the wrong token and your message was not authorised. You do not need to add this parameter if the recipient does not have a `mailToken` filter.

A sample POST request:
```json
{
  "from": "Apple",
  "subject": "You have been invited to WWDC",
  "message": "Hello there, you look amazing and just because of that we are inviting you to Apple Park on October 18th. See you there!",
  "additionalContent": "nil"
}
```

Alternatively, you can use the [mailSender.py](https://github.com/Prakhar896/Mailman/blob/main/mailSender.py) script to send a message in a more interactive and easier manner.

© 2021 Prakhar Trivedi
