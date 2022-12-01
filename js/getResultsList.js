function getResultsList(results) {



    return new Promise((resolve, _reject) => {

        let resultGotten = results[results.length - 1];




        resolve(resultGotten);

    }

    );


}
exports.getResultsList = getResultsList;
