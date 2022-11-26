


function AddTwoDataToListsSave(ListA, ListB, DataA, DataB) {


  return new Promise((resolve,_reject) =>{

    let process = require("process");

    let path = require("path");
  
    const currentWorkingDirectory = process.cwd();


    const { AddTwoDataToListsSaveFunction } = require(path.join(currentWorkingDirectory, './js/AddTwoDataToListsSaveFunction'));
  
  
    Done = AddTwoDataToListsSaveFunction(ListA, ListB, DataA, DataB)

  
    resolve(Done);

}

)



  // FindCoordinateInImageStep3()
}
exports.AddTwoDataToListsSave = AddTwoDataToListsSave;
