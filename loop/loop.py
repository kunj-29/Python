# 1)

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

# size = 6
# for i in range(1, size):
#         for j in range(1 , i+1):
#             print(j , end=" ")
#         print()

# 2)

# 5 
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

# for i in range(size-1, 0, -1):
#         for j in range(size-1, i-1, -1):
#             print(j , end=" ")
#         print()

# 3)

# 1 
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

# for i in range(1, size):
#         for j in range(i, 0, -1):
#             print(j, end=" ")
#         print()

# 4)

# 5 
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5

# for i in range(size-1, 0, -1):
#         for j in range(i, size):
#             print(j, end=" ")
#         print()

# 5)

# a 
# a b
# a b c
# a b c d
# a b c d e

# s = "abcdef"
# size = len(s)
# for i in range(97, 102):
#         for j in range(97, i+1):
#             print(chr(j),end=" ")
#         print()

# 6)

# A 
# A B
# A B C
# A B C D
# A B C D E

# s = "ABCDE"
# size = len(s)
# for i in range(size):
#         for j in range(i+1):
#             print(s[j], end=" ")
#         print()

# 7)

# a 
# b a
# c b a
# d c b a
# e d c b a

# s="abcde"
# size = len(s) + 1
# for i in range(1, size):
#         for j in range(i, 0, -1):
#             print(s[j-1], end=" ")
#         print() 

# 8)

# A 
# B A
# C B A
# D C B A
# E D C B A

# s="ABCDE"
# size = len(s) + 1
# for i in range(1, size):
#         for j in range(i, 0, -1):
#             print(s[j-1], end=" ")
#         print()   

# 9)

# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# size = 5
# for i in range(1,size+1):
#         for j in range(i, 0, -1):
#             print(i, end=" ")
#         print()

# 10)

# 5 
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1

# size = 5
# for i in range(size, 0, -1):
#         for j in range(i, size+1):
#             print(i, end=" ")
#         print()

# 11)
 
# a 
# b b
# c c c
# d d d d
# e e e e e

# s = "abcde"
# size = len(s)
# for i in range(1, size+1):
#         for j in range(i, 0, -1):
#             print(s[i-1], end=" ")
#         print()

# 12)

# E 
# D D
# C C C
# B B B B
# A A A A A

# s = "ABCDE"
# size = len(s)
# for i in range(size, 0, -1):
#         for j in range(i, size+1):
#             print(s[i-1], end=" ")
#         print()
        
# 15)

# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# size = 5
# c = 1
# for i in range(1, size+1):
#         for j in range(1, i+1):
#             print(c, end=" ")
#             c+=1
#         print()

# 16)

# 1 
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

# size = 5
# for i in range(size, 0, -1):
#         for j in range(i, size+1):
#             print(j%2, end=" ")
#         print()



# 17)

# 0 
# 1 0
# 0 1 0
# 1 0 1 0
# 0 1 0 1 0

# size = 5
# for i in range(size, 0, -1):
#         for j in range(i, size+1):
#             if j%2==0:
#                 print(1,end=" ")
#             else:
#                print(0, end=" ")
#         print()


# 18)

# 1 
# 0 0
# 1 1 1
# 0 0 0 0
# 1 1 1 1 1

# size = 5
# for i in range(1, size+1):
#         for j in range(i, 0, -1):
#             print(i%2, end=" ")
#         print()

# 19)

# 0
# 1 1
# 0 0 0
# 1 1 1 1
# 0 0 0 0 0

# size = 5
# for i in range(1, size+1):
#         for j in range(i, 0, -1):
#             if i%2==0:
#                 print(1, end=" ")
#             else:
#                 print(0, end=" ")
#         print()

# 20)

# 5 
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1

# size = 5
# for i in range(size , 0, -1):
#         for j in range(i, size+1):
#             print(i, end=" ")
#         print()

# 21)

# 1 
# 1 2
# 2 3 4
# 4 5 6 7
# 7 8 9 10 11
# size = 5
# c=1
# for i in range(1, size+1):
#         for j in range(1, i+1):
#             print(c , end=" ")
#             c = c + 1
#         c = c - 1
#         print()

