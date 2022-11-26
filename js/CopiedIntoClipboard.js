

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
    <h1>Click on XYXYXYXYX to add this mark to</h1>
    <h1>your clipboard. Copy it into the</h1>
    <h1>auto fill input areas (cells) of your </h1>
    <h1>Excel document then save the document</h1>
    <h1>and click OK.</h1>
    

</div>

<div id="foreGroundImage" class="containingArea centered MainLogo noClickImg">

    <img src="_images/LogInImg.png" onclick="hideImage()" alt="MainLogo" >

</div>
<div>
<button type="button" class="btn optionsbtn mid btn-secondary" onclick="copyToClipboard()" >XYXYXYXYX</button>
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

    text="XYXYXYXYX"
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

// function checkListValues(){

//     console.log("checkListValues start");

//     checkIfSavedAndFilled();



//     // document.getElementById("EnterDataSave").classList.remove('hidden');

// }


function GetNewStampIfSaved(results){

    function GetNewStampIfSaved2(results)

}


async function GetNewStampIfSaved2(results){


    let IfSaved = await results[results.length - 1];

        // console.log(IfSaved);

        
    if(IfSaved=="FileChanged"){

        // console.log("file changed and saved properly, continue from here");
        
        getLocationsExcel();


    }else if(IfSaved=="NOTchanged"){

        pageCopiedIntoClipboard();

        // console.log("Document not changed or not Saved");
        document.getElementById("EnterDataSave").classList.remove('hidden');

    }else{

        pageCopiedIntoClipboard();

        // console.log("check if last python value is one of the values above");

    }


    
}


function GetNewStamp(){

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()

    const { gotResults } = require(path.join(currentWorkingDirectory, "./js/gotResults"));
    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));



    gotResults();



    // function runPythonFile(filename,fileLocation){
    let filename="GetNewStamp.py"

    let callback=GetNewStampIfSaved




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

        // let IfSaved = results[results.length - 1];

        // // console.log(IfSaved);

        
        // if(IfSaved=="FileChanged"){

        //     // console.log("file changed and saved properly, continue from here");
            
        //     getLocationsExcel();


        // }else if(IfSaved=="NOTchanged"){

        //     pageCopiedIntoClipboard();

        //     // console.log("Document not changed or not Saved");
        //     document.getElementById("EnterDataSave").classList.remove('hidden');

        // }else{

        //     pageCopiedIntoClipboard();

        //     // console.log("check if last python value is one of the values above");

        // }

        
        


    // }
    // )    
}


function getLocationsExcelResult(results){


    getLocationsExcelResult2(results)


}


async function getLocationsExcelResult2(results){



    // let NumList = results[results.length - 3];

    // let listOfRows = results[results.length - 2];

    // let listOfColumns = results[results.length - 1];

    // console.log("getLocationsExcelResult location")

    // var process = require("process");

    // var path = require("path")

    // const currentWorkingDirectory=process.cwd()


    // // const { StartTableData } = require(path.join(currentWorkingDirectory, "./js/StartTableData"));


    // const { AddToTable } = require(path.join(currentWorkingDirectory, "./js/AddToTable"));



    // let AwaitProveData="started"

    // // let data1=listOfRows
    // // let dataName1=listOfRows
    // // let TableName1="listOfRows"


    // let Database=''


    // // let data1=[listOfRows,listOfColumns,NumList]
    // // let dataName1=['listOfRows','listOfColumns','NumList']
    // // let TableName1="ValuesAndLocations"


    // // let TabledataStarted1=StartTableData(AwaitProveData,data1, dataName1, TableName1,Database)
    // // console.log(TableName1)
    // // console.log('TableName1')
    
    // // console.log(TabledataStarted1)
    // // console.log('TabledataStarted1 ')

    // let data1=[listOfRows,listOfColumns,NumList]
    // let dataName1=['listOfRowsExcelInput','listOfColumnsExcelInput','NumListExcelInput']
    // let TableName1=""

    // let TabledataStarted1 =AddToTable(AwaitProveData,data1, dataName1, TableName1,Database)
    // // let TabledataStarted1=StartTableData(AwaitProveData,data1, dataName1, TableName1,Database)
    // console.log(TableName1)
    // console.log('TableName1')
    
    // console.log(TabledataStarted1)
    // console.log('TabledataStarted1 ')



    // // let data2=listOfColumns
    // // let dataName2=listOfColumns
    // // let TableName2="listOfColumns"
    

    // // let TabledataStarted2=StartTableData(AwaitProveData,data2, dataName2, TableName2,Database)
    // // console.log(TableName2)
    // // console.log('TableName2')
    
    // // console.log(TabledataStarted2)
    // // console.log('TabledataStarted2 ')




    // // let data3=NumList
    // // let dataName3=NumList
    // // let TableName3="NumList"
    
    // // let TabledataStarted3=StartTableData(AwaitProveData,data3, dataName3, TableName3,Database)
    // // console.log(TableName3)
    // // console.log('TableName3')
    
    // // console.log(TabledataStarted3)
    // // console.log('TabledataStarted3 ')







    // // myObj = {listOfRows: listOfRows, listOfColumns: listOfColumns, NumList: NumList};
    // // myJSON = JSON.stringify(myObj);
    // // localStorage.setItem("RowColumn", myJSON);



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

