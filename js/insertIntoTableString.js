function insertIntoTableString(TableName, ColumnList, ValuesList) {
    // return new Promise((resolve,_reject) =>{

    let string1 = " ( ";
    let string2 = " VALUES ( ";


    // console.log(TableName)

    // console.log('TableName above')


    // console.log(ValuesList)

    // console.log('ValuesList above 2')


    // console.log(ColumnList)

    // console.log('ColumnList above 2')


    for (i = 0; i < ColumnList.length; i++) {


        string1 = string1 + String(ColumnList[i]) + ", ";

        string2 = string2 + '"' + String(ValuesList[i]) + '"' + ", ";

    }


    string1 = string1.slice(0, -2);

    string1 = string1 + ")";


    string2 = string2.slice(0, -2);

    string2 = string2 + ")";



    commandMade = `INSERT INTO ${TableName} ${string1} ${string2}`;
    // commandMade = `INSERT INTO ${TableName} ${string2} ${string1}`;



    // console.log(commandMade)

    // console.log('insert insto table commandMade above')


    // resolve(commandMade);
    return commandMade;

    // }
    // )
}
exports.insertIntoTableString = insertIntoTableString;
