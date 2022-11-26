// const { getNameOfLocations } = require("./getNameOfLocations");


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

    // console.log(objToCheck)

    // console.log('objToCheck above')

    // Below is to check what type of file it is to know where to get the data

    let ExtensionType = await objToCheck['ExtensionType'];

    if (ExtensionType=='excel'){
        // isert here the data for excel files


        let NumList=await objToCheck['NumList'];

        // console.log(NumList)

        // console.log('NumList above')

        getAllFilledInputs2(NumList);


    }else if(ExtensionType=='image' || ExtensionType=='pdf'){
        // insert here the data for image files

        let finalLocationsY= await objToCheck['finalLocationsY'];

        let finalLocationsYList = finalLocationsY.replace('[','').replace(' ','').replace(']','').replace("'",'').split(',')

        let NumList = finalLocationsYList.length

        // console.log(NumList)

        // console.log('NumList above')

        getAllFilledInputs2(NumList);



    }else if(ExtensionType=='word'){
        // insert here the data for word files



    }

    

    }



async function getAllFilledInputs2(NumList){

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()

    
    // const { gotResults } = require(path.join(currentWorkingDirectory, "./js/gotResults"));

    const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, "./js/AddtoTablePromise"));

    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));


    const { getNameOfLocations } = require(path.join(currentWorkingDirectory, "./js/getNameOfLocations"));


    // NumList=parseInt(NumList)

    // let valuesList=[];
    // let i;

    // let firstValue=document.getElementById("validationTooltip0"+'1'.toString()).value;

    // console.log(firstValue)
    
    // let MissingValuesList=[]

    // let valuegotten='';

    // for (i = 0; i < NumList; i++) {

    //     console.log("i used: "+ i)
   
    //     valuegotten=document.getElementById("validationTooltip0"+(i)).value;

    //     console.log(valuegotten);

    //     console.log('valuegotten above');

    //     valuesList.push(valuegotten)
    //     if (valuegotten==''){

    //         MissingValuesList.push(true)
    //     }else{

    //         MissingValuesList.push(false)
    //     }

    // } 

    let resultOut = await getNameOfLocations(NumList);

    // console.log(resultOut)

    let valuesList = await resultOut[0];

    let MissingValuesList = await resultOut[1];

    // console.log(MissingValuesList)

    // console.log('MissingValuesList above')

    // this is not a text true respose 'true' or 'false' but a logical operation
    let MissingValues=MissingValuesList.includes(true)

    // console.log(MissingValues)

    // console.log('MissingValues? above')

    // this is a logical optiona so do not put it under ''
    if (MissingValues==true){

        // console.log("stay on page and show warning message");

        // document.getElementById("identifiersMissingAlert").classList.remove('hidden')

        document.getElementById("waitFunction").classList.remove('hidden')
        let alertDiv= `
            <div id= "identifiersMissingAlert" class="alert alert-dismissible">
                <button type="button" class="close" data-dismiss="alert">&times;</button>
                There are Identifiers missing! All Identifiers must be filled!
            </div> 
        `
        // let d1 = document.getElementById('MissingData');
        let d1 = document.getElementById('alert MissingData');
        
        d1.insertAdjacentHTML('afterbegin', alertDiv);

    }else{



        // here it will run the python function to remove all unwanted characters and 
        // then recheck for missing values if there are missing values the above function will
        // run again
        // else the rest of this will run


            


        // add 1_ 2_ ... in front fo each clumn data value

        // console.log(valuesList)

        // console.log('valuesList above')


        let awaitProvedata="it has started"

        let data=String(valuesList)

        let dataName='AddToTablevaluesList'

        let tableName=''
        
        let Database=''

        let Done = await AddtoTablePromise(awaitProvedata,data,dataName,tableName,Database)
        // AddToTable(awaitProvedata,data,dataName,tableName,Database)

        // console.log(Done)

        // console.log("go to the processing page and continue the program");


        filename= "RemoveCharacters.py"

        callback=''

        let OutputRemoveCharaters = await RunPythonFile(filename,callback, gotResultsFuction=false)

        // console.log(OutputRemoveCharaters);

        // console.log(OutputRemoveCharaters[OutputRemoveCharaters.length-1])

        // console.log('OutputRemoveCharaters[OutputRemoveCharaters.length-1]')

        let MissingValues2 = await OutputRemoveCharaters[OutputRemoveCharaters.length-1]


        if (MissingValues2=='True'){

            // console.log('values are missing go back')

            // console.log("stay on page and show warning message");

            
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
            
            // console.log('no values are missing continue')


            filename= "clickedAddFile.py"

            callback=clickedAddFile
    
            RunPythonFile(filename,callback)


        }else{

            // console.log('something is wrong')
            // console.log(MissingValues2)


        }



        // // gotResults()


        // filename= "clickedAddFile.py"

        // callback=clickedAddFile

        // RunPythonFile(filename,callback)

    }



}



// async function noMissingValues(valuesList){



    


        // // add 1_ 2_ ... in front fo each clumn data value

        // console.log(valuesList)

        // console.log('valuesList above')


        // let awaitProvedata="it has started"

        // let data=String(valuesList)

        // let dataName='AddToTablevaluesList'

        // let tableName=''
        
        // let Database=''

        // let Done = await AddtoTablePromise(awaitProvedata,data,dataName,tableName,Database)
        // // AddToTable(awaitProvedata,data,dataName,tableName,Database)

        // console.log(Done)

        // console.log("go to the processing page and continue the program");

        // gotResults()


        // filename= "clickedAddFile.py"

        // callback=clickedAddFile

        // RunPythonFile(filename,callback)



// }



function checkIfAllInputsFilled(){

    document.getElementById("waitFunction").classList.add('hidden')

    // in this case since its checking if there this alert obj, and not
    // a true and false statement stored  in a database, it will work only the way shown
    // if used as if(AlertExists=='true'){}else if(AlertExists=='false'){}else{} there will be errors
    let AlertExists = document.getElementById("identifiersMissingAlert");
    if(AlertExists){

        let element = document.getElementById('identifiersMissingAlert');
        element.parentNode.removeChild(element);

    }else{}


    getAllFilledInputs()

    
}


async function clickedAddFile(){

    // if the original file is pdf this will guide to another page asking if the user would like to 
    // add another image file from that pdf

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

        // console.log("something is wrong with the value below it must be either true or false")
        // console.log("PDFfile = " + PDFfile)

    }



        
        

}    










