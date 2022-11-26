



// function BackToIndex (){

// const { gotResults } = require("./gotResults");

//     location.replace("index.html");
// }

function OperationComplete(){

    location.replace("OperationComplete.html");
    
}


async function getAllFilledInputs(){

    // return new Promise((resolve,_reject) =>{

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()

    const { gotResults } = require(path.join(currentWorkingDirectory, "./js/gotResults"));

    const { getDbDataSimple } = require(path.join(currentWorkingDirectory, "./js/getDbDataSimple"));

    const { AddToTable } = require(path.join(currentWorkingDirectory, "./js/AddToTable"));

    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));


    
    

    let anydata="it has started"


    let tableName=''
    
    let Database=''


    objToCheck= await getDbDataSimple(anydata,tableName,Database)

    console.log(objToCheck)

    console.log('objToCheck above')

    // const { gotResults } = require("./js/gotResults");


    // text = localStorage.getItem("RowColumn");
    // obj = JSON.parse(text);

    NumList=objToCheck.NumList

    console.log(NumList)

    console.log('NumList above')

    NumList=parseInt(NumList)

    let valuesList=[];
    let i;
    // let MissingValues=false;
    let MissingValuesList=[]

    for (i = 0; i < NumList; i++) {
   
        valuegotten=document.getElementById("validationTooltip0"+i).value;

        console.log(valuegotten);

        console.log('valuegotten above');

        valuesList.push(valuegotten)
        if (valuegotten==''){

            // MissingValues=true;
            MissingValuesList.push(true)
        }else{

            MissingValuesList.push(false)
        }

    } 

    



    console.log(MissingValuesList)

    console.log('MissingValuesList above')

    let MissingValues=MissingValuesList.includes(true)


    console.log(MissingValues)

    console.log('MissingValues? above')


    if (MissingValues==true){

        console.log("stay on page and show warning message");

        document.getElementById("waitFunction").classList.remove('hidden')
       let alertDiv= `
        <div id= "identifiersMissingAlert" class="alert alert-dismissible">
            <button type="button" class="close" data-dismiss="alert">&times;</button>
            There are Identifiers missing! All Identifiers must be filled!
        </div> 
        `
        let d1 = document.getElementById('MissingData');
        d1.insertAdjacentHTML('afterbegin', alertDiv);

        // document.getElementById("MissingData").appendChild(node);

        // document.getElementById("MissingData").classList.remove('hidden');

    }else{

        // add 1_ 2_ ... in front fo each clumn data value

        console.log(valuesList)

        console.log('valuesList above')

        // let newValuesList=[]

        // for (i=0; i < valuesList.length ; i++){

        //     let step=String(i+1)+"_"+valuesList[i]

        //     newValuesList.push(step)


        // }

        // console.log(newValuesList)

        // console.log('newValuesList above')

        let awaitProvedata="it has started"

        let data=String(valuesList)

        let dataName='AddToTablevaluesList'


        AddToTable(awaitProvedata,data,dataName,tableName,Database)

        console.log("go to the processing page and continue the program");


        gotResults()




        filename= "clickedAddFile.py"

        callback=clickedAddFile

        RunPythonFile(filename,callback)



        // clickedAddFile(valuesList)



    }


    

    }

//     )
// }

// function addInfoToTheDocumentHtmltemplate(){


    
//     document.body.innerHTML =`<div id="MissingData" class="alert hidden">
          
//     <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
//     There are Identifiers missing! All Identifiers must be filled!
    
//   </div>


//   <div class=text>

//       <h1>Fill the Identifier column with information</h1>
//       <h1>and press OK to continue or press Cancel </h1>
//       <h1>to cancel the operation</h1>

//   </div>

//   <div id="foreGroundImage" class="containingArea centered MainLogo ">

//     <img src="_images/LogInImg.png" onclick="hideImage()" alt="MainLogo" >

// </div>

// <form class="needs-validation" novalidate>

//   <div class="screen parentofOverflow">

//       <div class="container-fluid topPartSize scrolloff">

//         <!-- <div id="foreGroundImage" class="containingArea centered MainLogo ">

//             <img src="_images/LogInImg.png" onclick="hideImage()" alt="MainLogo" >

//         </div> -->
//         <div class="content-wrapper">
          
//             <table id= "table" class="table table-dark table-striped scrollableArea" onclick="UnhideScroll()">
//               <thead>
//                 <tr>
//                   <th scope="col">#</th>
//                   <th scope="col">Row Position</th>
//                   <th scope="col">Column Position</th>
//                   <th scope="col">Identifier</th>
                                      
//                 </tr>
//               </thead >
//               <tbody id="tableData">

//                 <script>getRowColumnData();</script>  
                
//               </tbody>
              
//             </table>
          
//         </div>
//       </div>                   
//   </div>

//   <div class= "buttons container-fluid">
    
//     <div class="row bottom">

