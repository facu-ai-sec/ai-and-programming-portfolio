import requests

WEBHOOK_URL = "DISCORD_WEBHOOK_URL"

message = input("Enter the message: ")

def send_to_discord(webhook, message):
    data = {"content": message}
    response = requests.post(webhook, json=data, timeout=5)

    if response.status_code == 204:
        print("The message was sent successfully")
    else:
        print(f"Error sending the message: {response.status_code}")

send_to_discord(WEBHOOK_URL, message)
