Latar Belakang :
Pemanfaatan sistem geografis yang ada pada sistem digital dapat menggunakan berbagai macam cara. Terlebih dengan banyaknya media yang sudah menyediakan map sesuai dengan keinginan kita, diantaranya yaitu Maps. Setiap orang kini sudah tahu apa itu google maps. Kebutuhan akan maps ini seolah-olah sudah menjadi kebutuhan primer setiap orang, namun ternyata kita bisa membuatnya secara custom, sesuai dengan kebutuhan kita.

1. Cara Menjalankan Map Proxy dan Map Server
Solusi :
1. Ketika hendak menampilkan data geografis, kita perlu menyiapkan terlebih dulu apa yang akan ditampilkan di Map Proxy. Kalian dapat mendownload data geospasial pada link di bawah ini.
http://www.halaman.download/p/gis.html
Lalu klik "Producer", kemudian klik "Indonesia Mapproxy".
2. Setelah mendownload file tersebut hal yang penting lainnya yaitu mengekstrak file tersebut. Supaya file yang telah anda download dapat anda ubah. Simpan file pada direktori Downloads.

3. Kemudian buka file agm.yaml pada direktori Downloads/indomap/mapproxy.
4. Lalu edit file agm.yaml, sesuaikan dengan direktori tempat anda menyimpan filenya:
- Ubah baris di bawah ini
	binary: /usr/libexec/mapserver
 menjadi
	binary: /usr/lib/cgi-bin/mapserv
- Lalu ubah juga pada baris di bawah ini
	map: var/mapdata/mapfile/indo.map
 menjadi
	map: /home/syarahulyaa/Downloads/indomap/mapfile/indo.map
- Kemudian buat direktori baru dengan nama tmp pada Downloads/indomap
- Lalu ubah baris di bawah ini
	working_dir: /var/mapdata/tmp
 menjadi
	/home/syarahulyaa/Downloads/indomap/tmp
- Kemudian simpan.

5. Lalu pada direktori mapproxy (di terminal/cmd), gunakan perintah :
	vi mapproxy.ini
- Kemudian ubah baris di bawah ini
	chdir = /var/mymapproxy/
 menjadi
	chdir = /home/syarahulyaai/Downloads/indomap/mapproxy
- Lalu simpan.
6. Kemudian ubah file config.py pada direktori Downloads/indomap/mapproxy
- Lalu ubah baris di bwah ini
	application = make_wsgi_app(r'/var/mymapproxy/agm.yaml')
 menjadi
	application = 	make_wsgi_app(r'/home/syarahulyaa/Downloads/indomap/mapproxy/agm.yaml')
7. Lalu untuk menjalankan program dapat menggunakan perintah di bawah ini.
	uwsgi mapproxy.ini
8. Kemudian untuk mengecek mapproxy sudah terinstall dapat dilakukan dengan cara membuka browser kemudian ketik localhost:8080
9.  Kemudian klik demo atau ketikan url localhost:8080/demo
10. Terakhir pada bagian WMTS klik di bawah Image Format yaitu png, tunggu sampai gambar petanya muncul.

Kesimpulan
Pada pertemuan ke-7, kita dapat mengetahui bagaimana cara menginstal dan menjalankan map server juga map proxy pada Sistem Operasi Ubuntu dalam VirtualBox.

Saran
Perdalam lagi wawasan serta pemahaman dari banyak sumber seperti buku ataupun pustaka yang terdapat di internet.
