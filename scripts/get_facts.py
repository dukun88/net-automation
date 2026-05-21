import os
import yaml
from napalm import get_network_driver

# 1. Baca file YAML
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
yaml_path = os.path.join(base_dir, 'config', 'devices.yaml')

with open(yaml_path, 'r') as file:
    config_data = yaml.safe_load(file)

global_creds = config_data['credentials']
devices_list = config_data['devices']

print("=== Mengambil Informasi Perangkat via NAPALM ===\n")

# 2. Looping menggunakan Driver NAPALM
for dev in devices_list:
    print(f"[*] Mengambil data dari {dev['name']} menggunakan driver: {dev['driver']}...")
    
    # Inisialisasi driver berdasarkan variabel di YAML
    driver = get_network_driver(dev['driver'])
    device = driver(
        hostname=dev['host'], 
        username=global_creds['username'], 
        password=global_creds['password']
    )
    
    try:
        device.open()
        facts = device.get_facts()
        
        print(f"[+] {dev['name']} Sukses!")
        print(f"    Vendor/Model : {facts['vendor']} / {facts['model']}")
        print(f"    OS Version   : {facts['os_version'][:50]}...") # Potong agar tidak terlalu panjang
        print(f"    Uptime       : {facts['uptime']} detik\n")
        
        device.close()
    except Exception as e:
        print(f"[X] NAPALM Gagal di {dev['name']}: {e}\n")
