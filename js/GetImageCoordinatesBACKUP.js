


function FindCoordinateInImageStep2(){

  location.replace("FindCoordinateInImageStep2.html");

};



function GetImageCoordinates(){

  GetImageCoordinates1();

};

async function GetImageCoordinates1(){

  let process = require("process");
  
  let path = require("path");

  const currentWorkingDirectory=process.cwd();


  const { getDbDataSimple } = require(path.join(currentWorkingDirectory, './js/getDbDataSimple'));

  const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, './js/AddtoTablePromise'));

  const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));

  // RunPythonFile



  // AddtoTablePromise


  let AwaitProveData="getting Db Data";
  
  let TableName='';
  
  let Database='';

  let DataGotten = await getDbDataSimple(AwaitProveData,TableName,Database);

  let newFileLocationImg = await DataGotten['newFileLocationImg'];

  let newFileLocatiOpt = await DataGotten['newFileLocation'];

  let fileNameOnly = await DataGotten['fileNameOnly'];



  let PDFfile = await DataGotten['PDFfile'];

  let newFileLocation;

  if (PDFfile == 'true'){

    newFileLocation = newFileLocationImg;


    }else if (PDFfile == 'false'){

      newFileLocation = newFileLocatiOpt;


    }else{

      // console.log("something is wrong it can only be pdf can be true or false")

      newFileLocation = 'Error';
    };



  


  // console.log(newFileLocation)

  // console.log('newFileLocation above')



  let newFileLocation0=newFileLocation.split("\\");

  let newFileLocation1= await newFileLocation0[newFileLocation0.length-1];



  // let newFileLocation1=fileNameOnly;    // test, block after


  // console.log(newFileLocation1)

  // console.log('newFileLocation1 above')

  let imageFolderLocation='_clientImageFiles\\';

  
  let LocationToPlaceOnWebPage=imageFolderLocation+newFileLocation1;

  // console.log(LocationToPlaceOnWebPage)

  // console.log('LocationToPlaceOnWebPage above')

  // console.log(currentWorkingDirectory)

  // console.log('currentWorkingDirectory')


  let LocationToAddFileOnApp = currentWorkingDirectory +'\\'+LocationToPlaceOnWebPage;


  // console.log(LocationToPlaceOnWebPage)

  // console.log('LocationToPlaceOnWebPage above')

  // console.log(LocationToAddFileOnApp)

  // console.log('LocationToAddFileOnApp above')



  AwaitProveData = 'Adding image locations to database';

  let data = [LocationToPlaceOnWebPage, LocationToAddFileOnApp];

  // let dataName = ['OriginalImageLocation', 'LocationToAddFileOnApp']

  let dataName = ['LocationToPlaceOnWebPage', 'LocationToAddFileOnApp'];






  let Done = await AddtoTablePromise(AwaitProveData,data, dataName, TableName,Database);

  // console.log(Done)

  // console.log('LocationToAddFileOnApp')

  let filename = 'copyImageToAppFolder.py';

  let callback =GetImageCoordinates1Return;


  RunPythonFile(filename, callback);




};


async function GetImageCoordinates1Return(results){

  // console.log(results)

  let process = require("process");
  
  let path = require("path");

  const currentWorkingDirectory=process.cwd();


  const { getDbDataSimple } = require(path.join(currentWorkingDirectory, './js/getDbDataSimple'));


  let AwaitProveData = 'starting to get newlocationData';
  
  let TableName = '';
  
  let Database = '';


  let DataGotten = await getDbDataSimple(AwaitProveData,TableName,Database);

  let newFileLocation = await DataGotten['LocationToPlaceOnWebPage'];   
  
  

  

  // console.log(newFileLocation)

  // console.log('location to place on web page above')


  GetImageCoordinates2(newFileLocation);



};



function GetImageCoordinates2(newFileLocation){

  // console.log(newFileLocation)

  // console.log('newFileLocation in GetImageCoordinates2 function above')

  document.body.innerHTML = `
  <div class=text>

      <h1>Click the location in the image bellow</h1>
      <h1>where you want to place text</h1>

  </div>


  </div>

    <div class="wrapper scrollON">

        <img class='ScrollImage' id="DocumentToClick" src="${newFileLocation}" alt="Document Image" >

    </div>

  <script>

    let path = require("path");
    let jquerypath = path.join(__dirname, './js/jquery');
    window.jQuery = window.$ = require(jquerypath);
    
  </script>

  <script src="./js/popper.min.js"></script>
  <script src="./js/bootstrap.min.js"></script>

  `;


  GetImageCoordinates3();


};



