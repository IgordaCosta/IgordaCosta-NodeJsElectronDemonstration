async function continuationLoadMultipleFilesFromDatabase(MydocumentsDbPath, CurrentWorkingPath, ItemChecked, ItemNOTchecked,typeOfButton) {
   
    var path = require('path')

    
    
    
    const { getRowNumberInTableByClass } =   require(path.join(CurrentWorkingPath, "./js/getRowNumberInTableByClass" ));

    const { insertIntoDatabase } =  require(path.join(CurrentWorkingPath,"./js/insertIntoDatabase" ));

    

    const { validate } = require(path.join(CurrentWorkingPath,"./js/validate" ));


    const { getDbData } = require(path.join(CurrentWorkingPath,"./js/getDbData"));


    const { getRealdatafillName } = require(path.join(CurrentWorkingPath,"./js/getRealdatafillName"));


    const { AddtoTablePromise } = require(path.join(CurrentWorkingPath,"./js/AddtoTablePromise"));




    const { gotResultsIndexOut } = require(path.join(CurrentWorkingPath,"./js/gotResultsIndexOut"));

    


    // const { gotResultsAdd } = require(path.join(CurrentWorkingPath,"./js/gotResultsAdd"));







    







    // AddtoTablePromise



    // getRealdatafillName


    // var process = require('process');
    // CurrentWorkingPath=process.cwd()
    // const getDbData = require("./js/getDbData");
    




    // console.log(+new Date);





    // console.log(MydocumentsDbPath);

    // console.log('MydocumentsDbPath after return');

    // console.log(CurrentWorkingPath);

    // console.log('New CurrentWorkingPath after return');



    // LoadSingleFileFromDatabase
    tableClass = "table";

    // getRowNumberInTableByClass(tableClass);
    let TableEmpty=true;
    try{

        numberOfRows = getRowNumberInTableByClass(tableClass);

    }catch{

        TableEmpty=false;

    }
    

    // this is a logical operation so its ok
    if (TableEmpty){

        

        let AnyChecked = false;

    let checkedNumber = 0;

    let NeedWait = true;

    if (numberOfRows > 0) {

        let documentIDInitiral = "customRadio";

        let isChecked = false;

        for (i = 0; i < numberOfRows; i++) {

            documentID = documentIDInitiral + String(i);
            isChecked = validate(documentID);
            if (isChecked == true) {

                checkedNumber = i;

                AnyChecked = true;

            }



        }



        if (AnyChecked == true) {


            // gotResultsAdd()


            gotResultsIndexOut()




            // console.log('ItemChecked');

            // console.log('checkedNumber', checkedNumber);




            //  fix bellow 
            // let datafillName = document.getElementById("tableData").rows[checkedNumber].cells[2].innerHTML;    // this is how datafillName was found however now it finds the JobItem

            // checkedNumber  // this in the number chosen it shoud also be the same ordered one for the datafillname







            // let JobItemGotten = document.getElementById("tableData").rows[checkedNumber].cells[2].innerHTML;    // this is how datafillName was found however now it finds the JobItem

            // let data1 = JobItemGotten

            // let dataName1 = 'JobItemGotten'


            
            let data1 = checkedNumber

            let dataName1 = 'checkedNumber'




            let TableName = "qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq";

            let Database = './AutoFormFiller.db';

            let AwaitProveData = 'start function'
            let FaliedAddTable;
            try{

            let DoneAddtoTablePromise = await AddtoTablePromise(AwaitProveData, data1, dataName1, TableName, Database);
            FaliedAddTable = false
           
            // console.log(DoneAddtoTablePromise);
            }catch{
                FaliedAddTable = true
            }




            if (FaliedAddTable){
            try {

                resultDatabase = await insertIntoDatabase(data1, dataName1, CurrentWorkingPath, TableName, Database);
                // console.log(resultDatabase);
                FaliedAddTable = false
            }
            catch (e) {

                // console.log(e);

            }
        }else{}


            if (FaliedAddTable == false){

            filename = 'getRealdatafillName.py'

            datafillName = await getRealdatafillName(filename);





            // console.log('datafillName', datafillName);

            FilesInDatabaseLocation = 'FilesInDatabase';

            columnsFileinDatabase = ['Job Name', 'File KEY', 'File Saved Location'];

            


            NeedWait = false;

            

            const path = require('path');

            const dbPath = path.resolve(__dirname, './AutoFormFiller.db');

            let data = [datafillName, dbPath,typeOfButton];

            let dataName = ['datafillName', 'dbPath','typeOfButton'];


            // let TableName = "qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq";

            // let Database = './AutoFormFiller.db';



            // try {

            //     resultDatabase = await insertIntoDatabase(data, dataName, MydocumentsDbPath, CurrentWorkingPath, TableName, Database);
            //     console.log(resultDatabase);

            // }
            // catch (e) {

            //     console.log(e);

            // }


            // let AwaitProveData = 'start function'


            let DoneAddtoTablePromise2 = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);

            // console.log(DoneAddtoTablePromise2)


            // console.log(MydocumentsDbPath);
            // console.log('MydocumentsDbPath above');

            // console.log("goes into handleData function after this function");

            try {


                let returnFromDB;

                // returnFromDB=await getDbData(resultDatabase,TableName,Database,CurrentWorkingPath,MydocumentsDbPath,handleData);
                returnFromDB = await getDbData(resultDatabase, TableName, Database, CurrentWorkingPath, MydocumentsDbPath);

                // console.log(returnFromDB);


                // console.log('returnFromDB is above');


            }
            catch (e) {

                // console.log(e);



            }




            // console.log("before going into LMFItemChecked()");


            process.chdir(CurrentWorkingPath);


            ItemChecked();



        }
        else {

            // console.log('ItemNOTchecked');

            NeedWait = false;

            process.chdir(CurrentWorkingPath);


            ItemNOTchecked();



        }

    }
    else {
        // console.log("wait to load");

        NeedWait = false;


        process.chdir(CurrentWorkingPath);


        ItemNOTchecked();








    }

    // console.log([AnyChecked, checkedNumber, NeedWait]);

    // return [AnyChecked, checkedNumber,NeedWait]

    }else{}

}else{}
    
}
exports.continuationLoadMultipleFilesFromDatabase = continuationLoadMultipleFilesFromDatabase;
