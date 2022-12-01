


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

  let AwaitProveData="getting Db Data";
  
  let TableName='';
  
  let Database='';

  let DataGotten = await getDbDataSimple(AwaitProveData,TableName,Database);

  let newFileLocationImg = await DataGotten['newFileLocationImg'];

  let newFileLocatiOpt = await DataGotten['newFileLocation'];

  let fileNameOnly = await DataGotten['fileNameOnly'];

  let imageFolderLocation =   await DataGotten['imageFolderLocation'];

  let PDFfile =   await DataGotten['PDFfile'];

  if (PDFfile == 'true'){
    newFileLocation = newFileLocationImg;

    }else if (PDFfile == 'false'){
      newFileLocation = newFileLocatiOpt;

    }else{
      newFileLocation = 'Error';

    };

  
  let newFileLocation0=newFileLocation.split("\\");

  let newFileLocation1= await newFileLocation0[newFileLocation0.length-1];

  
  
  let LocationToPlaceOnWebPage = imageFolderLocation + '\\' + newFileLocation1;

  let LocationToAddFileOnApp = currentWorkingDirectory +'\\' +LocationToPlaceOnWebPage;

  AwaitProveData = 'Adding image locations to database';



  let data = [LocationToPlaceOnWebPage, LocationToAddFileOnApp, imageFolderLocation];

  let dataName = ['LocationToPlaceOnWebPage', 'LocationToAddFileOnApp', `imageFolderLocation`];

  let Done = await AddtoTablePromise(AwaitProveData,data, dataName, TableName,Database);


  let filename = 'copyImageToAppFolder.py';

  let callback =GetImageCoordinates1Return;

  RunPythonFile(filename, callback);

};

async function GetImageCoordinates1Return(results){

  let process = require("process");
  
  let path = require("path");

  const currentWorkingDirectory=process.cwd();

  const { getDbDataSimple } = require(path.join(currentWorkingDirectory, './js/getDbDataSimple'));

  let AwaitProveData = 'starting to get newlocationData';
  
  let TableName = '';
  
  let Database = '';

  let DataGotten = await getDbDataSimple(AwaitProveData,TableName,Database);

  let newFileLocation = await DataGotten['LocationToPlaceOnWebPage'];   

  GetImageCoordinates2(newFileLocation);

};


function GetImageCoordinates2(newFileLocation){

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

        let ImgPosition=[Math.round(px),Math.round(py)];

        GetImageCoordinatesAfter(ImgPosition);
      });
};


async function GetImageCoordinatesAfter(ImgPosition){

  let process = require("process");

  let path = require("path");

  const currentWorkingDirectory=process.cwd();

  const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, "./js/AddtoTablePromise"));
  const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));

  let data=String(ImgPosition);

  let dataName='ImgPosition';

  let AwaitProveData=data;

  let TableName='';

  let Database='';

  let DoneValue = await AddtoTablePromise(AwaitProveData,data, dataName, TableName,Database);

  let filename="CreateImageWithMarker.py";

  let callback=FindCoordinateInImageStep2;

  RunPythonFile(filename,callback);

};


