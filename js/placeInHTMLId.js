function placeInHTMLId(HtmlAdded, datafillName, ID) {

    return new Promise((resolve, _reject) => {

        // console.log(HtmlAdded);

        // console.log("HtmlAdded in placeInHTMLId func above ");

        document.getElementById(ID).innerHTML = datafillName;

        let Done = true;

        resolve(Done);

    }

    );


}
exports.placeInHTMLId = placeInHTMLId;
