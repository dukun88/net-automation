import requests

# Mengaktifkan REST API di Mikrotik v7 bisa via: /ip/service/set rest winbox=yes
url = "https://192.168.88.1/rest/ip/address"
auth = ('admin', 'SuperPassword123')

# Ambil data IP (verify=False jika tidak pakai sertifikat SSL resmi)
response = requests.get(url, auth=auth, verify=False)

if response.status_code == 200:
    for addr in response.json():
        print(f"Interface: {addr['interface']} | IP: {addr['address']}")
