from utils import konversi_suhu

print("=== Program Konversi Suhu ===")
dari = input("Masukkan satuan asal (C/F/K): ")
ke = input("Masukkan satuan tujuan (C/F/K): ")

try:
    nilai = float(input("Masukkan nilai suhu: "))
except ValueError:
    print("Error: Nilai suhu harus angka.")
    exit()

hasil = konversi_suhu(nilai, dari, ke)
print(f"Hasil konversi dari {nilai} {dari.upper()} ke {ke.upper()} adalah: {hasil}")
