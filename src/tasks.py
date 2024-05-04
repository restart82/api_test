import http.client
import json
from config import *


def add_device(dev_id, name):
    conn = http.client.HTTPSConnection(HTTPS_CONNECTION_ADDR)
    payload = json.dumps({
      "device": {
        "applicationId": APP_ID,
        "description": DESCRIPTION,
        "devEui": dev_id,
        "deviceProfileId": DEVICE_PROFILE_ID,
        "isDisabled": False,
        "joinEui": "0000000000000000",
        "name": name,
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


def delete_device(dev_id):
    conn = http.client.HTTPSConnection(HTTPS_CONNECTION_ADDR)
    boundary = ''
    payload = ''
    headers = {
        'Authorization': AUTHORIZATION_TOKEN,
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }
    link = "/api/devices/" + dev_id
    conn.request("DELETE", link, payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def get_device_list():
    conn = http.client.HTTPSConnection(HTTPS_CONNECTION_ADDR)
    payload = ''
    headers = {
        'Authorization': AUTHORIZATION_TOKEN
    }
    conn.request("GET", "/api/devices?limit=10&applicationId=" + APP_ID, payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def update_device(dev_id, name):
    conn = http.client.HTTPSConnection(HTTPS_CONNECTION_ADDR)
    payload = json.dumps({
        "device": {
            "applicationId": APP_ID,
            "deviceProfileId": DEVICE_PROFILE_ID,
            "name": name
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': AUTHORIZATION_TOKEN
    }
    link = "/api/devices/" + dev_id
    conn.request("PUT", link, payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
