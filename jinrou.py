import random
from time import sleep
print('にんずうはなんにんですか？')
menber = int(input('人数は何人ですか:'))
print(str(menber) + '人')
villager = int(input('村人は何人ですか:'))
print(str(villager) + '人')
wolf = int(input('人狼は何人ですか:'))
print(str(wolf) + '人')
print('一人ずつ名前を入力してください')


profession = list()
for i in range(villager):
    profession.append('村人')
for i in range(wolf):
    profession.append('人狼')
print(profession)






profession_choose = profession
print(profession_choose)
peaples = {}
def peaple(hito,syokugyou):
    peaples[hito] = syokugyou
random_count = menber - 1
ran = random.randint(0,random_count)
print(ran)
for i in range(menber):
    peaple_name = input('名前を入力:')
    ran = random.randint(0,random_count)
    peaple_profession = profession_choose[ran]
    random_count -= 1
    peaple(peaple_name,peaple_profession)
    print(peaples)
    profession_choose.pop(ran)






print('それでは会議を始めてください')
print('制限時間は３分です')
for i in range(0,10):
    print("\r"+str(i),end="" )
    sleep(1)
print(' ')
print('３分経過しました')
print('誰を追放しますか')
for i in peaples.keys():
    print(i)

exiled = input('名前を入力してください')
print('追放されたのは' + exiled + 'です')
del peaples[str(exiled)]
print(peaples)

judge = ()
a = 0
b = 0
for i in peaples:
    if peaples[i] == '村人':
        a += 1
    else:
        b += 1

if b == 0:
    print('村人の勝利です')
else:
    print('人狼側の勝利です')

