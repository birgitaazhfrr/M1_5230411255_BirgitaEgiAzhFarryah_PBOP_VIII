#Menghitung luas persegi
def persegi(sisi): 
    luas = sisi * sisi
    return luas
sisi = 12
luas = persegi(sisi)
print(f"luas persegi dengan sisi {sisi} adalah {luas}")

#menghitung luas bangun limas
def limas_alas(sisi, tinggi):
    luas = (1/3) * sisi * tinggi
    return luas
sisi = 12
tinggi = 21
luas = limas_alas(sisi, tinggi)
print(f"luas limas dengan sisi {sisi} dan tinggi {tinggi} adalah {luas}")


