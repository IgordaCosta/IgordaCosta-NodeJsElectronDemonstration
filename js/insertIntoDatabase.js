

function insertIntoDatabase(data, dataName, CurrentWorkingPath, TableName,Database) {

    return new Promise((resolve, _reject) => {

        results = insertIntoDatabase0(data, dataName, CurrentWorkingPath, TableName,Database)

    resolve(results);


}
);

};



// async function insertIntoDatabase0(data, dataName, MydocumentsDbPath, CurrentWorkingPath, TableName,Database) {

async function insertIntoDatabase0(data, dataName, CurrentWorkingPath, TableName,Database) {

   
        var path = require("path");


        const { RunPythonFile } = require(path.join(CurrentWorkingPath, "./js/RunPythonFile"));


        let filename = 'insertIntoDatabase.py';

        let callback = '';


        if (Database == ''){

        Database="AutoFormFiller.db";

        }

        if (TableName == ''){

        TableName="qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq";

        };




        let dataUsed = [data, dataName, TableName, Database, CurrentWorkingPath];

        // console.log(dataUsed);

        // console.log('dataUsed above');

        let NoArgs = false;

        
        results = await RunPythonFile(filename=filename, callback=callback, gotResultsFuction=true, dataUsed = dataUsed, NoArgs=NoArgs);

        // console.log('insie insert data function (should apper first)')

        return results;


};
exports.insertIntoDatabase = insertIntoDatabase;
