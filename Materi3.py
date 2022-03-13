#menghitung gaji seorang karyawan 


nama ="Arifatwa" 
gaji_pokok = 1000000 
lama_lembur = 11 
gaji_lemburperjam = 5000 
gaji_lembur = gaji_lemburperjam * lama_lembur 
gaji_kotor = gaji_pokok + gaji_lembur 
pajak =9/100 
potongan = gaji_pokok*pajak 
gaji_bersih = gaji_kotor - potongan 

print("nama          : ",nama) 
print("Gaji pokok    =Rp",gaji_pokok) 
print("Gaji_lembur/jam =Rp",gaji_lemburperjam) 
print("Gaji lembur     =Rp",gaji_lembur) 
print("Gaji kotor      =Rp",gaji_pokok) 
print("pajak           =",pajak) 
print("potongan        =Rp",potongan) 
print("Gaji bersih     =Rp",gaji_bersih)