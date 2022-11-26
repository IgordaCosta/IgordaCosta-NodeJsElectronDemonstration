function LMFItemCheckedHTML(datafillName, htmlBodyObject) {

    return new Promise((resolve, _reject) => {

        // console.log(datafillName);

        document.body.innerHTML = htmlBodyObject;

        let Done = true;

        resolve(Done);


    }
    );
}
exports.LMFItemCheckedHTML = LMFItemCheckedHTML;
