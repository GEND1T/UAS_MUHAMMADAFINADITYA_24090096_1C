
from Soal_3_md import antrian

antrians = antrian()
antrians.push("adit")
antrians.push("afin")
antrians.push("tya")

while True:
    for i, data in enumerate(antrians.items,1):
        print(f'Antrian Ke-{i} {data}')


    antrians.tampilan()
    pilih = int(input('Masukan Pilihan : '))
    print("="*40)

    if pilih == 1:
        nama = str(input("Masukan Nama :"))
        antrians.push(nama())
        1
        print("="*100)
    if pilih == 2:
        antrians.pop()
    if pilih == 3:
        keluar = str("Ingin Keluar Program? (Y/T) : ").upper()
        if keluar == "Y":
            break
