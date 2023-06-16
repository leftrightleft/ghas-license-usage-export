import requests
import os
import json

admin_token = os.environ.get('ADMIN_TOKEN')

enterprise = os.environ.get('ENTERPRISE_NAME')

def get_billing(enterprise):
    headers =  {
        "Authorization": f"Bearer {admin_token}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }

    url=f"https://api.github.com/enterprises/{enterprise}/settings/billing/advanced-security?per-page=100"
    response = requests.get(url, headers=headers)
    repos = response.json()
    # build paging 
    while 'next' in response.links.keys():
        response = requests.get(response.links['next']['url'], headers=headers)
        page_repos = response.json()
        repos['repositories'].extend(page_repos['repositories'])

    return repos

def main():
    response = get_billing(enterprise)
    with open('GHAS-committers.json', 'w') as f:
        json.dump(response, f)


if __name__ == '__main__':
    main()