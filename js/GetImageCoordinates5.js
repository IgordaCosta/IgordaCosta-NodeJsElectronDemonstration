

function FindCoordinateInImageStep4(){

    location.replace("FindCoordinateInImageStep4.html");

}


function GetImageCoordinates5(){

    PreCreateImageWithMarkerStep5Return()

}


function PreCreateImageWithMarkerStep5Return(){

  let process = require("process");

  let path = require("path");

  const currentWorkingDirectory = process.cwd();

  // const { fontSelect } = require(path.join(currentWorkingDirectory, './js/fontSelect'));
  // const { CreateImageWithMarkerStep5Return } = require(path.join(currentWorkingDirectory, './js/CreateImageWithMarkerStep5Return'));



  const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));


  let filename='GetTitleAndDataForSingleRowTable.py'
  
  let callback=PutListDataIntoImageWithFontSizeStep5
  
  
  RunPythonFile(filename, callback, gotResultsFuction=false)



  // PutListDataIntoImageWithFontSizeStep5




  

}


function PutListDataIntoImageWithFontSizeStep5(){

  let process = require("process");

  let path = require("path");

  const currentWorkingDirectory = process.cwd();

  // const { fontSelect } = require(path.join(currentWorkingDirectory, './js/fontSelect'));
  const { CreateImageWithMarkerStep5Return } = require(path.join(currentWorkingDirectory, './js/CreateImageWithMarkerStep5Return'));



  const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));

  let filename='PutListDataIntoImageWithFontSizeStep5.py'
  
  let callback=CreateImageWithMarkerStep5Return
  
  
  RunPythonFile(filename, callback, gotResultsFuction=false)


}








