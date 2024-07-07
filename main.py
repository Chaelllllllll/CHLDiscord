import requests

# Your Discord webhook URL
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1241780772210343996/ZCIBOm5rV3xQ9MFVy0R2RcwOHXeAxCcNFp0supY4EQjIs_PbJjfZ7S0cSkal7WrThuFc'

def get_response(prompt_input):
    api_url = 'https://markdevs-api.onrender.com/api/gpt4o'
    data = {'q': prompt_input}

    try:
        response = requests.get(api_url, params=data)
        if response.status_code == 200:
            response_json = response.json()
            if response_json.get('status'):
                return response_json['response']
            else:
                return "Failed to get response from the API."
        else:
            return "Failed to get response from the API."
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def send_to_discord(message):
    data = {
        "content": message
    }
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=data)
        if response.status_code == 204:
            print("Message sent to Discord successfully.")
        else:
            print(f"Failed to send message to Discord: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def main():
    while True:
        prompt_input = input("Enter your prompt (or 'exit' to quit): ")
        if prompt_input.lower() == 'exit':
            break
        response = get_response(prompt_input)
        send_to_discord(response)

if __name__ == "__main__":
    main()
