# acak â€” Library Random Berbahasa Indonesia

**acak** adalah library Python yang membungkus modul standar 
andom dengan antarmuka berbahasa Indonesia. Dibuat agar lebih mudah dipahami oleh developer Indonesia.

## Instalasi

`ash
pip install acak
`

## Contoh Penggunaan

`python
from acak import acak, acak_bulat, pilih, acak_urutkan, bibit

# Float acak 0.0 - 1.0
print(acak())              # 0.374...

# Integer acak antara 1 - 10
print(acak_bulat(1, 10))   # 7

# Pilih satu elemen
print(pilih(["apel", "mangga", "jeruk"]))  # "mangga"

# Acak urutan list
buah = ["apel", "mangga", "jeruk", "durian"]
acak_urutkan(buah)
print(buah)                # ['durian', 'apel', 'jeruk', 'mangga']

# Set seed (bibit)
bibit(42)
print(acak_bulat(1, 10))   # 2
`

## Daftar Fungsi

| Fungsi | Deskripsi |
|--------|-----------|
| cak() | Float acak 0.0 <= x < 1.0 |
| cak_bulat(a, b) | Integer acak antara a dan b (inklusif) |
| cak_seragam(a, b) | Float acak antara a dan b |
| pilih(urutan) | Pilih satu elemen dari urutan |
| pilih_banyak(urutan, jumlah) | Pilih beberapa elemen (dengan pengembalian) |
| contoh(populasi, jumlah) | Ambil sample tanpa pengembalian |
| cak_urutkan(urutan) | Acak urutan list (in-place) |
| ibit(n) | Set seed untuk reproduksibilitas |

## Lisensi

MIT
