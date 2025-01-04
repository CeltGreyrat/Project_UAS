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

