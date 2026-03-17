# Tugas PaaS Django - Railway

Project Django sangat sederhana untuk tugas kuliah PaaS.

Identitas:

- Nama: Muhammad Irsyad Dimas Abdillah
- Kelas: TI-3F
- Absen: 14

## 1) Setup Lokal

1. Pastikan Python 3.11+ sudah terpasang.
1. Buat virtual environment:

```bash
python -m venv .venv
```

1. Aktifkan virtual environment:

Windows (PowerShell):

```bash
.\.venv\Scripts\Activate.ps1
```

1. Install dependency:

```bash
pip install -r requirements.txt
```

1. Salin env template:

```bash
copy .env.example .env
```

## 2) Menjalankan Lokal

1. Jalankan migrasi:

```bash
python manage.py migrate
```

1. Jalankan server lokal:

```bash
python manage.py runserver
```

1. Akses:

- Home: `http://127.0.0.1:8000/`
- Health: `http://127.0.0.1:8000/health/`

## 3) Daftar Environment Variable

- `APP_NAME` (default: `Tugas PaaS Saya`)
- `DJANGO_SECRET_KEY` (default aman untuk local dev saja)
- `DEBUG` (default: `False`)
- `DJANGO_ALLOWED_HOSTS` (default: `*`)
- `DJANGO_ENV` (default: `production`)

Contoh nilai yang direkomendasikan:

```env
APP_NAME=Tugas PaaS - Muhammad Irsyad Dimas Abdillah (TI-3F/14)
DJANGO_SECRET_KEY=ganti-dengan-secret-key-aman
DEBUG=False
DJANGO_ALLOWED_HOSTS=*
DJANGO_ENV=production
```

## 4) Deploy ke Railway via GitHub

1. Push project ini ke repository GitHub Anda.
2. Login ke Railway.
3. Klik **New Project** > **Deploy from GitHub repo**.
4. Pilih repository project ini.
5. Railway akan build otomatis menggunakan `requirements.txt`.
6. File `railway.toml` sudah menyiapkan start command dan healthcheck.

Jika auto-detect Railway gagal, isi start command manual di Railway:

```bash
python manage.py migrate && gunicorn tugas_paas.wsgi
```

## 5) Start Command Railway (Rekomendasi)

```bash
python manage.py migrate && gunicorn tugas_paas.wsgi
```

## 6) Menambahkan APP_NAME di Railway

1. Buka project Anda di Railway.
2. Masuk ke tab **Variables**.
3. Tambahkan key `APP_NAME` dengan value contoh:
   `Tugas PaaS - Muhammad Irsyad Dimas Abdillah (TI-3F/14)`
4. Simpan, lalu lakukan redeploy bila diperlukan.

## 7) Generate Public Domain di Railway

1. Masuk ke service yang sudah terdeploy.
2. Buka tab **Settings** > **Networking**.
3. Klik **Generate Domain**.
4. Buka URL domain untuk mengakses aplikasi publik.

## 8) Cek Log di Railway

1. Masuk ke service di Railway.
2. Buka tab **Deployments** atau **Logs**.
3. Akses endpoint `/` dan `/health/` dari browser.
4. Pastikan log berikut terlihat:
   - `HOME_ACCESS path=/ method=GET app_name=...`
   - `HEALTH_ACCESS path=/health/ method=GET app_name=...`

## 9) Checklist Bukti Penilaian

- [ ] Deployment sukses (`200 OK` pada `/` dan `/health/`)
- [ ] Nilai environment variable `APP_NAME` tampil benar di halaman utama
- [ ] Endpoint `/health/` mengembalikan JSON status aplikasi
- [ ] Log akses `/` dan `/health/` terlihat jelas di Railway logs
- [ ] Menunjukkan pemahaman alur: request masuk -> view dipanggil -> log tercetak -> response kembali
