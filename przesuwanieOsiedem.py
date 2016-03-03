# -*- coding: utf-8 -*-
import string

tekst_jawny = "tekst jawny niezaszyfrowany super fajny i malo tajny"

table = string.maketrans('abcdefghijklmnopqrstuwxyz','hijklmnopqrstuwxyzabcdefg')
reverse_table = string.maketrans('abcdefghijklmnopqrstuwxyz','stuwxyzabcdefghijklmnopqr')


def przesun(tekst, tabela):
    przesuniety = ''
    for line in tekst:
        przesuniety += string.translate(line,tabela)
    return przesuniety

def sprawdzPrzesuniecia(zaszyfrowany):
    for i in range(1,5):
        temp = zaszyfrowany
        for j in range(1,i):
            temp = przesun(temp,table)
        print temp

zaszyfrowany = przesun(tekst_jawny,reverse_table)
zaszyfrowany = przesun(zaszyfrowany, reverse_table)
sprawdzPrzesuniecia(zaszyfrowany)