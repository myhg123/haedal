class starcraft:
    starcraft_count = 0

    def __init__(self, 종족, 유닛, 체력, 스킬):
        self.종족 = 종족
        self.유닛 = 유닛
        self.체력 = 체력
        self.스킬 = 스킬
        starcraft.starcraft_count += 1

    def info(self):
        print(f'종족 : {self.종족}')
        print(f'유닛 : {self.유닛}')
        print(f'체력 : {self.체력}')
        print(f'스킬 : {self.스킬}')
        print()

    def order(self, skill_num):
        print(self.스킬[skill_num])


unit1 = starcraft('테란', 'scv', 50, ['커맨드센터', '배럭스', '팩토리'])
unit2 = starcraft('프로토스', '프로브', 40, ['넥서스', '게이트웨이', '로보틱스'])
unit3 = starcraft('저그', '드론', 40, ['해처리', '스포닝풀', '성큰'])

unit1.info()
unit2.info()
unit3.info()

unit1.order(0)
unit2.order(1)
unit3.order(2)
