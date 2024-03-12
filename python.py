

#a, b=c=7,8
#print(a)
#print(b)
#print(c)
#a=b,c =4,2
#print(a,b,c)
#----> swapping of vsriables
a=7
b=5
temp=a # temp=7
#a=b #a=5
b=temp #b=7
# # a=5,b=7
#print(a,b)
a=a+b #a=12
b=a-b #b=12-7=5
#a=a-b #a=12-5-7

#print(a,b)
a, b=b, a # only in python
#print(a,b)

 #a=a*b #a=35
 #b=a/b  #b=35/7 =5.0
 #a-a/b # a=35/5 =7.0
 #print(int(a),int(b))
a=7
# id()--> used to find the memory address of the variable
#a=7
#b-8
#print(id(a))
#print(id(b))
#-----> keywords
# keywords are reserved words  which provides special meaning  to
# compiler or interpretor
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(type(keyword.kwlist))
# To check if the string is keyword or not
print(keyword.iskeyword("sid"))# flse
#if =8
# print((if) #error coz if is a keyword
#!-----> literals
#literal is the Constant value assigned to a variable
#a variable is consider to be constant when it is difines
#in caps

#a=78 #ais the variable
#A=78 #A is constant

# hash ()--> it creates a hash value for constant ditatyes and
# provides error for non constant datatypes
#n1= 89+7j
#print(hash(n1))
#f1 =[7,8,9]
#print (hash(f1)) # error ---> list is non constant or mutable datatype
#b=90
#print (id(a))
#print (id(b))

  #!-----> operators
# operators are symbles which is used to perfeorm various operions
# between 2 or more operands
# arithmatic
# assignment
#logical
# relational or comparison
# bitwise
# identity
# membership


   # todo ----> arithimatic --> +,-,*,/,%,//,**
    # eg :1
    # a =8
    # b =6
    # c =9
    #print (a+b+c)
    #input()--> used to get the runtime input
    #eval()--> used to get the runtime values of all datatypes
    #n1 - int(input ("Enter the value ;"))
    #print(typ(n1))


    #a=4
    #b=2
    # print(a/b) # is used to get the quotient value
    # print(a%b) # is used to get the remained value
    # ! // --> floor deision
    # a=765433
    # b=19
    #print(a/b)# -> the output wwill be inn integer & the output will be
    # based on floor value
    # #! ** -->sed for power of a number
    # print (2**4) # ----> 16
    # ! assignment ----> +-=, -=, /=, +=, //=, **=, &=,=
    # a=8
    #a+=2
    # print(a)

    # a=30
    # a-=5
    # print(a)


    # ! comparison --> ==, >, <, !=, <=, >=
    # a=8
    # B=7
    #print (a>b) # true


    #a =9
    #b=5
    # print (a==b)



    # ! Bitwise operator --> &,|, ~,<<, >>
    # a=7
    # b=4
    # prin (a&b)                 
# a= ""
#if a;
#print("yes")
#else;
#print("no")
#anumber is even or odd
n = int (input("enter the number: "))
#if n %2 ==0
# print (n, "is even")
#else:
#print (n, "is odd")

 #m =str(input("enter the name:"))
 #n= str (input("enter the nationality:"))
 #if n= "indian":
     #print(n,"eligible")
     #t= int(input("enter the age:")
    #if t=="":
   # print(t, "eligible")
    #else:
        #print(t, "not eligible")

      


  