# 22)

# 1 2 3 4 5 
# 1 2 3 4
# 1 2 3
# 1 2
# 1
size = 5
# for i in range(size, 0, -1):
#         for j in range(1, i+1):
#             print(j, end=" ")
#         print()
    
# 23)

# 5 4 3 2 1 
# 5 4 3 2
# 5 4 3
# 5 4
# 5
# for i in range(1, size+1):
#         for j in range(size, i-1, -1):
#             print(j, end=" ")
#         print()

# 24)

# 1 2 3 4 5 
# 2 3 4 5
# 3 4 5
# 4 5
# 5
# size = 5
# for i in range(1, size+1):
#         for j in range(i, size+1):
#             print(j, end=" ")
#         print()

# 25)

# 5 4 3 2 1 
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# size = 5
# for i in range(size, 0, -1):
#         for j in range(i, 0, -1):
#             print(j, end=" ")
#         print()

# 26)

# 1 0 1 0 1 
# 0 1 0 1
# 1 0 1
# 0 1
# 1
# size = 5
# for i in range(1, size+1):
#         for j in range(i, size+1):
#             print(j%2, end=" ")
#         print()

# 27)

# 1 1 1 1 1 
# 2 2 2 2
# 3 3 3
# 4 4
# 5
# size = 5
# for i in range(1, size+1):
#         for j in range(i, size+1):
#             print(i, end=" ")
#         print()


# 28)

# a b c d e 
# a b c d
# a b c
# a b
# a


# for i in range(101, 96, -1):
#         for j in range(97, i+1):
#             print(chr(j), end=" ")
#         print()

#     print()

# 29)

# a b c d e 
# b c d e
# c d e
# d e
# e
# s = "abcde"
# size = len(s)
# for i in range(1,size+1):
#         for j in range(i, size+1):
#             print(s[j-1], end=" ")
#         print()

# 30)

# A B C D E 
# A B C D
# A B C
# A B
# A
# s = "ABCDE"
# size = len(s)
# for i in range(size, 0, -1):
#         for j in range(1, i+1):
#             print(s[j-1], end=" ")
#         print()

# 31)

# A B C D E 
# B C D E
# C D E
# D E
# E
# s = "ABCDE"
# size = len(s)
# for i in range(1, size+1):
#         for j in range(i, size+1):
#             print(s[j-1], end=" ")
#         print()

# 32)

# a a a a a 
# b b b b
# c c c
# d d
# e
# s = "abcde"
# size = len(s)
# for i in range(1,size+1):
#         for j in range(i, size+1):
#             print(s[i-1], end=" ")
#         print()
    
# 33)

# e e e e e 
# d d d d
# c c c
# b b
# a
# s = "abcde"
# size = len(s)
# for i in range(size, 0, -1):
#         for j in range(1, i+1):
#             print(s[i-1], end=" ")
#         print()

# 33 )

# A A A A A 
# B B B B
# C C C
# D D
# E
# s = "ABCDE"
# size = len(s)
# for i in range(1, size+1):
#         for j in range(i, size+1):
#             print(s[i-1], end=" ")
#         print()

# 34)

# E E E E E 
# D D D D
# C C C
# B B
# A
# s = "ABCDE"
# size = len(s)
# for i in range(size, 0, -1):
#         for j in range(1, i+1):
#             print(s[i-1], end=" ")
#         print()

# 35)

# 1 0 1 0 1 
# 0 1 0 1
# 1 0 1
# 0 1
# 1
# size = 5
# for i in range(1, size+1):
#         for j in range(i, size+1):
#             print(j%2, end=" ")
#         print()


# 36)

# 1 1 1 1 1 
# 0 0 0 0
# 1 1 1
# 0 0
# 1
# size = 5
# for i in range(1, size+1):
#         for j in range(i, size+1):
#             print(i%2, end=" ")
#         print()


# 37)

# 0 0 0 0 0 
# 1 1 1 1
# 0 0 0
# 1 1
# 0
# size = 5
# for i in range(1, size+1):
#         for j in range(i, size+1):
#             if(i%2==0):
#                 print(1,end=" ")
#             else:
#                 print(0,end=" ")
#         print()