function GetImageCoordinates3(){


    document.getElementById('DocumentToClick').addEventListener('click', function (event) {
        
        bounds=this.getBoundingClientRect();
        let left=bounds.left;
        let top=bounds.top;
        let x = event.pageX - left;
        let y = event.pageY - top;
        let cw=this.clientWidth;
        let ch=this.clientHeight;
        let iw=this.naturalWidth;
        let ih=this.naturalHeight;
        let px=x/cw*iw;
        let py=y/ch*ih;
        // console.log("click on "+this.tagName+" at pixel ("+px+","+py+") mouse pos ("+x+"," + y+ ") relative to boundingClientRect at ("+left+","+top+") client image size: "+cw+" x "+ch+" natural image size: "+iw+" x "+ih );

        let ImgPosition=[Math.round(px),Math.round(py)];

        // console.log(ImgPosition)

        // console.log('ImgPosition above')

        GetImageCoordinatesAfter(ImgPosition);
      });
};


async function GetImageCoordinatesAfter(ImgPosition){

  

  let process = require("process");

  let path = require("path");

  const currentWorkingDirectory=process.cwd();


  // const { getDbData } = require(path.join(currentWorkingDirectory, './js/getDbData'));

  const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, "./js/AddtoTablePromise"));
  const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));


  // let folder="_clientImageFiles/"

  // let data=[String(ImgPosition), folder+'TestImageFile.jpg' ];

  let data=String(ImgPosition);

  let dataName='ImgPosition';

  // let dataName=['ImgPosition', 'OriginalImageLocation' ];


  let AwaitProveData=data;

  let TableName='';

  let Database='';

  // console.log(data);
  // console.log("before first AddToTable");


  let DoneValue = await AddtoTablePromise(AwaitProveData,data, dataName, TableName,Database);

  // console.log(DoneValue)

  // console.log('DoneValue above')

  

  let filename="CreateImageWithMarker.py";

  let callback=FindCoordinateInImageStep2;


  RunPythonFile(filename,callback);

};


// async function CreateImageWithMarkerReturn(){
//   let process = require("process");

//   let path = require("path")

//   const currentWorkingDirectory=process.cwd()


//   const { getDbDataSimple } = require(path.join(currentWorkingDirectory, './js/getDbDataSimple'));


//   let AwaitProveData="getting Db Data"
  
//   let TableName=''
  
//   let Database=''

//   let DataGotten = await getDbDataSimple(AwaitProveData,TableName,Database) 

//   let newFileLocation = DataGotten['newFileLocation']

//   CreateImageWithMarkerReturn2(newFileLocation)

// }

// function CreateImageWithMarkerReturn2(newFileLocation){
    

//     document.body.innerHTML = `
    
//     <div class=text>

//         <h1>Click the location in the image bellow</h1>
//         <h1>where you want to place text</h1>
//         <h1>and press OK to continue or press Cancel </h1>
//         <h1>to cancel the operation</h1>

//     </div>


//   <form class="needs-validation" novalidate>
 

//     <div class= "buttons container-fluid">
      
//       <div class="row bottom">

//         <div class="col-xs-4"></div>
//           <button type="button" class="btn optionsbtn left btn-secondary" onclick="Cancel()">Cancel</button>
//           <button id="waitFunction" type="button" class="btn optionsbtn right btn-secondary" onclick="checkIfAllInputsFilled()">OK</button>   
//         </div>
      
//       </div>
      
//     </div>  

//   </form>

//   </div>

//     <div class="wrapper scrollON">

//         <img class='ScrollImage' id="DocumentToClick" src= ${newFileLocation} alt="Document Image" >

//     </div>

//     <script>

//         GetImageCoordinates()

//     </script>

//   <script>

//     let path = require("path");
//     let jquerypath = path.join(__dirname, './js/jquery');
//     window.jQuery = window.$ = require(jquerypath);
    
//   </script>

//   <script src="./js/popper.min.js"></script>
//   <script src="./js/bootstrap.min.js"></script>
  
  
//     `


// }




