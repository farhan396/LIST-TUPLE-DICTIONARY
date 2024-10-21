# LIST
# Daftar buah
fruits = ["apel", "pisang", "ceri"]

# Tambahkan buah baru
fruits.append("jeruk")

# Tampilkan daftar
print(fruits)  # Hasil: ["apel", "pisang", "ceri", "jeruk"]

# Hapus pisang
fruits.remove("pisang")

# Tampilkan daftar
print(fruits)  # Hasil: ["apel", "ceri", "jeruk"]

# TUPLE
# Daftar buah
fruits_tuple = ("apel", "pisang", "ceri")

# Hitung jumlah buah
length = len(fruits_tuple)

# Tampilkan daftar dan jumlah
print(fruits_tuple, length)  # Hasil: ("apel", "pisang", "ceri") 3

# DICTIONARY
# Data orang
person = {
    "nama": "Farhan",
    "umur": 18,
    "kota": "Mataram"
}

# Tambahkan pekerjaan
person["pekerjaan"] = "tentara"

# Hapus kota
del person["kota"]

# Tampilkan data orang
print(person)  # Hasil: {'nama': 'Najhan', 'umur': 18, 'pekerjaan': 'tentara'}
