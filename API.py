from requests import get
from configparser import ConfigParser

config = ConfigParser()

try:
    config.read("cfg/config.cfg")
except Exception as e:
    print(e)

def ReadConfig(value):
    return f"{config['Data'][value]}"

def Get(url):
    headers = {
        "Authorization": ReadConfig('api_key')
    }

    response = get(url, headers=headers)

    # Check response status
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.status_code, response.text)