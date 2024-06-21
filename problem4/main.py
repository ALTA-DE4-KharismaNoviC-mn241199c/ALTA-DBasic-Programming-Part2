'''
Input Harga: 370000
Input Diskon: 15
Output: harga yang harus dibayar adalah Rp. 314.500
'''

def harga_akhir(harga_awal,diskon):
    harga_akhir = harga_awal - diskon
    return harga_akhir

#harga akhir sesudah diskon
harga_awal = float(input("Enter Harga =  "))
diskon_awal = float(input("Enter Diskon =  "))

harga_sesudah_diskon = harga_akhir(harga_awal , diskon_awal)
print("harga_yang_harus_dibayar =  ", harga_sesudah_diskon)
