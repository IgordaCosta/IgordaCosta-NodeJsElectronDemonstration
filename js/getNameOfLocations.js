function getNameOfLocations(NumList) {

    return new Promise((resolve, _reject) => {

        NumList = parseInt(NumList);

        let valuesList = [];
        let i;

        let firstValue = document.getElementById("validationTooltip0" + '1'.toString()).value;


        let MissingValuesList = [];

        let valuegotten = '';

        let valuegotten0 = '';






            valuegotten0 = document.getElementById("validationTooltip0" + (i)).value;

            valuegotten = String(valuegotten0).replace(/,/g, '');



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
