from bs4 import BeautifulSoup
import requests
import os
import random
import time


from io import BytesIO

import matplotlib.pyplot as plt
import matplotlib.image as mpimg








'''
기본 세팅 : 최대cp 기준으로 사냥터 정리. 공격력 방어력 등 저장.

아이템 종류 : 상처약, 몬스터볼

- 스타트 포켓몬 선택.
- 포켓몬 상태 체크 / 현재 사냥터 : ___
    - 사냥하기 : 이미지 한번 띄워주기. 공격 기술 나열
        - 공격하기 (스킬 구현 고민)
        - 아이템 사용
            - 상처약 : 체력 회복.
            - 몬스터 볼 : 남은 체력에 따라 확률 다르게
        - 도망가기
    - 가방 열기.
        - 남은 아이템 개수 확인.  
        - 나가기.
    - 보유 포켓몬 확인하기.
    - 사냥터 이동
        -현재 사냥터 : / 이동할 사냥터 : 
        

'''
    


res=requests.get("https://pokemongo.inven.co.kr/dataninfo/pokemon/?lang=kor")
soup=BeautifulSoup(res.text,"html.parser")


# grass, poison, fire, water, bug, flying, dark, normal, electric, ice, steel, psychic
# ground, fairy, fighting, rock, ghost, dragon

# 속성 영 -> 한
def changeAtt(att):
    if att=='normal':
        return '노말'
    if att=='fighting':
        return '격투'
    if att=='flying':
        return '비행'
    if att=='poison':
        return '독'
    if att=='ground':
        return '땅'
    if att=='rock':
        return '바위'
    if att=='bug':
        return '벌레'
    if att=='ghost':
        return '고스트'
    if att=='steel':
        return '강철'
    if att=='fire':
        return '불'
    if att=='water':
        return '물'
    if att=='grass':
        return '풀'
    if att=='electric':
        return '전기'
    if att=='psychic':
        return '에스퍼'
    if att=='ice':
        return '얼음'
    if att=='dragon':
        return '드래곤'
    if att=='dark':
        return '악'
    if att=='fairy':
        return '페어리'
    
# url 주소에 사용할 변수 설정
def changeAttNum(att):
    if att=='노말':
        return 1
    if att=='격투':
        return 2
    if att=='비행':
        return 3
    if att=='독':
        return 4
    if att=='땅':
        return 5
    if att=='바위':
        return 6
    if att=='벌레':
        return 7
    if att=='고스트':
        return 8
    if att=='강철':
        return 9
    if att=='불':
        return 10
    if att=='물':
        return 11
    if att=='풀':
        return 12
    if att=='전기':
        return 13
    if att=='에스퍼':
        return 14
    if att=='얼음':
        return 15
    if att=='드래곤':
        return 16
    if att=='악':
        return 17
    if att=='페어리':
        return 18 
    
    



all={}      # 모든 포켓몬 모음{이름 : 정보} 순서로.


# 데이터 저장
for i in soup.select('.pokemonicon'):
    new=[]
    save=[]
    att=[]  # 타입

    # # 사진
    link=i.select_one('img').get('src')
    link='https:'+link
    link2={'link':link}

    # 이름
    name=i.select('.pokemonname')[0].text.split('.')[1][:-1]
    # 속성

    for j in i.select('.pokemontype>img'):
        temp=j.get('src').split('.')[3].split('_')[3]

        att.append(changeAtt(temp))
        
    att2={'타입':att}
    # 능력치
    for j in i.select('li'):
        save.append(j.text)
        # info=j.select_one('.pokemoninfo>li')
        # print(info)

    cp={save[0]:save[1]}
    atc={save[2]:save[3]}
    deff={save[4]:save[5]}
    phy={save[6]:save[7]}
    
    all[name]=[cp,atc,deff,phy,att2,link2]

print(all['이상해풀'])
# 사냥터 나누기.
cp1=[]
cp2=[]
cp3=[]
cp4=[]
for i in all.keys():
    cp=int(list(all[i][0].values())[0])
    # 왕초보
    if cp<=1000:
        cp1.append(i)
    # 초심자
    elif 1000<cp<=2000:
        cp2.append(i)
    # 중급자
    elif 2000<cp<=3000:
        cp3.append(i)
    # 고수
    else:
        cp4.append(i)



# 사냥터 변환(사냥터 입력 받아서 랜덤 포켓몬 리턴해주기)
def huntPlace(a):
    if a=='초보':
        return random.choice(cp1)
    if a=='초급자':
        return random.choice(cp2)
    if a=='중급자':
        return random.choice(cp3)
    if a=='고수':
        return random.choice(cp4)


# # 포켓몬 선택
# info=[]
# rand=random.randrange(0,22)
# cnt=0
# for i in cp1:
#     cnt+=1
#     if cnt==rand:
#         for j in all[i]:
#             info.append(j)




