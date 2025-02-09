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

# 🎯 1715. 카드 정렬하기
## 💡 어려웠던 점
문제 이해를 전반적으로 잘 못하는 것 같다... 비교하는 것 자체를 비용이라고 생각하고 비교할 때마다 비교한 횟수끼리 더해줘야 하는 문제이다.  
이런 문제 유형이 처음이라 헷갈렸지만 지피티의 도움을 받아 힙이라는 것을 사용해 볼 것을 고려할 수 있었다.
## 💡 배운 점
1. 힙이란?
  - 완전 이진 트리 기반의 자료구조
  - 부모 노드의 값이 항상 자식 노드들의 값보다 크거나(Max Heap) 작아야(Min Heap) 한다.
  - 즉, 최대 힙에서는 최댓값이 최상위 루트이고 최소 힙에서는 최솟값이 최상위 루트이다.
  - 최댓값과 최솟값을 빠르게 찾을 수 있는 점이 장점이다. (시간복잡도 : O(NlogN))
2. heapq
  - Python의 모듈로, 이진 힙을 활용한 우선순위 큐 구현을 제공한다. 
  - 최소 힙만 제공하므로 최대 힙을 만들려면 값을 -num으로 변환하여 저장하고 사용할 때 다시 -를 붙여야 한다.
```python
# 최대 힙 사용 예제

import heapq

heap = []
heapq.heappush(heap, -5)
heapq.heappush(heap, -2)
heapq.heappush(heap, -9)
heapq.heappush(heap, -1)
heapq.heappush(heap, -3)

print(-heapq.heappop(heap))  # 9
print(-heapq.heappop(heap))  # 5
print(-heapq.heappop(heap))  # 3
print(-heapq.heappop(heap))  # 2
print(-heapq.heappop(heap))  # 1

# n개의 가장 작은/큰 값 찾기
import heapq

arr = [5, 2, 9, 1, 3, 6]

print(heapq.nsmallest(3, arr))  # [1, 2, 3]
print(heapq.nlargest(3, arr))  # [9, 6, 5]

```