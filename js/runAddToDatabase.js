

function runAddToDatabase(){
    

    let {PythonShell} = require("python-shell");
    let path = require("path");

    const currentWorkingDirectory=process.cwd()

    let opcoes = {
        scriptPath : path.join(__dirname, './_engine/'),
        // pythonPath: 'C:\\ProgramData\\Anaconda3\\python',

        pythonPath: currentWorkingDirectory + '\\e564\\Scripts\\python',
    };

    // console.log(path.join(__dirname, './_engine/'));
    // console.log("startprint");
    PythonShell.run('AddToDatabase.py', opcoes, function (err, results) {
        if (err) throw err;
        
        // console.log("Finished Python File")

        location.replace("dragAndDrop.html")
        
    });
}