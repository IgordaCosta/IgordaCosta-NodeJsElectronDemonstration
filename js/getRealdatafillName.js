


function getRealdatafillName(filename){

    return new Promise((resolve,_reject) =>{

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()
    

    // const { gotResults } = require(path.join(currentWorkingDirectory,"./js/gotResults"));

    
    // if (gotResultsFuction){gotResults();}else{};
    

    // console.log("LoadMultipleFile function Started");


    let { PythonShell } = require("python-shell");

    let opcoes = {
        scriptPath: path.join(currentWorkingDirectory,"./_engine/"),
        // pythonPath: 'C:\\ProgramData\\Anaconda3\\python',

        pythonPath: currentWorkingDirectory + '\\e564\\Scripts\\python',

        
    };

    PythonShell.run(filename, opcoes, function (err, results) {
        if (err)
            throw err;

        // console.log(results);


        
            result = results[results.length - 1]
            // callback(results)

            resolve(result)
    
        
    }
    )   

    }

    );




}


exports.getRealdatafillName = getRealdatafillName;