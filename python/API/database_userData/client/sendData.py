import requests

url = 'http://SERVER_IP:5000/addUser'

data = {
    'username': 'Max Musterman',
    'password': '123456789'
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("User successfully saved!")
else:
    print("An error occurred while saving the user:", response.json()['message'])