#      38 )

# 0 1 0 1 0 
# 1 0 1 0
# 0 1 0
# 1 0
# 0
# size = 5
# for i in range(size, 0, -1):
#             for j in range(i, 0, -1):
#                 if(j%2==0):
#                     print(1, end=" ")
#                 else:
#                      print(0, end=" ")
#             print()

# 39)

# 5 5 5 5 5 
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# size = 5
# for i in range(size, 0, -1):
#         for j in range(1, i+1):
#             print(i, end=" ")
#         print()

#      40 )

# 5 4 3 2 1 
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# size = 5
# for i in range(size, 0, -1):
#         for j in range(i, 0, -1):
#             print(j, end=" ")
#         print()

#  41)

#         1 
#       2 1
#     3 2 1
#   4 3 2 1
# 5 4 3 2 1
# size = 5
# for i in range(1, size+1):
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(i, 0, -1):
#             print(j, end=" ")
#         print()


# 42)

#         1 
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5
# size = 5
# for i in range(1, size+1):
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(1, i+1):
#             print(j, end=" ")
#         print()

# 43)

#         5 
#       4 5
#     3 4 5
#   2 3 4 5
# 1 2 3 4 5
# size = 5
# for i in range(size, 0, -1):
#         for j in range(1, i):
#             print(end="  ")
#         for j in range(i, size+1):
#             print(j, end=" ")
#         print()

# 44)

#         1 
#       2 1
#     3 2 1
#   4 3 2 1
# 5 4 3 2 1
# size = 5
# for i in range(1, size+1):
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(i, 0, -1):
#             print(j, end=" ")
#         print()


# 45)

#         5 
#       4 5
#     3 4 5
#   2 3 4 5
# 1 2 3 4 5 
# size = 5
# for i in range(size, 0, -1):
#         for j in range(1, i):
#             print(end="  ")
#         for j in range(i, size+1):
#             print(j, end=" ")
#         print()



# 46)

#         1 
#       1 0
#     1 0 1
#   1 0 1 0
# 1 0 1 0 1
# size = 5
# for i in range(1, size+1):
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(1, i+1):
#             print(j%2, end=" ")
#         print()


# 47)

#         0 
#       0 1
#     0 1 0
#   0 1 0 1
# 0 1 0 1 0
# size = 5
# for i in range(1, size+1):
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(1, i+1):
#             if(j%2==0):
#                 print(1, end=" ")
#             else:
#                 print(0, end=" ")
#         print()

# 48 )

#         A 
#       A B
#     A B C
#   A B C D
# A B C D E
# size = 69
# for i in range(65, size+1):
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(65, i+1):
#             print(chr(j), end=" ")
#         print()


# 49 )

#         a 
#       a b
#     a b c
#   a b c d
# a b c d e
# s = "abcde"
# size = len(s)
# for i in range(1, size+1):
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(1, i+1):
#             print(s[j-1], end=" ")
#         print()

# 50 )
#         A 
#       B B
#     C C C
#   D D D D
# E E E E E
# s = "ABCDE"
# size = len(s)
# for i in range(1, size+1):
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(1, i+1):
#             print(s[i-1], end=" ")
#         print()


# 51 )

#         e 
#       d d 
#     c c c 
#   b b b b 
# a a a a a 
# s = "abcde"
# size = len(s)
# for i in range(size, 0, -1):
#         for j in range(1, i):
#             print(end="  ")
#         for j in range(i, size+1):
#             print(s[i-1], end=" ")
#         print()

# 52 )

#         E 
#       D D 
#     C C C 
#   B B B B
# A A A A A
# s = "ABCDE"
# size = len(s)
# for i in range(size, 0, -1):
#         for j in range(1, i):
#             print(end="  ")
#         for j in range(i, size+1):
#             print(s[i-1], end=" ")
#         print()

#  54)

# 1 2 3 4 5 
#   1 2 3 4
#     1 2 3
#       1 2
#         1
# size = 5
# for i in range(size, 0, -1):
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(1, i+1):
#             print(j, end=" ")
#         print()


