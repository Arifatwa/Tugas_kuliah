#buatlah contoh codingan colection(list, set, tuple, dictionary)
print("="*90)   

print("list".center(90))
li = ["mangga", "pisang", "kelapa", "durian", "apel"]
li[2] = "str" #ganti 
del li[3] #hapus
li.append(363) #tambah
for li in li:    
    print(li)
print("="*90)  
  
print("set".center(90))   
se = { "kelly", "hayato" ,"maxim", "adam" "jotta"}
se.add("hshshs") #menambahkan
se.remove("hayato") #menghapus
#se[4] = 2627 
for se in se:
    print(se)
       
print("="*90)    
print("tuple".center(90))
tu = ("naruto", "sasuke", "sakura", "kakasi", " hinata")
#tu.append("53")
#tu.remove("sakura")
#tu[2] = "boruto"
for tu in tu:
    print(tu)
    
print("="*90)
print("dictionary".center(90))
dic = {"hayato ":80, "maxim":90, "alok":50, "kelly":100}
itm = dic.items()
dic[2] = 85 # mengupdate velue
dic["aldi"] = 78 #menambah nilai/velue
del dic[2] #menghapus

for i,j in itm :
    print(i, ":",j)
    