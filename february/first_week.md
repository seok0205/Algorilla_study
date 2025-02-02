# 🎯 11718 그대로 출력하기
## 💡 어려웠던 점
### 1. 종료하는 법
stdin.read()와 stdin.readlines() 사용 시 (mac) command + d / (windows) ctrl+z+enter 를 해야 입력 받는 것을 끝내고 출력을 해줌
## 💡 배운 점
### 1. sys
파이썬 인터프리터를 제어하는 데 사용되는 기본 모듈
### 2. stdin : read(), readline(), readlines()
```python
import sys
print("=== read() ===")
print(sys.stdin.read()) # 출력
                        # Hello
                        # Baekjoon
                        # Online Judge
lines = sys.stdin.read()
print(type(lines)) # <class 'str'>

print("=== readline() ===")
print(sys.stdin.readline()) # Hello
line = sys.stdin.readline()
print(type(line)) # <class 'str'>

print("=== readlines() ===")
lines = sys.stdin.readlines() #list로 반환됨
print(lines) # ['Hello\n', 'Baekjoon\n', 'Online Judge']
print(lines.strip()) # AttributeError: 'list' object has no attribute 'strip'
print(line.strip() for line in lines) # <generator object <genexpr> at 0x10b4fd310>
print(list(line.strip() for line in lines)) # ['Hello', 'Baekjoon', 'Online Judge']
```
### 3. 왜 input() 말고 stdin.read...을 쓸까?
속도가 더 빠름. input()은 엔터 키를 누를 때 마다 그 줄의 데이터가 버퍼에 들어가서 디코드 되어 유니코드 문자열로 변환됨.  
stdin.read 메서드들은 한 번에 읽어와 버퍼를 여러 번 사용하지 않기 때문에 빠름.  

🔹 한 줄 입력이 필요할 때 → input() 사용  
🔹 여러 줄 입력을 받을 때 → sys.stdin.read() 사용 (속도 빠름)  
🔹 리스트 형태로 여러 줄을 다루려면 → sys.stdin.readlines() 사용  

---

