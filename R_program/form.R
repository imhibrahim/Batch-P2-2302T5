install.packages("shiny")
library(shiny)

ui<-fluidPage(
  
  textInput("username","Please Enter Yor Name"),
  textInput("usermail","Please Enter Yor Gmail"),
  textInput("usersalary","Please Enter Yor Salary"),
  textInput("userdepart","Please Enter Yor depart"),
  actionButton('btn',"Show Data"),
  verbatimTextOutput("result")
)


server<-function(input,output){
  observeEvent(
    input$btn,{
      
      
      output$result<-renderText({
        paste(
          "User Name Is :",input$username,
          "\n User Mail Is :",input$usermail,
          "\n User Salary Is :",input$usersalary,
          "\n User Depart Is :",input$userdepart
              )
      })
    }
  )
}

shinyApp(ui=ui,server=server)