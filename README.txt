************************ README ************************
IF4031 - Pengembangan Aplikasi Terdistribusi
Tugas 2 :
	Aplikasi IRC sederhana berbasis AMQP
	menggunakan RabbitMQ server

Abraham Krisnanda - 13510033
Anasthasia Amelia - 13510093
	
--------------------------------------------------------
CARA MENJALANKAN PROGRAM (Windows 8):
--------------------------------------------------------
1. Pastikan pyhton sudah terdaftar di dalam PATH pada environment variable system anda. Apabila belum, lakukan hal berikut:
	- Buka Control Panel, pilih System.
	- Klik Advance System Settings
	- Buka Environment Vaiables...
	- edit Path pada System variables. Ketikkan direktori python.
		contoh: C:\Python27\;
	- klik Ok
2. Buka Command Prompt dengan  menekan tombol Windows+R. Ketikkan cmd, lalu klik OK.
3. Pindah ke direktori di mana file/script akan dijalankan.
4. Jalankan program dengan mengetik sesuai format: pyhton <namafile.py>
	contoh: pyhton patmirc_13510033_13510093.py
	lalu tekan enter.
5. Jalankan program sesuai spesifikasi.

--------------------------------------------------------
DAFTAR TES
--------------------------------------------------------
Fitur yang diuji: /NICK, /JOIN, /LEAVE, /EXIT
* nickname akan dibangkitkan secara random oleh aplikasi saat pertama kali dijalankan
lakukan command di bawah secara bergantian per baris per window, dari window #1 sampai window #3

1. WINDOW #1
Untuk menguji program, ketikkan command berikut setelah menjalankan program sesuai petunjuk sebelumnya:
/NICK amel
/JOIN basdat
/JOIN sister
@basdat hi ken
@sister ayo kerjakan tugas 2
coba broadcast ah
@basdat iya ken. ada urusan tiba-tiba. leave juga ya.
/LEAVE basdat
/EXIT

2. WINDOW #2
Untuk menguji program, ketikkan command berikut setelah menjalankan program sesuai petunjuk sebelumnya:
/NICK bram
/JOIN basdat
/JOIN sister
@basdat halo asisten basdat!
@sister hari ini beres
/LEAVE basdat
/EXIT


3. WINDOW #3
Untuk menguji program, ketikkan command berikut setelah menjalankan program sesuai petunjuk sebelumnya:
/NICK kenny
/JOIN basdat
@basdat hi all!
@basdat hehe
/JOIN lab
@basdat bram leave?
/EXIT

--------------------------------------------------------
HASIL EKSEKUSI TES PROGRAM
--------------------------------------------------------
1. WINDOW #1
C:\Users\Anasthasia Amelia\Desktop\miniIRC>python patmirc.py
your nickname: DVKZ6A
/NICK amel
your nickname: amel
/JOIN basdat
your list of channels: [basdat]
you've just joined Channel: basdat
[basdat] (amel has just joined basdat)
[basdat] (bram has just joined basdat)
[basdat] (kenny has just joined basdat)
/JOIN sister
your list of channels: [basdat, sister]
you've just joined Channel: sister
[sister] (amel has just joined sister)
[sister] (bram has just joined sister)
[basdat] (kenny) hi all!
@basdat hi ken

[basdat] (amel) hi ken
[basdat] (bram) halo asisten basdat!
[basdat] (kenny) hehe
@sister ayo kerjakan tugas 2

[sister] (amel) ayo kerjakan tugas 2
[sister] (bram) hari ini beres
coba broadcast ah
[basdat] (amel) coba broadcast ah
broadcast coba broadcast ah[basdat, sister]
[sister] (amel) coba broadcast ah
[basdat] (bram has just leaved basdat)
[basdat] (kenny) bram leave?
@basdat iya ken. ada urusan. leave juga ya.

[basdat] (amel) iya ken. ada urusan. leave juga ya.
/LEAVE basdat
[basdat] (amel has just leaved basdat)
your list of channels: [sister]
you've just leaved Channel: basdat
/EXIT

--------------------------------------------------------
2. WINDOW #2
C:\Users\Anasthasia Amelia\Desktop\miniIRC>python patmirc.py
your nickname: 49D71E
/NICK bram
your nickname: bram
/JOIN basdat
your list of channels: [basdat]
you've just joined Channel: basdat
[basdat] (bram has just joined basdat)
[basdat] (kenny has just joined basdat)
/JOIN sister
your list of channels: [basdat, sister]
you've just joined Channel: sister
[sister] (bram has just joined sister)
[basdat] (kenny) hi all!
[basdat] (amel) hi ken
@basdat halo asisten basdat!

[basdat] (bram) halo asisten basdat!
[basdat] (kenny) hehe
[sister] (amel) ayo kerjakan tugas 2
@sister hari ini beres

[sister] (bram) hari ini beres
[basdat] (amel) coba broadcast ah
[sister] (amel) coba broadcast ah
/LEAVE basdat
[basdat] (bram has just leaved basdat)
your list of channels: [sister]
you've just leaved Channel: basdat
/EXIT

--------------------------------------------------------
3. WINDOW #3
C:\Users\Anasthasia Amelia\Desktop\miniIRC>python patmirc.py
your nickname: RZ6ZOE
/NICK kenny
your nickname: kenny
/JOIN basdat
your list of channels: [basdat]
you've just joined Channel: basdat
[basdat] (kenny has just joined basdat)
@basdat hi all!

[basdat] (kenny) hi all!
[basdat] (amel) hi ken
[basdat] (bram) halo asisten basdat!
@basdat hehe

[basdat] (kenny) hehe
/JOIN lab
your list of channels: [basdat, lab]
you've just joined Channel: lab
[lab] (kenny has just joined lab)
[basdat] (amel) coba broadcast ah
[basdat] (bram has just leaved basdat)
@basdat bram leave?

[basdat] (kenny) bram leave?
[basdat] (amel) iya ken. ada urusan. leave juga ya.
/EXIT

