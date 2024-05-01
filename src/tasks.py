import http.client
import json
from config import *


def add_device():
    conn = http.client.HTTPSConnection(HTTPS_CONNECTION_ADDR)
    payload = json.dumps({
      "device": {
        "applicationId": APP_ID,
        "description": "SPV Test Device",
        "devEui": "fa41a5fffe666860",
        "deviceProfileId": DEVICE_PROFILE_ID,
        "isDisabled": False,
        "joinEui": "0000000000000000",
        "name": "SPV Test Device POASTMAN",
        "skipFcntCheck": False
      }
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': AUTHORIZATION_TOKEN
    }
    conn.request("POST", "/api/devices", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def delete_device():
    conn = http.client.HTTPSConnection(HTTPS_CONNECTION_ADDR)
    boundary = ''
    payload = ''
    headers = {
        'Authorization': AUTHORIZATION_TOKEN,
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }
    conn.request("DELETE", "/api/devices/fa41a5fffe666860", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def get_device_list():
    conn = http.client.HTTPSConnection(HTTPS_CONNECTION_ADDR)
    payload = ''
    headers = {
        'Authorization': AUTHORIZATION_TOKEN
    }
    conn.request("GET", "/api/devices?limit=5&applicationId=1bad2baa-585a-41cf-9478-d43e8f0ac96a", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def update_device():
    conn = http.client.HTTPSConnection(HTTPS_CONNECTION_ADDR)
    payload = json.dumps({
        "device": {
            "applicationId": APP_ID,
            "deviceProfileId": DEVICE_PROFILE_ID,
            "name": "SPV Test Device POSTMAN updated"
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': AUTHORIZATION_TOKEN
    }
    conn.request("PUT", "/api/devices/fa41a5fffe666860", payload, headers)
