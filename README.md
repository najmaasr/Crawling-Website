**Crawling Website - Tempo.com and CNN Indonesia
Najma Syarifa Rahmah**

---

**Deskripsi**

Program ini adalah sebuah alat yang digunakan untuk mengumpulkan data berita terkini harian dari dua sumber tepercaya: Tempo.com dan CNN Indonesia. Dengan menjalankan program ini, Anda dapat dengan mudah mengakses informasi terbaru dari kedua situs web tersebut dalam satu tempat.

**Cara Kerja Crawling**

Saat program dijalankan, program akan mengambil tanggal saat ini dan menggunakan informasi ini untuk mengumpulkan berita terkini pada hari itu. Kemudian, program akan membuka halaman web Tempo.com dan CNN Indonesia untuk mengambil informasi yang diperlukan. Informasi yang dikumpulkan meliputi judul berita dan waktu publikasi berita. Semua informasi ini akan disimpan dalam bentuk daftar (array list) sehingga Anda dapat dengan mudah mengaksesnya.

**Cara Penggunaan Aplikasi (pada Docker)**

1. Buka GitBash atau terminal yang Anda gunakan.
2. Clone repository ini ke komputer Anda dengan perintah:
   git clone https://github.com/najmaasr/Crawling-Website.git
3. Pindah ke direktori proyek dengan menjalankan perintah:
   cd Crawling-Website
4. Ketik perintah berikut untuk menjalankan program di Docker:
   docker-compose up
5. Install extension MongoDB di Visual Studio Code
6. Setelah program selesai dijalankan, Anda dapat membuka koneksi ke database MongoDB menggunakan Visual Studio Code atau alat lainnya. Koneksi tersedia di alamat: `127.0.0.1:27017`.
7. Anda juga dapat memeriksa status container yang sedang berjalan dengan melihat tampilan container pada Docker.

---

Selamat menggunakan program ini untuk mengumpulkan data berita terkini dari Tempo.com dan CNN Indonesia! Jika Anda memiliki pertanyaan atau masalah, jangan ragu untuk menghubungi.
