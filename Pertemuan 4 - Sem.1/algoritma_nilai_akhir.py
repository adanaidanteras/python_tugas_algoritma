
print("-" * 50)
print("\t\t  Menghitung Nilai Akhir")
print("-" * 50)

nim = input("Masukan NIM : ")
nama = input("Masukan Nama Mahasiswa : ")
mat_kul = input("Masukan Mata Kuliah : ")
nilai_absesnsi = float(input("Masukan Nilai Absensi [1-100] : "))
nilai_tugas = float(input("Masukan Nilai Tugas [1-100] : "))
nilai_UTS = float(input("Masukan Nilai UTS [1-100] : "))
nilai_UAS = float(input("Masukan Nilai UAS [1-100] : "))

persentase_nilai_absesnsi = nilai_absesnsi * 20 / 100
persentase_nilai_tugas = nilai_tugas * 25 / 100
persentase_nilai_UTS = nilai_UTS * 25 / 100
persentase_nilai_UAS = nilai_UAS * 30 / 100

nilai_akhir = persentase_nilai_absesnsi + persentase_nilai_tugas + persentase_nilai_UTS + persentase_nilai_UAS

grade=""
if (nilai_akhir >= 81) and (nilai_akhir <= 100):
    grade = "A"
elif (nilai_akhir >= 75) and (nilai_akhir <= 80):
    grade = "B"
elif (nilai_akhir >= 60) and (nilai_akhir <= 74):
    grade = "C"
elif (nilai_akhir >= 41) and (nilai_akhir <= 59):
    grade = "D"
else:
    grade = "E"

print("-" * 50)
print("Nim              : "+nim)
print("Nama             : "+nama)
print("Mata Kuliah      : "+mat_kul)
print("Nilai Akhir      : "+str(nilai_akhir))
print("Grade            : "+grade)
