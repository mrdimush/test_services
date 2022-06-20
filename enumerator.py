import requests

URL = "http://localhost:8888/"

# resp = requests.post(URL, data = {"login": "vasya", "password": "1234"})

password_list = [
    "password",
    "12345",
    "qwerty",
    "1q2w3e",
    "12345678",
    "pass",
    "qwerty123"
]

for password in password_list:
    data = { "login": "skillbox", "passwprd": password}
    print("Trying:", data, end='')
    response =requests.post(URL, data)
    print("Code ", response.status_code)
    if response.status_code != 200:
        print(respose.content)
        break

