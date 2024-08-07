# Task 1 : 
# salary = int(input("Enter Salary:"))
# if  salary < 1000:
# 	print("You are poor")
# elif salary >=1000 and salary<20000:
# 	print("Good salary")
# elif salary >= 20000:
# 	print("You are rich")
#
#Task 2 :
# age=int(input("Enter Age:"))
# if age>= 18 : 
#     print("You can drive")
# else:
# 	print("You are not allowed to drive")
#
#Task 3  :
# x,y,z=map(float,input("Enter 3 numbers :").split())
# ans =x 
# if ans >y : 
# 	ans= y
# 	print(f"Number 2:{ans} is the smallest")
# elif ans>z : 
#     print(f"Number 3: {ans} is the smallest")
# else:
#     print(f"Number 1: {ans} is the smallest")
#
#Task4 :
# x,y=map(float,input("Enter 2 numbers :").split())
# if y!=0 : 
#     print(x/y)
# else: 
#     print("Can not divide as result = infinity")
#
#Task 5 :
# for i in range(0,13,3):
#     print(i,end=" ")
#
#Task 6 : 
# for i,j in enumerate(range(0,13,3)):
# 	print(i,j)
#
#Task 7 : 
# lst = [1, 2, 3, 4, 5, 6, 7]
# result=[i*i for i in lst ] 
# print(result)
#
# #Task 8 : 
# lst1= ["Mohamed", 3 ,"ITI"]
# lst2= ["Ibrahim", 4 , "Mansoura"]
# conc= lst1 + lst2
# print(conc)
#Task 8 (Another method): 
# lst1= ["Mohamed", 3 ,"ITI"]
# lst2= ["Ibrahim", 4 , "Mansoura"]
# conc = [*lst1,*lst2]
# print(conc)
#
# #Task 9 : 
# tuple=("bounce")
# print(tuple[::-1])
#
#Task 10 : 
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dic= dict(zip(keys,values))
# print(dic)