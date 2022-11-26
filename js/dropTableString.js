function dropTableString(TableName) {
    // return new Promise((resolve,_reject) =>{

    dropTableStatement = "DROP TABLE IF EXISTS " + TableName;

    // resolve(dropTableStatement)
    return dropTableStatement;


    // }
    // )
}
exports.dropTableString = dropTableString;
