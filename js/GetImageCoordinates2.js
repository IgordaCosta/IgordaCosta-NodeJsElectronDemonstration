


function FindCoordinateInImageStep2(){

  location.replace("FindCoordinateInImageStep2.html");

};

function FindCoordinateInImage(){

    location.replace("FindCoordinateInImage.html");

};



function GetImageCoordinates2(){

    CreateImageWithMarkerReturn();

};



function FindCoordinateInImageStep3(){

  location.replace("FindCoordinateInImageStep3.html");


};





async function CreateImageWithMarkerReturn(){
  let process = require("process");

  let path = require("path");

  const currentWorkingDirectory=process.cwd();


  const { getDbDataSimple } = require(path.join(currentWorkingDirectory, './js/getDbDataSimple'));


  let AwaitProveData="getting Db Data";
  
  let TableName='';
  
  let Database='';

  let DataGotten = await getDbDataSimple(AwaitProveData,TableName,Database);

  let newFileLocation = await DataGotten['LocationToPlaceOnWebPage'];

  













  CreateImageWithMarkerReturn2(newFileLocation);

}


function CreateImageWithMarkerReturn2(newFileLocation){



    document.body.innerHTML = `
    <div class=text>

      <h1>If the new location shown is correct press Next</h1>
      <h1>if it is not press Back to fix it</h1>
      <h1>or press Cancel to cancel the operation </h1>
      
  </div>

  <form class="needs-validation" novalidate>

    <div class= "buttons container-fluid">
       
        <div class= 'row top'>
  
          <div class="col-xs-4"></div>
            
            <button type="button" class="btn optionsbtn left btn-secondary" onclick="FindCoordinateInImage()" >Back</button>
            <button type="button" class="btn optionsbtn right btn-secondary"onclick="GetImageCoordinatesNext()">Next</button>   
          </div>
  
        <div class="row bottom">
  
          <div class="col-xs-4"></div>
            <button type="button" class="btn optionsbtn left btn-secondary" onclick="Cancel()">Cancel</button>
            
          </div>
        
        </div>
        
      </div>  

  </form>

    
  </div>

    <div class="wrapper scrollON">

        <img class='ScrollImage' id="DocumentToClick" src="${newFileLocation}" alt="Document Image" >

    </div>

    <script>

        GetImageCoordinates2()

    </script>

  <script>AddJqueryToHtml()</script>
  <script src="./js/popper.min.js"></script>
  <script src="./js/bootstrap.min.js"></script>

  `;

};

function PutListDataIntoImage(){

  let process = require("process");

  let path = require("path");

  const currentWorkingDirectory=process.cwd();


  const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));


  let filename = 'PutListDataIntoImage.py';
  
  let callback = FindCoordinateInImageStep3;

  RunPythonFile(filename, callback);



};



async function GetImageCoordinatesNext(){

  console.log(`Done Test Run!`)

};




