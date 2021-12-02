######################################### 1.7 ####################################################


#a = int(input()) 
#print(a//1000)


#a = int(input())
#b = int(input())
#print(b//a)


#a = int(input())
#b = int(input())
#print(a//b)


#a = int(input())
#print(a%10)


#b = int(input())
#b %= 1000
#b //= 100
#print(b)


#a = int(input())
#print(((a % 100) // 10) + (a % 10) + (a // 100))


#a = int(input())
#b = a // 100
#c = a % 100
#b1 = c // 20
#c1 = c % 20
#b2 = c1 // 10
#c2 = c1 % 10
#b3 = c2 // 5
#c3 = c2 % 5
#b4 = c3 // 1
#c4 = c3 % 1
#print(b + b1 + b2 + b3 + b4)


#n = int(input())
#print((n % 1440) // 60, n % 60)


#n = int(input())
#print((n % 2) + ((n + 1) % 2) * 2 + n)


#n = int(input())
#h = (n % 86400) // 3600
#mx = n - h * 3600 
#m = mx // 60
#s = mx % 60
#md = str(m // 10) + str(m % 10)
#sd = str(s // 10) + str(s % 10)
#print(h, md, sd, sep = ':')


################################### 1.8 ####################################################


#n = int(input())
#print( n > 0)


#n = int(input())
#print((n % 2) == 0)


#print(int(input()) % 6 == 0)


#print(int(input()) % 9 != 0)


#print((int(input()) % 10) == 2)


#n, m = map(int, input().split())
#print(n % 7 == 0 and m % 7 == 0)

#!!!!!!!!!!!!!!!!           print(all([not int(i) % 7  for i in input().split()])) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!


#a, b, c, = map(int, input().split())
#print((a + b + c) // 3 == a)


#print(*[(a + b + c) // 3 == a for a, b, c in [map(int, input().split())]])


#print(int(input()) in range(6,20))


#print(*[n == "awesome" or m == "awesome" for n, m in [map(str, input().split())]])

#print(any(input() == 'awesome' for _ in '__'))


