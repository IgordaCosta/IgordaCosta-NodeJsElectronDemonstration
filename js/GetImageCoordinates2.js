// const { callbackify } = require("util");
// const { AddTwoDataToListsSave } = require("./AddTwoDataToListsSave");



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

  
  // let newFileLocation2 = DataGotten['asdfasdfasdfsdf']

    // console.log(newFileLocation2)

    // console.log(newFileLocation2==undefined)

    // console.log("wrong table data above")





  // console.log(newFileLocation)

  // console.log('newFileLocation above')

  // console.log('this is the location of the image file that will show above')



  CreateImageWithMarkerReturn2(newFileLocation);

}


function CreateImageWithMarkerReturn2(newFileLocation){

    // console.log(newFileLocation)

    // console.log("newFileLocation inside new function")

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

  <script>

    let path = require("path");
    let jquerypath = path.join(__dirname, './js/jquery');
    window.jQuery = window.$ = require(jquerypath);
    
  </script>

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

  let process = require("process");

  let path = require("path");

  const currentWorkingDirectory=process.cwd();



  const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));


  let filename = 'getFinalLocationItens.py';
  
  // let callback = PutListDataIntoImage


  let callback = FindCoordinateInImageStep3;



  RunPythonFile(filename, callback);


  // FindCoordinateInImageStep3()







  // // const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, './js/AddtoTablePromise'));

  // const { getDbDataSimple } = require(path.join(currentWorkingDirectory, './js/getDbDataSimple'));

  // const { AddTwoDataToListsSave } = require(path.join(currentWorkingDirectory, './js/AddTwoDataToListsSave'));


  // let AwaitProveData="getting Db Data"
  
  // let TableName=''
  
  // let Database=''

  // let DataGotten = await getDbDataSimple(AwaitProveData,TableName,Database) 

  

  
  // let lastTempLocationPointX = DataGotten['lastTempLocationPointX']

  // let lastTempLocationPointY = DataGotten['lastTempLocationPointY']



  // let finalLocationsX = DataGotten['finalLocationsX']



  // let finalLocationsX0 = String(finalLocationsX)


  // if (finalLocationsX0=='undefined'){

  //   finalLocationsX=[]

  //   let finalLocationsY=[]


  //   let ListA = finalLocationsX

  //   let ListB = finalLocationsY

  //   let DataA = lastTempLocationPointX

  //   let DataB = lastTempLocationPointY

  //   // let callback = PutListDataIntoImage


  //   DoneOutput = await AddTwoDataToListsSave(ListA,ListB,DataA,DataB)

  //   console.log(DoneOutput)


  //   PutListDataIntoImage()

  // }else{

  //   let finalLocationsY = DataGotten['finalLocationsY']

  //   let ListA = finalLocationsX

  //   let ListB = finalLocationsY

  //   let DataA = lastTempLocationPointX

  //   let DataB = lastTempLocationPointY

  //   // let callback = PutListDataIntoImage


  //   DoneOutput = await AddTwoDataToListsSave(ListA,ListB,DataA,DataB)

  //   console.log(DoneOutput)
    

    // PutListDataIntoImage()

    


  // }





  // finalLocationsX.push(lastTempLocationPointX);

  // finalLocationsY.push(lastTempLocationPointY);


  // AwaitProveData='add table started'
  
  // data=[finalLocationsX, finalLocationsY]
  
  // dataName=['finalLocationsX', 'finalLocationsY']
  
  // TableName=''
  
  // Database=''
  

  // let Done = await AddtoTablePromise(AwaitProveData,data, dataName, TableName,Database)


  // console.log(Done)


  // console.log("GetImageCoordinatesNext function finished")

  // FindCoordinateInImageStep3()





};




