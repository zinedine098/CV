# Platform Kursus Online

Selamat datang di Platform Kursus Online - sebuah aplikasi web berbasis Django yang komprehensif yang dirancang untuk menyediakan pendidikan online dengan fokus pada pengalaman pengguna dan manajemen kursus.

## Gambaran Proyek

Proyek ini merupakan platform pembelajaran online yang dibangun dengan Django yang memungkinkan siswa untuk menelusuri kursus, terhubung dengan instruktur, dan mengakses konten pendidikan. Platform ini memiliki desain responsif dengan elemen UI modern dan kemampuan manajemen kursus yang komprehensif.

## Kemajuan & Fitur Saat Ini

### Struktur Inti
- **Django Project**: Dibangun dengan Django 5.2.8
- **Database**: SQLite3 untuk pengembangan
- **Sistem Template**: Template Django dengan inheritance base.html
- **File Statis**: Manajemen aset komprehensif dengan desain berbasis Bootstrap

### UI & Desain
- **Tata Letak Responsif**: Desain berbasis mobile menggunakan Bootstrap 5.3.7
- **Template Modern**: Template "Learner" dengan estetika profesional
- **Aset Statis**: CSS, JavaScript, gambar, dan pustaka vendor diatur dengan baik
- **Framework Frontend**: Bootstrap dengan CSS dan fungsionalitas JavaScript kustom

### Fitur Halaman Depan
- **Bagian Hero**: Perkenalan menarik dengan statistik dan tombol aksi
- **Kursus Unggulan**: Tampilan kursus dengan detail (tingkat kesulitan, durasi, instruktur, peringkat)
- **Kategori Kursus**: Kategorisasi komprehensif dengan lebih dari 18 bidang studi
- **Instruktur Unggulan**: Profil profesional dengan peringkat dan jumlah kursus
- **Testimoni**: Sistem umpan balik siswa dengan tampilan peringkat
- **Bagian Blog**: Postingan terbaru dengan informasi penulis
- **Ajakan Bertindak**: Bagian pendaftaran dengan statistik kunci

### Navigasi & Pengalaman Pengguna
- **Navigasi Utama**: Menu lengkap dengan Kursus, Tentang, Instruktur, Harga, Blog
- **Menu Dropdown**: Opsi navigasi yang diperluas untuk akses konten terperinci
- **Desain Responsif**: Toggle navigasi mobile dan tata letak responsif
- **Integrasi Media Sosial**: Tautan ke Twitter, Facebook, Instagram, LinkedIn

### Fungsionalitas yang Diimplementasikan
- **Routing URL**: Struktur URL yang bersih dengan pola URL Django
- **Sistem View**: Implementasi view dasar untuk halaman depan
- **Inheritance Template**: Template dasar dengan struktur blok untuk konten
- **Manajemen File Statis**: Penanganan file statis Django yang tepat

### Teknologi yang Digunakan
- **Backend**: Django 5.2.8
- **Frontend**: HTML5, CSS3, JavaScript dengan Bootstrap 5
- **Database**: SQLite3
- **Template Engine**: Django Templates
- **Framework CSS**: Bootstrap dengan styling kustom
- **Pustaka JavaScript**: AOS, Swiper, PureCounter untuk elemen interaktif

### Fitur Manajemen Kursus
- **Kategori Kursus**: Lebih dari 18 kategori termasuk Ilmu Komputer, Bisnis, Desain, Kesehatan, Bahasa, dll.
- **Penampilan Kursus**: Kartu kursus terperinci dengan harga, tingkat kesulitan, durasi, dan informasi instruktur
- **Sistem Peringkat**: Peringkat bintang visual dan skor numerik
- **Statistik Siswa**: Data pendaftaran dan metrik keberhasilan

### Manajemen Instruktur
- **Profil Instruktur**: Profil terperinci dengan spesialisasi, peringkat, dan jumlah kursus
- **Integrasi Media Sosial**: Tautan ke jaringan profesional instruktur
- **Metrik Kinerja**: Jumlah siswa dan tampilan peringkat

## Struktur Aplikasi

```
online_course/
├── config/                 # Pengaturan proyek Django
│   ├── settings.py         # Konfigurasi proyek
│   ├── urls.py            # Routing URL utama
│   └── wsgi.py            # Aplikasi WSGI
├── landing/               # Aplikasi utama
│   ├── views.py           # Fungsi view
│   ├── urls.py            # URL khusus aplikasi
│   ├── models.py          # Model database (kosong untuk saat ini)
│   └── admin.py           # Konfigurasi antarmuka admin
├── templates/             # Template HTML
│   ├── base.html          # Template dasar dengan tata letak
│   └── landing/           # Template halaman depan
├── static/                # Aset statis
│   └── assets/            # CSS, JS, gambar, vendor
└── db.sqlite3             # File database
```

## Status Saat Ini

✅ **Komponen yang Telah Selesai:**
- Struktur proyek Django dasar
- Halaman depan dengan implementasi UI lengkap
- Desain responsif dan kompatibilitas mobile
- Manajemen file statis
- Konfigurasi routing URL
- Sistem inheritance template

🔄 **Sedang Dalam Proses:**
- Pengembangan model database
- Sistem otentikasi pengguna
- Fungsionalitas pendaftaran kursus
- Portal instruktur
- Dashboard siswa

## Pengembangan Mendatang

 Fitur yang DIRENCANAKAN:
- Otentikasi dan otorisasi pengguna
- Sistem pendaftaran kursus
- Integrasi pembayaran
- Pelacakan kemajuan siswa
- Dashboard instruktur
- Sistem manajemen konten
- Materi pembelajaran interaktif
- Kemampuan streaming video
- Forum diskusi
- Alat kuis dan penilaian

## Petunjuk Instalasi

1. Clone repositori ini
2. Buat lingkungan virtual: `python -m venv venv`
3. Aktifkan lingkungan virtual: `source venv/bin/activate` (Linux/Mac) atau `venv\Scripts\activate` (Windows)
4. Instal dependensi: `pip install django`
5. Jalankan migrasi: `python manage.py migrate`
6. Mulai server pengembangan: `python manage.py runserver`
7. Kunjungi `http://127.0.0.1:8000/` untuk melihat aplikasi

## Kontribusi

Kami menyambut kontribusi untuk meningkatkan fungsionalitas dan fitur platform kursus online ini. Silakan kirim pull request atau buat issue untuk bug dan permintaan fitur.