

function RunPythonFile(filename, callback, gotResultsFuction=true, dataUsed = '', NoArgs=true) {

    if (callback ==''){

    return new Promise((resolve, _reject) => {

        
    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory=process.cwd();

    

    
    if (gotResultsFuction){
        
        // const { gotResults } = require(path.join(currentWorkingDirectory,"./js/gotResults"));

        const { gotResultsAdd } = require(path.join(currentWorkingDirectory,"./js/gotResultsAdd"));

        const { gotResultsRemove } = require(path.join(currentWorkingDirectory,"./js/gotResultsRemove"));
        
        

        gotResultsAdd();
        // gotResults();
    
    }else{};
    

    // console.log("LoadMultipleFile function Started");


    let { PythonShell } = require("python-shell");

    // let PythonPathUsed = 'C:\\ProgramData\\Anaconda3\\python'

    let PythonPathUsed = currentWorkingDirectory + '\\e564\\Scripts\\python';

    let opcoes;

    // console.log(NoArgs);

    // console.log('NoArgs above');


    if (NoArgs){
        opcoes = {
            scriptPath: path.join(currentWorkingDirectory,"./_engine/"),
            pythonPath: PythonPathUsed,
        
        };
    
    }else{
        opcoes = {
            args : [dataUsed],
            scriptPath: path.join(currentWorkingDirectory,"./_engine/"),
            pythonPath: PythonPathUsed,
            
        };
    
    }

    PythonShell.run(filename, opcoes, function (err, results) {
        if (err)
            throw err;

            // console.log(results);

            resolve(results);


    }

    );

}

);


}else{



    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory=process.cwd();

    
    if (gotResultsFuction){
        
        const { gotResults } = require(path.join(currentWorkingDirectory,"./js/gotResults"));
        
        gotResults();
    
    }else{};
    

    // console.log("LoadMultipleFile function Started");


    let { PythonShell } = require("python-shell");

    // let PythonPathUsed = 'C:\\ProgramData\\Anaconda3\\python'

    let PythonPathUsed = currentWorkingDirectory + '\\e564\\Scripts\\python';

    let opcoes;

    // console.log(NoArgs);

    // console.log('NoArgs above');


    if (NoArgs){
        opcoes = {
            scriptPath: path.join(currentWorkingDirectory,"./_engine/"),
            pythonPath: PythonPathUsed,
        
        };
    
    }else{
        opcoes = {
            args : [dataUsed],
            scriptPath: path.join(currentWorkingDirectory,"./_engine/"),
            pythonPath: PythonPathUsed,
            
        };
    
    }

    PythonShell.run(filename, opcoes, function (err, results) {
        if (err)
            throw err;

        // console.log(results);

        
    callback(results);

    }



);

};

try{
    gotResultsRemove();

}catch{}

};
exports.RunPythonFile = RunPythonFile;
