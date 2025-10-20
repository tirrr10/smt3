import socket
import threading

# List untuk menyimpan socket client yang terhubung
clients = []
lock = threading.Lock()  # Lock untuk menghindari race condition saat mengakses list clients

def broadcast(message, sender_socket):
    """Mengirim pesan ke semua client kecuali pengirim."""
    with lock:
        for client in clients:
            if client != sender_socket:
                try:
                    client.send(message.encode('utf-8'))  # Kirim pesan
                except:
                    # Jika gagal kirim, hapus client dari list (koneksi mungkin terputus)
                    clients.remove(client)
                    client.close()

def handle_client(client_socket):
    """Menangani koneksi dari satu client."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')  # Terima pesan
            if message:  # Jika pesan tidak kosong
                print(f"Pesan diterima: {message}")
                broadcast(message, client_socket)  # Broadcast ke client lain
        except:
            # Handle error, seperti koneksi terputus
            print("Koneksi client terputus.")
            with lock:
                if client_socket in clients:
                    clients.remove(client_socket)
            client_socket.close()
            break  # Keluar dari loop

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('10.184.184.64', 8080))  # Bind ke localhost dan port 12345
    server.listen(5)  # Maksimal 5 koneksi antrian
    print("Server berjalan dan menunggu koneksi...")

    while True:
        try:
            client_socket, address = server.accept()  # Terima koneksi baru
            print(f"Koneksi baru dari {address}")
            with lock:
                clients.append(client_socket)  # Tambahkan client ke list
            thread = threading.Thread(target=handle_client, args=(client_socket,))
            thread.start()  # Mulai thread untuk handle client
        except Exception as e:
            print(f"Error pada server: {e}")
            break  # Hentikan server jika error fatal

if __name__ == "__main__":
    main()