# data=all['이상해씨']
def prt(data):
    cnt=0
    for i in data:
        for j in i:
            if cnt<4:
                print(j," : ",i[j])
                cnt+=1
            elif cnt==4:
                blank=''
                for k in i[j]:
                    blank+=f'{k}  '
                print(f"{j} : {blank}")
                cnt+=1
        if cnt==5:
            break



# 말하기 속도 조절
def speak01(word):
    for i in word:
        print(i)
        time.sleep(0.1)
def speak01n(word):
    for i in word:
        print(i,end='')
        time.sleep(0.1)

def speak03n(word):
    for i in word:
        print(i,end='')
        time.sleep(0.3)

def speak03(word):
    for i in word:
        print(i)
        time.sleep(0.3)


# 체력 표시
def drawFit(num1,num2):
    fit2=int(num1/num2*10)
    print('●'*fit2+'○'*(10-fit2))



# 사냥터 저장
hunt='초보'

# 지갑
money=0

# [{'최대 CP': '946'}, {'공격력': '94'}, {'방어력': '121'}, {'체력': '127'}, {'타입': ['water']}, {'link': 'https://static.inven.co.kr/image_2011/site_image/pokemongo/pokemonicon/pokemon_007.png?v=20181121a'}]



# 포켓몬 이름을 입력받아 스킬 리스트 리턴
def getSkill(name):
    
    # https://pokemongo.inven.co.kr/dataninfo/move/?mtype=10&mclass=&sname=&sort=dps&sort2=desc&code=
    
    # link=f"https://pokemongo.inven.co.kr/dataninfo/move/?mtype=A{changeAttNum(name)}0&mclass=&sname=&sort=dps&sort2=desc&code="
    link=f"https://pokemongo.inven.co.kr/dataninfo/move/?mtype={changeAttNum(name)}&mclass=&sname=&sort=dps&sort2=desc&code="
    
    res=requests.get(link)

    soup=BeautifulSoup(res.text,"html.parser") 
    skillList=[]
    # 'tbody>tr>td>span>a'

    for i in soup.select('.moveList>table>tbody>tr'):
        try:
            skillName=i.select('td>span>a')[0].text.split()[0]
            skillPower=int(i.select('td:nth-child(5)')[0].text.split()[0])
            skillSet={skillName:skillPower}
            skillList.append(skillSet)
        except:
            pass
    random.shuffle(skillList)
    skillList=skillList[:4]

    # skill 4 return
    # [{'꽃보라': 110}, {'파워휩': 90}, {'풀묶기': 90}, {'리프블레이드': 70}]
    return skillList
#pokemongoList > div > table > tbody > 

# /html/body/div[4]/div[1]/section/article/section[2]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[5]
# 포켓몬 만들기
# '이상해씨'
class MakeCh:
    # 이름
    def __init__(self,name):
        self.name=name
        # self.info=[]
    def makeInfo(self):
        self.atk=int(all[self.name][1]['공격력'])
        self.fit=int(all[self.name][3]['체력'])
        self.fitsave=int(all[self.name][3]['체력'])
        self.chrtype=all[self.name][4]['타입'][0]
        self.money=0
        self.potion=0
    # 스킬 정보 저장(크롤링)
    # def makeInfo(self):
        
    

print('스토리 처음')
print()
print('1. 이상해씨')
prt(all['이상해씨'])
print()
print('2. 파이리')
prt(all['파이리'])
print()
print('3. 꼬부기')
prt(all['꼬부기'])
print()



while True:
    try:
        a=int(input('스타팅 포켓몬을 선택하세요.\n'))
        if a==1:
            #링크 가져와서 이미지 띄우기
            name='이상해씨'

            # 스타팅 포켓몬 객체 생성
            mainCh=MakeCh(name)

            # 링크
            link=all[name][5]['link']
            res2 = requests.get(link)
            img = mpimg.imread(BytesIO(res2.content))
            # plt.imshow(img)
            # plt.axis('off')  # 축을 표시하지 않도록 설정 (선택사항)
            # plt.show()

            mainCh.makeInfo()

            # 속성 설정.
            # atk=mainCh.atk
            # fit=mainCh.fit
            # chrtype=mainCh.chrtype
            break


        elif a==2:
            #링크 가져와서 이미지 띄우기
            name='파이리'
            mainCh=MakeCh(name)

            # 링크
            link=all[name][5]['link']
            res2 = requests.get(link)
            img = mpimg.imread(BytesIO(res2.content))
            plt.imshow(img)
            plt.axis('off')  # 축을 표시하지 않도록 설정 (선택사항)
            plt.show()

            mainCh.makeInfo()
            break

        elif a==3:
            #링크 가져와서 이미지 띄우기
            name='꼬부기'
            mainCh=MakeCh(name)

            # 링크
            link=all[name][5]['link']
            res2 = requests.get(link)
            img = mpimg.imread(BytesIO(res2.content))
            plt.imshow(img)
            plt.axis('off')  # 축을 표시하지 않도록 설정 (선택사항)
            plt.show()

            mainCh.makeInfo()
            break

        elif a==4:
            #링크 가져와서 이미지 띄우기
            name='피카츄'
            mainCh=MakeCh(name)

            # 링크
            link=all[name][5]['link']
            res2 = requests.get(link)
            img = mpimg.imread(BytesIO(res2.content))
            plt.imshow(img)
            plt.axis('off')  # 축을 표시하지 않도록 설정 (선택사항)
            plt.show()

            mainCh.makeInfo()
        else:
            print('잘못 입력하셨습니다. 다시 입력해주세요.')
    except:
        pass





