from data import Pegawai, Data
from view import View

class Process:
    def __init__(self):
        self.data = Data()
        self.view = View()

    def tambah(self):
        try:
            nama = input("Masukkan nama: ")
            alamat = input("Masukkan alamat: ")
            departemen = input("Masukkan departemen: ")
            if not nama or not alamat or not departemen:
                raise ValueError("Semua field harus diisi.")
            pegawai = Pegawai(nama, alamat, departemen)
            self.data.tambah(pegawai)
            print(f'Data {nama} berhasil ditambahkan')
        except ValueError as e:
            print(f"Error: {e}")

    def ubah(self):
        try:
            nama = input("Masukkan nama pegawai yang ingin diubah: ")
            alamat = input("Masukkan alamat baru: ")
            departemen = input("Masukkan departemen baru: ")
            if not alamat or not departemen:
                raise ValueError("Alamat dan departemen baru harus diisi.")
            if not self.data.ubah(nama, alamat, departemen):
                print("Data Tidak Ditemukan")
            else:
                print(f"Data {nama} berhasil diubah")
        except ValueError as e:
            print(f"Error: {e}")

    def hapus(self):
        try:
            nama = input("Masukkan nama pegawai yang ingin dihapus: ")
            if not self.data.hapus(nama):
                print("Data Tidak Ditemukan")
            else:
                print(f"Data {nama} berhasil dihapus")
        except Exception as e:
            print(f"Error: {e}")

    def tampilkan(self):
        data_pegawai = self.data.lihat()
        self.view.tampilkan_tabel(data_pegawai)

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Tambah Pegawai")
            print("2. Lihat Pegawai")
            print("3. Ubah Pegawai")
            print("4. Hapus Pegawai")
            print("5. Keluar")

            pilihan = input("Pilih menu (1-5): ")

            if pilihan == '1':
                self.tambah()
            elif pilihan == '2':
                self.tampilkan()
            elif pilihan == '3':
                self.ubah()
            elif pilihan == '4':
                self.hapus()
            elif pilihan == '5':
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
