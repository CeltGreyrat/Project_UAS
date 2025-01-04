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

