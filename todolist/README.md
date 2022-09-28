tautan menuju aplikasi Heroku: https://pbp-tugas.herokuapp.com/todolist<br>
informasi akun:
* username 1: dummy1 || username 2: dummy2 || password (both): dummyfortesting123
* username admin: admin || pass: admin123

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