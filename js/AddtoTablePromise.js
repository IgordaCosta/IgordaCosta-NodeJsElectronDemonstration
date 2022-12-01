
function AddtoTablePromise(AwaitProveData,data, dataName, TableName,Database){
    return new Promise((resolve,_reject) =>{

        let Done = AddtoTablePromise0(AwaitProveData,data, dataName, TableName,Database);

    
        resolve(Done);



    }
    )

};

async function AddtoTablePromise0(AwaitProveData,data, dataName, TableName,Database){

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory=process.cwd();


    const { AddToTable } = require(path.join(currentWorkingDirectory, "./js/AddToTable"));



    Done = await AddToTable(AwaitProveData,data, dataName, TableName,Database);

    
    


    return Done;



};

exports.AddtoTablePromise = AddtoTablePromise;