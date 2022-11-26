




function getDbDataSimple (AwaitProveData,TableName,Database) {

    return new Promise((resolve, _reject) => {

    let resultDatabase = AwaitProveData

    // console.log(resultDatabase);

    // console.log('promise function started')


    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()


    const { getDbData } = require(path.join(currentWorkingDirectory, "./js/getDbData"));


    let valueGotten = getDbData (resultDatabase,TableName,Database);

    resolve(valueGotten);




    // let valueGotten = getDbData0 (resultDatabase,TableName,Database);

    // resolve(valueGotten);





    // getDbData0 (resultDatabase,TableName,Database, (err, res) => {
    //     if (err) {

    //         console.log(err);
    //         console.log('error is above');
    //       reject(err);
    //     }
    //     else {

    //         console.log(res);
    //         console.log('res is above');
    //       resolve(res);
    //     }
    //   })
    // }) 




  }

  )

}


// async function getDbData0 (resultDatabase,TableName,Database) {
    
//     // this gets the data in a dictionary format
//     // I must turn it from a string into a dictionary 
//     // after getting the data in javascript

//     console.log(resultDatabase);

//     var path = require("path")

//     const currentWorkingDirectory = process.cwd();
    
//     const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));

//     const { PythonOrdToString } = require(path.join(currentWorkingDirectory, "./js/PythonOrdToString"));


//     if (TableName == ''){


//       TableName = 'qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq';

//       Database = 'None';


//     }


//     let filename = 'CallgetDbData.py';

//     let callback = '';

//     let dataUsed = [ "[" + TableName + ', '+ Database + ', '+ currentWorkingDirectory +']' ];

//     let NoArgs = false;

//     console.log(dataUsed);

//     console.log('dataUsed is above before funciton')

//     let results = await RunPythonFile(filename=filename, callback=callback, gotResultsFuction=false, dataUsed = dataUsed, NoArgs=NoArgs);

//     console.log(results);

//     let names000 = results[results.length - 1];

//     let Datalist000 = results[results.length - 2];


//   //   const search0 = '\\[';
//   // const searchRegExp0 = new RegExp(search, 'g'); // Throws SyntaxError
//   // const replaceWith = '';
//   // const result = '5+2+1'.replace(searchRegExp0, replaceWith);

//   // const search1 = '\\]';
//   // const searchRegExp1 = new RegExp(search, 'g'); // Throws SyntaxError
  
//   // const result = '5+2+1'.replace(searchRegExp1, replaceWith);


//     // let names00 = names000.replace(/\[/g,'').replace('/]/g','').split(',').map(Number);

//     // let Datalist00 = Datalist000.replace(/\[/g,'').replace('/]/g', '').split(',')




//     const search0 = '\\[';
//     const searchRegExp0 = new RegExp(search0, 'g'); 
//     const replaceWith = '';
 

//     const search1 = '\\]';
//     const searchRegExp1 = new RegExp(search1, 'g'); 



//     const searchcommaReplaceData1 = '%$1&*&';
//     const commaReplaceData1Exp1 = new RegExp(searchcommaReplaceData1, 'g'); 
//     const commaReplaceData1 = ', ';


//     const searchcommaReplaceData2= '%$2&*&';
//     const commaReplaceData2Exp2 = new RegExp(searchcommaReplaceData2, 'g'); 
//     const commaReplaceData2 = ', ';


//     const searchRealcomma1 = ', ';
//     const searchRealcomma1Exp1 = new RegExp(searchRealcomma1, 'g'); 
//     const realCommaReplace = '$#@&5$' ;

//     const searchRealcomma2 = ',';
//     const searchRealcomma2Exp2 = new RegExp(searchRealcomma2, 'g'); 
    



//     // let Datalist00 = Datalist000.replace(searchRegExp0, replaceWith).replace(searchRegExp1, replaceWith).replace(searchRealcomma1Exp1, realCommaReplace).replace(searchRealcomma2Exp2, realCommaReplace).replace(commaReplaceData1Exp1, commaReplaceData1).replace(commaReplaceData2Exp2, commaReplaceData2).split(realCommaReplace);
    
//     // .split(realCommaReplace).map(Number);



//     // commaReplaceData1 = '%$1&*&' 
//     // commaReplaceData2 = '%$2&*&' 

//     // realCommaReplace = '$#@&5$' 

//     // OutputValueToAppend2 = OutputValueToAppend.replace(commaReplaceData1, ', ').replace(commaReplaceData2, ',')



    
//     // let DataList = Datalist0.replace("'",'').replace('"','').replace('[','').replace(']','').replace(', ',realCommaReplace).replace(commaReplaceData1,', ' ).replace(commaReplaceData2,',').split(realCommaReplace);

  




//     let names00 = names000.replace(searchRegExp0, replaceWith).replace(searchRegExp1, replaceWith).split(',').map(Number);

//     let Datalist00 = Datalist000.replace(searchRegExp0, replaceWith).replace(searchRegExp1, replaceWith).split(',').map(Number);



//     // let Datalist00 = Datalist000.replace(searchRegExp0, replaceWith).replace(searchRegExp1, replaceWith).replace(searchRealcomma1Exp1, realCommaReplace).replace(searchRealcomma2Exp2, realCommaReplace).replace(commaReplaceData1Exp1, commaReplaceData1).replace(commaReplaceData2Exp2, commaReplaceData2).split(realCommaReplace);





//     console.log(names00);

//     console.log('names00 above');

//     console.log(Datalist00);

//     console.log('Datalist00 above');



//     let names0 = PythonOrdToString(names00);

//     let Datalist0 = PythonOrdToString(Datalist00);


//     // let names0 = decodeBase64(names00);

//     // let Datalist0 = decodeBase64(Datalist00);

//     console.log(names0);

//     console.log(Datalist0);

//     console.log('names0 and datalist0 on javascrit part of the program')


//     let namesList = await names0.replace(/'/g, '').replace(/"/g, '').replace(/\[/g, '').replace(/]/g, '').split(', ');


//     // let namesList0 = await names0.replace("'",'').replace('"','').replace('[','').replace(']','');

//     // let namesList = await namesList0.split(', ');


    
//     // let DataList = await Datalist0.replace(/'/g, '').replace(/"/g, '').replace(/\[/g, '').replace(/]/g, '').split(', ');


//     let DataList = await Datalist0.replace(/'/g, '').replace(/"/g, '').replace(/\[/g, '').replace(/]/g, '').replace(searchRealcomma1Exp1, realCommaReplace).replace(searchRealcomma2Exp2, realCommaReplace).replace(commaReplaceData1Exp1, commaReplaceData1).replace(commaReplaceData2Exp2, commaReplaceData2).split(realCommaReplace);

//     // let DataList00 = await Datalist0.replace("'",'').replace('"','').replace('[','').replace(']','');

//     // let DataList = await DataList00.split(', ');




//     // let Datalist00 = Datalist000.replace(searchRegExp0, replaceWith).replace(searchRegExp1, replaceWith).replace(searchRealcomma1Exp1, realCommaReplace).replace(searchRealcomma2Exp2, realCommaReplace).replace(commaReplaceData1Exp1, commaReplaceData1).replace(commaReplaceData2Exp2, commaReplaceData2).split(realCommaReplace);



//     console.log(namesList);

//     console.log('namesList above');

//     console.log(DataList);

//     console.log('DataList above');


//     let columns = namesList;
//     let rows = DataList;
//     let result =  rows.reduce(function(result, field, index) {
//       result[columns[index]] = field;
//       return result;
//     }, {})
    
//     console.log(result);


//     return result


// }
exports.getDbDataSimple = getDbDataSimple;
