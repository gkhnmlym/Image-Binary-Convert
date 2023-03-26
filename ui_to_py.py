from PyQt5 import uic

with open('Designer.py', 'w', encoding="utf-8") as fout:
   uic.compileUi('Designer.ui',fout)
