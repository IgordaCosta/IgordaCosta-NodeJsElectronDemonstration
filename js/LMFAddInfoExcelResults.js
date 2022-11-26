
function LMFAddInfoExcelResults(results) {

    LMFAddInfoExcelResults2(results)


}


async  function LMFAddInfoExcelResults2(results) {
    // before is LMFAddInfoExcel
    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();



    const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));

    const { LMFNotValidFileNames } = require(path.join(currentWorkingDirectory, './js/LMFNotValidFileNames'));

    const { EmpyFieldsHtmlCodehiddenReverced } = require(path.join(currentWorkingDirectory, './js/EmpyFieldsHtmlCodehiddenReverced'));

    const { placeValuesInFile } = require(path.join(currentWorkingDirectory, './js/placeValuesInFile'));

    // console.log(results);
    // console.log('LMFAddInfoExcel Results above');

    let PossibleOptions = await results[results.length - 1];





    if (PossibleOptions == 'ContinueToNextPart') {



        // console.log("ForceCloseExcel file next");

        let filename = 'CloseWorkbook.py';
        let callback = placeValuesInFile;


        // console.log("before placeValuesInFile callback")



        RunPythonFile(filename, callback);








    }
    else if (PossibleOptions == 'PriorityFileNamesUsed') {

        LMFNotValidFileNames();

    }
    else if (PossibleOptions == 'ExistsNanTrue') {


        let filename = 'LoadToMultipleFilesDetails.py' 
        let callback = EmpyFieldsHtmlCodehiddenReverced;
    
        RunPythonFile(filename, callback);





    }
    else {

        // console.log("Something is wrong, the last print variable for the python function should be one of the above");
    }






}
exports.LMFAddInfoExcelResults = LMFAddInfoExcelResults;
