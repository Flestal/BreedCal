import csv

palCSV = []
f=open('pals.csv','r',encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
    palCSV.append(line)
    

def FindPalIngredient(target):
    resData=[]
    for data1 in palCSV:
        for data2 in palCSV:
            if data1==data2:
                continue
            if (int(data1[2])+int(data2[2]))/2==target:
                s = ''+data2[1]+' + '+data1[1]
                if s in resData:
                    continue
                resData.append(''+data1[1]+' + '+data2[1])
    for data in resData:
        print(data)

def FindNewPal(boxIDList):
    tempIDList=[]
    resIDList=[]
    resNameList=[]
    for data1 in boxIDList:
        for data2 in boxIDList:
            for search in palCSV:
                if (data1+data2)/2 == int(search[2]):
                    tempIDList.append(int(search[2]))
    for Id in tempIDList:
        if Id not in boxIDList:
            resIDList.append(Id)
    for i in resIDList:
        for search in palCSV:
            if i == int(search[2]):
                if search[1] not in resNameList:
                    resNameList.append(search[1])

    print(resNameList)

if __name__=="__main__":
    print('메인 시작')
    what = input('1: 원하는 팔 재료 찾기\n2: 팔 박스 기준 새로 만들 수 있는 팔 찾기 : \n')
    if what=='1':
        targetID=-1
        targetName=input('원하는 팔의 이름을 입력하세요 : ')
        for search in palCSV:
            if targetName == search[1]:
                targetID=int(search[2])
                break 
        FindPalIngredient(targetID)
    elif what=='2':
        boxlist=input('박스에 있는 팔 목록을 스페이스바로 구분지어 입력하세요 : ').split()
        boxIDList = []
        for item in boxlist:
            for search in palCSV:
                if item == search[1]:
                    boxIDList.append(int(search[2]))
        FindNewPal(boxIDList)

