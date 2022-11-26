async function AddAnyDataToHtml(htmlBodyObject,DataToAdd,HtmlID) {

    var process = require('process');

    var path = require('path');

    let CurrentWorkingDirectory = process.cwd();

    // console.log(CurrentWorkingDirectory);

    // console.log('CurrentWorkingDirectory is above');

    const { LMFItemCheckedHTML } = require(path.join(CurrentWorkingDirectory, "./js/LMFItemCheckedHTML"));
    const { placeInHTMLId } = require(path.join(CurrentWorkingDirectory, "./js/placeInHTMLId"));

    
    let datafillName = DataToAdd;
    let ID = HtmlID;

    HtmlAdded = await LMFItemCheckedHTML(datafillName, htmlBodyObject);

    Done = await placeInHTMLId(HtmlAdded, datafillName, ID);

    // console.log("Finished placing variable on HTML:", Done);

    process.chdir(CurrentWorkingDirectory)

}
exports.AddAnyDataToHtml = AddAnyDataToHtml;