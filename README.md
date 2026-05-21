
# net-automation
net-automation-core/  
│  
├── config/  
│   └── devices.yaml       <-- Tempat menyimpan semua variabel perangkat (IP, Pass, dll)  
│  
├── scripts/  
│   ├── run_command.py     <-- Kode untuk menjalankan perintah 'show' (Netmiko)  
│   └── get_facts.py       <-- Kode untuk mengambil data terstruktur (NAPALM)  
│  
└── requirements.txt       <-- Daftar library Python yang dibutuhkan  

# Cara Menggunakan Folder Ini:

1. Buat folder dan file-file di atas sesuai strukturnya.
2. Buka terminal/CMD Anda, masuk ke direktori folder tersebut, lalu install library yang dibutuhkan:

```

    pip install -r requirements.txt

```
3. Edit file config/devices.yaml sesuaikan dengan IP, username, password, dan jenis perangkat di laboratorium atau kantor Anda.
