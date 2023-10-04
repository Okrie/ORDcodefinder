import requests
import numpy as np
import random
from bs4 import BeautifulSoup
from . import printResult

def randomRule():
    rules = []
    
    rules.append('상위 개수는?')                             # 1
    rules.append('인생의 고도')                              # 2
    rules.append('랜유 강제전')                             # 3
    rules.append('신세계 보상치기')                          # 4
    rules.append('강제 상위전')                             # 5
    rules.append('상위 밴')                                 # 6
    rules.append('갈수 있는 상위 (4개 중 마음대로)')         # 7
    # rules.append('-악몽-')   
    # rules.append('순서대로 갈수 있는 상위 제한')
    # rules.append('이 캐릭 필수! 전설 / 히든')

    print('---- Random Rule Picker-----')
    randomrule = np.random.randint(1, len(rules)+1)
    printResult.printresult(rules[randomrule-1])
    print(' ', rules[randomrule-1])
    if randomrule < 3:
        if randomrule == 1:
            randnum = []
            for i in range(4):
                randnum.append(str(np.random.randint(1, 5)))
            printResult.printresult(', '.join(randnum))
        else:
            printResult.printresult(np.random.randint(6, 15))
    elif randomrule < 5:
        printResult.printresult('')        
    elif randomrule < 6:
        result = unit_rule(1)
        printResult.printresult(''.join(result))
    elif randomrule == 6:
        result = unit_rule(10)
        printResult.printresult(', '.join(result))
    elif randomrule == 7:
        result = unit_rule(4)
        printResult.printresult(', '.join(result))

    print('----- Done -----\n\n')


def unit_rule(inputnum):
    print("-----Start Scrapy----")
    unit_list = []
    unit_level = ['9', '10', '12', '13']

    headers = {'User-Agent':'Chrome/66.0.3359.181'}
    webpage = requests.get('https://ordsearch.net/mix/helper', headers=headers)

    status = webpage.status_code

    if status==200:
        soup = BeautifulSoup(webpage.content, "html.parser")
        units = soup.select('table .helper-units')
        
        for i in units:
            if i.attrs['data-level'] in unit_level:
                unit_list.append(i.text.strip())

        unit_list.pop(unit_list.index('상디 (강화)'))
        unit_list.pop(unit_list.index('조로 (강화)'))
        unit_list.pop(unit_list.index('조로 (염왕)'))
        unit_list.pop(unit_list.index('니카 (루초)'))
        unit_list.pop(unit_list.index('니카 (뱀초)'))
        unit_list.pop(unit_list.index('초월쿠마'))
        unit_list.append('니카')
    print("-----Scrapy  Done----\n\n")
    return random.choices(unit_list, k=inputnum)



def load(inputnum):
    str_name = []
    listname = []
    naming = []
    count = []
    splitList = []
    
    naming.append('제한됨')
    naming.append('초월함')
    naming.append('불멸의')
    naming.append('영원한')

    headers = {'User-Agent':'Chrome/66.0.3359.181'}
    webpage = requests.get('https://ordsearch.net/mix/helper', headers=headers)
    status = webpage.status_code
    strnum = '11'
    
    if status==200:
        soup = BeautifulSoup(webpage.content, "html.parser")
        titles = soup.select('table', class_='table table-sm table-hover p-0 mt-3')
        
        for title in titles[8:]:
            str_name.append(' '.join(title.text.split()))

        listAll = str_name[0] + ' ' + str_name[2] + ' ' + str_name[4] + ' ' + str_name[5]
        
        listname = listAll.split(' ')
        listname.pop(listname.index('초월쿠마'))
        listname.pop(listname.index('스코퍼'))
        listname.pop(listname.index('호킨스'))

        print(listname)

        count.append(listname.index(naming[1]) - listname.index(naming[0])-1)
        count.append(listname.index(naming[2]) - listname.index(naming[1])-2)
        count.append(listname.index(naming[3]) - listname.index(naming[2])-1)
        count.append(len(listname[listname.index(naming[3]):])-1)

        

        sum = 0
        for i in range(4):
            sum += count.pop()

        count.append(listname.index(naming[0]))
        count.append(listname.index(naming[1])-1)
        count.append(listname.index(naming[2])-2)
        count.append(listname.index(naming[3])-3)

        listname.pop(listname.index(naming[0]))
        listname.pop(listname.index(naming[1]))
        listname.pop(listname.index(naming[2]))
        listname.pop(listname.index(naming[3]))

        maxnum = sum
        
        choicecharacter = []
        randcheck = []

        print(inputnum)
        while True:
            
            randcheck.append(np.random.randint(inputnum, maxnum))
            list(set(randcheck))

            if len(randcheck) is inputnum:
                break
        
        randnum = []
        randnum = sorted(randcheck)

        print(count)
        for i in randnum:
            print(i)
            print(count)
            if int(i) >= count[3]:
                choicecharacter.append(listname[i] + naming[3][:2])
            elif int(i) >= count[2]:
                choicecharacter.append(listname[i] + naming[2][:2])
            elif int(i) >= count[1]:
                choicecharacter.append(listname[i] + naming[1][:2])
            else:
                choicecharacter.append(listname[i] + naming[0][:2])

        result = ' '.join(choicecharacter)

        printResult.printresult(result)
    else:
        print('server error')