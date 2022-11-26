

function Cancel (){
    location.replace("index.html");
}



function addInfoToTheDocument (){
    location.replace("addInfoToTheDocument.html");
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


function pageCopiedIntoClipboard(){


    document.body.innerHTML=`
<div class="text">
    <h1>Click on Ÿ to add this mark to</h1>
    <h1>your clipboard. Copy it into the</h1>
    <h1>location you wish to add text on your </h1>
    <h1>Word document then save the document</h1>
    <h1>and click OK to continue.</h1>
        

</div>

<div id="foreGroundImage" class="containingArea centered MainLogo noClickImg">

    <img src="_images/LogInImg.png" onclick="hideImage()" alt="MainLogo" >

</div>
<div>
<button type="button" class="btn optionsbtn mid btn-secondary" onclick="copyToClipboard()" >Ÿ</button>
</div>

<div>
<button type="button" class="btn optionsbtn right btn-secondary" onclick="GetNewStamp()" >OK</button>
</div>
<div>
<button type="button" class="btn optionsbtn left btn-secondary" onclick="Cancel()" >Cancel</button>
</div>


<div id="EnterDataSave" class="alert hidden">

<span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
Add information to the document, save the document and click OK to continue or CANCEL to cancel the operation.

</div>


<script>

copyToClipboard()

</script>


<script>

let jquerypath = path.join(__dirname, './js/jquery');
window.jQuery = window.$ = require(jquerypath);

</script>
<script src="./js/popper.min.js"></script>
<script src="./js/bootstrap.min.js"></script>`

}


function copyToClipboard() {

    text="Ÿ"
    var dummy = document.createElement("textarea");
    // to avoid breaking orgain page when copying more words
    // cant copy when adding below this code
    // dummy.style.display = 'none'
    document.body.appendChild(dummy);
    //Be careful if you use texarea. setAttribute('value', value), which works with "input" does not work with "textarea". – Eduard
    dummy.value = text;
    dummy.select();
    document.execCommand("copy");
    document.body.removeChild(dummy);
}


function GetNewStampIfSaved(results){

    GetNewStampIfSaved2(results)

}


async function GetNewStampIfSaved2(results){


    let IfSaved = await results[results.length - 1];

        // console.log(IfSaved);

        
    if(IfSaved=="FileChanged"){

        // console.log("file changed and saved properly, continue from here");
        
        // getLocationsExcel();

        // before the above function it is needed to check if anything else was altered
        // in this word document since for the case of the word document
        // the documnt saved at the end will be the temp file instead of
        // the original file like the oher cases

        checkIfThereAreOtherChanges()


    }else if(IfSaved=="NOTchanged"){

        pageCopiedIntoClipboard();

        // console.log("Document not changed or not Saved");
        document.getElementById("EnterDataSave").classList.remove('hidden');

    }else{

        pageCopiedIntoClipboard();

        // console.log("check if last python value is one of the values above");

    }


    
}


function checkIfThereAreOtherChanges(){

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()

    const { gotResults } = require(path.join(currentWorkingDirectory, "./js/gotResults"));
    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));

    gotResults();

    let filename="checkIfThereAreOtherChanges.py"

    let callback=checkIfThereAreOtherChangesReturn

    RunPythonFile(filename,callback)




}


async function checkIfThereAreOtherChangesReturn(){

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()

    
    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));


    const { getDbDataSimple } = require(path.join(currentWorkingDirectory, "./js/getDbDataSimple"));


    let DataGotten = await getDbDataSimple(AwaitProveData,TableName,Database) 

    let isSameValues = await DataGotten['isSameValues']


    if (isSameValues == 'SameValues'){

        // everthing is ok here, going into the next section


    }else if (isSameValues == 'NOTtheSame'){

        // other characters were added apart of the locator symnbol
        // or some sort of formatting or alteration was done on the document
        // a screen wil apear telling the user not to do that
        // the document will reopen with the changes deleted
        // the user wil then be asked to add the locator characters again


    }else if (isSameValues == 'ValueNOTAdded'){

        // the user did either did not save or did not add the
        // locator charactor
        // the screen to to add the charater will be added here (already meade)


    }else if (isSameValues == 'ERRORoriginalDocumentHasLetterCode'){

        // in this case for some reason the is the locator charator in the 
        // origianl document and the system did not detect it before 
        // this will go into the three question section about this issue
        // which was made in another section  (html is done it just 
        // needs to contune codeing the issues)


    }else{

        // console.log('somethin went wront value gotten bellow for isSameValues:')

        // console.log(isSameValues)

    }
    

    // let filename="checkIfThereAreOtherChanges.py"

    // let callback=checkIfThereAreOtherChangesReturn

    RunPythonFile(filename,callback)




}


function GetNewStamp(){

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()

    const { gotResults } = require(path.join(currentWorkingDirectory, "./js/gotResults"));
    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));

    gotResults();

    let filename="GetNewStamp.py"

    let callback=GetNewStampIfSaved

    RunPythonFile(filename,callback)

}

function getLocationsExcelResult(results){

    getLocationsExcelResult2(results)

}

async function getLocationsExcelResult2(results){

    ListEmpty = await results[results.length - 1]

    if (ListEmpty=='ListEmpty'){

        pageCopiedIntoClipboard();

        // console.log("Document not changed or not Saved");
        document.getElementById("EnterDataSave").classList.remove('hidden');


    }else{

    addInfoToTheDocument(); 

    }


}



function getLocationsExcel(){


    // console.log("Started getLocationsExcel Function")

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()

    // const { gotResults } = require(path.join(currentWorkingDirectory, "./js/gotResults"));
    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));






    let filename="getLocationsExcel.py"

    let callback=getLocationsExcelResult


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

    //     let NumList = results[results.length - 3];

    //     let listOfRows = results[results.length - 2];

    //     let listOfColumns = results[results.length - 1];


    //     myObj = {listOfRows: listOfRows, listOfColumns: listOfColumns, NumList: NumList};
    //     myJSON = JSON.stringify(myObj);
    //     localStorage.setItem("RowColumn", myJSON);





    //     addInfoToTheDocument(); 




        




        

        




    // }
    // )    



}





// function checkIfSavedAndFilled(){

//     // function runPythonFile(filename,fileLocation){
//         let filename="OpenExcelDocument.py"

//         let path = require("path");
    
//         let filenamecheck=path.basename(__dirname);
//         console.log(filenamecheck);
//         console.log("filename check above");
    
    
//         if (filenamecheck=="CSSAutoFormFiller"){}else{
//             __dirname = path.join(__dirname, '../../../../../../');
    
//         }
        
//         console.log(__dirname)
//         console.log("__dirname")
        
    
//         let {PythonShell} = require("python-shell");
    
//         let opcoes = {
//             scriptPath : path.join(__dirname, './_engine/'),
//             pythonPath: 'C:\\ProgramData\\Anaconda3\\python',
//         };
    
//         console.log(path.join(__dirname, './_engine/'));
//         console.log("startprint");
//         PythonShell.run(filename, opcoes, function (err, results) {
//             if (err) throw err;

//             console.log(results);

//             let IfSaved = results[results.length - 1];

//             console.log(IfSaved);

//             if(IfSaved=="AllOk"){

//                 console.log("continue for all is ok");


//             }else if(IfSaved=="ERROR"){

//                 console.log("document not filled or saved show alert to do so");
//                 document.getElementById("EnterDataSave").classList.remove('hidden');

//             }else{

//                 console.log("check if last python value is one of the values above");

//             }


    
//         }
//         )    
// }

