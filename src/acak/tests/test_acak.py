"""Unit test untuk library acak."""

import pytest
from acak import acak, acak_bulat, acak_seragam, pilih, pilih_banyak, contoh, acak_urutkan, bibit


class TestAcak:
    def test_acak_kembali_float(self):
        """acak() harus mengembalikan float antara 0 dan 1."""
        hasil = acak()
        assert isinstance(hasil, float)
        assert 0.0 <= hasil < 1.0

    def test_acak_bulat_range(self):
        """acak_bulat(a, b) harus mengembalikan integer dalam range."""
        hasil = acak_bulat(1, 10)
        assert isinstance(hasil, int)
        assert 1 <= hasil <= 10

    def test_acak_seragam_range(self):
        """acak_seragam(a, b) harus mengembalikan float dalam range."""
        hasil = acak_seragam(1.5, 5.5)
        assert isinstance(hasil, float)
        assert 1.5 <= hasil <= 5.5

    def test_bibit_reproduksibel(self):
        """bibit() harus membuat hasil reproducible."""
        bibit(42)
        a1 = acak_bulat(1, 100)
        bibit(42)
        a2 = acak_bulat(1, 100)
        assert a1 == a2


class TestPilih:
    def test_pilih_satu(self):
        """pilih() harus memilih satu elemen dari list."""
        buah = ["apel", "mangga", "jeruk"]
        hasil = pilih(buah)
        assert hasil in buah

    def test_pilih_banyak_jumlah(self):
        """pilih_banyak() harus mengembalikan list dengan jumlah sesuai."""
        buah = ["apel", "mangga", "jeruk"]
        hasil = pilih_banyak(buah, jumlah=5)
        assert len(hasil) == 5
        for item in hasil:
            assert item in buah


class TestContoh:
    def test_contoh_tanpa_pengembalian(self):
        """contoh() harus mengembalikan elemen unik."""
        populasi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        hasil = contoh(populasi, 3)
        assert len(hasil) == 3
        assert len(set(hasil)) == 3  # semua unik

    def test_contoh_error(self):
        """contoh() harus raise ValueError jika jumlah > populasi."""
        with pytest.raises(ValueError):
            contoh([1, 2, 3], 5)


class TestAcakUrutkan:
    def test_acak_urutkan_in_place(self):
        """acak_urutkan() harus mengubah urutan list in-place."""
        buah = ["apel", "mangga", "jeruk", "durian"]
        salinan = buah.copy()
        acak_urutkan(buah)
        assert sorted(buah) == sorted(salinan)  # isi sama, urutan mungkin beda
