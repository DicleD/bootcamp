# 1
giris = "hi my name is john and i am learning python"
sonuc = "Hi My NaMe Is JoHn AnD i Am LeArNiNg PyThOn"
def change(metin): # new_metin tanımlamazsak da yazdırır ama o zaman bir cümle içinde yazdırmıyor
    new_metin = ""
    for i in range(0, len(metin)):
       if i % 2 == 0:
           new_metin = new_metin + metin[i].upper()
       else:
           new_metin = new_metin + metin[i].lower()
    return new_metin

#enumerate
# 2
students = ["John", "mark", "Vanessa", "Mariam"] #öğrencileri index numaralarına göre 2 gruba böl
for student in students:
    liste = [[],[]] 
    for i in range(len(students)):
       if i % 2 == 0:
          liste[0].append(students[i])
       else:
           liste[1].append(students[i])

def divide(students):
   liste = [[], []]
   for index, student in enumerate(students, 1): #indexlemeye 1'den başlar bu drumda
       if index % 2 == 0:
          liste[0].append(student)
       else:
           liste[1].append(student)
   return liste
#################################
#ilk soru enumerate ile yaparsak
def change(metin):
    new_metin = ""
    for i, letter in enumerate(metin):
       if i % 2 == 0:
           new_metin = new_metin + letter.upper()
       else:
           new_metin = new_metin + letter.lower()
    return new_metin

#COMPREHENSIONS
students = ["John", "mark", "Vanessa", "Mariam"]
no_students = ["John", "Vanessa"]
[student.upper() if student in no_students else student.lower() for student in students]
#dictionary comprehensions
dict = {"a":1, "b": 2, "c": 3, "d": 4}
{key.upper() for key in dict.keys()}
{value+5 for value in dict.values()}
{k.upper(): v*5 for (k,v) in dict.items()} ##HAYAT KURTARAN SERİSİNDEN


# döngü kullanarak sözlüğe eleman eklemek
numbers = range(10)
{n**2 if n %2 == 0 else n for n in numbers }
{n: n**2 for n in numbers if n % 2 ==0} # sözlük yapısına çevirmiş oluyoruz böylece!

# UYGULAMALAR
import seaborn as sns
df = sns.load_dataset("car_crashes")
#1 amaç değişkenlerin isimlerini büyütmek
df.columns = [col.upper() for col in df.columns]
#isminde "INS" olanların başına FLAG diğerlerine NO_FLAG eklemek istiyorum
df.columns = ["FLAG "+ col if "INS" in col else "NO_FLAG " + col for col in df.columns]

#2 categorical değişkenlerin başına CAT yazmak
df.columns = ["CAT_"+ col if df[col].dtype == "O" else col for col in df.columns ]####
#3 key si string value su sabit bir liste olan sözlük oluşturmak, ["mean","min","max","var"]
agg_list = ["mean","min","max","var"]
{col: agg_list for col in df.columns} # ya da direkt o listeyi value olarak belirtebiliriz

num_cols = [col for col in df.columns if df[col].dtype != "O"]
new_dict = {col: agg_list for col in num_cols}
df.groupby("CAT_NO_FLAG ABBREV").agg(new_dict) ### agg önemli

df = sns.load_dataset("tips")
num_cols = [col for col in df.columns if df[col].dtype in [int, float]]
new_dict = {col: agg_list for col in num_cols}
df.groupby("time").agg(new_dict)

#4 values kısmının başına "total_" eklemek
new_agg = ["total_" + x for x in agg_list]
new_dict = {col: new_agg for col in num_cols}

##5 mülakat sorusu// values kısmına da etki etmek istiyoruz, tek bir satırda
df = sns.load_dataset("car_crashes")
agg_list = ["mean","min","max","var"]
num_cols = [col for col in df.columns if df[col].dtype in [int, float]]
{col: [str(col)+"_" + c for c in agg_list] for col in num_cols}

#6 mülakat sorusu//bir listenin ilk elemanını key diğerlerini values olarak atamak(int olarak)
{df[col][0]: df[col][1:] for col in df[num_cols].values}
{row[0]: [int(s) for s in row[1:]] for row in df[num_cols].values}