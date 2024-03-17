import requests
import urllib.parse
import os
import json

# if platform is windows, change the following line to your own address
if os.name == "nt":
    ADDR = "URL"
elif os.name == "posix":
    ADDR = os.getenv("REQUEST_URL")


def fetch_student_data(class_id):
    endpoint = "/crud"
    data = {"class_id": class_id}
    query_string = urllib.parse.urlencode(data)
    url = f"{ADDR}{endpoint}?{query_string}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch student data. Status code: {response.status_code}")
    

def fetch_login_status(username, password):
    endpoint = "/login"
    data = json.dumps({"account": username, "passwd": password})
    url = f"{ADDR}{endpoint}"
    response = requests.post(url, data=data)
    return response


def fetch_token_status(token):
    endpoint = "/user"
    headers = {"Authorization" : token}
    url = f"{ADDR}{endpoint}"
    response = requests.get(url, headers=headers)
    return response


def fetch_register_status(username, password):
    endpoint = "/register"
    data = json.dumps({"account": username, "passwd": password})
    url = f"{ADDR}{endpoint}"
    response = requests.post(url, data=data)
    return response
