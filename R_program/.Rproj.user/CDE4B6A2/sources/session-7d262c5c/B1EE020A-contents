#ui page create
install.packages('shiny')
#multiple packe like ggplot 
install.packages('tidyverse')
#create dashboard theme
install.packages('shinydashboard')
#Data Table
install.packages('DT')
#data Compine  
install.packages('Plotly')
#connection sql
install.packages('DBI')
#sql queries runs
install.packages('RMysql')
#data filter
install.packages('plotrix')
library(shiny)
library(tidyverse)
library(shinydashboard)
library(DT)
library(DBI)
library(plotly)
library(RMySQL)
library(plotrix)
#Database Connect

conn<-dbConnect(
  MySQL(),
  user='root',
  password='',
  dbname='company',
  host='localhost'
)
query<-'select * from employee'
employee<-dbGetQuery(conn,query)
View(employee)

#Dashboard UI
ui<-dashboardPage(
  dashboardHeader(title = "Employee Dashboard"),
  dashboardSidebar(
    sidebarMenu(
      menuItem("Dashboard",icon = icon("dashboard"),tabName = 'dashbaord'),
      menuItem("All Employess",icon=icon('users'),tabName = 'employeies'),
      menuItem("Salaries",icon=icon('coins'),tabName = 'salary')
    )
  ),
  dashboardBody(
    tabItems(
      #dashboard tabs
      tabItem(
        tabName = 'dashbaord',
        fluidRow(
          valueBoxOutput("totel_employee"),
          valueBoxOutput("Totel_department"),
          valueBoxOutput("avg_salary")
        ),
        fluidRow(
          box(plotOutput("salary"),width = 6),
          box(plotOutput("department"),width = 6)
        
      )
      
    ),
    
    #employee table tab
    tabItem(
      tabName = 'employeies',
      DTOutput("emp_table")
    ),
    #employee salary tab
    tabItem(
      tabName = 'salary',
      DTOutput("emp_salary")
  )
  )
)
)

server<-function(input,output){
  
  output$totel_employee<-renderValueBox({
    valueBox(
      value = nrow(employee),
      subtitle = "Totel Employeies",
      icon = icon('users'),
      color = 'green'
    )
  })
  
  
  output$Totel_department<-renderValueBox({
    valueBox(
      value =length(unique(employee$depart)),
      subtitle = "Totel Deparments",
      icon = icon('building'),
      color = 'yellow'
    )
  })
  
  
  output$avg_salary<-renderValueBox({
    valueBox(
      value =round(mean(employee$salary)),
      subtitle = "Average Salary",
      icon = icon('coins'),
      color = 'blue'
    )
  })
  
  output$salary<-renderPlot({
    barplot(
      employee$salary,
      names.arg = employee$name,
      main = "Employee Salary Chart",
      col = "steelblue"
    )
  })
  
  
  output$department<-renderPlot({
  depart<-table(employee$depart)
  pie(depart,main = "All Departments")
  })
  
  output$emp_table<-renderDT({
    datatable(employee)
  })
  
  output$emp_salary<-renderDT({
    datatable(employee[,c('name','salary')])
  })
  
}

shinyApp(ui,server)















