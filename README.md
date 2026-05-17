# acak — Library Random Berbahasa Indonesia

**acak** adalah library Python yang membungkus modul standar `random` dengan antarmuka berbahasa Indonesia. Dibuat agar lebih mudah dipahami oleh developer Indonesia.

## Instalasi

```bash
pip install acak
```

Atau langsung dari GitHub:

```bash
pip install git+https://github.com/annaqibz01/acak.git
```

## Contoh Penggunaan

```python
from acak import acak, acak_bulat, pilih, acak_urutkan, bibit

# Float acak 0.0 - 1.0
print(acak())              # 0.374...

# Integer acak antara 1 - 10
print(acak_bulat(1, 10))   # 7

# Pilih satu elemen
print(pilih(["apel", "mangga", "jeruk"]))  # "mangga"

# Set seed (bibit)
bibit(42)
print(acak_bulat(1, 100))  # 82
```

## Daftar Fungsi

| Fungsi | Padanan `random` | Deskripsi |
|--------|-----------------|-----------|
| `acak()` | `random()` | Float 0.0 <= x < 1.0 |
| `acak_bulat(a, b)` | `randint(a, b)` | Integer antara a dan b |
| `acak_seragam(a, b)` | `uniform(a, b)` | Float antara a dan b |
| `pilih(urutan)` | `choice(seq)` | Pilih satu elemen |
| `pilih_banyak(urutan, jumlah)` | `choices(seq, k=n)` | Pilih banyak (dengan pengembalian) |
| `contoh(populasi, jumlah)` | `sample(pop, k)` | Sample tanpa pengembalian |
| `acak_urutkan(urutan)` | `shuffle(seq)` | Acak urutan in-place |
| `bibit(n)` | `seed(n)` | Set seed |

## Test

```bash
python -m pytest src/acak/tests/test_acak.py -v
```

## Lisensi

MIT © 2025 annaqibz01
~~~

