


function Cancel (){

    location.replace("index.html");
}



function TypeJobNameReload (){
    document.body.innerHTML =`
    <div id="FileExists" class="alert hidden">
        
        <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
        This file name already exist! Try a new name!
        
    </div> 

    <div id="OpenExcelError" class="alert hidden">
        
        <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
        There is a program dependent document that is currently opened and altered. Save or close this document, then name the file and click OK or press Cancel to quit this process.
        
    </div> 

    <div class="text">
        
            <h1>Name the new data file and click OK or </h1>
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
        <input type="text" class="form-control" placeholder="New Saved File Name" aria-label="New Saved File Name" aria-describedby="button-addon2">
        <div class="input-group-append">
          <!-- <button class="btn btn-outline-secondary" type="button" id="button-addon2" onclick="getTextValue()">OK</button> -->
          <button class="btn btn-outline-secondary" type="button" id="button-addon2" onclick="LSFCheckIfFileNameExists()">OK</button>
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



async function LSFCheckIfFileNameExists(){


    let jobName = document.getElementsByClassName("form-control")[0].value;

    document.getElementsByClassName("form-control")[0].value=''

    
    if (jobName==''){}else{


    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()

    const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, "./js/AddtoTablePromise"));
    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));

    const { AddDataCheckIfExists } = require(path.join(currentWorkingDirectory, "./js/AddDataCheckIfExists"));


    document.getElementsByClassName("input-group")[0].classList.add('hidden');
    document.getElementsByClassName("spinner")[0].classList.remove('hidden');

    let jobName1=jobName.split('.');
    
    
    let jobName0 = jobName1[0];

    let data0=jobName0+".xlsx"

    let data=data0;

    let dataName='SavedFileName';

    let AwaitProveData=data;

    let TableName=''

    let Database=''


    let DoneValue= await AddtoTablePromise(AwaitProveData,data, dataName, TableName,Database)

    // console.log(DoneValue)

    // console.log('DoneValue above')


    let filename='LSFcheckIfFileExistsInLocation.py';

    let callback=AddDataCheckIfExists



    RunPythonFile(filename,callback)



    }


}



