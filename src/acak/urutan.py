"""
Modul untuk operasi acak pada urutan (sequence).
Berisi fungsi wrapper dari random.choice(), random.choices(), random.sample(), random.shuffle().
"""

import random
from typing import Sequence, Any, List, Optional


def pilih(urutan: Sequence[Any]) -> Any:
    """
    Memilih satu elemen secara acak dari sebuah urutan (list, tuple, string).

    Args:
        urutan: Sebuah urutan (list, tuple, string) yang tidak boleh kosong.

    Returns:
        Satu elemen yang dipilih secara acak dari urutan.

    Raises:
        IndexError: Jika urutan kosong.
    """
    return random.choice(urutan)


def pilih_banyak(urutan: Sequence[Any], jumlah: int, peluang: Optional[Sequence[float]] = None) -> List[Any]:
    """
    Memilih beberapa elemen secara acak dari sebuah urutan (dengan pengembalian).

    Elemen yang sama bisa terpilih lebih dari sekali.

    Args:
        urutan: Sebuah urutan (list, tuple, string).
        jumlah: Jumlah elemen yang akan dipilih.
        peluang: Daftar bobot peluang untuk setiap elemen (opsional).

    Returns:
        List berisi elemen-elemen yang dipilih secara acak.
    """
    if peluang is not None:
        return random.choices(urutan, weights=peluang, k=jumlah)
    return random.choices(urutan, k=jumlah)


def contoh(populasi: Sequence[Any], jumlah: int) -> List[Any]:
    """
    Mengambil sample acak tanpa pengembalian dari sebuah populasi.

    Args:
        populasi: Sebuah urutan (list, tuple) yang berisi elemen-elemen.
        jumlah: Jumlah elemen yang akan diambil (tidak boleh melebihi panjang populasi).

    Returns:
        List berisi elemen-elemen yang dipilih secara acak (unik).

    Raises:
        ValueError: Jika jumlah > panjang populasi.
    """
    return random.sample(populasi, jumlah)


def acak_urutkan(urutan: List[Any]) -> None:
    """
    Mengacak urutan elemen dalam sebuah list (in-place).

    Args:
        urutan: List yang akan diacak urutannya.
    """
    random.shuffle(urutan)
