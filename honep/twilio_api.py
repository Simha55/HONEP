import os
from twilio.rest import Client

sid = os.environ['']
token = os.environ['']
client = Client(sid, token)

message = client.messages \
    .create(
         body='Will send the required oxygen cylinders to your hospital as soon as possible',
         from_='+918374711221',
         to='+1916281144681'
     )

print(message.sid)
