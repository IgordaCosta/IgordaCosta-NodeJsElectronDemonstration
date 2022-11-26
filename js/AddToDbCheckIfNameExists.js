// const { ifError } = require("assert");
// const { MyDocumentsDatabasePath } = require("./MyDocumentsDatabasePath");








function Cancel (){

    location.replace("index.html");
}

function MarkExcellSheet (){

    location.replace("MarkExcellSheet.html");
}

function TypeJobNameReload (){
    document.body.innerHTML =`
    <div id="FileExists" class="alert hidden">
        
        <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
        This job name already exist! Try a new name!
        
    </div> 

    <div id="OpenExcelError" class="alert hidden">
        
        <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
        There is a program dependent document that is currently opened and altered. Save or close this document and click OK to continue or click CANCEL to cancel the operation.
        
    </div> 

    <div class="text">
        
            <h1>Name the Job and click OK or </h1>
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
          <button class="btn btn-outline-secondary" type="button" id="button-addon2" onclick="getTextValue()">OK</button>
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


function gotResults(){
    
    document.body.innerHTML =`<div class="spinner spinner-border text-secondary" role="status">
                        <span class="sr-only">Loading...</span>
    
                    </div>
                    <div class="spinner down">
                        <h1>Loading...</h1>
                    </div>

                    <div id="foreGroundImage" class="containingArea centered MainLogo noClickImg">

                        <img src="_images/LogInImg.png" onclick="hideImage()" alt="MainLogo" >

                    </div>`
}




// function getTextValue(){

//     getTextValueAsync()

//     // var process = require("process");

//     // var path = require("path")

//     // const currentWorkingDirectory=process.cwd()


//     // const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));
//     // const { insertIntoDatabase } = require(path.join(currentWorkingDirectory, "./js/insertIntoDatabase"));
//     // const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory, "./js/MyDocumentsDatabasePath"));


    

//     // // var x = document.getElementById("myText").value;

//     // let jobName = document.getElementsByClassName("form-control")[0].value;
//     // // console.log(jobName);
//     // document.getElementsByClassName("form-control")[0].value=''

    
//     // if (jobName==''){}else{

//     // document.getElementsByClassName("input-group")[0].classList.add('hidden');
//     // document.getElementsByClassName("spinner")[0].classList.remove('hidden');
    
//     // let filename='CheckJobNameRedo.py';
//     // // data=jobName

//     // let callback=AddDataCheckIfExists




//     // let data=jobName;

//     // let dataName='datafillName';

//     // const MyDocumentsDatabasePath = await MyDocumentsDatabasePath(currentWorkingDirectory)


//     // let TableName=''

//     // let Database=''


//     // Done= await insertIntoDatabase(data, dataName, MyDocumentsDatabasePath,currentWorkingDirectory,TableName,Database)

//     // console.log(Done)

//     // RunPythonFile(filename,callback)

//     // // runPythonFile(filename,data);




//     // }
// }


async function getTextValue(){

    // var process = require("process");

    // var path = require("path")

    // const currentWorkingDirectory=process.cwd()


    // const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));
    // const { insertIntoDatabase } = require(path.join(currentWorkingDirectory, "./js/insertIntoDatabase"));
    // const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory, "./js/MyDocumentsDatabasePath"));

    // MyDocumentsDatabasePath(CurrenWorkingPath)
    

    // var x = document.getElementById("myText").value;

    let jobName = document.getElementsByClassName("form-control")[0].value;
    // console.log(jobName);
    document.getElementsByClassName("form-control")[0].value=''

    
    if (jobName==''){}else{


    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()


    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));
    const { AddToTable } = require(path.join(currentWorkingDirectory, "./js/AddToTable"));
    const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory, "./js/MyDocumentsDatabasePath"));



    document.getElementsByClassName("input-group")[0].classList.add('hidden');
    document.getElementsByClassName("spinner")[0].classList.remove('hidden');
    
    let filename='CheckJobNameRedo.py';
    // data=jobName

    let callback=AddDataCheckIfExists




    let data=jobName;

    let dataName='datafillName';

    let MyDocumentsDbPath = await MyDocumentsDatabasePath(currentWorkingDirectory)


    let TableName=''

    let Database=''
    

    Done= await AddToTable(data, dataName, MyDocumentsDbPath,currentWorkingDirectory,TableName,Database)

    // console.log(Done)

    RunPythonFile(filename,callback)

    // runPythonFile(filename,data);



AddDataCheckIfExists
    }


}


function AddDataCheckIfExists(results){

    function AddDataCheckIfExists2(results)

}

async function AddDataCheckIfExists2(results){

    let ifExists = await results[results.length - 1];
      

    if(ifExists=="True"){

        TypeJobNameReload();

        // console.log("variable is TRUE");

        // console.log("back to old window to try again")

        // document.getElementsByClassName("spinner")[0].classList.add('hidden');


        // // document.getElementsByClassName("spinner")[0].classList.add('hidden');
        // document.getElementsByClassName("input-group")[0].classList.remove('hidden');

        document.getElementById("FileExists").classList.remove('hidden');
        

    }else if(ifExists=="False"){

        // console.log("variable is False.... continue to next part from here");

        OpenExcelDocument();

    }else{

        TypeJobNameReload();
        // console.log("Last Variable must be either True or False and it is neither. Check last Python function output!");
        
        
        // document.getElementsByClassName("spinner")[0].classList.add('hidden');
        // document.getElementsByClassName("input-group")[0].classList.remove('hidden');
        
    
    };
    

    // document.getElementsByClassName("input-group")[0].classList.remove('hidden');

    // document.getElementsByClassName("spinner")[0].classList.add('hidden');

    // console.log("Finished Python File after check if file exists");

}



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

    
        // console.log(results);

        // let ifExists = results[results.length - 1];
        

        


        // if(ifExists=="True"){

        //     TypeJobNameReload();

        //     // console.log("variable is TRUE");

        //     // console.log("back to old window to try again")

        //     // document.getElementsByClassName("spinner")[0].classList.add('hidden');


        //     // // document.getElementsByClassName("spinner")[0].classList.add('hidden');
        //     // document.getElementsByClassName("input-group")[0].classList.remove('hidden');

        //     document.getElementById("FileExists").classList.remove('hidden');
            

        // }else if(ifExists=="False"){

        //     // console.log("variable is False.... continue to next part from here");

        //     OpenExcelDocument();

        // }else{

        //     TypeJobNameReload();
        //     // console.log("Last Variable must be either True or False and it is neither. Check last Python function output!");
            
            
        //     // document.getElementsByClassName("spinner")[0].classList.add('hidden');
        //     // document.getElementsByClassName("input-group")[0].classList.remove('hidden');
            
        
        // };
        

        // // document.getElementsByClassName("input-group")[0].classList.remove('hidden');

        // // document.getElementsByClassName("spinner")[0].classList.add('hidden');

        // // console.log("Finished Python File after check if file exists");
        
//     });
// }


function OpenExcelDocument(){


    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()


    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));
    // const { insertIntoDatabase } = require(path.join(currentWorkingDirectory, "./js/insertIntoDatabase"));
    // const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory, "./js/MyDocumentsDatabasePath"));



    let filename="OpenExcelDocument.py"

    let callback=AddDataOpenExcelDocumentReturn


    RunPythonFile(filename,callback)






    // let path = require("path");

    // let filenamecheck=path.basename(__dirname);
    // // console.log(filenamecheck);
    // // console.log("filename check above");


    // if (filenamecheck=="CSSAutoFormFiller"){}else{
    //     __dirname = path.join(__dirname, '../../../../../../');

    // }
    
    // // console.log(__dirname)
    // // console.log("__dirname")
       

    // let {PythonShell} = require("python-shell");

    // let opcoes = {
    //     scriptPath : path.join(__dirname, './_engine/'),
    //     pythonPath: 'C:\\ProgramData\\Anaconda3\\python',
        
    // };

    // // console.log(path.join(__dirname, './_engine/'));
    // // console.log("startprint");

    // PythonShell.run(filename, opcoes, function (err, results) {
    //     if (err) throw err;

        // // console.log(results)

        // IfError=(results[results.length -1]).trim()

        // // console.log(IfError);

        // // console.log(IfError=="AllOk");

        // // console.log('IfError=="AllOk above"');


        // if(IfError=="ERROR"){

        //     TypeJobNameReload();

        //     // console.log("There is an error opening the excel sheet");

        //     document.getElementById("OpenExcelError").classList.remove('hidden');
        //     // AlteredOrOpenedDocument() // use the red alert instead, its more professional


        // }else if(IfError=="AllOk"){

        //     // console.log("All is ok to continue from here");


        //     GetOldStamp();

        //     // MarkExcellSheet();

        //     // here is where the user copy and pastes a special code into 
        //     // his excel sheet and press ok for the location of the sheet to
        //     // be recognized by the program



        // }else{
        //     TypeJobNameReload();

        //     // console.log("IfError is a different value from the accepted check last python program print");


        // }

        

        

        // JSON.stringify(ifError) === JSON.stringify('ERROR')

        // if(ifError=="ERROR"){

        // if(JSON.stringify(ifError) === JSON.stringify('ERROR')){

        //     console.log("error happend it must run the self.InicioSalveDocumento() function then try again");
            
        //     // OpenExcelDocument()

        // }
        // // else if(ifError=="All Ok"){
        // else if (JSON.stringify(ifError) === JSON.stringify('AllOk')){

        //     console.log("continue");

        // }else{

        //     console.log("check last function print statemente it must be one of the above");

        // };

}
// )
// }

function AddDataOpenExcelDocumentReturn(results){

    function AddDataOpenExcelDocumentReturn2(results)

}



async function AddDataOpenExcelDocumentReturn2(results){


    let IfError=await (results[results.length -1]).trim()

        // console.log(IfError);

        // console.log(IfError=="AllOk");

        // console.log('IfError=="AllOk above"');


    if(IfError=="ERROR"){

        TypeJobNameReload();

        // console.log("There is an error opening the excel sheet");

        document.getElementById("OpenExcelError").classList.remove('hidden');
        // AlteredOrOpenedDocument() // use the red alert instead, its more professional


    }else if(IfError=="AllOk"){

        // console.log("All is ok to continue from here");


        GetOldStamp();

        // MarkExcellSheet();

        // here is where the user copy and pastes a special code into 
        // his excel sheet and press ok for the location of the sheet to
        // be recognized by the program



    }else{
        TypeJobNameReload();

        // console.log("IfError is a different value from the accepted check last python program print");


    }


}



function GetOldStamp(){


        var process = require("process");

        var path = require("path")

        const currentWorkingDirectory=process.cwd()


        const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));
        // const { insertIntoDatabase } = require(path.join(currentWorkingDirectory, "./js/insertIntoDatabase"));
        // const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory, "./js/MyDocumentsDatabasePath"));


    // function runPythonFile(filename,fileLocation){
        let filename="GetOldStamp.py"

        let callback = MarkExcellSheet

        RunPythonFile(filename,callback)


        // let path = require("path");
    
        // let filenamecheck=path.basename(__dirname);

        // // console.log(filenamecheck);
        // // console.log("filename check above");
    
    
        // if (filenamecheck=="CSSAutoFormFiller"){}else{
        //     __dirname = path.join(__dirname, '../../../../../../');
    
        // }
        
        // // console.log(__dirname)
        // // console.log("__dirname")
        
    
        // let {PythonShell} = require("python-shell");
    
        // let opcoes = {
        //     scriptPath : path.join(__dirname, './_engine/'),
        //     pythonPath: 'C:\\ProgramData\\Anaconda3\\python',
        // };
    
        // // console.log(path.join(__dirname, './_engine/'));
        // // console.log("startprint");

        // PythonShell.run(filename, opcoes, function (err, results) {
        //     if (err) throw err;

        //     // console.log(results);


            // MarkExcellSheet();

            
            // checkIfSavedAndFilled();

    
        }
//         )    
// }