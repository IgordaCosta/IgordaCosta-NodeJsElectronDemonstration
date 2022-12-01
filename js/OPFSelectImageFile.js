

function FindCoordinateInImageStep4(){

    location.replace("FindCoordinateInImageStep4.html");

}


async function OPFSelectImageFile(){

  let process = require("process");

  let path = require("path");

  const currentWorkingDirectory = process.cwd();


  const { getDbDataSimple } = require(path.join(currentWorkingDirectory, './js/getDbDataSimple'));

  let AwaitProveData = 'getting tableData'

  let TableName = ''

  let Database = ''

  let DataGotten= await getDbDataSimple(AwaitProveData,TableName,Database);


  let PDFfile =  await DataGotten['PDFfile'];

  if (PDFfile=='true'){

    const { OPFSelectImageFile3 } = require(path.join(currentWorkingDirectory, './js/OPFSelectImageFile3'));


    OPFSelectImageFile3()

  }else if (PDFfile=='false'){

    OPFSelectImageFile2()

  }else{

  }




    

}


async function ChoosenImage(IdChoosen){

  let process = require("process");

  let path = require("path");

  const currentWorkingDirectory = process.cwd();


  const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, "./js/AddtoTablePromise"));

  const { getDbDataSimple } = require(path.join(currentWorkingDirectory, './js/getDbDataSimple'));

  const { DragnDropMid0 } = require(path.join(currentWorkingDirectory, './js/DragnDropMid0'));


  let node = document.getElementById(IdChoosen);
  let ImageName  = node.textContent || node.innerText;


  textToRemove='Click to select '

  clickedImageName=ImageName.replace(textToRemove,'')


  let AwaitProveData = 'getting tableData'

  let TableName = ''

  let Database = ''

  let DataGotten= await getDbDataSimple(AwaitProveData,TableName,Database);

  let FolderImageSaveLocation = await DataGotten['FolderImageSaveLocation'];



  let pathUsed = FolderImageSaveLocation + clickedImageName 
  


  let data = 'true';

  let dataName = 'PDFfile';

  AwaitProveData = "changing PDFfile to true";

  let Done = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);




  DragnDropMid0(pathUsed)


  







}


function OPFSelectImageFile2(){

  let process = require("process");

  let path = require("path");

  const currentWorkingDirectory = process.cwd();


  const { OPFSelectImageFile3 } = require(path.join(currentWorkingDirectory, './js/OPFSelectImageFile3'));



  const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));


  let filename='OPFSelectImageFileTitleAndData.py'
  
  let callback=OPFSelectImageFile3
  
  
  RunPythonFile(filename, callback, gotResultsFuction=false)







  

}


function PutListDataIntoImageWithFontSizeStep5(){

  let process = require("process");

  let path = require("path");

  const currentWorkingDirectory = process.cwd();

  const { CreateImageWithMarkerStep5Return } = require(path.join(currentWorkingDirectory, './js/CreateImageWithMarkerStep5Return'));



  const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));

  let filename='PutListDataIntoImageWithFontSizeStep5.py'
  
  let callback=CreateImageWithMarkerStep5Return
  
  
  RunPythonFile(filename, callback, gotResultsFuction=false)


}








