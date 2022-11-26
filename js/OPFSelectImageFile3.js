

async function OPFSelectImageFile3() {
  let process = require("process");

  let path = require("path");

  const currentWorkingDirectory = process.cwd();

  const { getDbDataSimple } = require(path.join(currentWorkingDirectory, './js/getDbDataSimple'));

  const { OPFSelectImageFile4 } = require(path.join(currentWorkingDirectory, "./js/OPFSelectImageFile4"));




  let AwaitProveData = "getting Db Data";

  let TableName = '';

  let Database = '';

  let DataGotten = await getDbDataSimple(AwaitProveData, TableName, Database);

//   console.log(DataGotten)


  let tableTitles = await DataGotten['tableTitles'];

  let tableData = await DataGotten['tableData'];

  // console.log(tableTitles)


  OPFSelectImageFile4(tableTitles, tableData)

}
exports.OPFSelectImageFile3 = OPFSelectImageFile3;
