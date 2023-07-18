# Customers Churn Prediction

## Tujuan Proyek
Proyek ini dibuat untuk mengembangkan model prediksi customers churn. Tujuan utama dari proyek ini adalah untuk membangun sebuah sistem yang dapat memprediksi apakah pelanggan akan churn (berhenti menggunakan layanan) atau tidak. Hal ini akan membantu perusahaan dalam mengidentifikasi dan mengatasi masalah customers churn sehingga dapat mempertahankan lebih banyak pelanggan dan meningkatkan kepuasan pelanggan.

## Masalah yang Diselesaikan
Churn atau kehilangan pelanggan merupakan masalah serius bagi banyak perusahaan. Kehilangan pelanggan dapat berdampak negatif pada pendapatan dan reputasi perusahaan. Dalam proyek ini, kami berusaha untuk mengatasi masalah tersebut dengan menggunakan data historis pelanggan untuk memprediksi potensial churn di masa depan.

## Latar Belakang Masalah
Dalam industri layanan, perusahaan seringkali menghadapi tantangan dalam mempertahankan pelanggan yang sudah ada. Faktor-faktor seperti persaingan yang ketat, kepuasan pelanggan, dan penawaran dari pesaing dapat mempengaruhi keputusan pelanggan untuk beralih ke layanan lain. Oleh karena itu, penting bagi perusahaan untuk dapat mengidentifikasi pelanggan yang berisiko tinggi untuk churn dan mengambil tindakan yang tepat.

## Output Proyek
Output dari proyek ini adalah model prediksi churn pelanggan. Model kurang baik dalam memprediksi kelas 1 (customer churn) daripada kelas 0 (customer tidak churn). Oleh karena itu, untuk meminimalkan kerugian akibat kehilangan pelanggan, perlu dilakukan upaya yang lebih intensif untuk mempertahankan pelanggan yang termasuk dalam kelas 0, seperti memberikan penawaran khusus atau memberikan layanan yang lebih baik untuk meningkatkan kepuasan pelanggan. Selain itu, perlu juga dilakukan evaluasi lebih lanjut terhadap model untuk memperbaiki performa model dalam memprediksi kelas 0.

## Penjelasan Singkat Data yang Digunakan
Data yang digunakan dalam proyek ini adalah dataset churn.csv yang berisi informasi pelanggan serta kolom target "churn_risk_score". Kolom "churn_risk_score" menunjukkan skor churn, dengan nilai 0 menunjukkan pelanggan yang tidak churn dan nilai 1 menunjukkan pelanggan yang churn.

## Metode yang Digunakan
Metode yang akan digunakan mencakup:
- Pra-pemrosesan data: Membersihkan data dari nilai null, data duplikat,handling outliers, transformasi data (normalisasi, encoding, dll.)
- Klasifikasi: Menggunakan model ANN (Artificial Neural Network) seperti Sequential API dan Functional API untuk melatih model dengan data train dan melakukan prediksi pada data test.

## Stack yang Digunakan
Dalam proyek ini, kami akan menggunakan beberapa teknologi dan alat sebagai berikut:

- Bahasa Pemrograman: Python
- Library dan Framework: scikit-learn, pandas, numpy, matplotlib, tensorflow, feature_engine
- Lingkungan Pengembangan: Jupyter Notebook

## Kelebihan dan Kekurangan Proyek
Kelebihan proyek ini adalah:

- Dapat membantu perusahaan dalam mengidentifikasi pelanggan yang berisiko tinggi untuk churn dan mengambil tindakan yang tepat untuk mempertahankan mereka.
- Menggunakan teknik klasifikasi yang umum dan dapat diterapkan pada masalah churn prediksi.

Kekurangan proyek ini adalah:

- Hasil prediksi dapat dipengaruhi oleh pilihan algoritma dan parameter klasifikasi yang digunakan.

### [Deployment](https://huggingface.co/spaces/dayuima01/M1P2)

