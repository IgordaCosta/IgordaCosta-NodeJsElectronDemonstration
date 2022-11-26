// var iconv = require('iconv-lite');
// const { AddToDatabaseReturn } = require("./DragnDrop");




// dragAndDropQR.html


function dragAndDropQRReloadError(){

    document.body.innerHTML =`
        <div>
            <h1>Browse using the file input for .txli file and click OK or</h1>
            <br>
            <h1>Drag and Drop your .txli file inside this window</h1> 
            <br>
            <h1> to add it to the database</h1>
            <br>
            <h3>Check for the .txli in the file extesions</h3>

        </div>
        <div id="TempFile" class="alert hidden">

            <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
                Filename starts with temp_! This filename is not allowed! 

        </div> 
        <div id="ExcelFile" class="alert hidden">

            <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
                This is NOT an .txli file! Check if its a supported .txli extension file.

        </div> 


        <div id="NotValidQRFile" class="alert ">

            <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
                The file choosen for .txli is not supported. Please choose a supported .txli file and click OK to continue.

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


}








function dragAndDropQR (){
    location.replace('dragAndDropQR.html');
}



async function getTextfromQRReturn(){

    // console.log('getTextfromQRReturn function')

    // var iconv = require('iconv-lite');
    
    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();


  
    const { OperationComplete } = require(path.join(currentWorkingDirectory, "./js/OperationComplete"));

    var process = require("process");

    var path = require("path")


    const { getDbDataSimple } = require(path.join(currentWorkingDirectory, "./js/getDbDataSimple"));


    let AwaitProveData= "ok"

    let TableName = ''

    let Database = ''

    let tableGotten=await getDbDataSimple(AwaitProveData,TableName,Database)

    ResultFunction = tableGotten['ResultFunction']


    if (ResultFunction == 'Done'){


        OperationComplete()



    }else if (ResultFunction == 'Error'){

        dragAndDropQRReloadError()

    }else{

        // console.log('only two options possible, done or error, option chosen bellow')

        // console.log(ResultFunction)

    }




    






}



async function DragnDropMidQR0(pathUsed) {

    var iconv = require('iconv-lite');
    
    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory = process.cwd();


    // const { insertIntoDatabase } = require(path.join(currentWorkingDirectory,"./js/insertIntoDatabase"));
    const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, "./js/AddtoTablePromise"));


    // const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory,"./js/MyDocumentsDatabasePath"));
    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));

    // const { AddToDatabaseReturn } = require(path.join(currentWorkingDirectory, "./js/AddToDatabaseReturn"));

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


    // let excelExtensions = ['xlsx', 'xlsm', 'xlsb', 'xlam', 'xltx', 'xltm', 'xls', 'xla', 'xlt', 'xlm', 'xlw', 'csv'];

    // let imageExtensions = ['jpg', 'jpeg', 'jpe', 'jfif', 'gif', 'tif', 'tiff', 'png', 'heic', 'bmp', 'dib'];

    let txlieExtensions = ['txli'];

    // let pdfExtensions = ['pdf'];

    // let wordExtesions = ['doc', 'xml', 'docx', 'docm', 'dotx', 'dotm', 'dot', 'xps', 'mht', 'mhtml', 'htm', 'html', 'rtf', 'txt', 'xml', 'odt'];



    dataName = 'ExtensionType';

    let ok1 = false;

    // 

    let continueON = false;

    if (txlieExtensions.indexOf(filenameEnding) > -1) {

        continueON = true;

        // console.log('its an txtli file')

        

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

    // } else if (wordExtesions.indexOf(filenameEnding) > -1) {

    //     ok1 = true;

    //     data = 'word';

    //     AwaitProveData = "Started AddtoTablePromise for: " + data;

    //     let DoneAddtoTablePromise = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);

    //     console.log(DoneAddtoTablePromise);


    } else {
        // console.log("NOT an excel file");
        // document.getElementById("ExcelFile").classList.remove('hidden');
        NotSupportedFileRetun();
    }

    if (continueON){ 
        if (first5char == "temp_") {
            // console.log("Filename starts with temp_! This filename is not allowed!")
            // document.getElementById("TempFile").classList.remove('hidden');
            NotSupportedTempFileRetun();
        } else {
            if (ok1 == true) {
                // console.log("All is OK!!!!");

                // let filename = 'AddToDatabase.py';

                // let callback = AddToDatabaseReturn;

                // RunPythonFile(filename, callback);


                // console.log('continue from here for Its a Image file')


                // let filename = 'getTextfromQR.py';

                let filename = 'getTextfromTxli.py';

                


                let callback = getTextfromQRReturn;

                RunPythonFile(filename, callback);


            }

        } 

    }else{};
}




function NotSupportedFileRetun(){



    document.body.innerHTML =
    `
    <div>
    <h1>Browse using the file input and click OK or</h1>
    <br>
    <h1>Drag and Drop your QR file inside this window</h1> 
    <br>
    <h1> to add it to the database</h1>
    <br>
    <h3>The QR file uses image extesions</h3>
    <!-- <h3>.jpg , .xlsm, .xlsb, .xlam , .xltx, .xltm, .xls, .xla, .xlt, .xlm and .xlw</h3> -->
</div>
<div id="TempFile" class="alert hidden">

    <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
    Filename starts with temp_! This filename is not allowed! 

</div> 
<div id="ExcelFile" class="alert">
    
    <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
    This is NOT an Image file! Check if its a supported image extension.
    
</div> 


<div id="NotValidQRFile" class="alert hidden">
    
    <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
    The file choosen for QR is not supported. Please choose a supported QR file and click OK to continue.
    
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





}


















function NotSupportedTempFileRetun(){



    document.body.innerHTML =
    `
    <div>
    <h1>Browse using the file input and click OK or</h1>
    <br>
    <h1>Drag and Drop your QR file inside this window</h1> 
    <br>
    <h1> to add it to the database</h1>
    <br>
    <h3>The QR file uses image extesions</h3>
    <!-- <h3>.jpg , .xlsm, .xlsb, .xlam , .xltx, .xltm, .xls, .xla, .xlt, .xlm and .xlw</h3> -->
</div>
<div id="TempFile" class="alert">

    <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
    Filename starts with temp_! This filename is not allowed! 

</div> 
<div id="ExcelFile" class="alert hidden">
    
    <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
    This is NOT an Image file! Check if its a supported image extension.
    
</div> 


<div id="NotValidQRFile" class="alert hidden">
    
    <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
    The file choosen for QR is not supported. Please choose a supported QR file and click OK to continue.
    
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





}













exports.DragnDropMidQR0 = DragnDropMidQR0;
