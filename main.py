import math
import pandas as pd


def cosine_similarity(vec1: list[int], vec2: list[int]) -> float:
    dot_product: float = sum(a * b for a, b in zip(vec1, vec2))
    magnitude_vec1: float = math.sqrt(sum(a * a for a in vec1))
    magnitude_vec2: float = math.sqrt(sum(b * b for b in vec2))

    if magnitude_vec1 == 0 or magnitude_vec2 == 0:
        return 0.0

    return dot_product / (magnitude_vec1 * magnitude_vec2)


def boolean_and(
    term1: str,
    term2: str,
    inverted_index: dict[str, list[int]],
) -> list[int]:
    docs_term1: list[int] = inverted_index.get(term1, [])
    docs_term2: list[int] = inverted_index.get(term2, [])

    results: list[int] = []
    for doc_id in docs_term1:
        if doc_id in docs_term2 and doc_id not in results:
            results.append(doc_id)

    return results


def boolean_or(
    term1: str,
    term2: str,
    inverted_index: dict[str, list[int]],
) -> list[int]:
    docs_term1: list[int] = inverted_index.get(term1, [])
    docs_term2: list[int] = inverted_index.get(term2, [])

    results: list[int] = docs_term1.copy()
    for doc_id in docs_term2:
        if doc_id not in results:
            results.append(doc_id)

    return results


def boolean_not(
    term1: str,
    term2: str,
    inverted_index: dict[str, list[int]],
) -> list[int]:
    docs_term1: list[int] = inverted_index.get(term1, [])
    docs_term2: list[int] = inverted_index.get(term2, [])

    results: list[int] = []
    for doc_id in docs_term1:
        if doc_id not in docs_term2:
            results.append(doc_id)

    return results


# Data Obyek
data_obyek: dict[str, str] = {
    "DOK1": "mahasiswa fasilkom universitas jember adalah mahasiswa hebat. mahasiswa fasilkom universitas jember banyak memenangkan turnamen baik akademik maupun non akademik. mulai tahun pertama, mahasiswa fasilkom universitas jember telah menunjukkan semangat untuk maju yang sangat tinggi",
    "DOK2": "prodi pertama fasilkom universitas jember adalah prodi sistem informasi. prodi sistem informasi fasilkom universitas jember mulai menerima mahasiswa pada tahun 2009. prodi  sistem informasi fasilkom universitas jember berdiri sebagai prodi setara fakultas, sehingga prodi sistem informasi ini tidak berada di bawah fakultas manapun saat itu",
    "DOK3": "prodi informatika fasilkom universitas jember memiliki matakuliah pilihan yang bernama STKI. matakuliah STKI ditawarkan untuk mahasiswa yang ingin mempelajari metode pencarian informasi dari sekumpulan dokumen teks yang merupakan data tidak terstruktur. matakuliah STKI ditawarkan pada semester 6. Saat ini matakuliah STKI ditempuh 24 mahasiswa",
}

# Representasi Objek
print("Representasi obyek")
for number, (key, value) in enumerate(data_obyek.items(), start=1):
    print(key, "-> D", number, "=", value.split(" "))
print()

# Tokenizing & Vocab
words: list[str] = list(data_obyek.values())
tokenized_docs: list[list[str]] = [word.lower().split(" ") for word in words]

vocab: list[str] = []
for docs_word in tokenized_docs:
    for word in docs_word:
        if word not in vocab:
            vocab.append(word)

vocab.sort()

# Bag of Words
count_word_in_docs: list[list[int]] = []
for docs in tokenized_docs:
    counts: list[int] = [docs.count(w) for w in vocab]
    count_word_in_docs.append(counts)

df: pd.DataFrame = pd.DataFrame(
    count_word_in_docs,
    columns=vocab,
    index=[f"Doc {i + 1}" for i in range(len(words))],
)

# Inverted Index
inverted_index: dict[str, list[int]] = {}
for word in df.columns:
    docs_containing_word: list[str] = df.index[df[word] > 0].tolist()
    docs_number: list[int] = [int(doc.split(" ")[1]) for doc in docs_containing_word]
    inverted_index[word] = docs_number

print("Dictionary    | Inverted List")
print("----------------------------")
for word, doc_ids in inverted_index.items():
    print(f"{word:<12} | {doc_ids}")
print()

# Boolean Search Demo
query: str = "mahasiswa hebat"
theta: list[str] = query.lower().split(" ")

print("Membangun Query")
print("----------------")
print("Ketik yang anda cari:", query)
print("Theta:", theta)
print()

print("Dokumen yang sesuai dengan query")
print("---------------------------------")
for number, term in enumerate(theta, start=1):
    docs_term: list[int] = inverted_index.get(term, [])
    print(term, f"(S {number}) :", docs_term)

