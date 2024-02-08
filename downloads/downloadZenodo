"""
To assist downloading all files from Zenodo data repository
""" 
import requests

ACCESS_TOKEN = "[YOUR PRIVATE KEY]"
record_id = ""   # TO CHANGE, e.g, https://zenodo.org/records/2235448; 2235448 will be the record_id

url = f"https://zenodo.org/api/records/{record_id}"

r = requests.get(url, params={'access_token': ACCESS_TOKEN})
download_urls = [f['links']['self'] for f in r.json()['files']]
filenames = [f['key'] for f in r.json()['files']]

print(r.status_code)
print(download_urls)

for filename, url in zip(filenames, download_urls):
    print("Downloading:", filename)
    r = requests.get(url, params={'access_token': ACCESS_TOKEN})
    with open(filename, 'wb') as f:
        f.write(r.content)

  
