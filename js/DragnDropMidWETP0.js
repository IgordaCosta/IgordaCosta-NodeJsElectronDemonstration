// var iconv = require('iconv-lite');
// const { AddToDatabaseReturn } = require("./DragnDrop");


function LocationSaved(){

    location.replace("LocationSaved.html");

}






async function DragnDropMidWETP0(pathUsed) {

    var iconv = require('iconv-lite');
    
    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();


    // const { insertIntoDatabase } = require(path.join(currentWorkingDirectory,"./js/insertIntoDatabase"));
    const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, "./js/AddtoTablePromise"));


    // const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory,"./js/MyDocumentsDatabasePath"));
    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));

    // const { OperationComplete } = require(path.join(currentWorkingDirectory, "./js/OperationComplete"));

    // const { getDbData } = require(path.join(currentWorkingDirectory,"./js/getDbData"));
    let buff = Buffer.from(pathUsed, 'utf8');


    let fileLocation = iconv.decode(buff, 'utf8');


    let data = fileLocation;

    let dataName = 'fileLocation';




    // console.log(data);
    // console.log('ValuesList above 0');

    // console.log(dataName);
    // console.log('ColumnList above 0');

    ColumnList = dataName;

    ValuesList = data;

    // let MydocumentsDbPath = await MyDocumentsDatabasePath(currentWorkingDirectory)
    let TableName = '';

    let Database = '';

    let AwaitProveData = "first add to table promisse started";

    // let Done=await insertIntoDatabase(data,dataName,MydocumentsDbPath,currentWorkingDirectory,TableName,Database)
    let Done = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);


    // console.log(Done);


    // console.log('File(s) you dragged here: ', fileLocation);


    let FilelocationList = fileLocation.split("\\");

    // console.log(FilelocationList);
    let filename = FilelocationList[FilelocationList.length - 1];
    // console.log(filename);
    let filenameDotList = filename.split(".");

    let filenameEnding = filenameDotList[filenameDotList.length - 1];

    // console.log(filenameEnding);
    let first5char = filename.slice(0, 5);


    let excelExtensions = ['xlsx', 'xlsm', 'xlsb', 'xlam', 'xltx', 'xltm', 'xls', 'xla', 'xlt', 'xlm', 'xlw', 'csv'];

    // let imageExtensions = ['jpg', 'jpeg', 'jpe', 'jfif', 'gif', 'tif', 'tiff', 'png', 'heic', 'bmp', 'dib'];


    let imageExtensions = ['jpg' ,'jpeg' ,'jpe' ,'jfif' ,'bmp' ,'dib' ,'gif' ,'png' ,'tiff'];

    // let pdfExtensions = ['pdf'];

    // let wordExtesions = ['doc', 'xml', 'docx', 'docm', 'dotx', 'dotm', 'dot', 'xps', 'mht', 'mhtml', 'htm', 'html', 'rtf', 'txt', 'xml', 'odt'];

    let wordExtesions = ['docx'];



    dataName = 'ExtensionType';

    let ok1 = false;

    if (excelExtensions.indexOf(filenameEnding) > -1) {
        // console.log("this is an excel file");
        ok1 = true;

        data = 'excel';

        AwaitProveData = "Started AddtoTablePromise for: " + data;

        let DoneAddtoTablePromise = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);

        // console.log(DoneAddtoTablePromise);

    } else if (imageExtensions.indexOf(filenameEnding) > -1) {
            // console.log("this is an excel file");
            ok1 = true;
    
            data = 'image';
    
            AwaitProveData = "Started AddtoTablePromise for: " + data;
    
            let DoneAddtoTablePromise = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);
    
            // console.log(DoneAddtoTablePromise);

    // } else if (pdfExtensions.indexOf(filenameEnding) > -1) {

    //     ok1 = true;

    //     dataName = ['ExtensionType','PdfLocation'];

    //     data = ['pdf',fileLocation];

    //     AwaitProveData = "Started AddtoTablePromise for: " + data;

    //     let DoneAddtoTablePromise = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);

    //     console.log(DoneAddtoTablePromise);

    // 
    } else if (wordExtesions.indexOf(filenameEnding) > -1) {

        ok1 = true;

        data = 'word';

        AwaitProveData = "Started AddtoTablePromise for: " + data;

        let DoneAddtoTablePromise = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);

        // console.log(DoneAddtoTablePromise);


    } else {
        // console.log("NOT an excel file");
        // document.getElementById("ExcelFile").classList.remove('hidden');
        
        DragNDropWETPNotSupporteTypeReload()

    }


    if (first5char == "temp_") {
        // console.log("Filename starts with temp_! This filename is not allowed!")
        // document.getElementById("TempFile").classList.remove('hidden');
        DragNDropWETPTempNotSupporteReload(

        )
    } else {
        if (ok1 == true) {
            // console.log("All is OK!!!!");

            let filename = 'WordOrExcelToPdf.py';

            // let callback = OperationComplete;

            let callback = LocationSaved;

            RunPythonFile(filename, callback);


        }

    }
}






