import datetime
import sys

# Struktur data: List untuk menyimpan tugas
todo_list = []

def tambah_tugas():
    tugas = input("Masukkan tugas baru: ")
    todo_list.append(tugas)
    print(f"Tugas '{tugas}' berhasil ditambahkan!\n")

def lihat_tugas():
    print("\n=== Daftar Tugas ===")
    if not todo_list:
        print("Tidak ada tugas yang tersimpan.\n")
    else:
        for i, tugas in enumerate(todo_list, start=1):
            print(f"{i}. {tugas}")
    print()

def hapus_tugas():
    lihat_tugas()
    if todo_list:
        try:
            index = int(input("Masukkan nomor tugas yang ingin dihapus: ")) - 1
            if 0 <= index < len(todo_list):
                tugas_terhapus = todo_list.pop(index)
                print(f"Tugas '{tugas_terhapus}' berhasil dihapus.\n")
            else:
                print("Nomor tidak valid.\n")
        except ValueError:
            print("Harap masukkan angka yang valid.\n")

def menu():
    print("=== Aplikasi To-Do List Sederhana ===")
    print(f"Tanggal: {datetime.date.today()}\n")
    
    while True:
        print("1. Tambah Tugas")
        print("2. Lihat Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")
        
        if pilihan == '1':
            tambah_tugas()
        elif pilihan == '2':
            lihat_tugas()
        elif pilihan == '3':
            hapus_tugas()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan aplikasi To-Do List!\n")
            sys.exit()
        else:
            print("Pilihan tidak valid, coba lagi.\n")

# Jalankan program
menu()
