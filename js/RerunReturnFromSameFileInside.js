function RerunReturnFromSameFileInside() {

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();


    const { runReturnFromSameFileInside } = require(path.join(currentWorkingDirectory, "./js/runReturnFromSameFileInside"));



    runReturnFromSameFileInside();

}
