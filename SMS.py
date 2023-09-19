from twilio.rest import Client

account_sid = '[ACCOUNT SID HERE]'
auth_token = '[AUTH TOKEN HERE]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='[TWILIO PHONE NUMBER]',
  body = '[MESSAGE]',
  to='[PHONE NUMBER]'
)

print(message.sid)