BELAJAR CARA PEMBUATAN METHOD DAN
CLASS RETRIEVE DATA GEOSPASIAL
  
1. Penjelasan Retrive Data, Shapefile, dan Geometri.

a. Retrive Data

Retrieve Data yaitu melihat isi data geospasial berupa data vektor dengan shapefile ESRI ekstensi (.shp). Retrieve data menggunakan library pyshp dari bahasa pemrograman python.

b. Shapefile

Shapefile merupakan standart file data vektor oleh ESRI yang dibagi menjadi 2, diantaranya : 
 
Dalam postingan saya yang sebelumnya, data koordinat yang membentuk bangun datar atau ruang dapat di bentuk oleh :

1) Titik

2) Garis, merupakan kumpulan titik.

3) Polygon, yaitu kumpulan dari garis.

2. Penjelasan Operasi Pengambilan Data (.shp).

a. Operasi Pengambilan Data pada Library pyshp dengan cara sebagai berikut :

1) Membuka script di bawah ini :

2) SF = Shapefile.reader(“hello.shp”)

		Ket :

		SF = variabel perancangan

		Shapefile = class

		reader = method

		hello.shp = input file shp

b. Method of DBF

1) fields

2) record (n)

3) Record (n) pada baris ke-n records

c. Method of SHP

1) shapes() - menampilkan semua data

2) shape(n) - menampilkan data dengan menggunakan parameter

a) bbox (boading box), yaitu batas view pada peta.
 
b) parts, suatu record merupakan bagian dari record atau pecahan relasi yang mana.

c) points, yaitu titik koordinat pembentuk peta. 

d) shape type, adalah jenis geometri dari points.

3. Penggunaan Class dan Method

Untuk memahami class dan method, mari kita lakukan latihan di bawah ini :

a. Menampilkan jumlah semua record dengan menggunakan python cmd (CommandPrompt).

b. Menampillkan jumlah semua record dengan menggunakan pyshp.

	1) Membuat file script2.py seperti gambar di bawah ini (simpan di E:\Countries)

 	2) Menjalankan script.py dengan menggunakan cmd (CommandPrompt)
 
c. Menampilkan urutan record dengan menggunakan class geospasial editor.

	1) Membuat script2.py

 	2) Mengecek kesalahan pada cmd dan mencoba menjalankannya