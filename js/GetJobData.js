function GJDItemChecked(){

    location.replace("GJDItemChecked.html");

}

function GJDItemNOTchecked(){

    location.replace("GJDItemNOTChecked.html");

}


function Cancel (){
    location.replace("index.html");
}








function GetJobData(){

    const ItemChecked=GJDItemChecked;

    const ItemNOTchecked=GJDItemNOTchecked;

    let typeOfButton;

    typeOfButton="GJD";

    var path = require("path")
    var process = require("process")
    CurrrentWorkingDirectory=process.cwd()
    
    const { AsyncActionFunction } = require(path.join(CurrrentWorkingDirectory,"./js/AsyncActionFunction"));






    AsyncActionFunction(ItemChecked,ItemNOTchecked,typeOfButton);

}





