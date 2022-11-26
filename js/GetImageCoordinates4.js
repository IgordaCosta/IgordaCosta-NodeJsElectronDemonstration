

async function FindCoordinateInImageStep4(){
    var process = require("process");

    var path = require("path")
    
    const currentWorkingDirectory = process.cwd();

    const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, './js/AddtoTablePromise'));

    let AwaitProveData="starting add to table promise"
    

    let data='true';

    let dataName='SecondGoImageStep4';

    let TableName='';

    let Database='';

    let Done = await AddtoTablePromise(AwaitProveData,data, dataName, TableName,Database)

    // console.log(Done)

    location.replace("FindCoordinateInImageStep4.html");

}

function FindCoordinateInImageStep5(){

  StayScreen = false

  JustChange(StayScreen)


}

function FindCoordinateInImageStep5GO(){

  location.replace("FindCoordinateInImageStep5.html");

}


function GetImageCoordinates4(){

  let process = require("process");

  let path = require("path");

  const currentWorkingDirectory = process.cwd();

  // const { fontSelect } = require(path.join(currentWorkingDirectory, './js/fontSelect'));
  const { CreateImageWithMarkerReturn } = require(path.join(currentWorkingDirectory, './js/CreateImageWithMarkerReturn'));
  const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));


  
  // let filename2='copyBlankToTempFolder.py';
    
  // let callback2 = '';



  // RunPythonFile(filename2, callback2, gotResultsFuction=false)


  CreateImageWithMarkerReturn()

  // let filename = 'copyToTempFolder.py';

  
  // let callback =CreateImageWithMarkerReturn;

  // console.log('ran up to CreateImageWithMarkerReturn')

  // RunPythonFile(filename, callback,gotResultsFuction=false)



}

function JustChange(StayScreen){

  JustChangefunction(StayScreen);

}

async function JustChangefunction(StayScreen){
  
  let newFontSize = await document.getElementById("wordSize").value;

  // console.log(newFontSize);

  // console.log('newFontSize changed');

  if (newFontSize==''){

    // console.log("Font Size not Filled")

    PlaceChoosenSizeInDb2(StayScreen)

  }else if(newFontSize=='0'){

    // console.log("value is 0 so do nothing")
    
  }else{

    // console.log("continue")

    PlaceChoosenSizeInDb2(StayScreen)
  }


}

function PlaceChoosenSizeInDb(){




  StayScreen = true

  JustChange(StayScreen)


}

