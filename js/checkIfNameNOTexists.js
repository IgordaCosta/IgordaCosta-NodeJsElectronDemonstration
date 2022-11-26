
function Cancel (){

    location.replace("index.html");
}



function CheckIfNotExist(){
    var path = require("path");
    var process = require("process");
    CurrrentWorkingDirectory = process.cwd();
    const { CheckIfNotExistWithType } = require(path.join(CurrrentWorkingDirectory,"./js/CheckIfNotExistWithType"));


    const typeOfButton="Del";

    CheckIfNotExistWithType(typeOfButton);

}



