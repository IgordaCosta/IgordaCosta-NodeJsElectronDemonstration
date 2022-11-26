

async function CreateImageWithMarkerStep5Return() {
  let process = require("process");

  let path = require("path");

  const currentWorkingDirectory = process.cwd();

  // const { fontSelect } = require(path.join(currentWorkingDirectory, './js/fontSelect'));
  const { getDbDataSimple } = require(path.join(currentWorkingDirectory, './js/getDbDataSimple'));

  const { CreateImageWithMarkerStep5Return2 } = require(path.join(currentWorkingDirectory, "./js/CreateImageWithMarkerStep5Return2"));




  let AwaitProveData = "getting Db Data";

  let TableName = '';

  let Database = '';

  let DataGotten = await getDbDataSimple(AwaitProveData, TableName, Database);

  // console.log(DataGotten)

  let newFileLocation = await DataGotten['LocationToPlaceOnWebPage'];

  let FontSize = await DataGotten['FontSize'];



  let tableTitles = await DataGotten['tableTitles2'];

  let tableData = await DataGotten['tableData2'];






  // console.log(FontSize);

  // console.log('FontSize above');




  // console.log(newFileLocation);

  // console.log('newFileLocation above');

  
  CreateImageWithMarkerStep5Return2(newFileLocation, FontSize, tableTitles, tableData);

}
exports.CreateImageWithMarkerStep5Return = CreateImageWithMarkerStep5Return;
