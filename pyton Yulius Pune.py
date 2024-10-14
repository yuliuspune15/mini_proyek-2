import sys
from prettytable import PrettyTable

class Admin:
    def __init__(self):
        self.obat_obatan = []
        self.username = "IrvanMissa45"
        self.password = "Vannxxyy"

    def buat_obat(self, nama, dosis, jadwal):
        obat = {
            "nama": nama,
            "dosis": dosis,
            "jadwal": jadwal
        }
        self.obat_obatan.append(obat)
        print(f"Obat {nama} berhasil dibuat!")

    def lihat_obat_obatan(self):
        if not self.obat_obatan:
            print("Tidak ada obat yang tersedia.")
            return
        table = PrettyTable(["No", "Nama Obat", "Dosis", "Jadwal"])
        for i, obat in enumerate(self.obat_obatan):
            table.add_row([i + 1, obat["nama"], obat["dosis"], obat["jadwal"]])
        print(table)

    def perbarui_obat(self, nama, dosis_baru, jadwal_baru):
        for obat in self.obat_obatan:
            if obat["nama"] == nama:
                obat["dosis"] = dosis_baru
                obat["jadwal"] = jadwal_baru
                print(f"Obat {nama} berhasil diperbarui!")
                return
        print(f"Obat {nama} tidak ditemukan!")

    def hapus_obat(self, nama):
        for obat in self.obat_obatan:
            if obat["nama"] == nama:
                self.obat_obatan.remove(obat)
                print(f"Obat {nama} berhasil dihapus!")
                return
        print(f"Obat {nama} tidak ditemukan!")

    def login(self, username, password):
        return username == self.username and password == self.password


class Pasien:
    def __init__(self):
        self.riwayat_obat = []
        self.username = "imam"
        self.password = "paskan"

    def terima_pengingat(self, obat):
        print(f"Pengingat: Minum {obat['nama']} - {obat['dosis']} - {obat['jadwal']}")

    def lihat_riwayat_obat(self):
        if not self.riwayat_obat:
            print("Tidak ada riwayat obat.")
            return
        table = PrettyTable(["No", "Nama Obat", "Dosis", "Jadwal"])
        for i, obat in enumerate(self.riwayat_obat):
            table.add_row([i + 1, obat["nama"], obat["dosis"], obat["jadwal"]])
        print(table)

    def login(self, username, password):
        return username == self.username and password == self.password


def main():
    admin = Admin()
    pasien = Pasien()

    while True:
        print("\nSelamat Datang")
        print("1. Login sebagai Admin")
        print("2. Login sebagai Pasien")
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            # Admin login
            while True:
                print("\nSelamat Datang Admin")
                username = input("Masukkan username: ")
                password = input("Masukkan password: ")
                if admin.login(username, password):
                    print("Login berhasil!")
                    break
                else:
                    print("Username atau password salah!")

            # Admin menu
            while True:
                print("\nMenu Admin:")
                print("1. Buat Obat")
                print("2. Lihat Obat-Obatan")
                print("3. Perbarui Obat")
                print("4. Hapus Obat")
                print("5. Keluar")
                pilihan = input("Pilih opsi: ")

                if pilihan == "1":
                    nama = input("Masukkan nama obat: ")
                    dosis = input("Masukkan dosis obat: ")
                    jadwal = input("Masukkan jadwal obat: ")
                    admin.buat_obat(nama, dosis, jadwal)
                    print("End")
                elif pilihan == "2":
                    admin.lihat_obat_obatan()
                    print("End")
                elif pilihan == "3":
                    nama = input("Masukkan nama obat: ")
                    dosis_baru = input("Masukkan dosis obat baru: ")
                    jadwal_baru = input("Masukkan jadwal obat baru: ")
                    admin.perbarui_obat(nama, dosis_baru, jadwal_baru)
                    print("End")
                elif pilihan == "4":
                    nama = input("Masukkan nama obat: ")
                    admin.hapus_obat(nama)
                    print("End")
                elif pilihan == "5":
                    print("Keluar dari program")
                    sys.exit()
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
                    print("End")

        elif pilihan == "2":
            # Patient login
            while True:
                print("\nSelamat Datang Pasien")
                username = input("Masukkan username: ")
                password = input("Masukkan password: ")
                if pasien.login(username, password):
                    print("Login berhasil!")
                    break
                else:
                    print("Username atau password salah!")

            # Patient menu
            while True:
                print("\nMenu Pasien:")
                print("1. Lihat Riwayat Obat")
                print("2. Terima Pengingat")
                print("3. Keluar")
                pilihan = input("Pilih opsi: ")

                if pilihan == "1":
                    pasien.lihat_riwayat_obat()
                    print("End")
                elif pilihan == "2":
                    nama = input("Masukkan nama obat: ")
                    dosis = input("Masukkan dosis obat: ")
                    jadwal = input("Masukkan jadwal obat: ")
                    obat = {"nama": nama, "dosis": dosis, "jadwal": jadwal}
                    pasien.terima_pengingat(obat)
                    print("End")
                elif pilihan == "3":
                    print("Keluar dari program")
                    sys.exit()
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
                    print("End")

if __name__ == "__main__":
    main()