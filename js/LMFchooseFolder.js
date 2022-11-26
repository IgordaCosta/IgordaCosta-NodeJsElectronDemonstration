
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



            const { loadMultipleFileResults } = require(path.join(currentWorkingDirectory,"./js/loadMultipleFileResults"));
            
            const { RunPythonFile } = require(path.join(currentWorkingDirectory,"./js/RunPythonFile"));



            //const { AddToTable } = require(path.join(currentWorkingDirectory,"./js/AddToTable"));

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

            let FileNameOnly =  fileLocation.split("\\");

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
            
            let dataName='FolderSaveLocation';

            
            // let MydocumentsDbPath = await MyDocumentsDatabasePath(currentWorkingDirectory)
            
            
            let TableName=''
            
            let Database=''
            
            let AwaitProveData = 'start function'

            // let Done = await AddToTable(MydocumentsDbPath,data, dataName, TableName,Database)

            let Done = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);

            // console.log(Done)


            

            // atTheSameTime() // this is for testing, block this and unblock the next two blocked items to continue


            let filename = 'LoadToMultipleFilesDetails.py'   // unblock this to continue program

            
            RunPythonFile(filename,loadMultipleFileResults); // unblock this to continue program




            //  place here the proceding function direction

}



function atTheSameTime(){


    var iconv = require('iconv-lite');

            var process = require("process");

            var path = require("path")

            const currentWorkingDirectory=process.cwd()



            const { loadMultipleFileResults } = require(path.join(currentWorkingDirectory,"./js/loadMultipleFileResults"));
            
            const { RunPythonFile } = require(path.join(currentWorkingDirectory,"./js/RunPythonFile"));



    timeChangePage();
    


    let filename = 'LoadToMultipleFilesDetails.py'   // unblock this to continue program

            
    RunPythonFile(filename,loadMultipleFileResults); // unblock this to continue program



}



function timeChangePage(){



    Promise.resolve()
  .then(() => delay(3000))
  .then(() => log1(1))
  .then(() => delay(3000))
  .then(() => log1(2))
  .then(() => delay(3000))
  .then(() => log1(3))
  .then(() => delay(3000))
  .then(() => log1(4))
  .then(() => delay(3000))
  .then(() => log1(5))
  .then(() => delay(3000))
  .then(() => log1(6))
  .then(() => delay(3000))
  .then(() => log1(7))
  .then(() => delay(3000))
  .then(() => log1(8))
  .then(() => delay(3000))
  .then(() => log1(9))
  .then(() => delay(3000))
  .then(() => log1(10));

function delay(duration) {
  return new Promise((resolve) => {
    setTimeout(() => resolve(), duration);
  });
}

function log1(number) {
    document.body.innerHTML = `
    <div>
        <h1>` + number + `</h1>
    </div>  
    ` }









    


}

