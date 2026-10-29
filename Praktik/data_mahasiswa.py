# Praktik: Sistem Data Mahasiswa menggunakan Dictionary

def cari_mahasiswa(data, nim):
    """Mencari data mahasiswa berdasarkan NIM secara aman."""
    return data.get(nim)

def rata_rata_nilai(data):
    """Menghitung rata-rata nilai seluruh mahasiswa dalam dictionary."""
    if len(data) == 0:
        return 0
    total = 0
    for info in data.values():
        total += info["nilai"]
    return total / len(data)

# 1. Inisialisasi dictionary data mahasiswa dengan minimal 5 data
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

print("=== UJI PENCARIAN MAHASISWA ===")
# Test case pencarian tersedia (A003)
nim_cari = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim_cari)
if hasil is not None:
    print(f"Data {nim_cari}: {hasil}")
else:
    print("Data tidak ditemukan")

# Test case pencarian tidak tersedia (A999)
nim_tidak_ada = "A999"
hasil_tdk = cari_mahasiswa(data_mahasiswa, nim_tidak_ada)
if hasil_tdk is not None:
    print(f"Data {nim_tidak_ada}: {hasil_tdk}")
else:
    print(f"NIM {nim_tidak_ada}: Data tidak ditemukan")

print("\n=== PENAMBAHAN & PEMBARUAN DATA ===")
# Menambahkan satu mahasiswa baru (A006)
data_mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "B",
    "nilai": 80
}
print("Mahasiswa A006 berhasil ditambahkan.")

# Mengubah nilai salah satu mahasiswa (A002 menjadi 82)
data_mahasiswa["A002"]["nilai"] = 82
print("Nilai mahasiswa A002 diperbarui menjadi 82.")

print("\n=== REKAP SELURUH DATA MAHASISWA ===")
# Menampilkan seluruh data menggunakan items()
for nim, info in data_mahasiswa.items():
    print(f"NIM: {nim} | Info: {info}")

# Menghitung dan menampilkan rata-rata nilai kelas
rata_rata = rata_rata_nilai(data_mahasiswa)
print(f"\nRata-rata nilai seluruh mahasiswa: {rata_rata:.2f}")