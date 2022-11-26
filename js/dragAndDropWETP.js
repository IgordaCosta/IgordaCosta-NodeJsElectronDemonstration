


function loghere(){
    var log4js = require("log4js");
    var logger = log4js.getLogger();
    logger.level = "debug"; // default level is OFF - which means no logs at all.

    log4js.configure({
        appenders: {
        out: { type: 'stdout', layout: {
            type: 'pattern',
            pattern: '%d %p %c %m%n',
            
        }
        
        },

        app: { type: 'file', filename: 'application.log' }
        
        },
        categories: { default: { appenders: ['out'], level: 'info' } }
    });
    const logger = log4js.getLogger();

    return logger
}


function DragnDrop2 () {

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();


    const { DragnDropMidWETP } = require(path.join(currentWorkingDirectory, "./js/DragnDropMidWETP"));

    // location.replace("dragAndDrop.html")

    // var holder = document.getElementById('drag-file');
    var holder = document.getElementsByClassName('dragLocation')[0];
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


            DragnDropMidWETP(pathUsed);

        }
        
        return false;
    };
}


function DragnDrop3(){

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();


    const { DragnDropMidWETP } = require(path.join(currentWorkingDirectory, "./js/DragnDropMidWETP"));



    try {
        var pathUsed=document.getElementById("inputGroupFile04").files[0].path;
        DragnDropMidWETP(pathUsed);
     }
     catch (e) {
       
     }

    
}

function dragAndDropWETP (){
    location.replace("dragAndDropWETP.html");
    
}

function Cancel (){
    location.replace("index.html");
}

function OtherFunctions(){

    location.replace("OtherFunctions.html");

}


function jasonRerunReturnFromSameFileInside(){
    

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()


    const { gotResults } = require(path.join(currentWorkingDirectory,"./js/gotResults"));

    const { runReturnFromSameFileInside } = require(path.join(currentWorkingDirectory,"./js/runReturnFromSameFileInside"));

    
    gotResults()

    
    runReturnFromSameFileInside()
    
}


function StringFromInt(IntList){

    let result = IntList.substring(1, IntList.length-1);

    let result2=result.split(", ");

    let result3 = result2.map(function (x) { 
        return parseInt(x, 10); 
      });

    
    return result3
}


