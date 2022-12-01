

function RunPythonFile(filename, callback, gotResultsFuction=true, dataUsed = '', NoArgs=true) {

    if (callback ==''){

    return new Promise((resolve, _reject) => {

        
    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory=process.cwd();

    

    
    if (gotResultsFuction){
        

        const { gotResultsAdd } = require(path.join(currentWorkingDirectory,"./js/gotResultsAdd"));

        const { gotResultsRemove } = require(path.join(currentWorkingDirectory,"./js/gotResultsRemove"));
        
        

        gotResultsAdd();
    
    }else{};
    



    let { PythonShell } = require("python-shell");


    let PythonPathUsed = currentWorkingDirectory + '\\e564\\Scripts\\python';

    let opcoes;




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
    



    let { PythonShell } = require("python-shell");


    let PythonPathUsed = currentWorkingDirectory + '\\e564\\Scripts\\python';

    let opcoes;




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


        
    callback(results);

    }



);

};

try{
    gotResultsRemove();

}catch{}

};
exports.RunPythonFile = RunPythonFile;
