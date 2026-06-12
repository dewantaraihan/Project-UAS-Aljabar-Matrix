import raihan039 as han

vbaris = han.vector([[1,2,3]])
vkolom = han.vector([[4],[5],[6]])

Ma = han.matrix([[1, 2,],[3, 4]])
Mb = han.matrix([[5, 6],[7, 8]])

print("\nVector baris")
han.tampilkan(vbaris)

print("\nVector kolom")
han.tampilkan(vkolom)

print("\nMatriks A")
han.tampilkan(Ma)

print("\nMatriks B")
han.tampilkan(Mb)

print("\nTranspose A")
TA = han.transpose(Ma)
han.tampilkan(TA)

print("\nTranspose Vector baris")
Tvbaris = han.transpose(vbaris)
han.tampilkan(Tvbaris)

print("\nPenjumlahan A + B")
penjumlahan = han.tambah_matriks(Ma, Mb)
han.tampilkan(penjumlahan)

print("\nPengurangan A - B")
pengurangan = han.kurang_matriks(Ma, Mb)
han.tampilkan(pengurangan)

print("\nPerkalian A x B")
Perkalian = han.kali_matriks(Ma, Mb)
han.tampilkan(Perkalian)