# 55 )

# 5 4 3 2 1 
#   4 3 2 1
#     3 2 1
#       2 1
#         1
# size = 5
# for i in range(size, 0, -1):
#         for j in range(i, size):
#             print(end="  ")

#         for j in range(i, 0, -1):
#             print(j, end=" ")    
#         print()


# 56 )

# 1 2 3 4 5 
#   2 3 4 5
#     3 4 5
#       4 5
#         5
# size = 5
# for i in range(1, size+1):
#         for j in range(1, i):
#             print(end="  ")
#         for j in range(i, size+1):
#             print(j, end=" ")
#         print()


# 57 )

# 5 4 3 2 1 
#   4 3 2 1
#     3 2 1
#       2 1
#         1
# size = 5
# for i in range(size, 0, -1):
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(i, 0, -1):
#             print(j, end=" ")
#         print()



# 58 )

# 5 5 5 5 5 
#   4 4 4 4
#     3 3 3
#       2 2
#         1
# size = 5
# for i in range(size, 0, -1):
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(1, i+1):
#             print(i, end=" ")
#         print()


# 59 )

# 1 1 1 1 1 
#   2 2 2 2
#     3 3 3
#       4 4
#         5
# size = 5
# for i in range(1, size+1):
#         for j in range(1, i):
#             print(end="  ")
        
#         for j in range(i, size+1):
#             print(i, end=" ")
#         print()


# 60 )

# 1 0 1 0 1 
#   0 1 0 1
#     1 0 1
#       0 1
#         1
# size = 5
# for i in range(1, size+1):
#         for j in range(1, i):
#             print(end="  ")
#         for j in range(i, size+1):
#             print(j%2, end=" ")
#         print()


# 61 )

# 0 0 0 0 0 
#   1 1 1 1
#     0 0 0
#       1 1
#         0
# size = 5
# for i in range(1, size+1):
#         for j in range(1, i):
#             print(end="  ")
#         for j in range(i, size+1):
#             if(i%2==0):
#                 print(1, end=" ")
#             else:
#                 print(0, end=" ")
#         print()



# 62 )

# a b c d e 
#   a b c d
#     a b c
#       a b
#         a
# s = "abcde"
# size = len(s)
# for i in range(size, 0, -1):
#         for j in range(i, size):
#             print(end="  ")
#         for  j in range(1, i+1):
#             print(s[j-1], end=" ")
#         print()


#63 )

# A B C D E 
#   A B C D
#     A B C
#       A B
#         A
# s = "ABCDE"
# size = len(s)
# for i in range(size, 0, -1):
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(1, i+1):
#             print(s[j-1], end=" ")
#         print()

# 64 )

# a b c d e 
#   b c d e
#     c d e
#       d e
#         e
# s = "abcde"
# size = len(s)
# for i in range(1, size+1):
#         for j in range(1, i):
#             print(end="  ")
#         for j in range(i, size+1):
#             print(s[j-1], end=" ")
#         print()


# 65 )   

# A B C D E 
#   B C D E
#     C D E
#       D E
#         E               
# s = "ABCDE"
# size = len(s)
# for i in range(1, size+1):
#         for j in range(1, i):
#             print(end="  ")
#         for j in range(i, size+1):
#             print(s[j-1], end=" ")
#         print()



# 66 )

#     1 
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5
# size = 5
# for i in range(1, size+1):
#         for j in range(i+1, size+1):
#             print(end=" ")
#         for j in range(1, i+1):
#             print(j, end=" ")
#         print()


# 67 )

#     a 
#    a b
#   a b c
#  a b c d
# a b c d e
# s = "abcde"
# size = len(s)
# for i in range(1, size+1):
#         for j in range(i+1, size+1):
#             print(end=" ")
#         for j in range(1, i+1):
#             print(s[j-1], end=" ")
#         print()

# 68)

# * 
# * *
# * * *
# * * * *
# * * * * *
# size = 5
# for i in range(1, size+1):
#         for j in range(1, i+1):
#             print("*", end=" ")
#         print()

