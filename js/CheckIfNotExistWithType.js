

async function CheckIfNotExistWithType(typeOfButton) {

    var path = require("path");
    var process = require("process");
    CurrrentWorkingDirectory = process.cwd();

    const { RunPythonFile } = require(path.join(CurrrentWorkingDirectory, "./js/RunPythonFile"));
    // const { MyDocumentsDatabasePath } = require(path.join(CurrrentWorkingDirectory, "./js/MyDocumentsDatabasePath"));
    const { insertIntoDatabase } = require(path.join(CurrrentWorkingDirectory, "./js/insertIntoDatabase"));

    const { ResultsOfExist } = require(path.join(CurrrentWorkingDirectory, "./js/ResultsOfExist"));

    let jobName = document.getElementsByClassName("form-control")[0].value;

    document.getElementsByClassName("form-control")[0].value = '';

    if (jobName == '') { }
    else {

        document.getElementsByClassName("input-group")[0].classList.add('hidden');
        document.getElementsByClassName("spinner")[0].classList.remove('hidden');

        // MydocumentsDbPath = await MyDocumentsDatabasePath(CurrrentWorkingDirectory);

        // console.log(MydocumentsDbPath);

        let datafillName = jobName;

        let TableName = '';
        let Database = '';

        let data = "["+datafillName+", "+typeOfButton+"]";
        let dataName = "["+'datafillName'+", "+'typeOfButton'+"]";

        // console.log(datafillName)
        // console.log('datafillName')


        // console.log(typeOfButton)
        // console.log('typeOfButton')

        let Result = await insertIntoDatabase(data, dataName, CurrrentWorkingDirectory, TableName, Database);

        // console.log(Result);

        // console.log('Result of inserting data above');


        filename = 'CheckJobNameRedo.py';

        RunPythonFile(filename, ResultsOfExist);


    }
}
exports.CheckIfNotExistWithType = CheckIfNotExistWithType;