async function PlaceChoosenSizeInDb2(StayScreen){

    let defaultfont = 'Arial'

    let defaultFontSize = '30'

    let process = require("process");

    let path = require("path")
  
    const currentWorkingDirectory=process.cwd()

    const { getDbDataSimple } = require(path.join(currentWorkingDirectory, './js/getDbDataSimple'));

    

    let AwaitProveData ='Getting Db Data'

    let TableName =''

    let Database =''

    let newFont = await document.getElementById("font4").value;

    let newFontSize = await document.getElementById("wordSize").value;

    let TableGotten= await getDbDataSimple(AwaitProveData,TableName,Database)

    let oldFont = await TableGotten['oldFont'];

    let oldFontSize = await TableGotten['FontSize'];


    let SecondGoImageStep4 = await TableGotten['SecondGoImageStep4'];

    // let newFont = await document.getElementById("font4").value;

    // let newFont=newFont0.split(":")[0]

    // console.log(newFont)

    // console.log('this is the newFont above')

    // console.log(oldFont)

    // console.log('this is the oldFont above')

    // let newFontSize = await document.getElementById("wordSize").value;

    // console.log(newFontSize)

    // console.log('this is the newFontSize above')

    // console.log(oldFontSize)

    // console.log("this is the oldFontSize above")

    LeastOneTrue=true

    if (newFontSize==''){

      if (newFont==''){

        LeastOneTrue=false

        // console.log("All False")

      }else{


      }



    }else{



    }

    if (LeastOneTrue){


    

    if (oldFontSize==''){
      oldFontSize=defaultFontSize;

    }

    if ( String(oldFont)== 'undefined' ){
      oldFont=defaultfont;
      
    } 


    if (newFontSize==''){
      newFontSize=oldFontSize;
      
    }

    if (newFont==''){
      newFont=oldFont;
      
    } 

    // console.log(oldFont)

    // console.log('oldFont after above')


    // console.log(newFont)

    // console.log('newFont after above')

    // console.log(oldFontSize)

    // console.log('oldFontSize after above')

    // console.log(newFontSize)

    // console.log('newFontSize after above')

   
    

  

  // console.log('document.getElementById("font4").value above')



  let SecondGoImageStep4b = String(SecondGoImageStep4)



  if(SecondGoImageStep4b == 'true'){

    applyFont(newFont,newFontSize,StayScreen)

  }else if(SecondGoImageStep4b == 'false'){


  if (newFont==oldFont){

    // console.log('old and new fonts are the same')

    if (newFontSize==oldFontSize){

      // console.log('old and new fonts and font sizes are the same')

      // console.log('so do nothing')
      

      if (StayScreen){}else{

        applyFont(newFont,newFontSize,StayScreen)

      }
      

    }else{
      
      // console.log('old and new fonts are the same but Font size is different')

      // console.log('so continue')

      applyFont(newFont,newFontSize,StayScreen)

    }

  }else{
    // console.log('font is different but font sizes may be different')
    // console.log('so continue')

    applyFont(newFont,newFontSize,StayScreen)

  }

 
}else{

  // console.log("something went wrong variable SecondGoImageStep4b not true or false")
  // console.log(SecondGoImageStep4b)

}

}

}


function applyFont(newFont,newFontSize,StayScreen) {

  // console.log('You selected font: ' + newFont+' and font fize: '+ newFontSize);

  // let newFont0 = newFont.split(':');

  // let  newFontFamilySelected = newFont0[0];

  let newFontFamilySelected= newFont

  // console.log('fontFamilySelected: ',newFontFamilySelected)


  applyFont2(newFontFamilySelected,newFontSize,StayScreen)


  // if (newFontFamilySelected==oldFont){

  //   if (newFontSize==''){
      
  //     console.log("new font is old font so do nothing")
    
  //   }else{

  //     applyFont2(newFontFamilySelected,newFontSize)

  //     }

   
  // }else{

  //   applyFont2(newFontFamilySelected,newFontSize)

  

  // }

}


async function applyFont2(newFontFamilySelected,newFontSize,StayScreen){


  let process = require("process");

  let path = require("path");

  const currentWorkingDirectory = process.cwd();

  const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, './js/AddtoTablePromise'));

  const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));

  let AwaitProveData="starting add to table promise"
  

  let data=[newFontFamilySelected , newFontSize ];

  let dataName=['newFont', 'newFontSize'];

  let TableName='';

  let Database='';

  let Done = await AddtoTablePromise(AwaitProveData,data, dataName, TableName,Database)

  // console.log(Done)


  // console.log("before PutListDataIntoImageWithFontSize.py function")


  if (StayScreen){

  let filename = 'PutListDataIntoImageWithFontSize.py'
  
  let callback = FindCoordinateInImageStep4


  RunPythonFile(filename, callback)

  }else{

  let filename = 'PutListDataIntoImageWithFontSize.py'
  
  let callback = FindCoordinateInImageStep5GO


  RunPythonFile(filename, callback)


  }
  // let filename = 'PutListDataIntoImageWithFontSize.py'
  
  // let callback = FindCoordinateInImageStep4


  // RunPythonFile(filename, callback)


}


// function PutListDataIntoImage(){

//     console.log(Done)

//   let process = require("process");

//   let path = require("path")

//   const currentWorkingDirectory=process.cwd()


//   const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));


//   let filename = 'PutListDataIntoImageWithFontSize.py'
  
//   let callback = FindCoordinateInImageStep4

//   RunPythonFile(filename, callback)



// }


