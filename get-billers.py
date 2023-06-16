import requests
import os

admin_token = os.environ.get('ADMIN_TOKEN')
enterprise = os.environ.get('ENTERPRISE_NAME')

def get_billing(enterprise):
    headers =  {
        "Authorization": f"Bearer {admin_token}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }

    url=f"https://api.github.com/enterprises/{enterprise}/settings/billing/advanced-security"
    response = requests.get(url, headers=client.headers)
    
    if response.status_code == 202:
        return response.json()
    else:
        e = f"Response code: {response.status_code()}.  Response: {response.json()}"
        raise Exception(e)

def main():
    response = get_billing(enterprise)
    print(response)


if __name__ == '__main__':
    main()