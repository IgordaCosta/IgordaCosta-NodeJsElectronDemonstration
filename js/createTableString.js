function createTableString(TableName, ColumnList) {
    // return new Promise((resolve,_reject) =>{

    string = " ( id integer PRIMARY KEY,";

    let i;
    for (i = 0; i < ColumnList.length; i++) {
        string = string + String(ColumnList[i]) + " TEXT, ";

    }

    string = string.slice(0, -2);

    string = string + ")";

    madeString = `CREATE TABLE IF NOT EXISTS ${TableName} ${string}`;

    // resolve(madeString)
    return madeString;


    // }
    // )
}
exports.createTableString = createTableString;
