print("Nama : Muh. Arifatwa".center(30))
print("Nim : D0221081".center(24))
print("Kelas : Informatika F".center(31))
print("Matkul : Alogaritma dan struktur data".center(48))
print("/"*90)
print("TUGAS ASD".center(90))
print("=/=/=/=/=/=/=/=/=/=/=".center(90))


print("LIST".center(90))

list = ["mangga", "pisang", "pepaya", "anggur", "kelapa"]
for i in list:
    list[3]="durian"
    print(i)
    
print("="*90)
print("SET".center(90))

set = {"arifatwa", "hndra", "fyan", "inul"}
set.add("aywm") #menambah
set.remove("arifatwa") #menghapus
for i in set:     
    print(i)

print("="*90)
print("TUPLE".center(90))

tuple = ("mahasiswa", 123, 3.4)
for i in tuple:
    print(i)
    
print("="*90)   
 
print("DICTIONARY".center(90))
dictionary = {"alim":10, "sinta":20, "budi":30, "tasya":40}
key = dictionary.keys()
value = dictionary.values()
item = dictionary.items()
dictionary.pop("alim") #menghapus
dictionary["yaya"] = 36 #menambah

for k,v in item:
    print(k,":", v)
    