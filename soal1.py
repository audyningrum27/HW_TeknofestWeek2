arrBerat = []
bMin = 0
bMax = 0

def hitungMinMax(arrBerat):
    global bMin, bMax
    # Definisikan Proses Mencari Berat Maximum Dan Minimum
    arrBerat.sort()
    bMin = arrBerat[0]
    print("Berat balita minimum: %.2f" % bMin + " kg")
    arrBerat.sort(reverse=True)
    bMax = arrBerat[0]
    print("Berat balita maksimum: %.2f" % bMax + " kg")


def rerata(arrBerat):
    total = 0

    # Definisikan Proses Mencari Rerata Dari Total Berat
    total = sum(arrBerat) / len(arrBerat)

    # Return Hasil Rerata
    return "%.2f"%total


print('Masukkan Banyak Data Berat Balita :', end=" ")
n = int(input())

for i in range(n):
    print(f'Masukkan Berat Balita Ke-{i+1} :', end=' ')
    # Inisialisasi Input Data Berat
    Data_Berat = float(input())

    # Masukkan Data Berat Ke Array (arrBerat)
    arrBerat.append(Data_Berat)


# Panggil procedur hitungMinMax(arrBerat)

hitungMinMax(arrBerat)


# Print Data Minimum, Maximum, dan Rerata Berat
rata_rata = rerata(arrBerat)
print(f"Rerata berat balita: {rata_rata} kg")