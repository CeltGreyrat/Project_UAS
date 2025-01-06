class Pegawai:
    def __init__(self, nama, alamat, departemen):
        self.nama = nama
        self.alamat = alamat
        self.departemen = departemen

    def __str__(self):
        return f"{self.nama:<20} {self.alamat:<30} {self.departemen:<20}"


class Data:
    def __init__(self):
        self.data_pegawai = []

    def tambah(self, pegawai: Pegawai):
        self.data_pegawai.append(pegawai)

    def lihat(self):
        return self.data_pegawai

    def hapus(self, nama):
        for pegawai in self.data_pegawai:
            if pegawai.nama == nama:
                self.data_pegawai.remove(pegawai)
                return True
        return False

    def ubah(self, nama, alamat, departemen):
        for pegawai in self.data_pegawai:
            if pegawai.nama == nama:
                pegawai.alamat = alamat
                pegawai.departemen = departemen
                return True
        return False
