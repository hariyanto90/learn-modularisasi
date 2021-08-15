# menghitung luas segitiga dengan rumus alas * tinggi / 2
from geometrik.hitung_luas_segitiga import hitung_luas_segitiga
from geometrik.hitung_luas_persegi_panjang import hitung_luas_persegi_panjang

print('Program Menghitung Luas Segitiga')
user_input = int(input('Masukkan alas : '))
user_input1 = int(input('Masukkan tinggi: '))

output_hitung_luas_segitiga = hitung_luas_segitiga(user_input, user_input1)
print(output_hitung_luas_segitiga)
# print(f'diketahuai luas segitiga adalah = {geometrik (user_input, user_input1)} ')
print('=' * 100)

print('Program Menghitung Luas Persegi Panjang')
input_panjang = int(input('Masukkan panjang : '))
input_lebar = int(input('Masukkan lebar: '))

output_hitung_luas_persegi_panjang = hitung_luas_persegi_panjang(input_panjang, input_lebar)
print(output_hitung_luas_persegi_panjang)
