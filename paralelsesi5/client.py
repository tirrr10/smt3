import socket
import threading
import sys

def receive_messages(client_socket):
    """Thread untuk menerima pesan dari server."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')  # Terima pesan
            if message:
                print(f"Pesan dari server: {message}")  # Tampilkan pesan yang diterima
        except:
            print("Koneksi ke server terputus.")
            client_socket.close()
            sys.exit()  # Keluar dari program

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(('10.184.184.64', 8080))  # Hubungkan ke server
        print("Terhubung ke server. Mulai chat...")
        
        # Mulai thread untuk menerima pesan
        thread = threading.Thread(target=receive_messages, args=(client,))
        thread.start()
        
        while True:
            message = input()  # Input pesan dari user
            if message.lower() == 'quit':  # Keluar jika ketik 'quit'
                print("Meninggalkan chat...")
                break
            if message:  # Pastikan pesan tidak kosong
                print(f"Anda: {message}")  # TAMBAHAN: Tampilkan pesan yang diketik
                client.send(message.encode('utf-8'))  # Kirim pesan ke server
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()  # Tutup koneksi
        print("Koneksi ditutup.")

if __name__ == "__main__":
    main()