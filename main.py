import requests
import json

# Your Discord webhook URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/1241780772210343996/ZCIBOm5rV3xQ9MFVy0R2RcwOHXeAxCcNFp0supY4EQjIs_PbJjfZ7S0cSkal7WrThuFc'

# API endpoint
API_URL = 'https://markdevs-api.onrender.com/api/gpt4o'

def get_api_response(prompt_input):
    data = {'q': prompt_input}
    try:
        response = requests.get(API_URL, params=data)
        if response.status_code == 200:
            response_json = response.json()
            if response_json.get('status'):
                return response_json['response']
            else:
                return "Failed to get response."
        else:
            return "Failed to get response."
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def send_to_discord(message):
    data = {
        "content": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(WEBHOOK_URL, data=json.dumps(data), headers=headers)
    if response.status_code != 204:
        print(f"Failed to send message to Discord: {response.status_code} {response.text}")

def main():
    while True:
        prompt_input = input("Enter your prompt (or 'exit' to quit): ")
        if prompt_input.lower() == 'exit':
            break
        response = get_api_response(prompt_input)
        send_to_discord(response)

if __name__ == "__main__":
    main()
