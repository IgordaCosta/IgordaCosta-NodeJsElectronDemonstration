

function DragnDrop2 () {

    const holder = document.getElementsByClassName('dragLocation')[0];
    holder.ondragover = () => {
        return false;
    };

    holder.ondragleave = () => {
        return false;
    };

    holder.ondragend = () => {
        return false;
    };

    holder.ondrop = (e) => {
        e.preventDefault();

        let ok1=false;

        for (let f of e.dataTransfer.files) {

            let pathUsed=f.path;
            
            DragnDropBeforeMid(pathUsed)

        };
        
        return false;
    };
};


function DragnDropBeforeMid(pathUsed){

    const process = require("process");

    const path = require("path");

    const currentWorkingDirectory = process.cwd();

    const { DragnDropMid } = require(path.join(currentWorkingDirectory, "./js/DragnDropMid"));
   
    DragnDropMid(pathUsed);

};


function DragnDrop3(){

    DragnDrop3function();

};


async function DragnDrop3function(){

    const process = require("process");

    const path = require("path");

    const currentWorkingDirectory = process.cwd();

    const { DragnDropMid } = require(path.join(currentWorkingDirectory, "./js/DragnDropMid"));

    try {
    
        const pathUsed= await document.getElementById("inputGroupFile04").files[0].path;
        DragnDropMid(pathUsed);

     }
     catch (e) {
       
     };

    
};

function DragnDrop (){
    
    location.replace("dragAndDrop.html");
    
};

function Cancel (){
    
    location.replace("index.html");

};





function jasonRerunReturnFromSameFileInside(){

    const process = require("process");
    const path = require("path");
    const currentWorkingDirectory=process.cwd();

    const { gotResults } = require(path.join(currentWorkingDirectory,"./js/gotResults"));
    const { gotResultsAdd } = require(path.join(currentWorkingDirectory,"./js/gotResultsAdd"));   
    const { runReturnFromSameFileInside } = require(path.join(currentWorkingDirectory,"./js/runReturnFromSameFileInside"));

    gotResults();
 
    runReturnFromSameFileInside();
    
};


function StringFromInt(IntList){

    let result = IntList.substring(1, IntList.length-1);
    let result2=result.split(", ");
    let result3 = result2.map(function (x) { 

        return parseInt(x, 10); 

    });
    
    return result3;

};


