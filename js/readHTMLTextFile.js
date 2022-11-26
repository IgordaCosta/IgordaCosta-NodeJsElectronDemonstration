function readHTMLTextFile(file) {

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()


    const { getBodyObjectFromHTMLFile } = require(path.join(currentWorkingDirectory,"./js/getBodyObjectFromHTMLFile"));

    return new Promise((resolve, _reject) => {
        // let allText = '';
        // let rawFile = new XMLHttpRequest();
        // rawFile.open("GET", file, false);
        // rawFile.onreadystatechange = function () {
        //     if (rawFile.readyState === 4) {
        //         if (rawFile.status === 200 || rawFile.status == 0) {
        //             allText = rawFile.responseText;



        fetch(file)
        .then(response => response.text())
        .then(text => getBodyObjectFromHTMLFile(text))
        .then(allTextResult=>resolve(allTextResult))

                

                    // let allTextResult = getBodyObjectFromHTMLFile(allText);

                    // resolve(allTextResult);

                // }
        //     }
        // };
        // rawFile.send(null);
        // rawFile.send(allTextResult);
        // return allText
    }

    );

}
exports.readHTMLTextFile = readHTMLTextFile;
