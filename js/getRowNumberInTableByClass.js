function getRowNumberInTableByClass(tableClass) {

    let tablesize = document.getElementsByClassName(tableClass)[0].rows.length;

    // console.log('tablesize', tablesize);

    numberOfRows = tablesize - 1;

    // console.log('numberOfRows', numberOfRows);

    return numberOfRows;

}
exports.getRowNumberInTableByClass = getRowNumberInTableByClass;
