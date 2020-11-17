print("Klub A :", end=" ")
a = input()
print("Klub B :", end=" ")
b = input()

i = 0
arr = []
while i >= 0:
    i += 1
    print(f"Pertandingan {i} :", end=" ")
    n = input().split()
    arr.append(n)
    if int(n[0] or n[1]) <= -1:
        break


j = 0
for n in arr:
    j += 1
    na = int(n[0])
    nb = int(n[1])
    if (((na or nb) or (na and nb))) < 0:
        print("Pertandingan selesai")
        break
    elif na > nb:
        print(f"Hasil {j} : {a}", end=" ")
    elif nb > na:
        print(f"Hasil {j} : {b}", end=" ")
    elif na == nb:
        print(f"Hasil {j} : Draw", end=" ")

    print("")
