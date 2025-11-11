import requests, json, time, uuid

url = "https://chaosdiscord.onrender.com/"  # Đổi thành URL server của bạn

import requests, json

def send_special(name: str):
    data = {"data": {"user": name}}
    response = requests.post(
        url,
        headers={"Content-Type": "application/json"},
        data=json.dumps(data)
    )
    return response.text

try:
    send_special(str(uuid.uuid4()))
except:
    pass