# 69 )

#     * 
#    * *
#   * * *
#  * * * *
# * * * * *
# size = 5
# for i in range(1, size+1):
#         for j in range(i+1, size+1):
#             print(end=" ")
#         for j in range(1, i+1):
#              print("*", end=" ")
#         print()

# 70 )

#     A 
#    A B
#   A B C
#  A B C D
# A B C D E
# s = "ABCDE"
# size = len(s)
# for i in range(1, size+1):
#         for j in range(i+1, size+1):
#             print(end=" ")
#         for j in range(1, i+1):
#             print(s[j-1], end=" ")
#         print()
    

# 71 )

#     e 
#    e d
#   e d c
#  e d c b
# e d c b a
# s = "abcde"
# size = len(s)
# for i in range(size, 0, -1):
#         for j in range(1+1, i+1):
#             print(end=" ")
#         for j in range(size, i-1, -1):
#             print(s[j-1], end=" ")
#         print()

# 72) 

#         1 
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
# size = 5
# for i in range(1, size+1):
#         for j in range(i+1, size+1):
#             print(end="  ")
#         for j in range(1, i+1-1):
#             print(j, end=" ")
#         for j in range(i, 0, -1):
#             print(j, end=" ")
#         print()

#     73) 

#        1 
#       2 1 2
#     3 2 1 2 3
#   4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5
# size = 5
# for i in range(1, size+1):
#         for j in range(i+1, size+1):
#             print(end="  ")
#         for j in range(i, 0+1, -1):
#             print(j, end=" ")
#         for j in range(1, i+1):
#             print(j, end=" ")
#         print()


#     74) 

#         a 
#       a b a
#     a b c b a
#   a b c d c b a
# a b c d e d c b a
# s = "abcde"
# size = len(s)
# for i in range(1, size+1):
#         for j in range(i+1, size+1):
#             print(end="  ")
#         for j in range(1, i):
#             print(s[j-1], end=" ")
#         for j in range(i, 0, -1):
#             print(s[j-1], end=" ")
#         print()

#     75 )

#                  A 
#                 A B A
#               A B C B A
#             A B C D C B A
#           A B C D E D C B A
# size = 5
# for i in range(65, 65+size):
#         for j in range(i+1, 65+size):
#             print(end="  ")
#         for j in range(65, i+1-1):
#             print(chr(j), end=" ")
#         for j in range(i, 65-1, -1):
#             print(chr(j), end=" ")
#         print()

#     76 )

#         e 
#       e d e
#     e d c d e
#   e d c b c d e
# e d c b a b c d e
# s = "abcde"
# size = len(s)    
# for i in range(size, 0, -1):
#         for j in range(1, i):
#             print(end="  ")
#         for j in range(size, i, -1):
#             print(s[j-1], end=" ")
#         for j in range(i, size+1):
#             print(s[j-1], end=" ")
#         print()
    
#     77 )

#         E 
#       D E D
#     C D E D C
#   B C D E D C B
# A B C D E D C B A
# s = "ABCDE"
# size = len(s)
# for i in range(size, 0, -1):
#         for j in range(1, i):
#             print(end="  ")
#         for j in range(i, size):
#             print(s[j-1], end=" ")
#         for j in range(size, i-1, -1):
#             print(s[j-1], end=" ")
#         print()

#     78 )

#         5 
#       5 4 5
#     5 4 3 4 5
#   5 4 3 2 3 4 5
# 5 4 3 2 1 2 3 4 5
# size = 5
# for i in range(size, 0, -1):
#         for j in range(1, i):
#             print(end="  ")
#         for j in range(size, i, -1):
#             print(j, end=" ")
#         for j in range(i, size+1):
#             print(j, end=" ")
#         print()

#     79 )

# 1 2 3 4 5 4 3 2 1 
#   1 2 3 4 3 2 1
#     1 2 3 2 1
#       1 2 1
#         1
# size = 5
# for i in range(size, 0, -1):
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(1, i):
#             print(j, end=" ")
#         for j in range(i, 0, -1):
#             print(j, end=" ")
#         print()

