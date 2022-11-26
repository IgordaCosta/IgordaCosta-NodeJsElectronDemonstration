

async function CheckIfValueExistsInDb(TableName,Database,ValueToCheck){

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory=process.cwd();


    const { getDbDataSimple } = require(path.join(currentWorkingDirectory, "./js/getDbDataSimple"));


    let AwaitProveData="ok";


    let tableGotten=await getDbDataSimple(AwaitProveData,TableName,Database);

    // console.log(tableGotten)

    // console.log("tableGotten['KEY_file15'] above")

    // let ThingTOget= tableGotten.datafillName

    let ThingTOget= await tableGotten[ValueToCheck];

    if (ThingTOget==undefined){

        // console.log("variable is undefined")



        return false;


    }else{

        // console.log("value Exists")

        // console.log(ThingTOget)

        // console.log('value gotten above')


        return true;

};



}

exports.CheckIfValueExistsInDb = CheckIfValueExistsInDb;



// async function getData(){

//     let TableName=''
    
//     let Database=''
    
//     // let ValueToCheck='ListofInlist'

//     let ValueToCheck='adfsfa'


//     let isValueThere=await CheckIfValueExistsInDb(TableName,Database,ValueToCheck)

//     console.log(isValueThere)

//     console.log('isValueThere above')

// }



// getData()