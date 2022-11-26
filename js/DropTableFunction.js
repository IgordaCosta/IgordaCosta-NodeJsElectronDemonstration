// const { dropTableString } = require("./js/dropTableString");

// const { createTableString } = require("./js/createTableString");

// const { insertIntoTableString } = require("./js/insertIntoTableString");


async function DropTableFunction(data, dataName, MydocumentsDbPath, CurrentWorkingPath, TableName,Database) {

    // const { dropTableString } = require("./js/dropTableString");

    // const { createTableString } = require("./js/createTableString");

    // const { insertIntoTableString } = require("./js/insertIntoTableString");


    return new Promise((resolve, reject) => {


        if(TableName==''){
            TableName="qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq"
        }else{}
    
        if(Database==''){
            Database='./AutoFormFiller.db'
        }else{}

        




        
        const path = require('path');
        

        var process = require('process');

        let currentWorkingDirectory=CurrentWorkingPath

        // console.log(currentWorkingDirectory)

        // console.log('currentWorkingDirectory')


        const dropTableStringPath = path.resolve(currentWorkingDirectory, "./js/dropTableString");

        // const createTableStringPath = path.resolve(currentWorkingDirectory, "./js/createTableString");

        // const insertIntoTableStringPath = path.resolve(currentWorkingDirectory, "./js/insertIntoTableString");



        const { dropTableString } = require(dropTableStringPath);

        // const { createTableString } = require(createTableStringPath);

        // const { insertIntoTableString } = require(insertIntoTableStringPath);





        
        process.chdir(MydocumentsDbPath);



        if (data.constructor === Array) {

            ColumnList = dataName;

            ValuesList = data;

        }
        else {

            ColumnList = [dataName];

            ValuesList = [data];

        }

        // console.log(dataName)
        // console.log('dataName above')

        // console.log(data)

        // console.log('data above')

        const sqlite3 = require('sqlite3').verbose();
        // const path = require('path');
        // const dbPath = path.resolve(__dirname, './JavascriptPythonDatabase.db');
        // let insertString;
        // let createString;
        // let dropString;
        // dropString= await dropTableString(TableName);
        // createString= await createTableString(TableName,ColumnList);
        // insertString= await insertIntoTableString(TableName,ColumnList,ValuesList);
        // let DatabaseUsed=Database;
        let db = new sqlite3.Database(Database, sqlite3.OPEN_READWRITE | sqlite3.OPEN_CREATE, (err) => {
            if (err) {
                // console.error(err.message);
            }
            // console.log('Connected to the chinook database.');
        });

        db.serialize(function () {


            // let insertString;

            // let createString;

            let dropString;


            dropString = dropTableString(TableName);

            // createString = createTableString(TableName, ColumnList);

            // insertString = insertIntoTableString(TableName, ColumnList, ValuesList);

            // let FininshedWithData;
            // let valueOfDb;

            let sql = `SELECT * FROM ${TableName}`;

            try {

                valueOfDb = db.run(dropString).get(sql, (err, row) => {

                    if (err) {

                        process.chdir(currentWorkingDirectory);

                        // console.log(err)

                        reject(err);
                        // return console.error(err.message);
                        // console.log(err);

                    }
                    else {


                        // console.log(row)
                        // console.log("row is above")
                        // dados=JSON.stringify(row);
                        // console.log(dados)
                        // console.log("dados is above")
                        // callback(row);


                        process.chdir(currentWorkingDirectory);

                        // console.log(row)

                        resolve(row);



                    }





                    // ? console.log(row)
                    // : console.log(`No table found with the tablename: ${TableName}`);
                });



            }
            catch (e) {
                // console.log(e);

            }















            //     FininshedWithData=true;
            // }catch(e){
            //     console.log(e)
            //     FininshedWithData=false;
            // }
            // console.log(valueOfDb)
            // console.log("valueOfDb above")
            // resolve(valueOfDb);
            // if (FininshedWithData){
            //     console.log(+new Date)
            //     console.log('above is time of data done put')
            // }else{
            //     console.log(+new Date)
            //     console.log('above is time of data done put')
            //     reject(e);
            // }
            db.close();



            // console.log(+new Date)
            // console.log('above is time of data done put')
        });



    }
    );
}
exports.insertIntoDatabase = insertIntoDatabase;
