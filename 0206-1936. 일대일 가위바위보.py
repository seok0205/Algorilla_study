#SWEA D1 0206-1936.일대일 가위바위보
#일대일 가위바위보
#가위 1, 바위 2, 보 3
#비기는 경우는 없다.

#A가 이기면 A, B가 이기면 B 출력
a = 1 #가위
b = 2 #바위
c = 3 #보


A = int(input('A의 선택(가위=1, 바위=2, 보=3) : ')) 
B = int(input('B의 선택(가위=1, 바위=2, 보=3) : '))


#A가 이기면 A출력
if (A == 1 and B==3) or (A==2 and B==1) or (A==3 and B==2): #A가위 B보, A바위 B가위, A보 B바위위
    print('A')


#B가 이기면 B 출력
elif (A == 3 and B==1) or (A==1 and B==2) or (A==2 and B==3):
    print('B')


