from twilio.rest import Client

# Go to setting toggle for credentials
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:TWILIO PHONE NUMBER HERE',
    body='I Hate Java!',
    to='whatsapp:YOUR PHONE NUMBER HERE'
)

print(message.sid)