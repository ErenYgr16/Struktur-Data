# List Array
beli = ["Tomat","Kangkung","Bayam"]
cetak = beli[2] #ambil value di index ke 2
print(cetak) 

# Perulangan Array
for x in beli: #tercetak semua element value = Tomat,Kangkung,Bayam
    print (x)

# Panjang Array
panjang = len(beli) #len, jumlah value
print(panjang) #output 3

# Append
# Menambahkan Element Array
ambil = []
ambil.append("Mangga")
ambil.append("Jeruk")
print(ambil) #output ["Mangga", "Jeruk"]

# Pop
# Remove element array
sayur = ["Kol","Wortel","Buncis","Toge"]
# Remove Element di Index 0
sayur.pop(0)
print(sayur) #output (Kol,Buncis,Toge)

# Remove All Array Element
bunga = ["Melati","Mawar", "Anggrek"]
# Remove All
bunga.clear() #menghapus semua element
print(bunga) #output []

# Copy Array
motor = ["Yamaha","Honda","Suzuki"]
# Copy to Motor2
motor2 = motor.copy()
print(motor2) #output [Yamaha,Honda,Suzuki]

# Count Array
mahasiswa = ["Harry","John","Maya","Brisya","John"]
# Count
jumlah = mahasiswa.count("John")
print(jumlah) #output 2

# Extend Array
siswa = ["Juki","Ahmad","Roni"]
siswabaru = ["Maya","Ari","Aji"]
# Mengabungkan Array
siswa.extend(siswabaru)
print(siswa)

# Index Array Alement
kota = ["Jakarta","Bandung","Surabaya","Makasar"]
# Cek Posisi Element Surabaya
x = kota.index("Surabaya")
print(x)

# Insert Array Specific Position
fruits = ["apple", "banana", "cherry"]
# Insert Element at Index 1
fruits.insert(1, "orange")
print(fruits)

# Reverse
angka = [1,2,3,4,5]
angka.reverse()
print(angka)

# Sort Array
cars = ["Ford", "BMW", "Volvo"]
angka = [1,6,7,3,2,5]
# Sort Abjad (A-Z)
cars.sort()
# Sort Angka dari Terkecil
angka.sort()
print(cars) #output [BMW, Ford,"Volvo"]
print(angka)