#     80 )

# 1 2 3 4 5 4 3 2 1 
#   2 3 4 5 4 3 2
#     3 4 5 4 3
#       4 5 4
#         5
# size = 5
# for i in range(1, size+1):
#         for j in range(1, i):
#             print(end="  ")
#         for j in range(i, size):
#             print(j, end=" ")
#         for j in range(size, i-1, -1):
#             print(j, end=" ")
#         print()

#     81 )

# A B C D E D C B A 
#   A B C D C B A
#     A B C B A
#       A B A
#         A
# s = "ABCDE"
# size = len(s)
# for i in range(size, 0, -1):
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(1, i):
#             print(s[j-1], end=" ")
#         for j in range(i, 0, -1):
#             print(s[j-1], end=" ")
#         print()

#     82 )

# a b c d e d c b a 
#   b c d e d c b
#     c d e d c
#       d e d
#         e 
# s = "abcde"
# size = len(s)
# for i in range(1, size+1):
#         for j in range(1, i):
#             print(end="  ")
#         for j in range(i, size):
#             print(s[j-1], end=" ")
#         for j in range(size, i-1, -1):
#             print(s[j-1], end=" ")
#         print()


#     83 )

# A B C D E D C B A 
# A B C D   D C B A
# A B C       C B A
# A B           B A
# A               A
# s = "ABCDE"
# size = len(s)
# for i in range(size, 0, -1):
#         for j in range(1, i+1):
#             if i==size and j==size:
#                 continue
#             print(s[j-1], end=" ")
#         for j in range(i+1, size):
#             print(end="  ")
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(i, 0, -1):
#             print(s[j-1], end=" ")
#         print()

#     84) 

# a b c d e d c b a 
# a b c d   d c b a
# a b c       c b a
# a b           b a
# a               a
# size = 5+96
# for i in range(size, 96, -1):
#         for j in range(97, i+1):
#             if j==size and i==size:
#                 continue
#             print(chr(j), end=" ")
#         for j in range(i+1, size):
#             print(end="  ")
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(i, 96, -1):
#             print(chr(j), end=" ")
#         print()

    

# 85 )

# A               A 
# A B           B A
# A B C       C B A
# A B C D   D C B A
# A B C D E D C B A
# s = "ABCDE"
# size = len(s)
# for i in range(1, size+1):
#         for j in range(1, i+1):
#             if i==size and j==size:
#                 continue
#             print(s[j-1], end=" ")
#         for j in range(i+1, size):
#             print(end="  ")
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(i, 0, -1):
#             print(s[j-1], end=" ")
#         print()



#     86 )

# a               a 
# a b           b a
# a b c       c b a
# a b c d   d c b a
# a b c d e d c b a
# size = 101
# for i in range(97, size+1):
#         for j in range(97, i+1):
#             if(j==size and i==size):
#                 continue
#             print(chr(j), end=" ")
#         for j in range(i+1, size):
#             print(end="  ")
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(i, 96, -1):
#             print(chr(j), end=" ")
#         print()


#     87)

# 1 2 3 4 5 4 3 2 1 
# 1 2 3 4   4 3 2 1
# 1 2 3       3 2 1
# 1 2           2 1
# 1               1
# size = 5
# for i in range(size, 0, -1):
#         for j in range(1, i+1):
#             if(i==size and j==size):
#                 continue
#             print(j, end=" ")
#         for j in range(i+1, size):
#             print(end="  ")
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(i, 0, -1):
#             print(j, end=" ")
#         print()


#     88 )

# 1               1 
# 1 2           2 1
# 1 2 3       3 2 1
# 1 2 3 4   4 3 2 1
# 1 2 3 4 5 4 3 2 1
# size = 5
# for i in range(1, size+1):
#         for j in range(1, i+1):
#             if(i==size and j==size):
#                 continue
#             print(j, end=" ")
#         for j in range(i+1, size):
#             print(end="  ")
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(i, 0, -1):
#             print(j, end=" ")
#         print()


#     89 )

