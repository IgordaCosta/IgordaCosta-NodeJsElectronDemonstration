
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


}










    










async function DragnDropMid(pathUsed, DefaultPath=false){
    
            var iconv = require('iconv-lite');

            var process = require("process");

            var path = require("path")

            const currentWorkingDirectory=process.cwd()

            
            const { RunPythonFile } = require(path.join(currentWorkingDirectory,"./js/RunPythonFile"));



            const { AddtoTablePromise } = require(path.join(currentWorkingDirectory,"./js/AddtoTablePromise"));


            let FolderLocation;

            if(DefaultPath){
                
                FolderLocation=pathUsed;

            }else{

            let buff = Buffer.from(pathUsed, 'utf8');

  
            let fileLocation = iconv.decode(buff, 'utf8');




            let FileNameOnly0 = fileLocation.split("\\");



            let FileNameOnly = await FileNameOnly0[FileNameOnly0.length - 1];



            FolderLocation = fileLocation.replace(FileNameOnly, "");


            }



            let data=FolderLocation;
            
            let dataName='FolderImageSaveLocation';

            
            
            
            let TableName=''
            
            let Database=''

            let AwaitProveData = 'starting function'



            let Done = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);








            OPFSelectImageFile()
            



}