while True:
    try:
        a=int(input(f'{name}을 선택하였다! 이름을 지어주시겠습니까?\n1. Yes\n2. No\n'))
        if a==1 or a==2:
            break
        else:
            pass
    except:
        print('잘못 입력하셨습니다. 1과 2 중에 다시 선택해주세요.')
        pass
if a==1:
    b=input('이름은 무엇입니까?\n')
    name=b

    print(f"{name}이는 기분이 좋은 것 같다. {name}{name}!!")


mainCh_skillList=[]
for i in getSkill(mainCh.chrtype):
    mainCh_skillList.append({list(i.keys())[0]:list(i.values())[0]})

while True:
    print('------------------------------')
    print()
    print(f'포켓몬 이름 : {name}\t\t현재 사냥터 : {hunt}')
    print(f"{name}의 공격력 : {mainCh.atk}")
    print(f"{name}의 체력 : {mainCh.fit}")
    print(f"{name}의 타입 : {mainCh.chrtype}")
    print(f"소지 금액 : {mainCh.money}")
    print()
    ch=int(input('무엇을 하시겠습니까?\n1. 사냥하기\n2. 가방열기\n3. 도감\n4. 사냥터 이동\n5. 상점\n6. 포켓몬 센터\n\n'))

    # 내 포켓몬
    # mainCh.atk, ...
    # # 상대 포켓몬
    # en_atk, en_fit, en_chrtype

    # 1. 사냥하기.
    if ch==1:
        # 지정 사냥터에서 상대 포켓몬 이름 랜덤으로 가져옴.
        en_name=huntPlace(hunt)

        enemy=MakeCh(en_name)
        enemy.makeInfo()
        enemy_skillList=[]
        
        
        # skill 데이터 저장
        for i in getSkill(enemy.chrtype):
            enemy_skillList.append({list(i.keys())[0]:list(i.values())[0]})

        #enemy.skillList : [{9: '섀도크루'}, {10: '병상첨병'}, {8: '놀래키기'}, {100: '섀도볼'}]
        while True:
            print('----------------------')
            print('---------사냥터---------')
            print(f'{mainCh.name} VS {enemy.name}')
            print('----------------------')
            print('----------------------\n')
            # speak01('....')
            # speak01n('부스럭 부스럭')
            # speak01n(f"{en_name}(이)가 나타났다!")

        
            print(f"이름 : {en_name}")
            print(f"체력 : {enemy.fit}")
            print(f"공격력 : {enemy.atk}")
            print(f"타입 : {enemy.chrtype}")
            drawFit(enemy.fit,enemy.fitsave)

            print('----------------')
            print(f"내 포켓몬 : {name}")
            print(f"체력 : {mainCh.fit}")
            print(f"공격력 : {mainCh.atk}")
            print(f"타입 : {mainCh.chrtype}")
            drawFit(mainCh.fit,mainCh.fitsave)
            print()
            print()
            print()
            do=input('무엇을 하시겠습니까?\n1. 공격하기\n2. 아이템 사용\n3. 도망가기\n')
            # 공격하기.
            if do=='1':
                cnt=1
                print()
                print('---------스킬 목록---------')
                for i in mainCh_skillList:
                    print(f"{cnt}. {list(i.keys())[0]} : {list(i.values())[0]}")
                    cnt+=1
                print()
                print()
                ch=int(input('무슨 스킬을 사용하시겠습니까?\n'))
                # [{'기가드레인': 50}, {'하드플랜트': 100}, {'파워휩': 90}, {'리프블레이드': 70}]

                # 스킬 선택
                skillName=list(mainCh_skillList[ch-1].keys())[0]
                damage=int(list(mainCh_skillList[ch-1].values())[0]/2)



                # damage : ['하드플랜트']
                enemy.fit-=damage
                print(f"{mainCh.name}의 {skillName}공격!")
                print(f"{enemy.name}은 {damage}의 피해를 입었다!")
                print()
                # pause
                
                # enemy die
                if enemy.fit<=0:
                    # 돈 증가
                    up=random.randrange(100,301)
                    print(f"{enemy.name}(이)가 죽었다!")
                    print(f"{up}의 돈을 주웠다!")
                    mainCh.money+=up
                    com=random.randrange(1,3)
                    # 능력치 증가
                    up2=random.randrange(10,31)
                    if com==1:
                        mainCh.atk+=up2
                        print(f"{mainCh.name}의 공격력이 {up2}만큼 증가하였다!")
                    else:
                        mainCh.fit+=up2
                        print(f"{mainCh.name}의 체력이 {up2}만큼 증가하였다!")
                    break
                


                # enemy attack
                ran=random.randrange(0,4)
                enemy_skillName=list(enemy_skillList[ran].keys())[0]
                enemy_damage=int(list(enemy_skillList[ran].values())[0]/2)
                print(f"{enemy.name}의 {enemy_skillName} 공격!")
                print(f"{mainCh.name}은 {enemy_damage}의 피해를 입었다!")
                mainCh.fit-=enemy_damage
                print()
                print()
                # pause

                # mainCh 죽으면
                if mainCh.fit<=0:
                    # 천천히 말하기.
                    print(f"{mainCh.name}(이)가 죽었다!")
                    print(f"서둘러 도망가자...")
                    loss=random.randrange(100,301)
                    mainCh.money-=loss
                    print(f"돈을 {loss}만큼 잃어버렸다.")

                    break

                        #time.sleep(1)
                    ################1초 멈춰주기
                    

                    
            # 아이템 사용
            elif do=='2':
                print('무엇을 사용하시겠습니까?\n2. 뒤로가기')
                use=input(f"1. 상처약 : {mainCh.potion}개")
                if use=='1':
                    if mainCh.potion>0:
                        print('상처약을 사용하였습니다.')
                        print('체력이 20 증가합니다.')
                        if mainCh.fitsave>mainCh.fit+20:
                            mainCh.fit+=20
                        else:
                            mainCh.fit=mainCh.fitsave
                    else:
                        print('상처약의 개수가 부족합니다.')
                        # pause
                elif use=='2':
                    continue
                else:
                    print('잘못 입력하셨습니다.')
                    print('다시 입력해주세요.')
                # time stop

            # 도망치기
            elif do=='3':
                speak01n('후다다다닥...')
                speak01n('무사히 도망쳤다.\n')
                # time stop
                break
            
            
            else:
                print('잘못된 선택입니다.')
                print('다시 선택해주세요.')
            
    #     ch=int(input('무엇을 하시겠습니까?\n1. 사냥하기\n2. 가방열기\n3. 보유 포켓몬 확인\n4. 사냥터 이동\n\n'))
        


    # 가방 열기
    elif ch==2:
        print(f"--------물건 목록--------")
        print(f"포션 : {mainCh.potion}개")
        print("포켓몬 도감 1개")
        print('자전거')
        print('지도')



    
    # 도감
    elif ch==3:
        while True:
            a=input('알고 싶은 포켓몬 이름을 입력하세요 : \n')
            try:
                print()
                print()
                print('------------------------')
                print('------포켓몬 정보-------')
                print(f"이름 : {a}")
                prt(all[a])
                break
            except:
                print('도감에 없는 포켓몬입니다.')
                print()
                break

    
    # 사냥터 이동
    elif ch==4:
        a=input('어느 사냥터로 이동하시겠습니까?\n1. 초보\n2. 초급자\n3. 중급자\n4. 고수')
        if a=='1':
            print("초보 지역으로 이동합니다.")
            hunt='초보'
        if a=='2':
            print("초급자 지역으로 이동합니다.")
            hunt='초급자'
        if a=='3':
            print("중급자 지역으로 이동합니다.")
            hunt='중급자'
        if a=='4':
            print("고수 지역으로 이동합니다.")
            hunt='고수'
    # 상점
    elif ch==5:
        while True:
            print(f"현재 갖고 있는 금액 : {mainCh.money}")
            print('무엇을 구매하시겠습니까?')
            print('-------물품 목록--------')
            print('1. 상처약 : 200원')
            print('2. 나가기')
            a=input('')
            if a=='1':
                if mainCh.money>=200:
                    mainCh.money-=200
                    mainCh.potion+=1
                    print(f"상처약을 구매하였습니다.")
                else:
                    print('돈이 부족합니다.')
            elif a=='2':
                break
            else:
                print('잘못 입력하셨습니다.')

    elif ch==6:
        print('포켓몬 센터에 포켓몬을 맡겼다.')
        print(f"{mainCh.name}(의) 체력이 모두 회복되었다.")
        mainCh.fit=mainCh.fitsave
    else:
        print('잘못 입력하셨습니다. 다시 입력해주세요.')
        




