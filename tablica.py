#Создать словарь: студент и СЛОВАРЬ его оценок (дата - оценка)
#С помощью форматирования строк вывести табличку:


#Из за проблем приступил выполнять задание поздно,мало что получилось
#Не понял как вывести дату-оценку
#Особенно чтобы у каждого ученика были разные оценки используя random
from datetime import datetime
from random import randint
ocenka = randint(1, 12)
clas={
'Вася':{ 
    datetime(2024,12,6):ocenka,
    datetime(2024,3,14):ocenka,
},
'Ася':{
    datetime(2024,12,6):ocenka,
    datetime(2024,3,14):ocenka,
},
'Мася':{
    datetime(2024,12,6):ocenka,
    datetime(2024,3,14):ocenka,
},
}
sr_ocenka= 0
kol_ocenok= 0
for zzz in clas:
    clas[zzz] = ocenka
    kol_ocenok+=1
    sr_ocenka+=clas[zzz]
    ttt_1=sr_ocenka/kol_ocenok

res='''
       2024 12 6        2024 3 14       Cреднее 
Вася       %i                %i          %4.1f

Ася        %i                %i          %4.1f

Мася       %i                %i          %4.1f
'''
print(res%(
    clas[zzz],
    clas[zzz],
    ttt_1,
    clas[zzz],
    clas[zzz],
    ttt_1,
    clas[zzz],
    clas[zzz],
    ttt_1
))


