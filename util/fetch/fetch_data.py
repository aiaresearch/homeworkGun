import requests
import urllib.parse

SERVER_ADDRESS = "http://localhost:5000"

def fetch_student_data(class_id):
    endpoint = "/getinfo/student"
    data = {"class_id": class_id}
    query_string = urllib.parse.urlencode(data)
    url = f"{SERVER_ADDRESS}{endpoint}?{query_string}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch student data. Status code: {response.status_code}")
    
def fetch_login_status(username, password):
    endpoint = "/login"
    data = {"username": username, "password": password}
    query_string = urllib.parse.urlencode(data)
    url = f"{SERVER_ADDRESS}{endpoint}?{query_string}"
    response = requests.get(url)
    if response.status_code == 200:
        return True if response.text == 'success' else False

if __name__ == "__main__":
    class_id = "1"
    data = fetch_student_data(class_id)
    print(data)