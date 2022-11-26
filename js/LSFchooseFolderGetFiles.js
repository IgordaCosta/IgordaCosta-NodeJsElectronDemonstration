

function LSFFolderSaveLocation(){

location.replace("LSFFolderSaveLocation.html");

}



var iconv = require('iconv-lite');

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

    try {
        var pathUsed=document.getElementById("inputGroupFile04").files[0].path;
        DragnDropMid(pathUsed);
     }
     catch (e) {
       
     }

     
}

function DefaultFolder(){

    let pathUsed = ''

    let DefaultPath=true

    DragnDropMid(pathUsed,DefaultPath)

 

}

async function DragnDropMid(pathUsed, DefaultPath=false){
    


            var process = require("process");

            var path = require("path")

            const currentWorkingDirectory=process.cwd()



            const { loadMultipleFileResults } = require(path.join(currentWorkingDirectory,"./js/loadMultipleFileResults"));
            
            const { RunPythonFile } = require(path.join(currentWorkingDirectory,"./js/RunPythonFile"));



            const { AddToTable } = require(path.join(currentWorkingDirectory,"./js/AddToTable"));

            const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory,"./js/MyDocumentsDatabasePath"));

            let FolderLocation;

            if(DefaultPath){
                
                FolderLocation=pathUsed;

            }else{

            let buff = Buffer.from(pathUsed, 'utf8');

  
            let fileLocation = iconv.decode(buff, 'utf8');


            // console.log(fileLocation)

            // console.log('fileLocation above')

            let FileNameOnly = fileLocation.split("\\");

            // console.log(FileNameOnly)

            // console.log('FileNameOnly above 1')

            FileNameOnly = FileNameOnly[FileNameOnly.length - 1];

            // console.log(FileNameOnly)

            // console.log('FileNameOnly above 2')

            FolderLocation = fileLocation.replace(FileNameOnly, "");


            }

            // console.log(FolderLocation)

            // console.log('FolderLocation above')

            let data=FolderLocation;
            
            let dataName='FolderFileGottenLocation';

            
            let MydocumentsDbPath = await MyDocumentsDatabasePath(currentWorkingDirectory)
            
            
            let TableName=''
            
            let Database=''


            let Done = await AddToTable(MydocumentsDbPath,data, dataName, TableName,Database)

            // console.log(Done)


            LSFFolderSaveLocation()

            // LSFSaveQRDataToExcelFile()


            

}



// function LSFSaveQRDataToExcelFile(){

//     console.log("got into LoadSingleFileJason")
    
//     var process = require("process");

//     var path = require("path")

//     const currentWorkingDirectory=process.cwd()

//     const { gotResults } = require(path.join(currentWorkingDirectory,"./js/gotResults"));

//     gotResults()


//     console.log('continue from here LSFSaveQRDataToExcelFile')



// }



