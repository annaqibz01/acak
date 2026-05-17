"""
acak — Library Random Berbahasa Indonesia

Wrapper untuk modul random Python dengan antarmuka berbahasa Indonesia.
"""

from acak.dasar import acak, acak_bulat, acak_seragam, bibit
from acak.urutan import pilih, pilih_banyak, contoh, acak_urutkan

__all__ = [
    "acak",
    "acak_bulat",
    "acak_seragam",
    "bibit",
    "pilih",
    "pilih_banyak",
    "contoh",
    "acak_urutkan",
]

__version__ = "0.1.0"
