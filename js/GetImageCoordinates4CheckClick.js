




// function FindCoordinateInImageStep5(){

//     location.replace("FindCoordinateInImageStep5.html");

// }

function GetImageCoordinates4CheckClick(){

    GetImageCoordinates4CheckClick2()

}


async function GetImageCoordinates4CheckClick2(){

    let defaultFontSize = '30';

    let defaultFont= 'Arial';

    let process = require("process");

    let path = require("path");

    const currentWorkingDirectory = process.cwd();

    const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, './js/AddtoTablePromise'));

    // const { fontSelect } = require(path.join(currentWorkingDirectory, './js/fontSelect'));
    let newFontSize = document.getElementById("wordSize").value;

    let newFont = document.getElementById("font4").value

    // console.log(newFontSize);

    // console.log('newFontSize changed');

    // below if any of the two are equal to '' a default value is added

    if (newFont==''){

        // now for the second posibility bellow

        if (newFontSize==''){

            // both are equal to ''

            let AwaitProveData="starting add to table promise"

            let newFontFamilySelected = defaultFont;

            let newFontSize = defaultFontSize;
  

            let data=[newFontFamilySelected , newFontSize ];

            let dataName=['newFont', 'newFontSize'];

            let TableName='';

            let Database='';

            let Done = await AddtoTablePromise(AwaitProveData,data, dataName, TableName,Database)

            // console.log(Done)

            FindCoordinateInImageStep5()




        }else{

            // only newFont==''


            let AwaitProveData="starting add to table promise";

            let newFontFamilySelected = defaultFont;

            let data=newFontFamilySelected;

            let dataName='newFont';

            let TableName='';

            let Database='';

            let Done = await AddtoTablePromise(AwaitProveData,data, dataName, TableName,Database)

            // console.log(Done)

            FindCoordinateInImageStep5()



        }

    }else{

    if (newFontSize==''){

        // only newFontSize==''

        // console.log("Font Size not Filled")

        let AwaitProveData="starting add to table promise"
    
        let newFontSize = defaultFontSize;

        let data=newFontSize

        let dataName='newFontSize'

        let TableName='';

        let Database='';

        let Done = await AddtoTablePromise(AwaitProveData,data, dataName, TableName,Database)

        // console.log(Done)

        FindCoordinateInImageStep5()

    }else if(newFontSize=='0'){

        // font sizes can not be equal to 0

        // console.log("value is 0 so do nothing")
        
    }else{

        // console.log("continue")

        // both are not equal to '' so no need to add info

        FindCoordinateInImageStep5()
    }

}

}




