#data table----
library(readxl)
library(dplyr)
library(DT)
filepath<-"D:\\empdata.xlsx"
response<-read_excel(filepath)
filterdata=response %>% filter(Shift == 'Night')
datatable(response,
          options = list(
            dom="Bfrtip",
            buttons=c('copy','excel','cvs','pdf','print'),
            pageLength=5
          ),
          extensions = 'Buttons',
          rownames = FALSE
          )




#pie chart create----
library(readxl)
library(plotrix)
library(dplyr)
file_path<-"D:\\empdata.xlsx"
response<-read_excel(file_path)
#data merge (group & number)
empshift<-response %>% 
group_by(depart) %>%
summarise(number=n())
print(empshift)
#create pie chart design
pie3D(
  empshift$number,
  labels = empshift$depart,
  main="This is Our Employee Shift Chart",
  explode = 0.1
)

View(response)


#read My Sql Database
library(RMySQL)
library(DBI)

connection<-dbConnect(
  MySQL(),
  user="root",
  password="",
  dbname="school_managment",
  host="localhost",
)
query<-"select * from teachers"
allemployee<-dbGetQuery(connection,query)
View(allemployee)

query<-"update employee set name='Khizer' where id=2 "
updatedata<-dbExecute(connection,query)

del<-"delete from employee where id=3"
deldata<-dbExecute(connection,del)
View(deldata)


insert<-"insert into employee(name,mail,salary,depart)
values('Farhan','farhan@gmail.com',50000,'Project Managment')"
response<-dbExecute(connection,insert)
head(response)




















#create Graph chart
install.packages("ggplot2")
library(ggplot2)
ggplot(allemployee,aes(x=depart,fill = depart))+
  geom_bar()+
  labs(title = "Count All Employee Depart",
       y="Number of Count All Employees",
       x="All Depart Data Count by Graph"
       )

#data merge (group & number)
empshift<-allemployee %>% 
  group_by(depart) %>%
  summarise(number=n())
print(empshift)
#create pie chart design
pie3D(
  empshift$number,
  labels = empshift$depart,
  main="This is Our Employee Shift Chart",
  explode = 0.1
)





View(allemployee)