import requests
from requests.auth import HTTPBasicAuth


class SMSSender:
    def __int__(self, api_key, secret_key, base_url):
        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = base_url

    def send_sms(self, sender_id, receiver_addr, message):
        url = f"{self.base_url}"
        data = {
            "source_addr": sender_id,
            "encoding": 0,
            "message": message,
            "recipients": [
                {"recipient_id": 1,
                 "dest_addr": receiver_addr
                 }
            ]
        }

        auth = HTTPBasicAuth(self.api_key, self.api_key)
        response = requests.post(url, json=data, auth=auth)

        if response.status_code == 200:
            return True, "SMS sent"
        else:
            return False, f"SMS failed. status code: {response.status_code}, Response: {response.text}"
