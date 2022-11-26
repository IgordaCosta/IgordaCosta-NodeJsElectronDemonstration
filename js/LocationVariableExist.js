


function OptionChosenIfExist(){


    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()

    const { validate } = require(path.join(currentWorkingDirectory,"./js/validate" ));

    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));
    // const { insertIntoDatabase } = require(path.join(currentWorkingDirectory, "./js/insertIntoDatabase"));
    // const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory, "./js/MyDocumentsDatabasePath"));


    // documentID = documentIDInitiral + String(i);
    // isChecked = validate(documentID);

    DVchecked = validate('DV');

    KVUchecked = validate('KVU');

    KVNUchecked = validate('KVNU');

    if (DVchecked==true){

        // console.log('DVchecked option selected')

        // The program will delete all of the Location values 
        // and continue as if it never existed

    }else if(KVUchecked==true){

        // this option keeps the value and uses it 
        
        // this will carry the 'KeepValue' flag

        // however the file used for the user must not contain
        // this information or else the document will be one character off
        
        // at the end of the proces before adding the document to the database
        // the program will read this flag and if it is this one the document 
        // will delete all of this markup values before adding in to the database

        // console.log('KVUchecked option selected')

    }else if(KVNUchecked==true){

        // this option will keep the value just for show
        // so it will record the variables location 
        // and when giving the output locations
        // it will remove the ones recorded on the next step
        // this will carry the 'NOTkeepValues' flag

        // at the end of the program this values will NOT be deleted

        // console.log('KVNUchecked option selected')

    }else{

        // console.log('no option selected')

    }

    // let filename="OpenExcelDocument.py"

    // let callback=AddDataOpenExcelDocumentReturn


    // RunPythonFile(filename,callback)

}