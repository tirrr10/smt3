import socket

#Konfigurasi client
HOST = '127.0.01'
PORT = 5000

#Membuat socket dan menghubungkan ke server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    pesan = input("Kirim pesan ke server (ketik 'exit' untuk keluar): ")
    if pesan.lower() == 'exit':
        break
    client_socket.sendall(pesan.encode())

    #Menerima balasan dari server
    data = client_socket.recv(1024).decode()
    print(f"Balasan dari server: {data}")

client_socket.close()
print("Koneksi ditutup.")