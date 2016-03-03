# -*- coding: utf-8 -*-

tekst_jawny = "To jest tekst jawny i jest on bardzo jawny i czytelny. A dodatkowo sensowny"
przesuniecie = 7

def zaszyfruj(jawny,klucz):
    zaszyfrowany = ""
    for i in range(len(tekst_jawny)):
        if ord(jawny[i]) > 122 - klucz:
            zaszyfrowany += chr(ord(jawny[i]) + klucz - 26)
        else:
            zaszyfrowany += chr(ord(jawny[i]) + klucz)
    return zaszyfrowany


def odszyfruj(zaszyfrowany, przesuniecie):
    for i in range(len(zaszyfrowany)):
        if ord(zaszyfrowany[i]) > 122 - klucz:
            zaszyfrowany += chr(ord(jawny[i]) + klucz - 26)
        else:
            zaszyfrowany += chr(ord(jawny[i]) + klucz)
    return zaszyfrowany

print odszyfruj(zaszyfruj(tekst_jawny,7),7)

