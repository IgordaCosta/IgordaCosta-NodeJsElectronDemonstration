













async function GetJobDataJason1(){     // this is a copy from another part of the program

    let process = require("process");
    
    let path = require("path")
  
    const currentWorkingDirectory=process.cwd()
  
  
    const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, './js/AddtoTablePromise'));
    const { gotResults } = require(path.join(currentWorkingDirectory,"./js/gotResults"));
    

    let AwaitProveData = 'Adding image locations to database'
  
    let data = currentWorkingDirectory
  
    let dataName = 'currentWorkingDirectory'
  
    let TableName= ''

    let Database = ''

  
    let Done = await AddtoTablePromise(AwaitProveData,data, dataName, TableName,Database)
  
    // console.log(Done)


    
    

    gotResults()

    // console.log("will start GetJobDataJason function next")


    FindJobExcelLocations()


  
  
  
  }















function FindJobExcelLocations(){
    location.replace("FindJobExcelLocations.html");
    // console.log("here it will go to LSFchooseFolderGetFiles.html from FindJobExcelLocations")
}





function GetJobDataJason(){


    GetJobDataJason1()

    // console.log("got into LoadSingleFileJason")
    
    // var process = require("process");

    // var path = require("path")

    // const currentWorkingDirectory=process.cwd()

    // const { gotResults } = require(path.join(currentWorkingDirectory,"./js/gotResults"));

    // gotResults()

    // console.log("will start GetJobDataJason function next")


    // FindJobExcelLocations()



}