function DragNDropWETPTempNotSupporteReload (){
    document.body.innerHTML =`
    <div>
    <h1>Browse using the file input and click OK or</h1>
    <br>
    <h1>Drag and Drop your Image , Excel or Word (docx) file inside this window</h1> 
    <br>
    <h1>to change it to Pdf format</h1>
    <br>
    <h3>Only Image, Excel and Word supported extensions are allowed</h3>
   
</div>
<div id="TempFile" class="alert">

    <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
    Filename starts with temp_! This filename is not allowed! 

</div> 
<div id="ExcelFile" class="alert hidden">
    
    <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
    This file exentension is not suppoted! Please check supported file extensions.
    
</div> 

<div id="fileLocation" class="input-group">
    <div class="custom-file">
      <input type="file" class="custom-file-input" id="inputGroupFile04" aria-describedby="inputGroupFileAddon04">
      <label class="custom-file-label" for="inputGroupFile04">Choose file</label>
    </div>
    <div class="input-group-append">
      <button class="btn btn-outline-secondary" type="button" id="inputGroupFileAddon04" onclick="DragnDrop3()">OK</button>
    </div>
  </div>





<div id="foreGroundImage" class="containingArea centered MainLogo noClickImg">

    <img src="_images/LogInImg.png" onclick="hideImage()" alt="MainLogo" >

</div>
<div>
    <button type="button" class="btn optionsbtn left btn-secondary" onclick="Cancel()" >Cancel</button>
</div>

<script>
    DragnDrop2()
</script>

<script>

    let jquerypath = path.join(__dirname, './js/jquery');
    window.jQuery = window.$ = require(jquerypath);

</script>
<script src="./js/popper.min.js"></script>
<script src="./js/bootstrap.min.js"></script>
    `
    
};







function DragNDropWETPNotSupporteTypeReload (){
    document.body.innerHTML =`
    <div>
    <h1>Browse using the file input and click OK or</h1>
    <br>
    <h1>Drag and Drop your Image , Excel or Word (docx) file inside this window</h1> 
    <br>
    <h1>to change it to Pdf format</h1>
    <br>
    <h3>Only Image, Excel and Word supported extensions are allowed</h3>
   
</div>
<div id="TempFile" class="alert hidden">

    <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
    Filename starts with temp_! This filename is not allowed! 

</div> 
<div id="ExcelFile" class="alert">
    
    <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
    This file exentension is not suppoted! Please check supported file extensions.
    
</div> 

<div id="fileLocation" class="input-group">
    <div class="custom-file">
      <input type="file" class="custom-file-input" id="inputGroupFile04" aria-describedby="inputGroupFileAddon04">
      <label class="custom-file-label" for="inputGroupFile04">Choose file</label>
    </div>
    <div class="input-group-append">
      <button class="btn btn-outline-secondary" type="button" id="inputGroupFileAddon04" onclick="DragnDrop3()">OK</button>
    </div>
  </div>





<div id="foreGroundImage" class="containingArea centered MainLogo noClickImg">

    <img src="_images/LogInImg.png" onclick="hideImage()" alt="MainLogo" >

</div>
<div>
    <button type="button" class="btn optionsbtn left btn-secondary" onclick="Cancel()" >Cancel</button>
</div>

<script>
    DragnDrop2()
</script>

<script>

    let jquerypath = path.join(__dirname, './js/jquery');
    window.jQuery = window.$ = require(jquerypath);

</script>
<script src="./js/popper.min.js"></script>
<script src="./js/bootstrap.min.js"></script>
    `
    
};





exports.DragnDropMidWETP0 = DragnDropMidWETP0;
