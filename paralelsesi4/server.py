import socket

#Konfigurasi server
HOST = '127.0.0.1'
PORT = 5000

#Membuat socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server berjalan di {HOST}:{PORT}")
print("Menunggu koneksi dari client...")

#Menerima koneksi dari client
conn, addr = server_socket.acceppt()
print(f"Terhubung dengan client {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Pesan dari client: {data}")

    #Mengirim pesan ke client
    balasan = f"Pesan '{data}' diterima oleh server."
    conn.sendall(balasan.encode())

conn.close()
server_socket.close()
print("Koneksi ditutup.")