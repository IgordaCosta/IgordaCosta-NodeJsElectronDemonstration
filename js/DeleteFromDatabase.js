

function DelItemChecked(){

    location.replace("ItemChecked.html");

}

function DelItemNOTchecked(){

    location.replace("ItemNOTChecked.html");

}


function Cancel (){
    location.replace("index.html");
}



function DeleteFromDatabase(){

    const ItemChecked=DelItemChecked;

    const ItemNOTchecked=DelItemNOTchecked;

    let typeOfButton;

    typeOfButton="Del";

    var path = require("path")
    var process = require("process")
    CurrrentWorkingDirectory=process.cwd()

    const { AsyncActionFunction } = require(path.join(CurrrentWorkingDirectory,"./js/AsyncActionFunction"));

    AsyncActionFunction(ItemChecked,ItemNOTchecked,typeOfButton);

}