//       <div class="col-xs-4"></div>
//         <button type="button" class="btn optionsbtn left btn-secondary" onclick="Cancel()">Cancel</button>
//         <button type="button" class="btn optionsbtn right btn-secondary" onclick="checkIfAllInputsFilled()">OK</button>   
//       </div>
    
      
//     </div>
    
//   </div>  

// </form>

//   <!-- <div class= "buttons container-fluid">
    
//     <div class="row bottom">

//       <div class="col-xs-4"></div>
//         <button type="button" class="btn optionsbtn left btn-secondary" onclick="Cancel()">Cancel</button>
//         <button type="button" class="btn optionsbtn right btn-secondary" onclick="">OK</button>   
//       </div>
    
      
//     </div>
    
//   </div>   -->
// </div>
// <script>

//   let path = require("path");
//   let jquerypath = path.join(__dirname, './js/jquery');
//   window.jQuery = window.$ = require(jquerypath);
  
// </script>

// <script src="./js/popper.min.js"></script>
// <script src="./js/bootstrap.min.js"></script>`
// }






function checkIfAllInputsFilled(){

    // var process = require("process");

    // var path = require("path")

    // const currentWorkingDirectory=process.cwd()

    // const { gotResults } = require(path.join(currentWorkingDirectory, "./js/gotResults"));


    // gotResults()

    // addInfoToTheDocumentHtmltemplate()

    // const { getDbDataSimple } = require(path.join(currentWorkingDirectory, "./js/getDbDataSimple"));

    // let anydata="it has started"


    // let tableName=''
    
    // let Database=''



    // objToCheck= getDbDataSimple(anydata,tableName,Database)

    // // const { gotResults } = require("./js/gotResults");


    // // text = localStorage.getItem("RowColumn");
    // // obj = JSON.parse(text);

    // NumList=objToCheck.NumList

    // console.log(NumList)

    // console.log('NumList above')

    // NumList=parseInt(NumList)

    // let valuesList=[];
    // let i;
    // let MissingValues=false;

    // for (i = 0; i < NumList; i++) {
   
    //     valuegotten=document.getElementById("validationTooltip0"+i).value;

    //     // console.log(valuegotten);

    //     valuesList.push(valuegotten)
    //     if (valuegotten==''){

    //         MissingValues=true;
    //     }

    // } 

    // console.log('valuesList=',valuesList);
    // console.log('MissingValues=',MissingValues)

    // MissingValues = getAllFilledInputs()


    document.getElementById("waitFunction").classList.add('hidden')


    // let HasClassHidden=document.getElementById("MissingData").classList.contains('hidden')

    // console.log(HasClassHidden)

    // console.log('HasClassHidden above')

    // if (HasClassHidden==true){}else{

    //     // document.getElementById("MissingData").classList.add('hidden')

    // }

    let AlertExists = document.getElementById("identifiersMissingAlert");
    if(AlertExists){

        let element = document.getElementById('identifiersMissingAlert');
        element.parentNode.removeChild(element);

    }else{}


    getAllFilledInputs()

    // console.log(MissingValues)

    // console.log('MissingValues true above')



    // if (MissingValues==true){

    //     // console.log("stay on page and show warning message");

    //     document.getElementById("MissingData").classList.remove('hidden');

    // }else{

    //     // console.log("go to the processing page and continue the program");

    //     gotResults()

    //     // clickedAddFile(valuesList)



    // }

    
    

}


// function clickedAddFile(valuesList){
function clickedAddFile(){


    // filename= "clickedAddFile.py"

    // // console.log("started runReturnFromSameFileInside function before");
    
    // // logger=loghere();

    // // console.log("started runReturnFromSameFileInside function after");

    // let path = require("path");

    // let filenamecheck=path.basename(__dirname);
    // // console.log(filenamecheck);
    // // console.log("filename check above");

    // // console.log(fileLocation);
    // // console.log('fileLocation above')

    // if (filenamecheck=="CSSAutoFormFiller"){}else{
    //     __dirname = path.join(__dirname, '../../../../../../');

    // }
    
    // // console.log(__dirname)
    // // console.log("__dirname")
    // // let filenameUsed;
    // // filenameUsed=require('path').dirname(require.main.filename);

    // // console.log(filenameUsed);
    // // console.log('filenameUsed above');
    

    // let {PythonShell} = require("python-shell");

    // let opcoes = {
    //     scriptPath : path.join(__dirname, './_engine/'),
    //     pythonPath: 'C:\\ProgramData\\Anaconda3\\python',
    //     args : [valuesList]
    // };

    // // console.log(path.join(__dirname, './_engine/'));
    // // console.log("startprint");
    // PythonShell.run(filename, opcoes, function (err, results) {
    //     if (err) throw err;

        // console.log(results);

        // logger.info(results);
        

        // BackToIndex()
        
        OperationComplete()

    // }
    // )
}    

