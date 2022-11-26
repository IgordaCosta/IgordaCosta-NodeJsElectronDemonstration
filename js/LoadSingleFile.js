function LSFItemChecked(){

    location.replace("LSFItemChecked.html");

}

function LSFItemNOTchecked(){

    location.replace("LSFItemNOTChecked.html");

}


function Cancel (){
    location.replace("index.html");
}








function LoadSingleFileFromDatabase(){

    const ItemChecked=LSFItemChecked;

    const ItemNOTchecked=LSFItemNOTchecked;

    let typeOfButton;

    typeOfButton="LSF";

    var path = require("path")
    var process = require("process")
    CurrrentWorkingDirectory=process.cwd()

    const { AsyncActionFunction } = require(path.join(CurrrentWorkingDirectory,"./js/AsyncActionFunction"));

    AsyncActionFunction(ItemChecked,ItemNOTchecked,typeOfButton);

}





