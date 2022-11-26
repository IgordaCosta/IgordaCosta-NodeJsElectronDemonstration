function CurrentWorkingPathFunc() {
    return new Promise((resolve, reject) => {
        try {
            var process = require('process');

            let CurrentWorkingPath = process.cwd();
            
            resolve(CurrentWorkingPath);
        }
        catch (err) {
            // console.log(err);
            reject(err);
        }

    }
    );
}
exports.CurrentWorkingPathFunc = CurrentWorkingPathFunc;
