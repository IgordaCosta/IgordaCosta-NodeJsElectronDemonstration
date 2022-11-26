

// function FindCoordinateInImageStep5(){

// const { getResultsList } = require("./getResultsList");

//     location.replace("FindCoordinateInImageStep5.html");

// }



function fontSelect(){
    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()


    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));

    const { gotResultsAdd } = require(path.join(currentWorkingDirectory, "./js/gotResultsAdd"));

    gotResultsAdd()


    let filename='GetAllFontNamesFromFolder.py'

    let callback=fontSelect2


    RunPythonFile(filename, callback, gotResultsFuction=false)

    // console.log('fontselect part 1')



}


async function fontSelect2(results){



    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()


    const { getResultsList } = require(path.join(currentWorkingDirectory, "./js/getResultsList"));


    

    let resultGotten = await getResultsList(results);

    // console.log(resultGotten);


    fontSelect3(resultGotten);

    
}

async function fontSelect3(resultGotten){


    // console.log('fontSelect3 functioon now')
    


    let process = require("process");

    let path = require("path");
  
    const currentWorkingDirectory = process.cwd();

    const { getDbDataSimple } = require(path.join(currentWorkingDirectory, './js/getDbDataSimple')); 

    const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, './js/AddtoTablePromise')); 
    
    let AwaitProveData = "getting Db Data";
  
    let TableName = '';
  
    let Database = '';
  
    let DataGotten = await getDbDataSimple(AwaitProveData, TableName, Database);



    // console.log(DataGotten)
  
    let font = await DataGotten['oldFont'];



    AwaitProveData= "adding to table systemFontsResult"

    let data = resultGotten
    
    let dataName= 'systemFonts'


    let Done =await AddtoTablePromise(AwaitProveData,data, dataName, TableName,Database)

    // console.log(Done)


    let systemFontsResult=resultGotten.split('|')

    

    // let font='Lucida+Console'

    if (font==undefined){

        $('#font4').fontselect({

            systemFonts : systemFontsResult,

            localFontsUrl: [],

	        googleFonts: [],
    
            placeholder: 'Click here to select a font',
    
            placeholderSearch: 'Type here to search'
        })

        // console.log(document);

        // console.log('document.getElementById("createImageGetData") above')



        try{
            document.getElementById("createImageGetData").classList.remove('hidden');

        document.getElementById("ImageDocument").classList.remove('hidden');

        document.getElementById("OntopOfAll").classList.add('hidden')
        }catch(error){}
    
      


    }else{

        applyFontChange(font)

    $('#font4').fontselect({

        systemFonts : systemFontsResult,

        localFontsUrl: [],

	    googleFonts: [],

        placeholder: 'Click here to select a font',

	    placeholderSearch: 'Type here to search'
    })
    .trigger('setFont',font)
    .on('change', function() {
        applyFontChange(this.value);
    });
    
    try{
    document.getElementById("createImageGetData").classList.remove('hidden');

    document.getElementById("ImageDocument").classList.remove('hidden');

    document.getElementById("OntopOfAll").classList.add('hidden')

    }catch(error){}
   
    
    }

}



// async function applyFont(font) {

function applyFontChange(fontUsed) {

    applyFontChangefunction(fontUsed)
    
    }


async function applyFontChangefunction(fontUsed) {
    let font0 = fontUsed.replace(/\+/g, ' ');

    // Split font into family and weight
    let font = font0.split(':');
    let  fontFamily = await font[0];
    let  fontWeight = await font[1] || 400;

    // console.log('Font family', fontFamily, 'Font weight', fontWeight);

    $('#ShowFontTypeHere').css({fontFamily:"'"+fontFamily+"'", fontWeight:fontWeight});



}
//     console.log('You selected font: ' + font);

//     // let font0 = font.split(':');

//     // let  fontFamilySelected = font0[0];

//     fontFamilySelected=font

//     console.log('fontFamilySelected: ',fontFamilySelected)


//     let process = require("process");

//     let path = require("path");
  
//     const currentWorkingDirectory = process.cwd();

//     const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, './js/AddtoTablePromise'));

//     AwaitProveData='Starting add to table'

//     let data=fontFamilySelected;

//     let dataName='oldFont';

//     let TableName='';

//     let Database='';

//     let Done = await AddtoTablePromise(AwaitProveData,data, dataName, TableName,Database)

//     console.log(Done)

    




// }

exports.fontSelect = fontSelect;
