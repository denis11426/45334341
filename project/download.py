#we will download the raw data from the European Commission site and save in our foulder

import requests

url = "https://energy.ec.europa.eu/document/download/906e60ca-8b6a-44e7-8589-652854d2fd3f_en?filename=Weekly_Oil_Bulletin_Prices_History_maticni_4web.xlsx"

filename = "Weekly_Oil_Bulletin_Prices_History_maticni_4web.xlsx"

response = requests.get(url, timeout=30)
response.raise_for_status()

with open(filename, "wb") as f:
    f.write(response.content)

print("Download successful")
print("Status code:", response.status_code)
print("File size:", len(response.content), "bytes")
print("Saved as:", filename)