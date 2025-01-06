class View:
    @staticmethod
    def tampilkan_tabel(data_pegawai):
        if not data_pegawai:
            print("\nDaftar Pegawai:")
            print(f"{'No.':<5} | {'Nama':<20} | {'Alamat':<30} | {'Departemen':<20}")
            print("-" * 80)
            print("Data Tidak Ditemukan")
            return
        print("\nDaftar Pegawai:")
        print(f"{'No.':<5} | {'Nama':<20} | {'Alamat':<30} | {'Departemen':<20}")
        print("-" * 80)
        for i, pegawai in enumerate(data_pegawai, start=1):
            print(f"{i:<5} {pegawai}")
