'''1 1 1 1 1 
   1 1 1 1
   1 1 1
   1 1
   1'''
row = int(input())
while row >= 1:
    col =1
    while col <=row:
       print(1, end=' ')
       col += 1
    print()
    row -=1

