

async function CreateImageWithMarkerReturnPart2(){

  let process = require("process");

  let path = require("path");

  const currentWorkingDirectory = process.cwd();


  const { getDbDataSimple } = require(path.join(currentWorkingDirectory, './js/getDbDataSimple'));

  const { CreateImageWithMarkerReturn2 } = require(path.join(currentWorkingDirectory, "./js/CreateImageWithMarkerReturn2"));

  let AwaitProveData = "getting Db Data";

  let TableName = '';

  let Database = '';

  let DataGotten = await getDbDataSimple(AwaitProveData, TableName, Database);

  let newFileLocation = await DataGotten['LocationToPlaceOnWebPage'];    // for viewing images its relatvive location
                                                                        // for placing images its full location


  // LocationToAddFileOnApp

  let FontSize;

  try{
        FontSize = await DataGotten['FontSizeShow'];
        
    }catch{};


  if (String(FontSize) == 'undefined'){
    FontSize = 30;

    CreateImageWithMarkerReturn2(newFileLocation, FontSize);

  }else{

    CreateImageWithMarkerReturn2(newFileLocation, FontSize);
  }


}


function CreateImageWithMarkerReturn() {
  let process = require("process");

  let path = require("path");

  const currentWorkingDirectory = process.cwd();
  
  const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));


  // let filename = 'copyImageToAppFolder.py';


  // for add to database in the last section where the user
  // checks and chnges fornts, this part only copies the image to
  // the view it does not show the marked defalut look location
  // this can be changed by switing the function to the
  // putlistdataimagewithfontsize one
  
  // it is only possed to switch ending here
  // the firle should remain the original one
  // it seems like it in not only switching ending
  // but also chaging the files for another version
  // changing the beollow fixed the addTOdatabse Error
  // check if it altered other aread then adapt

//   let filename = 'copyImageToAppFolderSwitchEndingOnly.py';
  
//   let callback =CreateImageWithMarkerReturnPart2;

//   console.log('ran up to CreateImageWithMarkerReturnPart2')

//   RunPythonFile(filename, callback,gotResultsFuction=false)
// // // // // ====================================================================

//swtiched to the bellow to test the theory above
// the default copyImageToAppFolder in putlistdataintoimage already changes the filename
CreateImageWithMarkerReturnPart2()

}


exports.CreateImageWithMarkerReturn = CreateImageWithMarkerReturn;
