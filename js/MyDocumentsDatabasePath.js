function MyDocumentsDatabasePath(CurrenWorkingPath) {

    return new Promise((resolve, reject) => {
        // console.log("LoadMultipleFile function Started");

        let filename = 'FindMyDocumentsDatabasePath.py';

        let path = require("path");

        const currentWorkingDirectory=process.cwd();

        // let filenamecheck = path.basename(__dirname);

        // if (filenamecheck == "CSSAutoFormFiller") { }
        // else {
        //     __dirname = path.join(__dirname, '../../../../../../');

        // }
        // CurrenWorkingPath
        
        let { PythonShell } = require("python-shell");

        let opcoes = {

            // scriptPath: path.join(__dirname, './_engine/'),
            scriptPath: path.join(CurrenWorkingPath, './_engine/'),


            // pythonPath: 'C:\\ProgramData\\Anaconda3\\python',

            pythonPath: currentWorkingDirectory + '\\e564\\Scripts\\python',
        };



        PythonShell.run(filename, opcoes, function (err, results) {
            if (err)
                throw err;

            // console.log(results);

            let MydocumentsDbPath;

            MydocumentsDbPath = results[results.length - 1];



            // console.log(MydocumentsDbPath);

            // console.log('MydocumentsDbPath before return');

            // console.log('this is my document db path this should appear first')

            resolve(MydocumentsDbPath);

            if (err) { reject(err); }



        }


        );

        // return MydocumentsDbPath
    });

};
exports.MyDocumentsDatabasePath = MyDocumentsDatabasePath;
