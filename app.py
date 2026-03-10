nama_lengkap = input("Masukkan nama lengkap Anda: ")
stambuk = input("Tahun angkatan (contoh 2021): ")

semester_sekarang = int(input("Sekarang semester berapa?(contoh 8): "))

jawaban = input("Apakah kamu sudah memiliki judul skripsi? (sudah/belum): ")


print("\n" + "="*15)
print("HASIL ANALISIS DATA")
print("="*15)


if semester_sekarang >= 14:
    status = "TERANCAM DROP OUT"
elif semester_sekarang > 8:
    status = "STUDI TINGKAT AKHIR / PERPANJANGAN"
else:
    status = "MASIH SESUAI STUDI NORMAL"

    if jawaban == "sudah":
      pesan = ("Luar biasa! Segera ajukan ke dosen pembimbing ya.")
    else:
      pesan = ("Jangan khawatir " + nama_lengkap + " mulailah dengan membaca jurnal atau kasus hukum terbaru.")
print("="*30)

print("Mahasiswa :", nama_lengkap.upper())
print("Universitas: Universitas Sumatera Utara")
print("Angkatan  :", stambuk)
print("Semester  :", semester_sekarang)
print("STATUS    :", status)
print("status Judul:", jawaban)
print ("pesan:", pesan)

print("="*30)
