# n = int(input("enter the nmber you want to ffactories"))
# dot = 1
# for i in range (1,n+1):
#
#     dot = dot *i
#     print(dot)
# not using for loopp we find the factrial

def fact(n):

     if (n==0):
         return 1

     return n*fact(n-1)






result= fact(5)
print(result)