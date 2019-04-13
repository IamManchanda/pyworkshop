import requests

api_url = "http://shibe.online/api/shibes"
params = {
    "count": 10,
}

response = requests.get(api_url, params)
response_status_code = response.status_code
response_json = response.json()

print({
    "response_status_code": response_status_code,
    "response_json": response_json,
})
