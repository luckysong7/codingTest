# 문제
# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
#
# 1+1+1+1
# 1+1+2
# 1+2+1
# 1+3
# 2+1+1
# 2+2
# 3+1
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.
#
# 출력
# 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.

# dp[n] = dp[n-1] + dp[n-2] + dp[n-3] ( n >= 4)

t = int(input())

for _ in range(t):
    n = int(input())
    dp = [0] * 11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])



"""
1 - 4 
2 - 2
3 - 1

1 : 1

2 : 2
  1 + 1
  2
  
3 : 4
  1 + 1 + 1 
  1 + 2
  2 + 1 
  3
   
4 : 7
  1 + (3) => 1 * 4 = 4
  2 + (2) => 1 * 2 = 2
  3 + (1) => 1 * 1 = 1

5: 13
  1 + 1 + 1 + 1 + 1
  1 + 1 + 1 + 2
  1 + 1 + 2 + 1
  1 + 2 + 1 + 1
  1 + 2 + 2
  1 + 1 + 3
  1 + 3 + 1
  
  2 + 1 + 1 + 1
  2 + 1 + 2 
  2 + 2 + 1
  2 + 3
  
  3 + 1 + 1
  3 + 2
  
  1 + (4) => 1 * 7
  2 + (3) => 1 * 4 
  3 + (2) => 1 * 2 

6 : 13 + 7 + 4 = 24
    
7 : 44 = 24 + 13 + 7 = 37 + 7 = 44 
  1 + (6) => 
  2 + (5) => 
  3 + (4) =>
  
dp[n] = dp[n-1] + dp[n-2] + dp[n-3]

"""

