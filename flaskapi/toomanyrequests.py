import requests
for x in range(202):
    print(requests.get("http://localhost:2224/fast").text)
