

class Buah :
    #menginisialisasi atribut
    def __init__(self, nama, warna, rasa): 
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    # metode
    def setNama(self,item):
        self.nama = item

    def setWarna(self,item):
        self.warna = item
        
    def setRasa(self,item):
        self.rasa = item

    def information(self):
        return f'Nama buah : {self.nama} | Warna buah: {self.warna} | Rasa Buah : {self.rasa}'
    

# Membuat Object
buah1 =Buah('anggur', 'merah', 'asam')
print(buah1.information())


buah1.setNama('pepaya')
buah1.setWarna('kuning')
buah1.setRasa('manis')

print(buah1.information())


