
var iconv = require('iconv-lite');


function OPFSelectImageFile(){
    
    location.replace("OPFSelectImageFile.html");

}

function OPFFolderSaveLocation(){

    location.replace("OPFFolderSaveLocation.html");

}



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


            DragnDropMid(pathUsed);

        }
        
        return false;
    };
}


function DragnDrop3(){

    DragnDrop3funciton();

}
    
async function DragnDrop3funciton(){

    try {
        var pathUsed=await document.getElementById("inputGroupFile04").files[0].path;
        DragnDropMid(pathUsed);
     }
     catch (e) {
       
     }

     
}

function DefaultFolder(){

    let pathUsed = ''

    let DefaultPath=true

    DragnDropMid(pathUsed,DefaultPath)

    // DefaultFolder2()

}


// async function DefaultFolder2(){

//     var process = require("process");

//     var path = require("path")

//     const currentWorkingDirectory=process.cwd()


//     const { getDbData } = require(path.join(currentWorkingDirectory, "./js/getDbData"));


//     const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory, "./js/MyDocumentsDatabasePath"));

    

//     let pathUsed = await MyDocumentsDatabasePath(currentWorkingDirectory)

//     console.log(pathUsed)

//     console.log('default pathUsed above')

//     let DefaultPath=true


//     DragnDropMid(pathUsed,DefaultPath)

// }



async function DragnDropMid(pathUsed, DefaultPath=false){
    
            var iconv = require('iconv-lite');

            var process = require("process");

            var path = require("path")

            const currentWorkingDirectory=process.cwd()

            
            const { RunPythonFile } = require(path.join(currentWorkingDirectory,"./js/RunPythonFile"));

            // const { AddToTable } = require(path.join(currentWorkingDirectory,"./js/AddToTable"));


            const { AddtoTablePromise } = require(path.join(currentWorkingDirectory,"./js/AddtoTablePromise"));

            // const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory,"./js/MyDocumentsDatabasePath"));

            let FolderLocation;

            if(DefaultPath){
                
                FolderLocation=pathUsed;

            }else{

            let buff = Buffer.from(pathUsed, 'utf8');

  
            let fileLocation = iconv.decode(buff, 'utf8');


            // console.log(fileLocation)

            // console.log('fileLocation above')

            let FileNameOnly0 = fileLocation.split("\\");

            // console.log(FileNameOnly0)

            // console.log('FileNameOnly0 above 1')

            let FileNameOnly = await FileNameOnly0[FileNameOnly0.length - 1];

            // console.log(FileNameOnly)

            // console.log('FileNameOnly above 2')

            FolderLocation = fileLocation.replace(FileNameOnly, "");


            }

            // console.log(FolderLocation)

            // console.log('FolderImageLocation above')

            let data=FolderLocation;
            
            let dataName='FolderImageSaveLocation';

            
            // let MydocumentsDbPath = await MyDocumentsDatabasePath(currentWorkingDirectory)
            
            
            let TableName=''
            
            let Database=''

            let AwaitProveData = 'starting function'


            // let Done = await AddToTable(MydocumentsDbPath,data, dataName, TableName,Database)

            let Done = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);

            // console.log(Done)


            // console.log("this is after the save folder location functions")




            // here instead of going directly into OPFSelectImageFile function
            // the program must check to see if the chosen file is a one page only pdf
            // if it is instead of treating the whole thing as a pdf
            // it will treat it as an image file
            // and work it till the end as an image file
            // ignoring the pdf name variable
            //  add a RunPythonFile function to handle this in a python program

            OPFSelectImageFile()
            



}



