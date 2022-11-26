function LMFItemChecked(){
    

    // console.log("change to location here")

    location.replace("LMFItemChecked.html");

   

}

function LMFItemNOTchecked(){
    // LSFItemNOTchecked

    location.replace("LMFItemNOTChecked.html");

    // LSFItemNOTChecked

}




function LoadMultipleFilesFromDatabase(){

    const ItemChecked=LMFItemChecked;

    const ItemNOTchecked=LMFItemNOTchecked;

    let typeOfButton;

    typeOfButton="LMF";

    var path = require("path")
    var process = require("process")
    const CurrrentWorkingDirectory=process.cwd()

    // process.chdir(CurrrentWorkingDirectory)

    const { AsyncActionFunction } = require(path.join(CurrrentWorkingDirectory,"./js/AsyncActionFunction"));

    AsyncActionFunction(ItemChecked,ItemNOTchecked,typeOfButton);

}




