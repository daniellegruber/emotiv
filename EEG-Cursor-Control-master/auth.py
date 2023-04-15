import json
import ssl
from websocket import create_connection

# Initialize the WebSocket object
#receivedData = create_connection("wss://emotivcortex.com:54321", sslopt={"cert_reqs": ssl.CERT_NONE})
receivedData = create_connection("wss://localhost:6868", sslopt={"cert_reqs": ssl.CERT_NONE})


# Send a JSON request to the WebSocket:
# 1) Send data to websocket server using ws.send()
#   a) The data being sent here is a JSON request to the API
#   b) To send it in the string format, we use json.dumps()
# 2) Receive data using ws.recv()

# Authorization request:
# Will generate a token, the key that allows us to execute other requests
receivedData.send(json.dumps({
    "jsonrpc": "2.0",
    "method": "authorize",
    "params": {
        "clientId": "IJ6pOE6OGsy2SVlIxKvh6u9q5kfKpU2ReSmlnWoy",
        "clientSecret": "Mtlp9vqOeNHeYMUwdf7LEzS5UHdxwpXqXmLQ9aA1sbNAcTV4I6ApCuLVATHfw4Z4TjiIX9jG4ciSSkoBf3IUG9wKFW5tcrv5lE3kqT58HF1hfOygMfeFwvNoVkSfhHMz"
    },
    "id": 1
}))


#temp = json.loads(receivedData.recv())
#print(temp)
token = json.loads(receivedData.recv())["result"]["cortexToken"]

print("Hello USER.")
print("\nThe following set of letters is your session token. In order maintain security, do not share this token:\n\n"+str(token))
print("\n\nThis token has been automatically registered as your session token. You may use the headset as a client")