# e d c b a b c d e 
# e d c b   b c d e
# e d c       c d e 
# e d           d e
# e               e
# s = "abcde"
# size = len(s)
# for i in range(1, size+1):
#         for j in range(size, i-1, -1):
#             if(i==1 and j==1):
#                 continue
#             print(s[j-1], end=" ")
#         for j in range(2, i):
#             print(end="  ")
#         for j in range(1, i):
#             print(end="  ")
#         for j in range(i, size+1):
#             print(s[j-1], end=" ")
#         print()


#     90) 

#         1 
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
#   1 2 3 4 3 2 1
#     1 2 3 2 1
#       1 2 1
#         1
# size = 5
# for i in range(1, size+1):
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(1, i):
#             print(j, end=" ")
#         for j in range(i, 0, -1):
#             print(j, end=" ")
#         print()
# size = size-1
# for i in range(size, 0, -1):
#         for j in range(i, size+1):
#             print(end="  ")
#         for j in range(1, i+1):
#             print(j, end=" ")
#         for j in range(i-1, 0, -1):
#             print(j, end=" ")
#         print()


#     91) 

#          1 1 
#       2 1 1 2
#     3 2 1 1 2 3
#   4 3 2 1 1 2 3 4
# 5 4 3 2 1 1 2 3 4 5
#   4 3 2 1 2 3 4
#     3 2 1 2 3
#       2 1 2
#         1
# size = 5
# for i in range(1, size+1):
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(i, 0, -1):
#             print(j, end=" ")
#         for j in range(1, i+1):
#             print(j, end=" ")
#         print()
# size = size - 1
# for i in range(size, 0, -1):
#         for j in range(i, size+1):
#             print(end="  ")
#         for j in range(i, 1, -1):
#             print(j, end=" ")
#         for j in range(1, i+1):
#             print(j, end=" ")
#         print()


#     92 )

#         a 
#       a b a
#     a b c b a
#   a b c d c b a
# a b c d e d c b a
#   a b c d c b a
#     a b c b a
#       a b a
#         a
# s = "abcde"
# size = len(s)
# for i in range(1, size+1):
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(1, i):
#             print(s[j-1], end=" ")
#         for j in range(i, 0, -1):
#             print(s[j-1], end=" ")
#         print()
    
# size = size - 1
# for i in range(size, 0, -1):
#         for j in range(i, size+1):
#             print(end="  ")
#         for j in range(1, i):
#             print(s[j-1], end=" ")
#         for j in range(i, 0, -1):
#             print(s[j-1], end=" ")
#         print()



#     93 

#         A 
#       A B A
#     A B C B A
#   A B C D C B A
# A B C D E D C B A
#   A B C D C B A
#     A B C B A
#       A B A
#         A
# size = 69
# for i in range(65, size+1):
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(65, i):
#             print(chr(j), end=" ")
#         for j in range(i, 64, -1):
#             print(chr(j), end=" ")
#         print()

# size -= 1
# for i in range(size, 64, -1):
#         for j in range(i, size+1):
#             print(end="  ")
#         for j in range(65, i):
#             print(chr(j), end=" ")
#         for j in range(i, 64, -1):
#             print(chr(j), end=" ")
#         print()



#     94 

# 1 2 3 4 5 4 3 2 1 
#   1 2 3 4 3 2 1
#     1 2 3 2 1
#       1 2 1
#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
# size = 5
# for i in range(size, 0, -1):
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(1, i):
#             print(j, end=" ")
#         for j in range(i, 0, -1):
#             print(j, end=" ")
#         print()

# size -= 1
# for i in range(1, size+1):
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(1, i+2):
#             print(j, end=" ")
#         for j in range(i, 0, -1):
#             print(j, end=" ")
#         print()



    # 95 

# A B C D E D C B A 
#   A B C D C B A
#     A B C B A
#       A B A
#         A
#       A B A
#     A B C B A
#   A B C D C B A
# A B C D E D C B A
# s = "ABCDE"
# size = len(s)
# for i in range(size, 0, -1):
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(1, i):
#             print(s[j-1], end=" ")
#         for j in range(i, 0, -1):
#             print(s[j-1], end=" ")
#         print()

