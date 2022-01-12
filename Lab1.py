import requests

print("Request version: " + requests.__version__)

google = requests.get("http://www.google.com")
print("Request Google Status: " + str(google.status_code))

git = requests.get("https://raw.githubusercontent.com/YeeSkywalker/CMPUT404_Lab01/main/Lab1.py")
print("Request Github Python File" + git.text)
