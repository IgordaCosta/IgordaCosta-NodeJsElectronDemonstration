



async function AddToTable0(AwaitProveData,data, dataName, TableName,Database) {
    
    // console.log(AwaitProveData);

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory=process.cwd();

    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));


    if (TableName == ''){

        TableName = 'None';
    }

    if (Database == ''){

        Database = 'None';
    }

    let filename = 'AddToable.py';

    let callback = '';

    let dataUsed = ['['+data+'], ['+dataName+'], '+TableName, Database, currentWorkingDirectory];

    // console.log(dataUsed);
    // console.log('data used above')

    let NoArgs = false; 


    let results = await RunPythonFile(filename=filename, callback=callback, gotResultsFuction=false, dataUsed = dataUsed, NoArgs=NoArgs);

    // console.log(results);

    return results

    


};




function AddToTable(AwaitProveData,data, dataName, TableName,Database) {

    return new Promise((resolve, _reject) => {

        let Done= AddToTable0(AwaitProveData,data, dataName, TableName,Database);

        // console.log('insde Add to table should apper first')

        resolve(Done);



    }

    );


};


exports.AddToTable = AddToTable;

