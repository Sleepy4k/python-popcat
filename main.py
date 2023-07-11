import requests
import time

url = "https://stats.popcat.click/pop"
token = input("Input your token (optional) : ")
country = input("Input your country (optional) : ")
pop_count = input("Input your pop in one request (optional) : ")

if country == "":
    country = "ID"

if pop_count == "":
    pop_count = "800"

if token == "":
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" \
            ".eyJDb3VudHJ5Q29kZSI6IklEIiwiSVAiOiIzNi43My4zNC4xOTQiLCJJRCI6MzEsImV4cCI6MTY4OTEzMDY0OH0" \
            ".3rPlKZPLCY5vyEVr6alZ8lJYQEhZuPbFobAXjxGBc_I "

while url:
    try:
        response = requests.post(url + "?pop_count=800&country=" + country + "&token=" + token)
        response_code = response.status_code

        if response_code == 201:
            response_body = response.json()

            token = response_body.get("Token")
            location = response_body.get("Location")
            country = location.get("Code")

            print(f"Request success added 800 pop, ip detected from '{country}'")
        elif response_code == 429:
            print(f"Request failed 'Too Many Request' detected from pop cat server with code {response_code}")
        else:
            print(f"Request failed with status code {response_code}")
    except requests.exceptions.RequestException as err:
        print(f"Request error with exception {err}")

    time.sleep(31)
else:
    print("Token not found, please input your token")