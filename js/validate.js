
function validate(documentID) {

    let checked = false;

    if (document.getElementById(documentID).checked) {
        checked = true;

        // console.log("checkbox is checked");
    }
    else {
        checked = false;

        // console.log("checkbox NOT checked");
    }
    return checked;
}
exports.validate = validate;
