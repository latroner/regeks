# -*- coding: utf-8 -*-
"""rehex.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YbDcdwLTpA_mFx29FVoptZCNT0zhRR-u
"""

import re 
patfh ="/content/Прикл. прогр. (090303++)_ Лабораторная работа № 3 «Регулярные выражения. Работа с Git».html"#input("введите путь: ")

with open(patfh) as f:
  match = re.findall('https?:\/\/(?:\w*)(?:\.[a-z]+)+(?:\/[a-zA-Z0-9.?=&%;\-_]*)*[^,\'.?"}\]]', f.read() ) 
  if match:
    for ssil in match:
      print(ssil)
  else:
    print("ссылок нет")