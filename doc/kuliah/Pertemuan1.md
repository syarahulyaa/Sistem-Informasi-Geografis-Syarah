<h2 align="center">TUTORIAL GITHUB</h2> 
<p align="justify">
<strong>Membuat SSH KEYS</strong>
<br>
1. Buka github masuk ke setting, buka sub <strong><i>ssh and gpg keys</i></strong>.
<br>
2. Buka tab baru <strong><i>generating ssh keys</i></strong> dan <strong><i>new ssh keys</i></strong>.
<br>
3. Kemudian klik kanan dimana saja, => <strong>Git bash here</strong>.
<br>
4. Buka generating a new ssh key and ... lalu salin perintah
	<strong>ssh-keygen -t rsa -b 4096 -C "<i>your_email@example.com</i>"</strong>
	ganti email diatas dengan alamat email github anda.
<br>
5. Kemudian enter terus masukkan perintah
<strong>cat ~/.ssh/id_rsa.pub</strong>
<br>
6. Setelah itu, salin hasilnya ke kolom key lalu beri judul dan tekan tombol add ssh key.
<br>
<br>
Membuat Folder Kerja
1. Masukkan perintah "git init" untuk menginisialisasi.
2. Lalu masukkan perintah "git remote add origin (link repository by ssh)" (pada repository di github)
3. Masukkan "git pull origin master" untuk mengunduh file-file yang ada pada repository.
4. Di dalam folder Kapita Selekta buat folder bernama doc.
   Kemudian di dalam folder doc buat kembali folder yang bernama kuliah.
   Selanjutnya buat file dengan nama pertemuan1.md
5. Ketikkan "git status" untuk mengetahui perubahan yang ada.
6. Kemudian ketikkan "git add doc/".
7. Ketikkan kembali "git status" untuk mengetahui folder yang ada di dalam folder doc.
8. Kemudian ketikkan "git add doc/kuliah/pertemuan1.md".
9. Laku ketikkan "git status" (jika muncul:On branch master Changes to be committed) langsung ketikkan perintah selanjutnya.
9. Lalu "git commit -m "menambahkan pertemuan1"" -m disini untuk menambahkan message.
10.Kemudian "git status" kembali, (jika muncul:nothing to commit, working tree clean) langsung ketikkan perintah di bawah ini.
11.Terakhir, ketikkan "git push origin master" untuk mensinkronisasi file yang sudah ditambahkan.
<br>
<br>
<strong>Create Organization</strong>
<br>
1. Klik tanda plus=> <i><strong>Create Organization</strong></i>
<br>
2. Masukan Judul Organisasi dan email kemudian enter.
<br>
3. Masukkan anggota kelompok beserta koordinator proyek 2.
<br>
4. Untuk merubah profil dari organization masuk ke setting.
<br>
5. Anggota yang di invite harus terlebih dahulu menyetujuinya.
</p>