import requests

def client():
    credentials = {"username": "admin2", "password":"123"}

    response = requests.post("http://localhost:8000/api/v1/rest-auth/login/",
                            data=credentials)

    print("Status Code: ", response.status_code)
    token = f"Token {response.json()['key']}"
    headers = {"Authorization": token}

    response2 = requests.get("http://localhost:8000/api/v1/profiles/",
                            headers=headers)

    print("Status Code: ", response2.status_code)
    print(response2.json())

if __name__ == "__main__":
    client()