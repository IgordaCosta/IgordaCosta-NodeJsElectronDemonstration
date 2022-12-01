
function OperationComplete(){

    location.replace("OperationComplete.html");
    
}

function GetAnotherImageFromPdf(){

    location.replace("GetAnotherImageFromPdf.html");

}

async function getAllFilledInputs(){

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()

    const { getDbDataSimple } = require(path.join(currentWorkingDirectory, "./js/getDbDataSimple"));

  
    let anydata="it has started"

    let tableName=''
    
    let Database=''


    objToCheck= await getDbDataSimple(anydata,tableName,Database)

    let ExtensionType = await objToCheck['ExtensionType'];

    if (ExtensionType=='excel'){


        let NumList=await objToCheck['NumList'];


        getAllFilledInputs2(NumList);


    }else if(ExtensionType=='image' || ExtensionType=='pdf'){

        let finalLocationsY= await objToCheck['finalLocationsY'];

        let finalLocationsYList = finalLocationsY.replace('[','').replace(' ','').replace(']','').replace("'",'').split(',')

        let NumList = finalLocationsYList.length


        getAllFilledInputs2(NumList);



    }else if(ExtensionType=='word'){



    }

    

    }



async function getAllFilledInputs2(NumList){

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()



    const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, "./js/AddtoTablePromise"));

    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));


    const { getNameOfLocations } = require(path.join(currentWorkingDirectory, "./js/getNameOfLocations"));



    let resultOut = await getNameOfLocations(NumList);


    let valuesList = await resultOut[0];

    let MissingValuesList = await resultOut[1];


    let MissingValues=MissingValuesList.includes(true)


    if (MissingValues==true){


        document.getElementById("waitFunction").classList.remove('hidden')
        let alertDiv= `
            <div id= "identifiersMissingAlert" class="alert alert-dismissible">
                <button type="button" class="close" data-dismiss="alert">&times;</button>
                There are Identifiers missing! All Identifiers must be filled!
            </div> 
        `
        let d1 = document.getElementById('alert MissingData');
        
        d1.insertAdjacentHTML('afterbegin', alertDiv);

    }else{





        let awaitProvedata="it has started"

        let data=String(valuesList)

        let dataName='AddToTablevaluesList'

        let tableName=''
        
        let Database=''

        let Done = await AddtoTablePromise(awaitProvedata,data,dataName,tableName,Database)


        filename= "RemoveCharacters.py"

        callback=''

        let OutputRemoveCharaters = await RunPythonFile(filename,callback, gotResultsFuction=false)


        let MissingValues2 = await OutputRemoveCharaters[OutputRemoveCharaters.length-1]


        if (MissingValues2=='True'){

            
            document.getElementById("waitFunction").classList.remove('hidden')
            let alertDiv= `
                <div id= "identifiersMissingAlert" class="alert alert-dismissible">
                    <button type="button" class="close" data-dismiss="alert">&times;</button>
                    There are Identifiers missing! All Identifiers must be filled!
                </div> 
            `
            
            let d1 = document.getElementById('alert MissingData');
            
            d1.insertAdjacentHTML('afterbegin', alertDiv);


        }else if(MissingValues2=='False'){
            

            filename= "clickedAddFile.py"

            callback=clickedAddFile
    
            RunPythonFile(filename,callback)


        }else{


        }




    }



}







    





function checkIfAllInputsFilled(){

    document.getElementById("waitFunction").classList.add('hidden')

    let AlertExists = document.getElementById("identifiersMissingAlert");
    if(AlertExists){

        let element = document.getElementById('identifiersMissingAlert');
        element.parentNode.removeChild(element);

    }else{}


    getAllFilledInputs()

    
}


async function clickedAddFile(){


    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()

    
    const { getDbDataSimple } = require(path.join(currentWorkingDirectory, "./js/getDbDataSimple"));

    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));





    let AwaitProveData = 'getting tableData'

    let TableName = ''

    let Database = ''

    let DataGotten= await getDbDataSimple(AwaitProveData,TableName,Database)

    let PDFfile = await DataGotten['PDFfile'];

    if (PDFfile=='true'){

        let filename ='RunDeleteObjFromTableFL.py'
        
        let callback = GetAnotherImageFromPdf

        RunPythonFile(filename, callback, gotResultsFuction=true)

        

    }else if (PDFfile=='false'){

        OperationComplete()

    }else{



    }



        
        

}    










