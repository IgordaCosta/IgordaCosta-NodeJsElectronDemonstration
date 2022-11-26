
async function DragnDropMid0(pathUsed) {

    const iconv = require('iconv-lite');
    const process = require("process");
    const path = require("path");
    const currentWorkingDirectory = process.cwd();

    const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, "./js/AddtoTablePromise"));
    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));
    const { AddToDatabaseReturn } = require(path.join(currentWorkingDirectory, "./js/AddToDatabaseReturn"));

    let buff = Buffer.from(pathUsed, 'utf8');
    let fileLocation = iconv.decode(buff, 'utf8');

    let ColumnList = 'fileLocation';
    let ValuesList = fileLocation;
    
    let dataName = [ColumnList,'currentWorkingDirectory'];
    let data = [ValuesList, currentWorkingDirectory ];
    let TableName = '';
    let Database = '';

    let AwaitProveData = "first add to table promisse started";

    let Done = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);
    let FilelocationList = fileLocation.split("\\");

    let filename = FilelocationList[FilelocationList.length - 1];

    let filenameDotList = filename.split(".");

    let filenameEnding = filenameDotList[filenameDotList.length - 1];

    let first5char = filename.slice(0, 5);

    let imageExtensions = ['jpg', 'jpeg', 'jpe', 'jfif', 'gif', 'tif', 'tiff', 'png', 'heic', 'bmp', 'dib'];
    let pdfExtensions = ['pdf'];

    dataName = 'ExtensionType';

    let ok1 = false;
   
    if (imageExtensions.indexOf(filenameEnding) > -1) {

        ok1 = true;
        data = 'image';

        AwaitProveData = "Started AddtoTablePromise for: " + data;

        let DoneAddtoTablePromise = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);

    } else if (pdfExtensions.indexOf(filenameEnding) > -1) {

        ok1 = true;

        dataName = ['ExtensionType','PdfLocation'];
        data = ['pdf',fileLocation];

        AwaitProveData = "Started AddtoTablePromise for: " + data;

        let DoneAddtoTablePromise = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);

    } else {

        DragNDropNotSupporteTypeReload ();

    }

    if (first5char == "temp_") {

        DragNDropTempNotSupporteReload();

    } else {
        
        if (ok1 == true) {
        
            let filename = 'AddToDatabase.py';
            let callback = AddToDatabaseReturn;

            RunPythonFile(filename, callback, gotResultsFuction=true, dataUsed = currentWorkingDirectory, NoArgs=false);

        }

    }


};


function DragNDropNotSupporteTypeReload (){

    document.body.innerHTML =`
        <div>
    
            <h1>Browse using the file input and click OK or</h1>
            <br>
            <h1>Drag and Drop a supported </h1>
            <br>
            <h1>pdf or image file inside this window</h1> 
            <br>
            <h1> to add it to the database</h1>

        
        </div>
        <div id="TempFile" class="alert hidden">

            <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
            Filename starts with temp_! This filename is not allowed! 

        </div> 
        <div id="ExcelFile" class="alert">
        
            <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
            This is NOT a pdf or image file type, please check supported extensions.
            
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
    `;
    
};




function DragNDropTempNotSupporteReload (){
    
    document.body.innerHTML =`
    
    <div>
        <h1>Browse using the file input and click OK or</h1>
        <br>
        <h1>Drag and Drop a supported </h1>
        <br>
        <h1>pdf or image file inside this window</h1> 
        <br>
        <h1> to add it to the database</h1>
        
    </div>
    <div id="TempFile" class="alert">

        <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
        Filename starts with temp_! This filename is not allowed! 

    </div> 
    <div id="ExcelFile" class="alert hidden">
        
        <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
        This is NOT a pdf or image file type, please check supported extensions.
        
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
    `;
    
};



exports.DragnDropMid0 = DragnDropMid0;