# for i in range(1, size):
#         for j in range(i, size-1):
#             print(end="  ")
#         for j in range(1, i+2):
#             print(s[j-1], end=" ")
#         for j in range(i, 0, -1):
#             print(s[j-1], end=" ")
#         print()


#     96 

# a b c d e d c b a 
#   a b c d c b a
#     a b c b a
#       a b a
#         a
#       a b a
#     a b c b a
#   a b c d c b a
# a b c d e d c b a
# s = "abcde"
# size = len(s)
# for i in range(size, 0, -1):
#         for j in range(i, size):
#             print(end="  ")
#         for j in range(1, i):
#             print(s[j-1], end=" ")
#         for j in range(i, 0, -1):
#             print(s[j-1], end=" ")
#         print()

# for i in range(1, size):
#         for j in range(i, size-1):
#             print(end="  ")
#         for j in range(1, i+2):
#             print(s[j-1], end=" ")
#         for j in range(i, 0, -1):
#             print(s[j-1], end=" ")
#         print()



#     97 

# 1 2 3 4 5 4 3 2 1 
# 1 2 3 4 a 4 3 2 1
# 1 2 3 a b a 3 2 1
# 1 2 a b c b a 2 1
# 1 a b c d c b a 1
# 1 2 a b c b a 2 1
# 1 2 3 a b a 3 2 1
# 1 2 3 4 a 4 3 2 1
# 1 2 3 4 5 4 3 2 1
# size = 5
# k = 97
# l = 96
# for i in range(size, 0 , -1):
#         for j in range(1, i+1):
#             if j == size:
#                 continue
#             print(j, end=" ")
#         k = 97
#         for j in range(i+1, size):
#             print(chr(k), end=" ")
#             k+=1
        
#         k = 97
#         for j in range(i, size):
#             if j == i:
#                 l += 1
#                 k = l
#             print(chr(k), end=" ")
#             k -= 1
#         for j in range(i, 0, -1):
#             print(j, end=" ")
#         print()

# size = size -1
# k = 97
# l = 96
# for i in range(1, size+1):
#         for j in range(1, i+2):
#             if j == size+1:
#                 continue
#             print(j, end=" ")
#         for j in range(i+1, size):
#             if j == i+1:
#                 k = 97
#             print(chr(k), end=" ")
#             k += 1
    
#         for j in range(i, size):
#             if j == i:
#                 l = 97
#                 l = l + (size - i - 1)
#             print(chr(l), end=" ")
#             l-=1
#         for j in range(i+1, 0, -1):
#             print(j, end=" ")
#         print()




#     98 

# k u n j n u k 
# k u n 1 n u k
# k u 1 2 1 u k
# k 1 2 3 2 1 k
# k u 1 2 1 u k
# k u n 1 n u k
# k u n j n u k
# s = "kunj"
# size = len(s)
# for i in range(size, 0, -1):
#         for j in range(1, i+1):
#             if j == size and i == size:
#                 continue
#             print(s[j-1], end=" ")
#         k = 1
#         for j in range(i+1, size):
#             print(k, end=" ")
#             k+=1
#         k = size-1
#         for j in range(i, size):
#             print(k+1-i, end=" ")
#             k-=1
#         for j in range(i, 0, -1):
#             print(s[j-1], end=" ")
#         print()

# for i in range(2, size+1):
#         for j in range(1, i+1):
#             print(s[j-1], end=" ")
#         k = 1
#         for j in range(i, size):
#             print(k, end=" ")
#             k+=1
#         k = size-1
#         for j in range(i+1, size):
#             print(k-i,end=" ")
#             k-=1
#         for j in range(i, 0, -1):
#             if(i==size and j==size):
#                 continue
#             print(s[j-1], end=" ")
#         print()


#  99

# 1 
# 1 2
# 3 4 5
# 12 13 14 15
# 54 55 56 57 58
# size = 5
# sum=0
# k=1
# for i in range(1, size+1):
#         for j in range(1, i+1):
#             print(k, end=" ")
#             sum = sum + k
#             k = k + 1
#         k = sum
#         sum = 0
#         print()