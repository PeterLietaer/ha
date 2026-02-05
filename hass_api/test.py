from requests import get

url = "http://192.168.1.199:8123/ENDPOINT"
headers = {
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJkYjkxNmYyM2QxZDA0MjIwODZmNjVjYzk2NDZmMjJmNyIsImlhdCI6MTc2NTMxMjM0OCwiZXhwIjoyMDgwNjcyMzQ4fQ.ludeenGzGUAGUOGTCniKUnaFHdzvG-bvn9WPCjfwsbQ",
    "content-type": "application/json",
}

response = get(url, headers=headers)
print(response.text)