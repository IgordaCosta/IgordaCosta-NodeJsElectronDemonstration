

function LMFchooseFolder(){
    location.replace("LMFchooseFolder.html");
}





function LoadMutipleFileJason(){

    // console.log("got into LoadMultipleFileJason")
    
    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()

    const { gotResults } = require(path.join(currentWorkingDirectory,"./js/gotResults"));

    gotResults()


    LMFchooseFolder()



}


