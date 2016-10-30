MANIPULASI DATA GEOSPASIAL

CRUD

1. Create

2. Retrive, berfungsi untuk melihat isi data geospasial berupa data vektor ESRI yaitu shapefile (.shp)

3. Update

4. Delete



File Data Geospasial terdiri dari:

1. Shp : berisi koordinat / titik

2. Dbf : merupakan sebuah tabel / database

3. Shx : berupa index data 


Ada 2 cara untuk membuka Data Geospasial yaitu :

1. Menggunakan QGIS, dengan cara klik kanan lalu pilih ‘view data’. Akan tetapi terlebih dahulu membuka datanya dengan cara drag and drop.

2. Menggunakan Library pyshp, merupakan library dari bahasa pemrograman python.


Aplikasi yang harus di instal:

1. Python, instal seprti biasa setelah mendownload aplikasinya.

2. Setelah terinstal, lalu instal pip dengan cara buka cmd dan masukan script di bawah ini:

	python -m pip install pyshp

3. Lalu upgrade pip dengan cara ketikkan script di bawah ini:

	python -m pip --upgrade pip

4. Setelah itu kita bisa mulai mengkode.

Jika kita memakai Dos windows maka kita harus menginstal aplikasi phyton terlebih dahulu. Jika kita memakai linux maka tidak perlu lagi menginstal python.


Cara membuka file.shp menggunakan Python dengan mengetikkan script di bawah ini:

 #python

 #import shapefile

 #sf = shapefile.Reader("E:/Countries/countries.shp")

 #shapes = sf.shapes()

 #print len (shapes)


Nb: File countries harus di download terlebih dahulu
