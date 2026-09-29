# Implementasi Inverted Index, Boolean Retrieval, dan Sistem Perangkingan Dokumen (Cosine Similarity)

Dokumentasi ini disusun sebagai media pembelajaran mandiri sekaligus penyelesaian tugas mata kuliah **Sistem Temu Kembali Informasi (STKI) / Information Retrieval**.
Kode program mengimplementasikan pemrosesan teks tingkat dasar, pembentukan matriks **Bag of Words (BoW)**, pembuatan struktur data **Inverted Index**, eksekusi query menggunakan operasi **Boolean Retrieval (AND, OR, NOT)**, serta sistem pemeringkatan dokumen berbasis perhitungan kemiripan vektor (**Vector Space Model**) menggunakan metode **Cosine Similarity**.

---

## Ringkasan Konsep

* **Representasi Objek & Tokenisasi**
  Dokumen teks mentah dipecah menjadi unit kata tunggal (*token*) dan diubah menjadi huruf kecil (*case folding*) untuk menyamakan format pembandingan.

* **Vocabulary (Kosakata)**
  Seluruh kata unik dari seluruh dokumen dikumpulkan dan diurutkan secara alfabetis. Kosakata ini menjadi acuan kolom pada matriks frekuensi sekaligus dimensi vektor.

* **Bag of Words (BoW)**
  Matriks berbasis Pandas DataFrame yang mengukur frekuensi kemunculan setiap kata (*Term Frequency*) dalam masing-masing dokumen. Setiap baris dokumen direpresentasikan sebagai sebuah vektor numerik sepanjang ukuran vocab.

* **Inverted Index**
  Struktur data pemetaan terbalik dari kata (*term*) ke daftar ID dokumen (*posting list*) tempat kata tersebut muncul. Struktur ini mempercepat pencarian dibandingkan pemindaian dokumen secara linier.

* **Boolean Retrieval**
  Sistem pencarian dokumen menggunakan logika himpunan:

  * **AND**: Mengambil irisan dokumen yang memuat seluruh kata kunci pencarian.
  * **OR**: Mengambil gabungan dokumen yang memuat salah satu atau seluruh kata kunci pencarian.
  * **NOT**: Mengambil dokumen yang memuat kata kunci pertama tetapi tidak memuat kata kunci kedua.

* **Stopword Removal**
  Pembuangan kata-kata umum yang tidak memiliki makna pembeda yang kuat (misalnya: *adalah, ini, yang, di*) sebelum tahap perangkingan dilakukan.

* **Vector Space Model & Cosine Similarity**
  Query dan dokumen direpresentasikan sebagai vektor pada ruang berdimensi *n* (sejumlah vocab). Kedekatan diukur dengan menghitung sudut antara kedua vektor menggunakan rumus:

  * **Cosine Similarity**: \(\frac{\vec{q} \cdot \vec{d}}{\|\vec{q}\| \times \|\vec{d}\|}\)
  
  where:
  * \(\vec{q} \cdot \vec{d}\) = *dot product* antara vektor query dan vektor dokumen
  * \(\|\vec{q}\|\) = magnitudo (panjang) vektor query
  * \(\|\vec{d}\|\) = magnitudo (panjang) vektor dokumen
  * Nilai berkisar antara `0.0` (tidak mirip) hingga `1.0` (sangat mirip)

---

## Struktur Dataset

Kode ini mendukung fleksibilitas penggantian koleksi dokumen (*dictionary data*).
Terdapat satu dataset sampel berbahasa Indonesia yang digunakan di dalam skenario pengujian:

### Koleksi Topik Akademik Fasilkom UNEJ

