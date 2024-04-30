import http.client
import json


def add_device():
    conn = http.client.HTTPSConnection("chirpstack-api.iotserv.ru")
    payload = json.dumps({
      "device": {
        "applicationId": "1bad2baa-585a-41cf-9478-d43e8f0ac96a",
        "description": "SPV Test Device",
        "devEui": "fa41a5fffe666860",
        "deviceProfileId": "29d26ba4-2bf0-452e-9341-2671f442c7da",
        "isDisabled": False,
        "joinEui": "0000000000000000",
        "name": "SPV Test Device POASTMAN",
        "skipFcntCheck": False
      }
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjY0ODE3NTkzLTMyYzYtNDBlNC05YTc5LTE4Y2M0MWFhMWNjNSIsInR5cCI6ImtleSJ9.xM_bU22aFukUzVC1v07aZ2T5OaIHUDSdHYtTsTPz7JA'
    }
    conn.request("POST", "/api/devices", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def delete_device():
    conn = http.client.HTTPSConnection("chirpstack-api.iotserv.ru")
    boundary = ''
    payload = ''
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjY0ODE3NTkzLTMyYzYtNDBlNC05YTc5LTE4Y2M0MWFhMWNjNSIsInR5cCI6ImtleSJ9.xM_bU22aFukUzVC1v07aZ2T5OaIHUDSdHYtTsTPz7JA',
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }
    conn.request("DELETE", "/api/devices/fa41a5fffe666860", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def get_device_list():
    conn = http.client.HTTPSConnection("chirpstack-api.iotserv.ru")
    payload = ''
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjY0ODE3NTkzLTMyYzYtNDBlNC05YTc5LTE4Y2M0MWFhMWNjNSIsInR5cCI6ImtleSJ9.xM_bU22aFukUzVC1v07aZ2T5OaIHUDSdHYtTsTPz7JA'
    }
    conn.request("GET", "/api/devices?limit=5&applicationId=1bad2baa-585a-41cf-9478-d43e8f0ac96a", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def update_device():
    conn = http.client.HTTPSConnection("chirpstack-api.iotserv.ru")
    payload = json.dumps({
        "device": {
            "applicationId": "1bad2baa-585a-41cf-9478-d43e8f0ac96a",
            "deviceProfileId": "29d26ba4-2bf0-452e-9341-2671f442c7da",
            "name": "SPV Test Device POSTMAN updated"
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjY0ODE3NTkzLTMyYzYtNDBlNC05YTc5LTE4Y2M0MWFhMWNjNSIsInR5cCI6ImtleSJ9.xM_bU22aFukUzVC1v07aZ2T5OaIHUDSdHYtTsTPz7JA'
    }
    conn.request("PUT", "/api/devices/fa41a5fffe666860", payload, headers)
