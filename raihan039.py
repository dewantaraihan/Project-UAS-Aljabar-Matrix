def vector(data):
    if not isinstance(data, list):
        return "Vector harus berupa list"
    return data

def matrix(data):
    if not isinstance(data, list):
        return "Matrix harus berupa list"
    if len(data) == 0:
        return "Matriks kosong"
    jumlah_kolom = len(data[0])
    for baris in data:
        if len(baris) != jumlah_kolom:
            return "Matriks tidak valid, jumlah kolom tiap baris harus sama"
    return data

def transpose(matriks):
    if len(matriks) == 0:
        return "Matriks kosong"
    hasil = []
    for j in range(len(matriks[0])):
        baris = []
        for i in range(len(matriks)):
            baris.append(matriks[i][j])
        hasil.append(baris)
    return hasil

def tambah_matriks(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "Penjumlahan tidak dapat dilakukan, ukuran matriks berbeda"
    hasil = []
    for i in range(len(A)):
        baris = []
        for j in range(len(A[0])):
            baris.append(A[i][j] + B[i][j])
        hasil.append(baris)
    return hasil

def kurang_matriks(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "Pengurangan tidak dapat dilakukan, ukuran matriks berbeda"
    hasil = []
    for i in range(len(A)):
        baris = []
        for j in range(len(A[0])):
            baris.append(A[i][j] - B[i][j])
        hasil.append(baris)
    return hasil

def kali_matriks(A, B):
    if len(A[0]) != len(B):
        return "Perkalian tidak dapat dilakukan, ukuran matriks tidak memenuhi syarat"
    hasil = []
    for i in range(len(A)):
        baris = []
        for j in range(len(B[0])):
            jumlah = 0
            for k in range(len(B)):
                jumlah += A[i][k] * B[k][j]
            baris.append(jumlah)
        hasil.append(baris)
    return hasil
        
def tampilkan(matriks):
    if isinstance(matriks, str):
        print(matriks)
    else:
        for baris in matriks:
            print(baris)