# Sistem Managemen Pegawai

## Penjelasan
Sistem Manajemen Pegawai adalah program Python yang dirancang untuk mengelola data karyawan secara efisien. Ini memungkinkan pengguna untuk menambah, melihat, memperbarui, dan menghapus catatan karyawan. Program ini dibangun menggunakan prinsip Pemrograman Berorientasi Objek (OOP), yang mengedepankan modularitas dan kemudahan pemeliharaan.

## Fitur
- Tambah Karyawan: Pengguna dapat menambahkan catatan karyawan baru dengan memberikan nama, alamat, dan departemennya.
- Lihat Karyawan: Pengguna dapat melihat daftar seluruh karyawan beserta detailnya dalam format terstruktur.
- Perbarui Karyawan: Pengguna dapat memperbarui alamat dan departemen karyawan yang ada dengan menentukan namanya.
- Hapus Karyawan: Pengguna dapat menghapus catatan karyawan dengan memberikan nama karyawan tersebut.
- Menu Ramah Pengguna: Program ini menampilkan menu berbasis teks sederhana untuk navigasi yang mudah.

## Struktur Program
### Pegawai : Mewakili pegawai perseorangan.
- Atribut:
nama: Nama karyawan.
alamat: Alamat karyawan.
departemen: Departemen karyawan.
- Metode:
__str__: Mengembalikan representasi string karyawan yang diformat.

### DataPegawai: Mengelola kumpulan objek Pegawai.
- Atribut:
data_pegawai: Daftar yang menyimpan catatan karyawan.
Metode:
tambah: Menambahkan karyawan baru ke daftar.
lihat: Menampilkan semua catatan karyawan.
hapus: Menghapus catatan karyawan berdasarkan nama.
ubah: Memperbarui alamat dan departemen karyawan.

### Menu: Menangani interaksi pengguna dan pengoperasian menu.
- Metode:
tampilkan_menu: Menampilkan menu dan memproses input pengguna.
tambah_pegawai: Meminta pengguna untuk menambah karyawan baru.
ubah_pegawai: Meminta pengguna untuk memperbarui karyawan yang ada.
hapus_pegawai: Meminta pengguna untuk menghapus karyawan.

## Code Program
````python
class Pegawai:
    def __init__(self, nama, alamat, departemen):
        self.nama = nama
        self.alamat = alamat
        self.departemen = departemen

    def __str__(self):
        return f"{self.nama:<20} {self.alamat:<30} {self.departemen:<20}"


class DataPegawai:
    def __init__(self):
        self.data_pegawai = []

    def tambah(self, pegawai: Pegawai):
        self.data_pegawai.append(pegawai)
        print(f'Data {pegawai.nama} berhasil ditambahkan')

    def lihat(self):
        if not self.data_pegawai:
            print("Data Tidak Ditemukan")
        else:
            print("\nDaftar Pegawai:")
            print(f"{'No.':<5} {'Nama':<20} {'Alamat':<30} {'Departemen':<20}")
            print("-" * 80)
            for i, pegawai in enumerate(self.data_pegawai, start=1):
                print(f"{i:<5} {pegawai}")

    def hapus(self, nama):
        for pegawai in self.data_pegawai:
            if pegawai.nama == nama:
                self.data_pegawai.remove(pegawai)
                print(f"Data {nama} berhasil dihapus")
                return
        print("Data Tidak Ditemukan")

    def ubah(self, nama, alamat, departemen):
        for pegawai in self.data_pegawai:
            if pegawai.nama == nama:
                pegawai.alamat = alamat
                pegawai.departemen = departemen
                print(f"Data {nama} berhasil diubah")
                return
        print("Data Tidak Ditemukan")


class Menu:
    def __init__(self):
        self.data_pegawai = DataPegawai()

    def tampilkan_menu(self):
        while True:
            print("\nMenu:")
            print("1. Tambah Pegawai")
            print("2. Lihat Pegawai")
            print("3. Ubah Pegawai")
            print("4. Hapus Pegawai")
            print("5. Keluar")

            pilihan = input("Pilih menu (1-5): ")

            if pilihan == '1':
                self.tambah_pegawai()
            elif pilihan == '2':
                self.data_pegawai.lihat()
            elif pilihan == '3':
                self.ubah_pegawai()
            elif pilihan == '4':
                self.hapus_pegawai()
            elif pilihan == '5':
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def tambah_pegawai(self):
        nama = input("Masukkan nama: ")
        alamat = input("Masukkan alamat: ")
        departemen = input("Masukkan departemen: ")
        pegawai = Pegawai(nama, alamat, departemen)
        self.data_pegawai.tambah(pegawai)

    def ubah_pegawai(self):
        nama = input("Masukkan nama pegawai yang ingin diubah: ")
        alamat = input("Masukkan alamat baru: ")
        departemen = input("Masukkan departemen baru: ")
        self.data_pegawai.ubah(nama, alamat, departemen)

    def hapus_pegawai(self):
        nama = input("Masukkan nama pegawai yang ingin dihapus: ")
        self.data_pegawai.hapus(nama)


def main():
    menu = Menu()
    menu.tampilkan_menu()


if __name__ == "__main__":
    main()
````

## Contoh Input Program
````
Masukkan nama: John Tor
Masukkan alamat: Cikarang
Masukkan departemen: IT
Data John Tor berhasil ditambahkan
````

## Contoh Output Program
````
Daftar Pegawai:
No. Nama               Alamat                        Departemen        
------------------------------------------------------------------------
1   John Tor          Cikarang                       IT                 
````
