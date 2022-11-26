// function Cancel (){

//     location.replace("index.html");
// }

// function OperationComplete(){
//     location.replace("OperationComplete.html");
// }



function TypeJobNameReload (){
    document.body.innerHTML =`
    <div id="FileExists" class="alert hidden">
        
        <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
        This job name does not exist! Try a new name!
        
    </div> 


    <div class="text">
        
            <h1>Name a valid Job and click OK or </h1>
            <h1>Press Cancel to quit this process. </h1>
            
    </div>

    <div id="foreGroundImage" class="containingArea centered MainLogo noClickImg">

        <img src="_images/LogInImg.png" onclick="hideImage()" alt="MainLogo" >

    </div>

    <div class="spinner spinner-border text-secondary hidden" role="status">
        <span class="sr-only">Loading...</span>

    </div>

    <div class="spinner down hidden">
        <h1>Loading...</h1>
    </div>


    <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="Job Name" aria-label="Job Name" aria-describedby="button-addon2">
        <div class="input-group-append">
          <button class="btn btn-outline-secondary" type="button" id="button-addon2" onclick="CheckIfNotExist()">OK</button>
        </div>
    </div>

    <div>
        <button type="button" class="btn optionsbtn left btn-secondary" onclick="Cancel()" >Cancel</button>
    </div>
    
    <script>

        let jquerypath = path.join(__dirname, './js/jquery');
        window.jQuery = window.$ = require(jquerypath);

    </script>
    
    <script src="./js/popper.min.js"></script>
    <script src="./js/bootstrap.min.js"></script>
    `
    
}


// function gotResults(){
    
//     document.body.innerHTML =`<div class="spinner spinner-border text-secondary" role="status">
//                         <span class="sr-only">Loading...</span>
    
//                     </div>
//                     <div class="spinner down">
//                         <h1>Loading...</h1>
//                     </div>

//                     <div>
//                         <img src="_images/LogInImg.png" alt="Img" >
//                     </div>`
// }




// function CheckIfNotExist(){
//     // var x = document.getElementById("myText").value;

//     let jobName = document.getElementsByClassName("form-control")[0].value;
//     // console.log(jobName);
//     document.getElementsByClassName("form-control")[0].value=''

    
//     if (jobName==''){}else{

//     document.getElementsByClassName("input-group")[0].classList.add('hidden');
//     document.getElementsByClassName("spinner")[0].classList.remove('hidden');
    
//     filename='CheckJobNameRedo.py'
//     data=jobName

//     runPythonFile(filename,data);
//     }
// }


// function runPythonFile(filename,data){

//     gotResults()

//     let path = require("path");

//     let filenamecheck=path.basename(__dirname);
//     // console.log(filenamecheck);
//     // console.log("filename check above");

//     // console.log(fileLocation);
//     // console.log('fileLocation above')

//     if (filenamecheck=="CSSAutoFormFiller"){}else{
//         __dirname = path.join(__dirname, '../../../../../../');

//     }
    
//     // console.log(__dirname)
//     // console.log("__dirname")
    
    

//     let {PythonShell} = require("python-shell");

//     let opcoes = {
//         scriptPath : path.join(__dirname, './_engine/'),
//         pythonPath: 'C:\\ProgramData\\Anaconda3\\python',
//         args : [data]
//     };

//     // console.log(path.join(__dirname, './_engine/'));
//     // console.log("startprint");

//     PythonShell.run(filename, opcoes, function (err, results) {
//         if (err) throw err;

    
//         // console.log(results);

//         let ifExists = results[results.length - 1];
        

        


//         if(ifExists=="True"){

//             console.log("continue the program from here")

//             datafillName=data

//             // DeleteItem(datafillName)
//             LoadSingleFile(datafillName)

            

            

            
            

//         }else if(ifExists=="False"){

//             console.log("variable is False.... going back");
//             TypeJobNameReload();

//             document.getElementById("FileExists").classList.remove('hidden');

//             //

//             // OpenExcelDocument();

//         }else{

//             TypeJobNameReload();
//             // console.log("Last Variable must be either True or False and it is neither. Check last Python function output!");
            
            
//             // document.getElementsByClassName("spinner")[0].classList.add('hidden');
//             // document.getElementsByClassName("input-group")[0].classList.remove('hidden');
            
        
//         };
        

//         // document.getElementsByClassName("input-group")[0].classList.remove('hidden');

//         // document.getElementsByClassName("spinner")[0].classList.add('hidden');

//         // console.log("Finished Python File after check if file exists");
        
//     });
// }



// function LoadSingleFile(datafillName){

//     console.log("LoadSingleFile function started");

//     // Split this file into multiple files so the progress bar works with the file progression


//     // let filename =

//     // let path = require("path");

//     // let filenamecheck=path.basename(__dirname);
    

//     // if (filenamecheck=="CSSAutoFormFiller"){}else{
//     //     __dirname = path.join(__dirname, '../../../../../../');

//     // }
    
    
    

//     // let {PythonShell} = require("python-shell");

//     // let opcoes = {
//     //     scriptPath : path.join(__dirname, './_engine/'),
//     //     pythonPath: 'C:\\ProgramData\\Anaconda3\\python',
//     //     args : [datafillName]
//     // };

    
//     // PythonShell.run(filename, opcoes, function (err, results) {
//     //     if (err) throw err;

        
        
//     //     OperationComplete()
    
//     // }


//     // )
        

// }


function Cancel (){

    location.replace("index.html");
}

function LSFchooseFolder(){
    location.replace("LSFchooseFolderGetFiles.html");

    // console.log("here it would go to the LSFchooseFolder.html location ")
}


async function CheckIfNotExist(){

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()


    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));

    const { insertIntoDatabase } = require(path.join(currentWorkingDirectory, "./js/insertIntoDatabase"));

    // const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory, "./js/MyDocumentsDatabasePath"));


    const { gotResults } = require(path.join(currentWorkingDirectory, "./js/gotResults"));


    let jobName = document.getElementsByClassName("form-control")[0].value;

    document.getElementsByClassName("form-control")[0].value=''


    if (jobName==''){}else{

    document.getElementsByClassName("input-group")[0].classList.add('hidden');
    document.getElementsByClassName("spinner")[0].classList.remove('hidden');
    
    let filename='CheckJobNameRedo.py'

    let data=jobName;

    let dataName='datafillName';

    let CurrentWorkingPath=currentWorkingDirectory;

    let TableName='';

    let Database='';

    gotResults()

    // let MydocumentsDbPath = await MyDocumentsDatabasePath(CurrentWorkingPath);
    

    let Done=await insertIntoDatabase(data, dataName, CurrentWorkingPath, TableName,Database);

    // console.log(Done);

    RunPythonFile(filename,CheckJobNameRedoResults);



    }
}


function CheckJobNameRedoResults(results){
    
        CheckJobNameRedoResults2(results)

}

async function CheckJobNameRedoResults2(results){

    let ifExists = await results[results.length - 1];
    
    if(ifExists=="True"){

        // console.log("continue the program from here")


        LSFchooseFolder()
        


    }else if(ifExists=="False"){

        // console.log("variable is False.... going back");
        TypeJobNameReload();

        document.getElementById("FileExists").classList.remove('hidden');

    }else{

        TypeJobNameReload();
        // console.log("Last Variable must be either True or False and it is neither. Check last Python function output!");
          
    
    };

}
        

        