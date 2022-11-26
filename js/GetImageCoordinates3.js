

// function FindJobExcelLocations(){

//   location.replace("FindJobExcelLocations.html");

// }




// function GetImageWithLocations(){
//   // let process = require("process");
  
//   // let path = require("path")

//   // const currentWorkingDirectory=process.cwd()


//   // const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));



//   // let filename = 'PlaceAboutImage.py'

//   // let callback =GetImageCoordinatesImage0


//   // RunPythonFile(filename, callback)


//   GetImageCoordinatesImage0()

// }

// async function GetImageCoordinatesImage0(){


//   let process = require("process");
  
//   let path = require("path")
  
//   const currentWorkingDirectory=process.cwd()
  
  
//   const { getDbDataSimple } = require(path.join(currentWorkingDirectory, './js/getDbDataSimple'));
  
  
//   let AwaitProveData="getting Db Data"
    
//   let TableName=''
    
//   let Database=''
  
//   let DataGotten = await getDbDataSimple(AwaitProveData,TableName,Database) 
  
//   let newFileLocation = DataGotten['LocationToPlaceOnWebPage']

//   // console.log(newFileLocation)

//   // console.log('newFileLocation after function above')

//   // console.log(__dirname)

//   // console.log('__dirname above')


//   CreateImageWithMarkerReturn3(newFileLocation)


// }




// function CreateImageWithMarkerReturn3(newFileLocation){


//   let process = require("process");
  
//   let path = require("path")
  
//   const currentWorkingDirectory=process.cwd()
  
  
//   const { addInforToTheDocumentHTMLcall } = require(path.join(currentWorkingDirectory,"./js/addInforToTheDocumentHTMLcall"));






//   console.log(newFileLocation)

//   console.log("newFileLocation inside new function")

//   document.body.innerHTML = `
  



//     <div class="wrapper scrollON">

//         <img class='ScrollImage' id="DocumentToClick" src="${newFileLocation}" alt="Document Image" >

//     </div>

//     <div class="row col-xs-4"></div>
//         <button type="button" class="btn optionsbtn left btn-secondary" onclick="addInforToTheDocumentHTMLcall()">Description</button>         
//         <button type="button" class="btn optionsbtn right btn-secondary" onclick="Cancel()">OK</button>   
//     </div>


    
  

//     <script>

//         GetImageWithLocations()

//     </script>

//   <script>

//     let path = require("path");
//     let jquerypath = path.join(__dirname, './js/jquery');
//     window.jQuery = window.$ = require(jquerypath);
    
//   </script>

//   <script src="./js/popper.min.js"></script>
//   <script src="./js/bootstrap.min.js"></script>



// `

// }
















function GetImageCoordinates(){

    CreateImageWithMarkerReturn();


};


function FindCoordinateInImage(){

    location.replace("FindCoordinateInImage.html");

};


async function FindCoordinateInImageStep4Antes(){

  const currentWorkingDirectory=process.cwd();

  const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, './js/AddtoTablePromise'));

  let AwaitProveData="starting add to table promise";
  

  let data='false';

  let dataName='SecondGoImageStep4';

  let TableName='';

  let Database='';

  let Done = await AddtoTablePromise(AwaitProveData,data, dataName, TableName,Database);

  // console.log(Done)


  location.replace("FindCoordinateInImageStep4.html");

}


async function RemoveLastAndTryAgain(){

    let process = require("process");
  
    let path = require("path");
  
    const currentWorkingDirectory=process.cwd();



    const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));



    let filename = 'RemoveLastAndTryAgain.py';

    let callback =FindCoordinateInImage;


    RunPythonFile(filename, callback);



  
  
    // const { getDbDataSimple } = require(path.join(currentWorkingDirectory, './js/getDbDataSimple'));

    // const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, './js/AddtoTablePromise'));


    // let AwaitProveData="getting Db Data"
    
    // let TableName=''
    
    // let Database=''
  
    // let DataGotten = await getDbDataSimple(AwaitProveData,TableName,Database) 
  
    // let finalLocationsX0 = DataGotten['finalLocationsX']

    // let finalLocationsY0 = DataGotten['finalLocationsY']

    // console.log(finalLocationsX0)

    // console.log('finalLocationsX0')

    // console.log(finalLocationsY0)

    // console.log('finalLocationsY0')


    

    // let commaReplacemet = '&%#5&&*'


    // let finalLocationsX= await finalLocationsX0.replace(/,\s/g, commaReplacemet).replace(/,/g, commaReplacemet).split(commaReplacemet)

    // let finalLocationsY = await finalLocationsY0.replace(/,\s/g, commaReplacemet).replace(/,/g, commaReplacemet).split(commaReplacemet)


    // console.log(finalLocationsX)

    // console.log('finalLocationsX1')

    // console.log(finalLocationsY)

    // console.log('finalLocationsY1')



    // finalLocationsX.pop();

    // finalLocationsY.pop();

    // console.log(finalLocationsX)

    // console.log('finalLocationsX')

    // console.log(finalLocationsY)

    // console.log('finalLocationsY')



    // AwaitProveData="add to table started"

    // let data = [finalLocationsX, finalLocationsY]
    
    // let dataName = ['finalLocationsX', 'finalLocationsY']
    
    



    // let Done = await AddtoTablePromise(AwaitProveData,data, dataName, TableName,Database)

    // console.log(Done)


    
    
    
    // FindCoordinateInImage()





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
  
  
    // console.log(newFileLocation)
  
    // console.log('newFileLocation above')
  
  
  
    CreateImageWithMarkerReturn2(newFileLocation);
  
  }



