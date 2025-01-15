data = [{
    'NIM' : '24090096',
    'NAMA': 'MUHAMMAD AFIN ADITYA'


}]

while True:
    
    nim = str(input('MASUKAN NIM : '))
    nama = str(input('MASUKAN NAMA : '))
    cetak = {"NIM": nim, "NAMA": nama}
    data.append(cetak)
    print("="*40)
    option = str(input('Ingin Tambah Lagi  ( YA/TIDAK ) ? '  ))


    
    if option == 'TIDAK' :
        break

    

