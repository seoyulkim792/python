a, b= map (int, input().split())
c= int(input())

if b + c < 60 :
    H = a
    M = b + c
     
elif b + c == 60:
    H = a +1
    M = 0
    
elif b + c > 60 :
    H = a + (b + c)// 60
    M = (b + c) % 60

if H >= 24:
    H = H % 24

print(H, M)
