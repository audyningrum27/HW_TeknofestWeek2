clubA = input("Klub A : ")
clubB = input("Klub B : ")

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
    scoreA = int(n[0])
    scoreB = int(n[1])
    if ((scoreA or scoreB) or (scoreA and scoreB)) < 0:
        print("Pertandingan selesai")
        break
    elif scoreA > scoreB:
        print(f"Hasil {j} : {clubA}", end=" ")
    elif scoreB > scoreA:
        print(f"Hasil {j} : {clubB}", end=" ")
    elif scoreA == scoreB:
        print(f"Hasil {j} : Draw", end=" ")

    print("")
