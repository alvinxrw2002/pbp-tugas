# Tugas 4
tautan menuju aplikasi Heroku: https://pbp-tugas.herokuapp.com/todolist<br>

**Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?**<br>
CSRF token digunakan untuk mencegah serangan CSRF, yaitu ketidaksengajaan pengguna ketika mengirimkan request melalui web, seperti saat mengisi form. Dengan adanya token CSRF, server dapat menggunakannya sebagai informasi tambahan untuk memastikan bahwa request tersebut berasal dari pengguna yang terotorisasi atau bukan.<br>

**Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.**<br>
Bisa, tetapi harus membuat setiap inputnya dalam format table. Misalnya:
```html
    <table>
        <tr>
            <td>Title: </td>
            <td><input id="title" type="text" name="title" value="{{ title }}"></td>
        </tr>

        <tr>
            <td>Description: </td>
            <td><input id="description" type="text" name="description" value="{{ description }}"></td>
        </tr>
    </table>
```
<br>

**Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.**<br>
Setelah pengguna menekan tombol atau link menuju form, terbentuk request ke path tertentu. Lalu, django akan mencari fungsi mana pada views yang menghandle form tsb. sehingga template HTML-nya dapat ditampilkan. Setelah user mengisi dan submit form, akan terbentuk request-request berupa HTTP request, method, dan argumen yang mengarahkan pada url tertentu. Kemudian, jalankan fungsi yang sesuai pada views untuk mengolah data-data dari form tersebut, meyimpan, lalu menampilkannya pada template HTML.<br>

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**<br>
1. Menginisiasi aplikasi todolist dengan python manage.py startapp mywatchlist dan tambahkan pada settings.py di folder project_django

2. Membuat model Task dan TaskForm untuk membuat task baru

3. Menyusun template HTML untuk login, logout, membuat task baru, dan menampilkan todolist.

4. Membuat fungsi-fungsi yang sesuai dengan keperluan pada template HTML tsb:
    * show_todolist: mengambil data-data bermodel Task pada database sesuai dengan user yang sedang login untuk ditampilkan dalam bentuk tabel
    * register: mendaftarkan pengguna baru melalui Form dengan method POST
    * login_user: meng-autentikasi username dan password untuk login ke aplikasi dengan username dan password tsb.
    * logout_user: mengeluarkan pengguna dari aplikasi dan menghapus session serta cookie-nya
    * create_task: menampilkan form untuk membuat task baru, kemudian menyimpannya ke dalam database dalam bentuk objek Task.
    
5. Menambahkan routing untuk aplikasi todolist pada project_django.urls.py dan routing fungsi-fungsinya pada todolist.urls.py

6. Commit ke GitHub untuk men-deploy di Heroku

7. Daftarkan 2 pengguna dan login untuk menambahkan 3 task pada kedua pengguna tsb.

# Tugas 5
**Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?**<br>
* Inline css merupakan styling css yang diberikan kepada suatu elemen html tepat di tag-nya langsung. Pemberian style css dengan cara seperti ini kurang efektif apabila terdapat banyak sekali style yang diberikan karena akan membuat file html menjadi berantakan dan terkesan kurang rapi, tetapi akan lebih bermanfaat jika hanya ingin memberikan satu buah style atau satu buah elemen saja untuk sekadar pengujian, perbaikan, atau melihat perubahan sekilas

* Internal css juga dibuat dalam satu file html. Namun, bukan ditumpuk pada tag spesifiknya, melainkan di tulis secara terpisah di antara tag head. Untuk menargetkan elemen html, bisa dengan menggunakan berbagai selector seperti class dan id. Style ini hanya bisa terjadi pada satu halaman sehingga tidak perlu menunggah beberapa file. Namun, ini menjadi tidak efisien apabila ingin menggunakan css yang sama untuk beberapa halaman.

* Eksternal css menggunakan file .css terpisah untuk memberikan style-nya. Dalam satu file ini, styling apapun dapat ditampilkan ke situsnya secara keseluruhan. File tersebut dihubungkan dengan cara memberikan link rel pada bagian head html-nya. Hal ini dapat membuat file html menjadi lebih rapi karena tidak ada styling css pada tag atau head-nya. Selain itu, satu file .css juga dapat digunakan untuk seluruh file html yang dibuat sehingga lebih efisien. Namun, apabila menggunakan ekternal css, perlu menyelesaikan pemanggilan file css-nya sebelum halaman dapat ditampilkan secara sempurna sehingga memerlukan sedikit lebih banyak waktu.<br>

**Jelaskan tag HTML5 yang kamu ketahui.**<br>
Beberapa tag html yang paling mendasar yaitu:
* ```<head>``` untuk membuat informasi tentang dokumen
* ```<body>```untuk membuat tubuh dari suatu halaman
* ```<h1 - h6>``` untuk membuat heading
* ```<p>``` untuk membuat paragraf
* ```<br>```untuk membuat new line
<br>

**Jelaskan tipe-tipe CSS selector yang kamu ketahui.**<br>
* tag selector: memilih elemen berdasarkan tagnya
* class selector: memlih elemen berdasarkan class yang didefinisikan pada sebuah elemen dengan tanda .
* ID selector: memilih elemen berdasarkan ID-nya dengan tanda #
* Attribute selector: memilih elemen berdasarkan attribute-nya, seperti input, dsb
* Universal selector: memilih semua elemen, biasa digunakan untuk menghilangkan styling css bawaan
<br>

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**<br>
1. Menginisiasi bootstrap dengan meletakkan link css dan js-nya pada dalam head base.html
2. Menggunakan class-class tertentu untuk membuat style sesuai keinginan pada elemen button, div, dsb.
3. Memberi id selector pada tag tertentu yang hendak diberikan style css tersendiri untuk responsive dan hover
4. Memberikan styling responsive dan hover sesuai elemen yang telah diberi id selecor sebelumnya
5. Menambahkan sedikit style lain pada beberapa elemen seperti background, background-color, border-radius, dan lain-lain
<br>