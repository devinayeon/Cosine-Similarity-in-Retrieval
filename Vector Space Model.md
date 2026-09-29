### Konten Dokumen Teks
Basicly, isi atau materi yang diungkapkan secara ucapan, tulisan, gerak, atau bentuk lain yang disajikan melalui berbagai media. Nah, itu definisi dari Konten. Dalam konteks komunikasi, Konten sendiri berarti pesan atau informasi.

Sooo, Konten dalam dokumen teks adalah informasi yang diungkapkan secara tulisan yang disajikan dalam bentuk dokumen teks melalui berbagai media yang mendukung. Konten sebuah dokumen teks biasanya tercermin dari penggunaan kata yang terkait dengan konten yang frekuensinya relaitf besar.

#### Contoh
Misalkan, terdapat tiga dokumen yang masing-masing seperti berikut.
1. Dokumen 1:
	mahasiswa fasilkom universitas jember adalah mahasiswa hebat. mahasiswa fasilkom universitas jember banyak memenangkan turnamen baik akademik maupun non akademik. mulai tahun pertama, mahasiswa fasilkom universitas jember telah menunjukkan semangat untuk maju yang sangat tinggi
2. Dokumen 2:
	prodi pertama fasilkom universitas jember adalah prodi sistem informasi. prodi sistem informasi fasilkom universitas jember mulai menerima mahasiswa pada tahun 2009. prodi  sistem informasi fasilkom universitas jember berdiri sebagai prodi setara fakultas, sehingga prodi sistem informasi ini tidak berada di bawah fakultas manapun saat itu
3. Dokumen 3:
	prodi informatika fasilkom universitas jember memiliki matakuliah pilihan yang bernama STKI. matakuliah STKI ditawarkan untuk mahasiswa yang ingin mempelajari metode pencarian informasi dari sekumpulan dokumen teks yang merupakan data tidak terstruktur. matakuliah STKI ditawarkan pada semester 6. Saat ini matakuliah STKI ditempuh 24 mahasiswa

Dari ketiga contoh di atas, sebenarnya dapat kita ekstrak mengenai pasanga term bobot dan term frequency. Pasangan term bobot disini mengartikan term yang belum muncul diberi nilai satu, jika sudah muncul diberi nilai nol. Kemudian pasangan term-frequency atau TF, diartikan sebagai berapa kali suatu term muncul dalam suatu dokumen. Jadi, frekuensi term atau kata dapat menunjukkan konten sebuah dokumen teks.

### Vector Space Model (VSM)
#### Vektor
Definisi dari vektor sendiri adalah besaran yang memiliki nilai dan arah. Misalnya gaya, percepatan, kecepatan, dan berat. Biasanya, vektor disajikan secara geometris sebagai ruas garis berarah dengan panah menunjukkan arah, sedangkan panjang garis menunjukkan besarannya. 

Vektor juga disimbolkan dengan satu huruf (besar atau kecil) atau dua huruf dengan tanda anak panah di atasnya atau satu huruf (besar atau kecil) atau dua huruf besr yang ditulis tebal (bold).

Pada bidang datar, sebuah vektor memiliki satu atau lebih pasang koordinat (x dan y). Ruang yang digunakan untuk menampung vektor yang disusun dari dua koordinat x dan y disebut dengan Ruang Vektor 2 Dimensi (2D Vector Space). Jadi, bila x adalah $v_1$ dan y adalah $v_2$, maka persamaan vektornya dapat ditulis menjadi $v = (v_1, v_2)$. Dengan deimikian, apabila vektor v adalah vektor berdimensi n, maka persamaan vektor tersebut ialah $v = (v_1, v_2,....,v_n)$
#### Matrik dan Vektor
Misalkan dalam sebuah koleksi obyek terdapat beberapa dokumen sebagai berikut:
D1 = "nasi goreng"
D2 = "nasi sambal"
D3 = "sambal goreng" 
D4 = "nasi sambal goreng"
Kalau kita ubah menjadi term, maka diperoleh T = {"nasi", "goreng", "sanbal"}

Apabila bobot setiap term ($w_i$) ditentukan berdasarkan frekuensi kemunculan term (TF) di setiap dokuen ($D_i$), maka matrik Term-by-Document-nya dapat dilihat sebagai himpunan vektor satuan berdimensi 3.

#### VSM
Model yang merepresentasikan dokumen dalam sebuah ruang multi dimensi (satu dokumen satu vektor). Model ini mulai diterapkan dengan menggunakan term sebagai dimensi ruang vektor. 

Contoh dengan dokumen yang sama seperti sebelumnya yaitu:
D1 = "nasi goreng"
D2 = "nasi sambal"
D3 = "sambal goreng" 
D4 = "nasi sambal goreng"
T = {"nasi", "goreng", "sambal"}

$$
\begin{array}{c|c|c|c|c}
\text{Term} & d_1 & d_2 & d_3 & d_4 \\
\hline
\text{nasi}   & 1 & 1 & 0 & 1 \\
\text{goreng} & 1 & 0 & 1 & 1 \\
\text{sambal} & 0 & 1 & 1 & 1 \\
\end{array}
$$
$$
\vec{d}_1 = (w_{1,1}, w_{2,1}, w_{3,1}) = (1, 1, 0)
$$
$$
\vec{d}_2 = (w_{1,2}, w_{2,2}, w_{3,2}) = (1, 0, 1)
$$
$$
\vec{d}_3 = (w_{1,3}, w_{2,3}, w_{3,3}) = (0, 1, 1)
$$
$$
\vec{d}_4 = (w_{1,4}, w_{2,4}, w_{3,4}) = (1, 1, 1)
$$

### Vector Similarity
Setiap dimensi vektor selalu memiliki arah tertentu dengan besaran tertentu. Similarity di sini artinya menunjukkan seberapa mirip sebuah obyek dengan obyek lain (dalam hal ini obyek adalah vektor). Nah, semakin besar nilai similarity, maka semakin tinggi pula tingkat kemiripannya. Pada vektor dokumen, semakin banyak nilai dimensi yang serupa, semakin besar tingkat kemiripannya.

Formula sederhana dari Vector Similarity adalah penjumlahan dari hasil operasi produk (sum of the products). Hal ini dapat dibenarkan jika kita merujuk pada konsep dot product (inner product) dalam aljabar linear. Vector similarity memang mengacu pada kesamaan antara dua vektor, misalnya dalam ruang fitur atau representasi teks. Bentuk paling dasarnya adalah dot product.

$$
A \cdot B = \sum_{i=1}^{n} A_i \cdot B_i
$$
Artinya, kita menjumlahkan hasil perkalian elemen-elemen yang bersesuaian dengan kedua vektor. Nah, si dot product ini menjadi dasar dari beberapa matriks kesamaan, salah satunya ada Cosine Similarity, Jaccard, Dice, atau Overlap.

Misalkan terdapa dua vektor,
$$
A = [1, 2, 3], \quad B = [4, 5, 6]
$$
Dot productnya ialah:
$$
A \cdot B = (1 \cdot 4) + (2 \cdot 5) + (3 \cdot 6) = 4 + 10 + 18 = 32
$$
Nah, hasil inilah yang merupakan bentuk paling sederhana dari vector similarity sebelum dinormalisasi.