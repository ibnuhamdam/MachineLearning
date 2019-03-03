import pandas as pd
import numpy as np

train = pd.read_csv('TrainsetTugas1ML.csv',index_col=False)
test = pd.read_csv('TestsetTugas1ML.csv',index_col=False)

# Inisiasi variable
ya = 0
no = 0
satuYes = 0
satuNo = 0
duaYes = 0
duaNo = 0
tigaYes = 0
tigaNo = 0
count = 0
age = []
work = []
education = []
maried = []
occup = []
relat =[]
hours = []


# Masukkan Rumus Disini
def Naive(Py,Pn,PNN,PYY):
    Ya = Py * PYY
    Tidak = Pn * PNN

    if (Ya > Tidak):
        return ">50K"
    else:
        return "<=50K"

def hitung(jumlah, total):
    return (jumlah / total)

def hasil(jumlah1,jumlah2,jumlah3,jumlah4,jumlah5,jumlah6,total,total1,arr):
    for i in range(6):
        if i==0:
            arr.append(hitung(jumlah1,total))
        elif i==1:
            arr.append(hitung(jumlah2,total))
        elif i==2:
            arr.append(hitung(jumlah3,total))
        elif i==3:
            arr.append(hitung(jumlah4,total1))
        elif i==4:
            arr.append(hitung(jumlah5,total1))
        elif i==5:
            arr.append(hitung(jumlah6,total1))

for x in range(6):
    if x == 0:
        a = "young"
        b = "adult"
        c = "old"
        d = age
    elif x==1:
        a = "Private"
        b = "Self-emp-not-inc"
        c = "Local-gov"
        d = work
    elif x==2:
        a = "Some-college"
        b = "Bachelors"
        c = "HS-grad"
        d = education
    elif x==3:
        a = "Married-civ-spouse"
        b = "Never-married"
        c = "Divorced"
        d = maried
    elif x==4:
        a = "Prof-specialty"
        b = "Craft-repair"
        c = "Exec-managerial"
        d = occup
    elif x==5:
        a = "Husband"
        b = "Not-in-family"
        c = "Own-child"
        d = relat
    else:
        a = "normal"
        b = "low"
        c = "many"
        d = hours
    
    ya = 0
    no = 0 

    for indextrain, rowtrain in train.iterrows():
        # Cari P untuk age, urutan young-adult-oldcount += 1

        if rowtrain[x+1] == a and rowtrain[8] == ">50K":
            satuYes += 1
        if rowtrain[x+1] == a and rowtrain[8] == "<=50K":
            satuNo  += 1

        if rowtrain[x+1] == b and rowtrain[8] == ">50K":
            duaYes += 1
        if rowtrain[x+1] == b and rowtrain[8] == "<=50K":
            duaNo  += 1    

        if rowtrain[x+1] == c and rowtrain[8] == ">50K":
            tigaYes += 1
        if rowtrain[x+1] == c and rowtrain[8] == "<=50K":
            tigaNo  +=1

        if rowtrain[8] == ">50K":
            ya += 1
        else:
            no += 1
    jumlah = satuYes+duaYes+tigaYes
    jumlah1 = satuNo+duaNo+tigaNo
    hasil(satuYes,duaYes,tigaYes,satuNo,duaNo,tigaNo,jumlah,jumlah1,d)
    satuYes = 0
    duaYes = 0
    tigaYes = 0
    satuNo = 0
    duaNo =0
    tigaNo = 0   


ProbYa = ya / (ya+no)
Probno = no / (ya+no)
Pyes = 1
Pno = 1
tebakan = []
for indextest,coltest in test.iterrows():
    for i in range(7):
        if i == 1:
            if (coltest[i]) == "young":
                Pyes = Pyes * age[0]
                Pno = Pno * age[3]
            if (coltest[i]) == "adult":
                Pyes = Pyes * age[1]
                Pno = Pno * age[4]
            if (coltest[i]) == "old":
                Pyes = Pyes * age[2]
                Pno = Pno * age[5]
        if i == 2:
            if (coltest[i]) == "Private":
                Pyes = Pyes * work[0]
                Pno = Pno * work[3]
            if (coltest[i]) == "Self-emp-not-inc":
                Pyes = Pyes * work[1]
                Pno = Pno * work[4]
            if (coltest[i]) == "Local-gov":
                Pyes = Pyes * work[2]
                Pno = Pno * work[5]
        if i == 3:
            if (coltest[i]) == "Some-college":
                Pyes = Pyes * education[0]
                Pno = Pno * education[3]
            if (coltest[i]) == "Bachelors":
                Pyes = Pyes * education[1]
                Pno = Pno * education[4]
            if (coltest[i]) == "HS-grad":
                Pyes = Pyes * education[2]
                Pno = Pno * education[5]
        if i == 4:
            if (coltest[i]) == "Married-civ-spouse":
                Pyes = Pyes * maried[0]
                Pno = Pno * maried[3]
            if (coltest[i]) == "Never-married":
                Pyes = Pyes * maried[1]
                Pno = Pno * maried[4]
            if (coltest[i]) == "Divorced":
                Pyes = Pyes * maried[2]
                Pno = Pno * maried[5]
        if i == 5:
            if (coltest[i]) == "Prof-specialty":
                Pyes = Pyes * occup[0]
                Pno = Pno * occup[3]
            if (coltest[i]) == "Craft-repair":
                Pyes = Pyes * occup[1]
                Pno = Pno * occup[4]
            if (coltest[i]) == "Exec-managerial":
                Pyes = Pyes * occup[2]
                Pno = Pno * occup[5]
        if i == 6:
            if (coltest[i]) == "Husband":
                Pyes = Pyes * relat[0]
                Pno = Pno * relat[3]
            if (coltest[i]) == "Not-in-family":
                Pyes = Pyes * relat[1]
                Pno = Pno * relat[4]
            if (coltest[i]) == "Own-child":
                Pyes = Pyes * relat[2]
                Pno = Pno * relat[5]
        if i == 7:
            if (coltest[i]) == "normal":
                Pyes = Pyes * hours[0]
                Pno = Pno * hours[3]
            if (coltest[i]) == "low":
                Pyes = Pyes * hours[1]
                Pno = Pno * hours[4]
            if (coltest[i]) == "many":
                Pyes = Pyes * hours[2]
                Pno = Pno * hours[5]
    tebakan.append(Naive(Pyes,Pno,Probno,ProbYa))
    Pyes = 1
    Pno = 1

print (tebakan)

export = pd.DataFrame(tebakan)

export.to_csv("TebakanTugas1ML.csv",encoding='utf-8', index=False,header=False)

# print (test)