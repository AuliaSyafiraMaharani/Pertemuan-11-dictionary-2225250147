# Latihan 6: Fungsi Pencarian
def cari(data, nim):
    return data.get(nim, "Data tidak ditemukan")

mahasiswa = {
    "A001": {"nama": "Ayu", "nilai": 85},
    "A002": {"nama": "Budi", "nilai": 78}
}

print(cari(mahasiswa, "A002"))
print(cari(mahasiswa, "A003"))