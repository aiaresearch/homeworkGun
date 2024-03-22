import requests
import urllib.parse
import os
import json

# if platform is windows, change the following line to your own address
if os.name == "nt":
    ADDR = "URL"
else:
    ADDR = os.getenv("REQUEST_URL")


def fetch_student_data(class_id):
    endpoint = "/students"
    data = {"class": class_id}
    query_string = urllib.parse.urlencode(data)
    url = f"{ADDR}{endpoint}?{query_string}"
    try:
        response = requests.get(url, data=data)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return e
    else:
        return response.json()

def fetch_login_status(username, password):
    endpoint = "/login"
    data = json.dumps({"account": username, "passwd": password})
    url = f"{ADDR}{endpoint}"
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return e
    else:
        return response.json()


def fetch_homeworks():
    endpoint = "/needtosub"
    url = f"{ADDR}{endpoint}"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return e
    else:
        return response.json()


def fetch_token_status(token):
    endpoint = "/user"
    headers = {"Authorization" : token}
    url = f"{ADDR}{endpoint}"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return e
    else:
        return response.json()


def fetch_register_status(username, password):
    endpoint = "/register"
    data = json.dumps({"account": username, "passwd": password})
    url = f"{ADDR}{endpoint}"
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return e
    else:
        return response.json()


def create_homework(homework_id, subject, start_date, end_date):
    endpoint = "/create"
    data = {"homework_id": homework_id, "submission_required": subject, "start_date": start_date, "end_date": end_date}
    url = f"{ADDR}{endpoint}"
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return e
    else:
        return response.json()


def submit_homework(school_id, subject, homework_id):
    endpoint = "/submit"
    data = {"school_id": school_id, "subject_id": subject, "homework_id": homework_id}
    url = f"{ADDR}{endpoint}"
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return e
    else:
        return response.json()