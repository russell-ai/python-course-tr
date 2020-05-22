#%% Dosya oluşturma ve yazma işlemleri
# boş bir dosya oluşturma-x
# f = open("file.txt","x",encoding="utf8")
# f.write("Text satırı.")
# f.close()

# yazma moduyla oluşturma -w
# f = open("file.txt","w",encoding="utf8")
# f.write("Bu bir deneme satırıdır.")
# f.close()

# for ve range kullanarak text ekleme:
# f = open("file.txt","w",encoding="utf8")
# for i in range(1,5):
#     f.write(f"{i}.Deneme satırı.\n")
# f.close()
# append ile yeni satır ekleme:
# f = open("file.txt","a",encoding="utf8")
# f.write("Bu satır append ile eklendi.")
# f.close()

#%% Dosya okuma işlemleri
# read() ile okuma:
# f = open("file.txt","r",encoding="utf8")
# print(f.read())
# f.close()

# Döngü yardımı ile okuma:
# f = open("file.txt","r",encoding="utf8")
# for line in f:
#     print(line,end="")
# f.close()
# readline() ile okuma:
# f = open("file.txt","r",encoding="utf8")
# print(f.readline(),end="")
# print(f.readline())
# f.close()
# readlines() ile okuma
# f = open("file.txt","r",encoding="utf8")
# print(f.readlines())
# f.close()

# Okuma ve yazma birlikte kullanalım
# f = open("file.txt","w+",encoding="utf8")
# f.writelines(['A.Deneme satırı.\n', 'B.Deneme satırı.\n', 'C.Deneme satırı.\n', 'D.Deneme satırı.\n'])
# f.seek(0)
# print(f.read())
# f.close()

#%% Dosya Metodları
# readable(),writable() metodlarını kullanma:
# f = open("file.txt","r+",encoding="utf8")
# print(f.readable())
# print(f.writable())
# f.close()

# name,encoding,mode niteliklerini kullanma:
# f = open("file.txt","r+",encoding="utf8")
# print(f.name)
# print(f.mode)
# print(f.encoding)
# f.close()

# seek(),tell() metodlarını kullanma:
# f = open("file.txt","r+",encoding="utf8")
# f.seek(20)
# print(f.tell())
# print(f.read())

# truncate() ile yeniden boyutlandırma:
# f = open("file.txt","r+",encoding="utf8")
# f.truncate(40)
# f.close()
# dosyanın kapalı olup olmadığını kontrol etme:
# print(f.closed)

#%% Context Manager with statement
# with open("file.txt","w+",encoding="utf8") as f:
#     for i in range(1,5):
#         f.write(f"{i}.Deneme satırı.\n")
#     f.seek(0)
#     print(f.read())
# print(f.closed)

#%% try-except-finally kullanımı
# try:
#     f = open("file.txt","r",encoding="utf8")
#     print(f.write("Yeni text."))
# except IOError as e:
#     print("Hata oluştu.",e)
# finally:
#     f.close()
#     print(f.closed)

#%% Örnek Uygulama - Kopyalama Fonksiyonu
# Text Dosyalar için:
# def kopyalama(file,newfile):
#     with open(file,"r",encoding="utf8") as okunacakDosya:
#         data = okunacakDosya.read()
#         with open(newfile,"w",encoding="utf8") as yazılacakDosya:
#             yazılacakDosya.write(data)
#
# kopyalama("file.txt","file2.txt")

# Binary Dosyalar için: (b ifadesini mode ifadesine ekliyoruz)

# def kopyalama(file,newfile):
#     with open(file,"rb") as okunacakDosya:
#         data = okunacakDosya.read()
#         with open(newfile,"wb") as yazılacakDosya:
#             yazılacakDosya.write(data)
#
# kopyalama("kapak.jpg","kapak2.jpg")


