function getNameOfLocations(NumList) {

    return new Promise((resolve, _reject) => {

        NumList = parseInt(NumList);

        let valuesList = [];
        let i;

        let firstValue = document.getElementById("validationTooltip0" + '1'.toString()).value;

        // console.log(firstValue);

        let MissingValuesList = [];

        let valuegotten = '';

        let valuegotten0 = '';

        // for (i = 0; i < NumList; i++) {
        for (i = 1; i < NumList + 1; i++) { // adding one to NumList and i allowed the the values to be gotten without error for Image



            // console.log("i used: " + i);

            // valuegotten = document.getElementById("validationTooltip0" + (i)).value;

            valuegotten0 = document.getElementById("validationTooltip0" + (i)).value;

            valuegotten = String(valuegotten0).replace(/,/g, '');

            // console.log(valuegotten);

            // console.log('valuegotten above');

            valuesList.push(valuegotten);
            if (valuegotten == '') {

                MissingValuesList.push(true);
            } else {

                MissingValuesList.push(false);
            };

        };

        let resultOut = [valuesList, MissingValuesList];

        resolve(resultOut);

    }




    );

}
exports.getNameOfLocations = getNameOfLocations;
