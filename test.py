#!/usr/bin/python3
# -*- coding: utf-8 -*-


from ep60 import *

x = Ep60()
x.head()
x.print_bold('BOLD')
x.LF()
x.print_txt('нормальный текст')
x.print_bold(' жирный в той же строке')
x.LF()
x.print_txt('Українські букви ЄєЇї')
x.LF()
x.print_txt('Русские буквы ЪъЫыЭэЁё')
x.LF()
x.footer()
