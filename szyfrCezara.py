# -*- coding: utf-8 -*-
import fileinput
import string

table = string.maketrans('abcdefghijklmnopqrstuwxyz ','ghijklmnopqrstuwxyzabcdef ')
tekst_jawny = "tekst jawny niezaszyfrowany super fajny i malo tajny"

def zaszyfruj(jawny):
    zaszyfrowany = ''
    for line in jawny:
        #line = line.rstrip()
        zaszyfrowany += string.translate(line,table)
    return zaszyfrowany

print zaszyfruj(tekst_jawny)

