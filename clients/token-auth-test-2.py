import requests

def client():
    data = {
        "username":"admin3",
        "email":"admin3@tes.com",
        "password1":"test12345",
        "password2":"test12345"
    }

    response = requests.post("http://localhost:8000/api/v1/rest-auth/registration/",
                            data=data)

    print("Status Code: ", response.status_code)
    print(response.json())

if __name__ == "__main__":
    client()