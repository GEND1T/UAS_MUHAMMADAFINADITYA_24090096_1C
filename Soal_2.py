import pandas as pd

df = pd.DataFrame([
    [90,80],
    [50,60],
    [65,75],
], 

index=['Mahasiswa 1','Mahasiswa 2','Mahasiswa 3'], 
columns=[ "Algoritma dan Struktur Data", "Matematika Numerik"])

df['Rata']=df.mean(axis=1)

nilai_rata2 = df.mean(axis=0)



print(df)
print(nilai_rata2)


# Untuk code export data ke csv, jika menggunakan parameter (sep=';'), untuk dilaptop saya hasilnya tidak rapi. Jadi saya tidak menggunakan parameter (sep=';') 
df.to_csv('DataPenjualan1.csv')
# df.to_csv('Data_Penjualan2.csv', sep=';')