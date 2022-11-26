function placeInHTML2Id(HtmlAdded, item1,item2, ID1, ID2) {

    return new Promise((resolve, _reject) => {

        // console.log(HtmlAdded);

        // console.log("HtmlAdded in placeInHTML2Id func above ");

        document.getElementById(ID1).innerHTML = String(item1);

        document.getElementById(ID2).innerHTML = String(item2);

        let Done = true;

        resolve(Done);

    }

    );


}
exports.placeInHTML2Id = placeInHTML2Id;
