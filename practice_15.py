#클래스 : 언제 사용하는지 아는게 중요
#객체지향 : 물체에 관련된 속성 넣어주고 컨트롤하는 함수 넣어준뒤 가운데에서는 함수만 불러다가 물체 제어 (몬스터1마리가 1개의 체력데이터를 갖고 조정가능)
class Monster():
    hp = 100 #hp 갖고있음
    alive = True #처음엔 무조건 살아야함
    
    def damage(self, attack): #데미지라는 함수 가지고 있어서 외부에서 부를 수 있음
        self.hp = self.hp-attack #hp가 attrack만큼 줄어들거야
        if self.hp<0:
            self.alive = False
        
    def status_check(self): #죽었는지 살았는지 알려주는 함수
        if self.alive: #true이면
            print('살았다')
        else:
            print('죽었다')
            
            
m1 = Monster()#인스턴스(몬스터)
m1.damage(150)#데미지 입힘
m1.status_check()#상태체크

m2 = Monster()
m2.damage(90)
m2.status_check()
