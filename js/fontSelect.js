







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




}


async function fontSelect2(results){



    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()


    const { getResultsList } = require(path.join(currentWorkingDirectory, "./js/getResultsList"));


    

    let resultGotten = await getResultsList(results);



    fontSelect3(resultGotten);

    
}

async function fontSelect3(resultGotten){


    


    let process = require("process");

    let path = require("path");
  
    const currentWorkingDirectory = process.cwd();

    const { getDbDataSimple } = require(path.join(currentWorkingDirectory, './js/getDbDataSimple')); 

    const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, './js/AddtoTablePromise')); 
    
    let AwaitProveData = "getting Db Data";
  
    let TableName = '';
  
    let Database = '';
  
    let DataGotten = await getDbDataSimple(AwaitProveData, TableName, Database);



  
    let font = await DataGotten['oldFont'];



    AwaitProveData= "adding to table systemFontsResult"

    let data = resultGotten
    
    let dataName= 'systemFonts'


    let Done =await AddtoTablePromise(AwaitProveData,data, dataName, TableName,Database)



    let systemFontsResult=resultGotten.split('|')

    


    if (font==undefined){

        $('#font4').fontselect({

            systemFonts : systemFontsResult,

            localFontsUrl: [],

	        googleFonts: [],
    
            placeholder: 'Click here to select a font',
    
            placeholderSearch: 'Type here to search'
        })





        try{
            document.getElementById("createImageGetData").classList.remove('hidden');

        document.getElementById("ImageDocument").classList.remove('hidden');

        document.getElementById("OntopOfAll").classList.add('hidden')

        document.getElementById("AllNormalItems").classList.remove('hidden');

        
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

    document.getElementById("OntopOfAll").classList.add('hidden')/

    document.getElementById("AllNormalItems").classList.remove('hidden');

    }catch(error){}
   
    
    }

}




function applyFontChange(fontUsed) {

    applyFontChangefunction(fontUsed)
    
    }


async function applyFontChangefunction(fontUsed) {
    let font0 = fontUsed.replace(/\+/g, ' ');

    let font = font0.split(':');
    let  fontFamily = await font[0];
    let  fontWeight = await font[1] || 400;


    $('#ShowFontTypeHere').css({fontFamily:"'"+fontFamily+"'", fontWeight:fontWeight});



}







  









    





exports.fontSelect = fontSelect;
