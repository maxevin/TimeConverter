import math

def timeconverter(seconds): #perhitungan time converter
    jam = math.floor(seconds/3600)
    menit = math.floor((seconds%3600)/60)
    detik = math.floor(((seconds%3600)%60))
    print('Konversi : %d:%d:%d' % (jam,menit,detik))

seconds = int(input('Masukkan Detik : ')) #user input
if seconds > 359999: #jika dimasukan angka lebih dari 359999 maka akan dihasilkan output error
    print('Invalid Input!')
elif seconds != type(int):
    print('Invalid Input!')
else:
    timeconverter(seconds) #panggil function
    



