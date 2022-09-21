tautan menuju aplikasi Heroku: https://pbp-tugas.herokuapp.com/mywatchlist

**Jelaskan perbedaan antara JSON, XML, dan HTML!**
JSON mampu untuk menyimpan data secara efisien karena menggunakan dictionary sebagai struktur data penyimpanannya, tetapi tampilannya terlihat kurang rapi, sedankan XML menampilkannya dalam bentuk markup language sehingga terlihat lebih rapi, tetapi tidak seefisien JSON. Sementara itu, HTML lebih menitikberatkan data delivery format tampilannya dalam situs.

**Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
Agar dapat memberikan akses pada pengguna lain untuk melihat data yang ada dalam aplikasi yang telah dibuat oleh developer.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
markup: - Menginisiasi aplikasi mywatchlist dengan python manage.py startapp mywatchlist
        - Membuat model data-data watchlist pada models.py
        - Menambahkan database JSON yang berisi 10 data-data film
        - Membuat fungsi yang me-render HTML serta men-deliver data-data tersebut dalam bentuk JSON dan XML
        - Menyusun template HTML untuk menampilkan data-data tadi
        - Menambahkan routing baru ke aplikasi mywatchlist, HTML, XML, dan JSON-nya pada urls.py
        - Melakukan migrasi dan load data
        - Menjalankan python manage.py runserver dan membuka localhost:8000 untuk menguji aplikasinya
        - Menambahkan python manage.py loaddata initial_watchlist_data.json pada PROCFILE agar data-datanya dapat muncul ketika di-deploy ke heroku
        - Membuat unit test menggunakan client dan cek responnya apakah mengembalikan HTTP 200 OK
        - Commit ke GitHub

**Akses ketiga URL menggunakan Postman**
[HTML](Postman HTML.png)

[XML](Postman XML.png)

![JSON](Postman JSON.png)
