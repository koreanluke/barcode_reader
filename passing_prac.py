import urllib.request

api_url = "https://www.google.co.jp/"

req = urllib.request.Request(api_url)
with urllib.request.urlopen(req) as response:
    page = response.read()
    print(page)