import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

discord_webhook_url = "https://discord.com/api/webhooks/1241780772210343996/ZCIBOm5rV3xQ9MFVy0R2RcwOHXeAxCcNFp0supY4EQjIs_PbJjfZ7S0cSkal7WrThuFc"

def send_to_discord(message):
    payload = {
        "content": message
    }
    try:
        response = requests.post(discord_webhook_url, json=payload)
        response.raise_for_status()
        print("Message sent to Discord")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send message to Discord: {e}")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    prompt_input = data.get('message')
    if prompt_input:
        # Assuming your API endpoint for processing is different, replace with your actual API endpoint
        api_url = 'https://markdevs-api.onrender.com/api/gpt4o'
        try:
            response = requests.get(api_url, params={'q': prompt_input})
            response.raise_for_status()
            data = response.json()
            if data.get('status'):
                send_to_discord(data.get('response'))
            else:
                send_to_discord('Failed to get response from API.')
        except requests.exceptions.RequestException as e:
            send_to_discord('Failed to connect to API.')
            print(f"Error accessing API: {e}")
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)

