import requests

print("Request version: " + requests.__version__)

google = requests.get("http://www.google.com")
print("Request Google Status: " + str(google.status_code))
