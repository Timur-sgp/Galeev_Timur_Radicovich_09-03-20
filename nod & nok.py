a = int(input())
b = int(input())
m = a * b

while (a != 0) and (b != 0):
      if a > b:
         a = a % b
      else:
         b = b % a

print( "nod =" , a + b )
print( "nok =" , m / ( a + b ))
