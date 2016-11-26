CRUD DATA GEOSPASIAL


 


Latar Belakang Masalah :
Pada Implementasi Sistem Informasi Geografis (Geography Information System) banyak hal yang dapat dilakukan. Namun untuk memulainya kita harus belajar terlebih dahulu bagaimana cara memanipulasi data CRUD (Create, Retrieve, Update, Delete). Kali ini saya akan mengajak anda mempelajari bagaimana cara penggunaan data shapefile geospasial menggunakan CRUD.

1. Bagaimana Cara Create shapefile?
2. Bagaimana Cara Update shapefile?
3. Bagaimana Cara Delete shapefile?

CREATE DATA GEOSPASIAL
Dalam pembuatan data geospasial kita akan menggunakan lybrari pyshp dan membutuhkan file filename.shp beserta file filename.dbf.
Langkah-langkah yang harus dilakukan, seperti di bawah ini:
1. Meng-import shapefile
2. Meng-instansiasi writer method
    Caranya :
Sf = shapefile.Writer(param)
Param disini dengan memilih shapetype di bawah ini:
a. shapeType = 1
b. shapeType = 3
c. shapeType = 5
3. Melakukan method dbf dan shp sama seperti read.

Pada Shapefile (shp)
Untuk menambahkan record (ESRI)
1. sf.point (x,y)
3. sf.line = (parts: [[x,y],[z,w],...])
5. sf.poly = (parts: [[x,y],[z,w],...])

Pada Databasefile (dbf)
Langkah yyang dapat dilakukan yaitu :
1. Membuat atribut terlebih dahulu kemudian menambahkan record.
Contoh:
sf.field (‘Name Field’, ’C’, ’40’)
Maksudnya C adalah Character atau tipe datanya, dan 40 adalah length atau panjang data. Pada contoh di atas dapat diartikan bahwa nama field dengan panjang 40 karakter.
2. Menambahkan record  seperti contoh di bawah ini
sf.record(‘Bandung’)
sf.record(‘Bandung’,’Sarijadi’)
3. Setelah selesai selanjutnya simpan dengan intruksi seperti di bawah ini:
sf.save(‘namefile.shp’)

UPDATE/EDIT DATA GEOSPASIAL
Editor merupakan alat yang digunakan untuk melakukan editing pada shapefile. Contohnya yaitu delete road. Selain itu ada writer yang merupakan sebuah method yang ada di shapefile untuk membuat file shp baru (shp dan dbf). Di bawah ini merupakan langkah-langkah untuk melakukan editing.
Import shape file
Sf = shape file.editor(warnas.shp)
Sf.point(17,12,0,0)
Sf.record (‘sunda’)
Sf.save
Sf.save (‘warnas.shp’)
a=shapefile.reoder(‘warnas.shp’)
a.recorders()
a.shapes().points
a.shape()[0]
a.shape()[0] points

[(10,0,10,0)]

DELETE DATA GEOSPASIAL
Sf.delete(0)
a.shapes()[0].points [(10,0,10,0)]
sf.points [17,12,0,0]
sf.record(‘sunda’)
sf.saver(‘wrns.shp’)

Penutup
Kesimpulan
Pada kali ini kita dapat mengetahui bagaimana cara membuat (CRUD) Data Geospasial.

Saran
Untuk lebih memahaminya anda dapat melakukan praktek sendiri.

