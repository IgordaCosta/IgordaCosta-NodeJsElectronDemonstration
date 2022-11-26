function getResultsList(results) {



    return new Promise((resolve, _reject) => {
        // console.log(results)

        let resultGotten = results[results.length - 1];




        // let systemFontsResult=resultGotten.split('|')
        resolve(resultGotten);

    }

    );


}
exports.getResultsList = getResultsList;
