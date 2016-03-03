# -*- coding: utf-8 -*-

tekst_jawny = "To jest tekst jawny i jest on bardzo jawny i czytelny. A dodatkowo sensowny"
klucz = 31


i=0

def zaszyfruj(jawny,klucz):
    zaszyfrowany = ""
    for i in range(len(tekst_jawny)):
        if ord(jawny[i]) > 122 - klucz:
            zaszyfrowany += chr(ord(jawny[i]) + klucz - 26)
        else:
            zaszyfrowany += chr(ord(jawny[i]) + klucz)
    return zaszyfrowany

    i+=1

print zaszyfruj(tekst_jawny,klucz)

