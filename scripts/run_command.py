import os
import yaml
from netmiko import ConnectHandler

# 1. Tentukan path ke file YAML
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
yaml_path = os.path.join(base_dir, 'config', 'devices.yaml')

# 2. Baca data dari file YAML
with open(yaml_path, 'r') as file:
    config_data = yaml.safe_load(file)

global_creds = config_data['credentials']
devices_list = config_data['devices']

# Perintah yang ingin dijalankan ke semua perangkat
# (Bisa Anda ganti sesuai kebutuhan tanpa merubah struktur device)
COMMAND = "show ip interface brief"

print(f"=== Memulai Eksekusi Perintah: '{COMMAND}' ===\n")

# 3. Looping ke setiap perangkat
for dev in devices_list:
    print(f"[*] Menghubungi {dev['name']} ({dev['host']})...")
    
    # Gabungkan data perangkat dengan kredensial global
    device_connection_info = {
        'device_type': dev['device_type'],
        'host': dev['host'],
        'username': global_creds['username'],
        'password': global_creds['password'],
        'secret': global_creds['secret'],
    }
    
    try:
        # Jalankan SSH Koneksi
        with ConnectHandler(**device_connection_info) as net_connect:
            net_connect.enable()
            output = net_connect.send_command(COMMAND)
            
            print(f"[+] Hasil dari {dev['name']}:")
            print("-" * 40)
            print(output)
            print("-" * 40 + "\n")
            
    except Exception as e:
        print(f"[X] GAGAL terhubung ke {dev['name']}: {e}\n")