result_and: list[int] = boolean_and("mahasiswa", "hebat", inverted_index)
result_or: list[int] = boolean_or("mahasiswa", "30.000", inverted_index)
result_not: list[int] = boolean_not("mahasiswa", "hebat", inverted_index)

print()
print('Retrieved object (R) dengan logika "AND"')
for doc_id in result_and:
    print(f"Obj {doc_id} :", data_obyek[f"DOK{doc_id}"])

print()
print('Retrieved object (R) dengan logika "OR"')
for doc_id in result_or:
    print(f"Obj {doc_id} :", data_obyek[f"DOK{doc_id}"])

print()
print('Retrieved object (R) dengan logika "NOT"')
for doc_id in result_not:
    print(f"Obj {doc_id} :", data_obyek[f"DOK{doc_id}"])
print()

# Input Query & Preprocessing
stopwords: list[str] = ["adalah", "ini", "yang", "di"]
query_pencarian: str = input("Masukkan query pencarian: ")
query_tokens: list[str] = query_pencarian.lower().split(" ")

query_terms: list[str] = []
for token in query_tokens:
    if token not in stopwords and token not in query_terms:
        query_terms.append(token)

# Inisialisasi Hasil Perangkingan
hasil_ranking_jaccard: list[tuple[str, float]] = []
hasil_ranking_dsc: list[tuple[str, float]] = []
hasil_ranking_overlap: list[tuple[str, float]] = []
hasil_ranking_cosine: list[tuple[str, float]] = []

# Vektor Query untuk Cosine Similarity
query_vec: list[int] = [query_tokens.count(w) for w in vocab]

for idx, (doc_id, text) in enumerate(data_obyek.items()):
    doc_tokens: list[str] = text.lower().split(" ")
    doc_terms: list[str] = []
    for token in doc_tokens:
        if token not in stopwords and token not in doc_terms:
            doc_terms.append(token)

    intersection: list[str] = [term for term in query_terms if term in doc_terms]

    union: list[str] = query_terms.copy()
    for term in doc_terms:
        if term not in union:
            union.append(term)

    # 1. Jaccard Score
    score_jaccard: float = len(intersection) / len(union) if len(union) > 0 else 0.0
    if score_jaccard > 0:
        hasil_ranking_jaccard.append((doc_id, score_jaccard))

    # 2. DSC Score
    total_terms: int = len(query_terms) + len(doc_terms)
    score_dsc: float = (2 * len(intersection)) / total_terms if total_terms > 0 else 0.0
    if score_dsc > 0:
        hasil_ranking_dsc.append((doc_id, score_dsc))

    # 3. Overlap Score
    min_len: int = min(len(query_terms), len(doc_terms))
    score_overlap: float = len(intersection) / min_len if min_len > 0 else 0.0
    if score_overlap > 0:
        hasil_ranking_overlap.append((doc_id, score_overlap))

    # 4. Cosine Similarity Score
    doc_vec: list[int] = count_word_in_docs[idx]
    score_cosine: float = cosine_similarity(query_vec, doc_vec)
    if score_cosine > 0:
        hasil_ranking_cosine.append((doc_id, score_cosine))

# Sorting
hasil_ranking_jaccard.sort(key=lambda item: item[1], reverse=True)
hasil_ranking_dsc.sort(key=lambda item: item[1], reverse=True)
hasil_ranking_overlap.sort(key=lambda item: item[1], reverse=True)
hasil_ranking_cosine.sort(key=lambda item: item[1], reverse=True)


def tampilkan_perangkingan(
    nama_metode: str,
    hasil_ranking: list[tuple[str, float]],
    query_pencarian: str,
    query_terms: list[str],
) -> None:
    print()
    print(f"Perangkingan dengan {nama_metode}")
    print("-" * (18 + len(nama_metode)))
    print("Query:", query_pencarian)
    print("Q =", query_terms)
    print()
    print("Peringkat | Dokumen | Skor")
    print("--------------------------")

    for peringkat, (doc_id, score) in enumerate(hasil_ranking, start=1):
        print(f"{peringkat:<9} | {doc_id:<7} | {score:.3f}")

    if not hasil_ranking:
        print("Tidak ada dokumen relevan (semua skor = 0)")

    print()
    print("Detail dokumen terurut")
    print("-----------------------")
    for doc_id, score in hasil_ranking:
        print(f"{doc_id} ({score:.3f}) :", data_obyek[doc_id])


# Cetak Hasil Perangkingan
tampilkan_perangkingan(
    "Koefisien Jaccard", hasil_ranking_jaccard, query_pencarian, query_terms
)
tampilkan_perangkingan(
    "Dice Similarity Coefficient (DSC)", hasil_ranking_dsc, query_pencarian, query_terms
)
tampilkan_perangkingan(
    "Overlap Similarity", hasil_ranking_overlap, query_pencarian, query_terms
)
tampilkan_perangkingan(
    "Cosine Similarity", hasil_ranking_cosine, query_pencarian, query_terms
)
