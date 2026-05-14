#variable----
var1<-50
var2<-10
sum<-var1+var2
print(sum)





#Data types----
#numeric
#integer
#complex
#charecter
#bool
# numeric : 50 , 50.67,
# integer : 50L ,
#complex : 45+34i

num1<-56L
typeof(num1)
class(num1)

print(num1)


text<-"ibrahim"
typeof(text)
print(text)


num<- 56i
class(num)

data<-FALSE
class(data)




num1<-c(3,5,8,0)
num2<-c(3,5,8,6)
print(num1+num2)




#Operaters in R----
a<-5
b<-10
c<-a%%b
print(c)

#relational opr----
#<, > <= , >= !=
a<-6
b<-40
print(a!=5)

#logical opr----
mail<-"ibrahim@gmail.com"
password<-"admin123"
data<-FALSE
print(!data)


#assigment opr----
a<-5
10->t
c=5
3=o
print(t)
r<-5
w<-10
t<-7
r<-t<-w
print(r)












#sequence opr----
num1<-1:30000
max.print(num1)





#control stetment----

#if else switch loops
num<-78
if(num>=90 && num<=100){
  print("A+")
}else if(num>=75){
  print("A")
}else{
  print("Fail")
}

num1<-0
ans<-switch(num1,
"Ibrahim",
"Khizer",
"Muskan",
"Arfa",
"Anus"
)
print(ans)


vector<-c(3,5,7,1,2)
for(i in vector){
  print(i)
}

#for loop----
for(o in 1:8){
  print(o)
}










# while loop----
s<-1
while(s<=10){
  print(s)
  s<-s+1
}










#repeat loop----
n<-1
repeat{
  print(n)
  n<-n+1
  if(n>9){
    break
  }
}

















#function ----
myfun<-function(name){
  print(paste("Welcome : ",name))
}

myfun("Ali")

myfun("usman")
myfun("fiza")



sum<-function(num1,num2){
  
  print(paste0("Your Sum is :",num1+num2))
  
}

sum(5,7)
sum(6,6)



newfun<-function(a=10,b=10){
  print(a+b)
}


newfun(12,6)


a<-10
b<-15


print(b)










#get user input----
name<-readline(prompt = "Enter your name : ")

print(paste("Welcome " ,name," to our Site"))









mysum<-function(num1,num2){
  print(paste("Your Sum ans is : ",num1+num2 ))
}

udata1<-readline(prompt = "enter Number one : ")
udata2<-readline(prompt = "enter Number two : ")
udata1<-as.numeric(udata1)
udata2<-as.numeric(udata2)
mysum(udata1,udata2)



















#paste vs paste0-----
a<-"Muhmmad"
b<-"Ibrahim"

c<-paste0(a,b)

print(paste(c,"afzal","Ahmed"))



















