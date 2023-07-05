#calculate the sum of all numbers from 1 to a given number

#n=int(input("enter the number:")) #5
#for i in range(1,n+1):
 #   print(i)


#n=7
#sum=0
#for i in range(1,n+1):
 #   sum+=1
 #  print(sum)   


#2.write a program to print multiplication table of a given number


#n=int(input("enter the number:"))
#for i in range(1,11):
 #   print(n,"x",i,"=",n*i)

#3.display numbers from a list using loop

#a=[1,2,3,4,5]
#for i in range(len(a)):
 #   print(i)


#4.reverse string

#s="maheshbabu"
#s1=''
#for i in s:
 #   s1=i+s1
#print("the reverse string is:",s1)   


#5.count the total number of digits

#l=[1,2,3,4,5,6,7,8,9,]
#count=0
#for x in l:
 #  count+=1
  # print(x)
#print("the total number of digits",count)

#6.display numbers -10 to -1 using for loop

#for i in range(-10,-0):
 #   for j in range(-10,-0):
  #      print(j)
#print()   

#7.all prime numbers

#n=100

#for i in range(2,101):
 #   for j in range(2,i):
  #      if (i%j==0):
   #         break
    #else:
     #   print(i)    



#fibonacci series upto 10 terms


n=10

n1=0
n2=1
count=0
while(count<n):
    print(n1)
    n3=n1+n2
    n1=n2
    n2=n3
    count=count+1
