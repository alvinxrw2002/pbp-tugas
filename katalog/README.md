**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;**

![Alur web berbasis Django](https://ibb.co/dcnt1Cg)
Dalam bagan tersebut, request akan muncul ketika user mengklik link aplikasinya. Setelah itu, URL (urls.py dalam project ini) akan mengarahkannya ke view (views.py). Views.py kemudian akan merender template katalog.html dengan data yang ada pada variabel context, yaitu nama, id, dan barang-barang katalog. Model data (class/object) barang-barang katalog tersebut ada pada models.py, dan instance-instancenya terdapat pada database (file json di folder fixtures).


**Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**

Virtual environment diperlukan untuk mencegah perbedaan versi package-package yang diinstall. Tanpa menggunakan virtual environment, package akan terinstall secara global sehingga jika ada project-project jango lain yang berbeda versi misalnya, perlu menginstall ulang versi yang sesuai untuk bisa menjalankan projek tersebut dan nantinya jika ingin kembali ke projek awal, perlu untuk menginstall ulang lagi versi django yang sesuai. Jadi, tanpa virtual environment-pun sebenarnya tetap bisa membuat web berbasis django, tetapi lebih dianjurkan menggunakan virtual environment untuk mencegah permasalahan tadi.

 

**Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.**

1. Membuat suatu fungsi bernama show_katalog yang menerima parameter berupa request dan mengembalikan fungsi render dengan parameter request, nama base html (katalog.html), dan data / tabel yang tentunya akan me-render request ke base html beserta tabel-nya.

 

2. Mengarahkan url ke arah aplikasi katalog dengan membuat path pada urls.py

 

3. Menyesuaikan nama variabel di base html dan views.py untuk nama, id, serta melakukan iterasi untuk setiap barang yang ada di tabel views.py untuk ditampilkan attribute-nya sehingga terbentuk tabel pada html.

 

4. Membuat secrets baru di gitlab berupa nama aplikasi (HEROKU_APP_NAME, pbp-tugas) dan api key (HEROKU_API_KEY, <API key di akun saya>) dengan name dan value yang sesuai.