function CreateImageWithMarkerReturn2(newFileLocation){

    // console.log(newFileLocation)

    // console.log("newFileLocation inside new function")

    document.body.innerHTML = `
   
    <div class=text>

        <h1>All of the Locations added are shown bellow</h1>
        <h1>if there are still locations to add click</h1>
        <h1>Add More, click Done Adding if you are done,</h1>
        <h1>click Back to fix the last add</h1>
        <h1>or click Cancel to cancel the operation</h1>
       
    </div>

    <form class="needs-validation" novalidate>
  
      <div class= "buttons container-fluid">
        
          <div class= 'row top'>
    
            <div class="col-xs-4"></div>

              <button type="button" class="btn optionsbtn left btn-secondary" onclick="RemoveLastAndTryAgain()" >Back</button>
              <button type="button" class="btn optionsbtn right btn-secondary"onclick="FindCoordinateInImage()">Add More</button>   

            </div>
    
          <div class="row bottom">
    
            <div class="col-xs-4"></div>

              <button type="button" class="btn optionsbtn left btn-secondary" onclick="Cancel()">Cancel</button>              
              <button type="button" class="btn optionsbtn right btn-secondary" onclick="FindCoordinateInImageStep4Antes()">Done Adding</button> 

            </div>
        
          </div>
          
        </div>  

    </form>
     
    </div>

      <div class="wrapper scrollON">

          <img class='ScrollImage' id="DocumentToClick" src="${newFileLocation}" alt="Document Image" >

      </div>

      <script>

          GetImageCoordinates()

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
















function GetImageCoordinatesImage(){


  CreateImageWithMarkerReturnImage();

  
};





async function CreateImageWithMarkerReturnImage(){
  let process = require("process");

  let path = require("path");

  const currentWorkingDirectory=process.cwd();


  const { getDbDataSimple } = require(path.join(currentWorkingDirectory, './js/getDbDataSimple'));


  let AwaitProveData="getting Db Data";
  
  let TableName='';
  
  let Database='';

  let DataGotten = await getDbDataSimple(AwaitProveData,TableName,Database);

  let datafillName = await DataGotten['datafillName'];


  let newFileLocation = await DataGotten['newFileLocation'];


  let KeyName = 'Key_' + datafillName;


  TableName = KeyName;


  // let DataGotten2 = await getDbDataSimple(AwaitProveData,TableName,Database) 


  // console.log(newFileLocation)

  // console.log('newFileLocation above')



  CreateImageWithMarkerReturnImage2(newFileLocation);

};



function CreateImageWithMarkerReturnImage2(newFileLocation){

  // console.log(newFileLocation)

  // console.log("newFileLocation inside new function")

  document.body.innerHTML = `
 
  <div class=text>

      <h1>All of the Locations added are shown bellow</h1>
      <h1>if there are still locations to add click</h1>
      <h1>Add More, click Done Adding if you are done,</h1>
      <h1>click Back to fix the last add</h1>
      <h1>or click Cancel to cancel the operation</h1>
     
  </div>

  <form class="needs-validation" novalidate>

    <div class= "buttons container-fluid">
      
        <div class= 'row top'>
  
          <div class="col-xs-4"></div>

            <button type="button" class="btn optionsbtn left btn-secondary" onclick="RemoveLastAndTryAgain()" >Back</button>
            <button type="button" class="btn optionsbtn right btn-secondary"onclick="FindCoordinateInImage()">Add More</button>   

          </div>
  
        <div class="row bottom">
  
          <div class="col-xs-4"></div>

            <button type="button" class="btn optionsbtn left btn-secondary" onclick="Cancel()">Cancel</button>              
            <button type="button" class="btn optionsbtn right btn-secondary" onclick="FindCoordinateInImageStep4Antes()">Done Adding</button> 

          </div>
      
        </div>
        
      </div>  

  </form>
   
  </div>

    <div class="wrapper scrollON">

        <img class='ScrollImage' id="DocumentToClick" src="${newFileLocation}" alt="Document Image" >

    </div>

    <script>

        GetImageCoordinates()

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




