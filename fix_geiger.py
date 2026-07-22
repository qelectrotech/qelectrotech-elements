import re

fpath = r'd:\aplicativos\Qeletrotech_Elementos\qelectrotech-elements\10_electric\20_manufacturers_articles\arduino\tube_geiger_j305b.elmt'
with open(fpath, 'rb') as f:
    raw = f.read()

new_text = 'Tubo detector Geiger-Muller J305B (sensor de radiao ionizante)'.encode('utf-8')
new_text = 'Tubo detector Geiger-M\u00fcller J305B (sensor de radia\u00e7\u00e3o ionizante)'.encode('utf-8')
pattern = re.compile(b'<name lang="pt_BR">(.*?)</name>')
new_raw = pattern.sub(b'<name lang="pt_BR">' + new_text + b'</name>', raw)

with open(fpath, 'wb') as f:
    f.write(new_raw)
print('Fixed: tube_geiger_j305b.elmt')
