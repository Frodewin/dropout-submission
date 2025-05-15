# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan dikenal memiliki reputasi baik dalam mencetak lulusan berkualitas. Namun, belakangan ini institusi menghadapi tantangan serius yaitu tingginya tingkat dropout mahasiswa. Fenomena ini tidak hanya berdampak pada reputasi institusi tetapi juga memengaruhi keberlanjutan operasional dan kepercayaan masyarakat terhadap kualitas pendidikan yang ditawarkan.

Untuk mengatasi hal tersebut, pihak manajemen ingin memanfaatkan pendekatan berbasis data untuk mendeteksi secara dini mahasiswa yang berpotensi dropout. Dengan demikian, mereka dapat memberikan intervensi atau bimbingan yang sesuai untuk mencegah terjadinya putus studi.

### Permasalahan Bisnis
1. Bagaimana mengidentifikasi faktor-faktor utama yang memengaruhi kemungkinan mahasiswa mengalami dropout?

2. Bagaimana membangun model prediktif yang dapat mengklasifikasikan mahasiswa yang berisiko tinggi untuk dropout secara akurat?

3. Bagaimana menyajikan informasi penting terkait performa mahasiswa dalam bentuk dashboard interaktif agar pihak institusi dapat mengambil tindakan secara cepat dan tepat?

### Cakupan Proyek
1. Eksplorasi dan analisis data siswa untuk memahami pola-pola umum dan faktor yang berhubungan dengan dropout.

2. Pemodelan prediktif menggunakan machine learning untuk mengklasifikasikan mahasiswa yang berpotensi dropout berdasarkan data historis.

3. Evaluasi performa model untuk memastikan tingkat akurasi dan efektivitas dalam mendeteksi risiko dropout.

4. Pembuatan dashboard interaktif yang dapat digunakan oleh pihak manajemen untuk memonitor performa mahasiswa dan mendeteksi potensi dropout secara real-time.

5. Pemberian rekomendasi berbasis data terkait intervensi yang dapat dilakukan untuk menurunkan angka dropout.

### Persiapan

Sumber data: (https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:
Buat environment baru menggunakan conda
```bash
conda create --name nama_env python=3.12.7
conda activate nama_env
```
kemudian install semua dependensi di requirements.txt
```bash
pip install -r requirements.txt
```
Metabase
username: frodewing@gmail.com
password: Iamnumber01.

## Business Dashboard
Business dashboard merupakan sarana untuk menyajikan hasil visualisasi data yang telah melalui proses pengolahan, dan digunakan sebagai alat untuk menyampaikan insight kepada pihak-pihak terkait. Dalam proyek ini, dashboard yang digunakan adalah **Metabase**.

Dashboard ini dibagi menjadi dua bagian utama. Bagian pertama menyajikan visualisasi berbasis **statistik deskriptif**, seperti perbandingan jumlah, rata-rata, maupun distribusi kategori, guna menggambarkan pola-pola dan wawasan dari data secara umum. Sementara itu, bagian kedua menampilkan **tabel hasil analisis regresi logistik**, yang digunakan untuk memperkirakan seberapa besar pengaruh masing-masing faktor terhadap kemungkinan terjadinya atrisi, dengan asumsi bahwa faktor lain bersifat tetap (ceteris paribus).

Melalui pendekatan ini, kita tidak hanya memperoleh gambaran umum dari data, tetapi juga memahami seberapa kuat kontribusi setiap faktor dalam memengaruhi keputusan karyawan untuk melakukan atrisi. Diharapkan hasil analisis ini dapat membantu tim HR dalam merumuskan strategi yang lebih tepat untuk mengurangi risiko attrition di lingkungan kerja.

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

Prototype yang dibuat menggunakan platform streamlit, platform yang terintegrasi dengan bahasa pemrograman Python untuk membuat sebuah dashboard interaktif dan efisien dengan visual yang simple dan mudah untuk digunakan.

Menjalankan prototype menggunakan streamlit cukup mudah, Anda bisa melakukannya dengan menggunakan terminal.
1. Buka terminal Anda
2. Aktifkan Environment yang sudah dibuat sebelumnya, setelahnya arahkan ke folder penyimpanan tempat anda menyimpan app.py
3. Di terminal, jalankan perintah berikut
```bash
streamlit run app.py
```
4. Secara otomatis, Anda bisa menggunakan prototype yang ada/


## Conclusion
Dari analisis ini, faktor-faktor yang **meningkatkan risiko dropout** antara lain:

* **Beban kuliah yang tinggi**, terutama jika mahasiswa mengambil terlalu banyak mata kuliah di semester awal.
* **Masalah keuangan**, seperti memiliki utang atau tidak membayar biaya kuliah tepat waktu.
* **Umur saat pendaftaran** yang lebih tua (mungkin karena tanggung jawab lain di luar kampus).
* **Gender** dan **status berpindah tempat** juga berperan, meskipun lebih lemah.

Sementara itu, faktor-faktor yang **menurunkan risiko dropout**:

* **Kinerja akademik yang baik** (nilai tinggi dan banyak mata kuliah lulus).
* **Kepemilikan beasiswa**.
* **Kepatuhan terhadap pembayaran biaya kuliah**.
* **Latar belakang pendidikan sebelumnya yang baik**.

### Rekomendasi Action Items
Berdasarkan temuan ini, berikut adalah rekomendasi untuk Jaya Jaya Institut:

### 1. **Manajemen Beban Kuliah**
* Batasi jumlah SKS/mata kuliah yang bisa diambil mahasiswa baru atau yang performanya rendah.
* Terapkan sistem *early warning* untuk mahasiswa yang mengambil terlalu banyak mata kuliah.

### 2. **Dukungan Finansial**
* Perluas program **beasiswa** atau bantuan keuangan untuk mahasiswa yang menunjukkan potensi akademik.
* Buat sistem cicilan atau bantuan keuangan darurat untuk menghindari keterlambatan pembayaran.

### 3. **Bimbingan untuk Mahasiswa Rentan**
* Identifikasi mahasiswa yang **berusia lebih tua**, **punya utang**, atau **berpindah domisili**, lalu berikan program pendampingan akademik dan psikososial.

### 4. **Pemantauan Performa Akademik**
* Buat sistem pemantauan **berbasis dashboard** yang dapat memantau nilai, SKS yang diambil, dan status keuangan.
* Beri intervensi lebih awal untuk mahasiswa dengan nilai rendah.

### 5. **Kolaborasi dengan HR/Keuangan**
* Satukan data akademik dan keuangan untuk **deteksi dini mahasiswa berisiko dropout**.
* Gunakan hasil regresi ini sebagai dasar untuk membuat **sistem prediksi dropout** otomatis di dashboard Metabase.