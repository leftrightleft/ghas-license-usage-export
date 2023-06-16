import requests
import os

admin_token = os.environ.get('ADMIN_TOKEN')

def get_billing(enterprise):
    headers =  {
        "Authorization": f"Bearer {admin_token}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }

    url="https://api.github.com/enterprises/burrito-party/settings/billing/advanced-security"
    response = requests.get(url, headers=self.client.headers)
    
    if response.status_code == 202:
        return response.json()
    else:
        e = f"Response code: {response.status_code()}.  Response: {response.json()}"
        raise Exception(e)

def main():
    response = get_billing()
    print(response)


if __name__ == '__main__':
    main()