* **DOK1 (Doc 1)**: "mahasiswa fasilkom universitas jember adalah mahasiswa hebat. mahasiswa fasilkom universitas jember banyak memenangkan turnamen baik akademik maupun non akademik. mulai tahun pertama, mahasiswa fasilkom universitas jember telah menunjukkan semangat untuk maju yang sangat tinggi"
* **DOK2 (Doc 2)**: "prodi pertama fasilkom universitas jember adalah prodi sistem informasi. prodi sistem informasi fasilkom universitas jember mulai menerima mahasiswa pada tahun 2009. prodi sistem informasi fasilkom universitas jember berdiri sebagai prodi setara fakultas, sehingga prodi sistem informasi ini tidak berada di bawah fakultas manapun saat itu"
* **DOK3 (Doc 3)**: "prodi informatika fasilkom universitas jember memiliki matakuliah pilihan yang bernama STKI. matakuliah STKI ditawarkan untuk mahasiswa yang ingin mempelajari metode pencarian informasi dari sekumpulan dokumen teks yang merupakan data tidak terstruktur. matakuliah STKI ditawarkan pada semester 6. Saat ini matakuliah STKI ditempuh 24 mahasiswa"

---

## Alur Kerja Kode

### Pra-pemrosesan Teks

* String dipisah (*split*) berdasarkan spasi.
* Karakter diubah ke huruf kecil menggunakan `.lower()`.
* Pada tahap perangkingan, daftar kata difilter dari token yang masuk dalam kategori *stopwords*.
* Token yang sama tidak dihitung lebih dari satu kali ketika membentuk himpunan query maupun dokumen (untuk metrik berbasis himpunan seperti Jaccard/DSC/Overlap).

### Ekstraksi Kosakata & Pembuatan BoW

* Membentuk vocab berurutan secara alfabetis.
* Menghitung frekuensi kata per dokumen via `.count()` — menghasilkan vektor *Term Frequency* untuk setiap dokumen.
* Mengonversi matriks angka menjadi `pandas.DataFrame` dengan kolom = vocab dan baris = dokumen.

### Konstruksi Inverted Index

* Memindai setiap kolom pada DataFrame BoW.
* Menyimpan indeks dokumen yang memiliki nilai frekuensi lebih dari nol (> 0).

### Pencarian Boolean (Boolean Search Functions)

* `boolean_and(term1, term2, index)` → Mengembalikan daftar dokumen di mana `doc_id` ada pada `term1` dan `term2`.
* `boolean_or(term1, term2, index)` → Mengembalikan daftar dokumen gabungan dari `term1` dan `term2` tanpa duplikasi.
* `boolean_not(term1, term2, index)` → Mengembalikan daftar dokumen pada `term1` dikurangi dokumen yang mengandung `term2`.

### Pembentukan Vektor Query

* Query pengguna di-tokenize dan difilter dari *stopwords*.
* Vektor query dibentuk dengan panjang sama dengan vocab, di mana setiap elemen berisi frekuensi kemunculan term query pada posisi vocab tersebut.
* Vektor query ini akan dibandingkan dengan vektor setiap dokumen menggunakan Cosine Similarity.

### Perhitungan dan Perangkingan Cosine Similarity

* Menghitung *dot product* antara vektor query dan vektor dokumen menggunakan `zip()`.
* Menghitung magnitudo masing-masing vektor dengan akar kuadrat dari jumlah kuadrat elemen (`math.sqrt`).
* Menerapkan rumus **Cosine Similarity** dengan penanganan kasus khusus ketika magnitudo bernilai nol (mengembalikan `0.0`).
* Dokumen dengan skor Cosine sebesar nol disingkirkan dari hasil perangkingan.
* Hasil akhir diurutkan dari skor terbesar ke terkecil (*descending*), sehingga dokumen dengan kemiripan arah vektor yang lebih tinggi terhadap query berada pada peringkat lebih atas.

### Perangkingan Tambahan (Metrik Himpunan)

Selain Cosine Similarity, kode juga menyediakan perangkingan berbasis himpunan sebagai pembanding:

* **Jaccard Similarity**: \(|intersection| / |union|\)
* **Dice Similarity Coefficient (DSC)**: \(2 \times |intersection| / (|query| + |doc|)\)
* **Overlap Similarity**: \(|intersection| / \min(|query|, |doc|)\)

---

## Kebutuhan Lingkungan Eksekusi

* **Python**: versi 3.8 atau lebih baru
* **Library**: `pandas`, `math` (*built-in*)

Atur pustaka yang diperlukan sebelum menjalankan skrip:

```bash
pip install pandas
```
