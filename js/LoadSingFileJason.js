




function LSFchooseFolderGetFiles(){
    location.replace("LSFchooseFolderGetFiles.html");
    // console.log("here it will go to LSFchooseFolderGetFiles.html from LoadSingFileJason")
}





function LoadSingFileJason(){

    // console.log("got into LoadSingleFileJason")
    
    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()

    const { gotResults } = require(path.join(currentWorkingDirectory,"./js/gotResults"));

    gotResults()


    LSFchooseFolderGetFiles()



}






// function LoadSingFileJason(){

//     var process = require("process");

//     var path = require("path")

//     const currentWorkingDirectory=process.cwd()


//     const { gotResults } = require(path.join(currentWorkingDirectory,"./js/gotResults"));

//     gotResults()
    
//     const { RunPythonFile } = require(path.join(currentWorkingDirectory,"./js/RunPythonFile"));

//     let filename = ''


//     let theNextJavascriptFunction=''

//     console.log("the net python funtion will come next")

    
//     // RunPythonFile(filename,theNextJavascriptFunction);



// }


