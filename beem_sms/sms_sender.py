import requests
from requests.auth import HTTPBasicAuth

class SMSSender:
    def __init__(self, api_key, secret_key, base_url):
        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = base_url

    def send_sms(self, source_addr, dest_addr, message):
        url = f"{self.base_url}"

        data = {
            "source_addr": source_addr,
            "encoding": 0,
            "message": message,
            "recipients": [
                {"recipient_id": 1,
                "dest_addr": dest_addr
                }
            ]
        }

        auth = HTTPBasicAuth(self.api_key, self.secret_key)
        response = requests.post(url, json=data, auth=auth)
        if response.status_code == 200:
            message = "SMS sent "
            return message

        else:
            message = f"SMS sending failed. Status code: {response.status_code}, Response: {response.text}"
            return message