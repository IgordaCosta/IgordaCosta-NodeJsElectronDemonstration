


async function AddTwoDataToListsSaveFunction(ListA, ListB, DataA, DataB) {


   
  let process = require("process");

  let path = require("path");

  const currentWorkingDirectory = process.cwd();



  const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, './js/AddtoTablePromise'));

  let finalLocationsX;
  let finalLocationsY;

  try {

    finalLocationsX = ListA.split(',');

    finalLocationsY = ListB.split(',');

  } catch {

    // console.log("it is just an empty list");

    // console.log('ListA :', ListA);

    // console.log('ListB :', ListB);

    finalLocationsX = ListA;

    finalLocationsY = ListB;

  }


  let lastTempLocationPointX = DataA;

  let lastTempLocationPointY = DataB;


  // console.log(finalLocationsX);

  // console.log('finalLocationsX');

  // console.log(finalLocationsY);

  // console.log('finalLocationsY');

  // console.log(lastTempLocationPointX);

  // console.log('lastTempLocationPointX');

  // console.log(lastTempLocationPointY);

  // console.log('lastTempLocationPointY');






  finalLocationsX.push(lastTempLocationPointX);

  finalLocationsY.push(lastTempLocationPointY);


  let AwaitProveData = 'add table started';

  let data = [finalLocationsX, finalLocationsY];

  let dataName = ['finalLocationsX', 'finalLocationsY'];

  let TableName = '';

  let Database = '';


  let Done = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);


  // console.log(Done);


  // console.log("GetImageCoordinatesNext function finished");

//   callback()

  return Done;



  // FindCoordinateInImageStep3()
}
exports.AddTwoDataToListsSaveFunction = AddTwoDataToListsSaveFunction;
