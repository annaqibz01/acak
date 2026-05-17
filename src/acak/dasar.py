"""
Modul dasar untuk fungsi acak sederhana.
Berisi fungsi wrapper dari random.random(), random.randint(), random.uniform(), dll.
"""

import random


def acak() -> float:
    """Mengembalikan bilangan float acak N sehingga 0.0 <= N < 1.0."""
    return random.random()


def acak_bulat(a: int, b: int) -> int:
    """
    Mengembalikan bilangan bulat acak N sehingga a <= N <= b.

    Args:
        a: Batas bawah (inklusif).
        b: Batas atas (inklusif).

    Returns:
        Bilangan bulat acak antara a dan b.
    """
    return random.randint(a, b)


def acak_seragam(a: float, b: float) -> float:
    """
    Mengembalikan bilangan float acak N sehingga a <= N <= b.

    Args:
        a: Batas bawah (inklusif).
        b: Batas atas (inklusif).

    Returns:
        Bilangan float acak antara a dan b.
    """
    return random.uniform(a, b)


def bibit(n: int) -> None:
    """
    Menyetel seed (bibit) generator angka acak.

    Gunakan fungsi ini agar hasil acak dapat direproduksi.

    Args:
        n: Nilai seed (bilangan bulat).
    """
    random.seed(n)
