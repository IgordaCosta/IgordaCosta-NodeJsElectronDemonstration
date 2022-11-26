



function Cancel (){
    location.replace("index.html");
}


function SelectText(){

    location.replace("SelectText.html");
}


function LocationSavedSub(){


    location.replace("LocationSavedSub.html");

}



// function SortFilesIntoFoldersReturn(){

//     console.log('SortFilesIntoFolders function complete')


//     LocationSavedSub()


// }





function getSelectionText() {
    var textGotten = "";
    if (window.getSelection) {
        s = window.getSelection()
        textGotten = window.getSelection().toString();

    } else if (document.selection && document.selection.type != "Control") {
        s = document.selection.createRange()
        textGotten = document.selection.createRange().text;
    }


    // console.log(textGotten)

    // console.log("text gotten first in function")
    if (textGotten == ''){

        // console.log('this IS "" inside')

        return '', '', '';

    }else{
    oRange = s.getRangeAt(0); //get the text range
    // oRect = oRange.getBoundingClientRect();

    // console.log('this is not "" inside')


    // console.log(oRange)


    // console.log('oRange')

    // console.log(oRange.startOffset)

    // console.log(oRange.endOffset)

    let MinRange = oRange.startOffset

    let MaxRange = oRange.endOffset

    


    return [MinRange, MaxRange, textGotten];

}
}



async function getComparedText(){

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()

    const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));

    // const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory, './js/MyDocumentsDatabasePath'));

    const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, './js/AddtoTablePromise'));

   


    let SelectedTextGotten = getSelectionText()

    // console.log(SelectedTextGotten)

    let textGotten =SelectedTextGotten[2]




    if (String(textGotten)=='undefined'){}else{

    let MinRange = SelectedTextGotten[0]

    let MaxRange =SelectedTextGotten[1]

   
    // let MydocumentsDbPath = await MyDocumentsDatabasePath(currentWorkingDirectory)

    // let CurrentWorkingPath = currentWorkingDirectory

    let Database=''

    let TableName=''

   
    
    AwaitProveData='starting add to database'

    // let data = [finalLocationsX, finalLocationsY]
    
    // let dataName = ['finalLocationsX', 'finalLocationsY']
    
    let data = [MinRange, MaxRange]
    
    let dataName = ['MinRange', 'MaxRange' ]



    let Done = await AddtoTablePromise(AwaitProveData,data, dataName, TableName,Database)

    // console.log(Done)


    let filename='SortFilesIntoFolders.py';
    let callback=LocationSavedSub;

    RunPythonFile(filename,callback)







    // console.log(MinRange)

    // console.log('MinRange')

    // console.log(MaxRange)

    // console.log('MaxRange')

    // console.log(textGotten)
    // console.log('textGotten')






    }
}


function placeDatafillName(){

    
    var path = require("path")

    var process = require("process")

    let CurrentWorkingDirectory = process.cwd();

    // console.log(CurrentWorkingDirectory);

    // console.log('CurrentWorkingDirectory is above');

    const { getFileName } = require(path.join(CurrentWorkingDirectory,"./js/getFileName"));

    htmlBodyObject = `<div class="text">
        
        <h1 class="disable-select">Drag on the text bellow to</h1>  
        <h1 class="disable-select">select the area where different </h1> 
        <h1 class="disable-select">text will be separate into </h1> 
        <h1 class="disable-select">different folders</h1>
        <h1 class="disable-select">while the same text in the </h1>  
        <h1 class="disable-select">location will be in the same folder</h1>
        <br>
        <h1 id="FilenameOnlyID"></h1>

     
</div>

<div id="foreGroundImage" class="containingArea centered MainLogo noClickImg">

    <img src="_images/LogInImg.png" onclick="hideImage()" alt="MainLogo" >

</div>
<div>
    <button type="button" class="btn optionsbtn right btn-secondary" onclick="getComparedText()" >OK</button>
</div>


<div id="TextNotSelected" class="alert hidden">
        
    <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
    Please click and drag to select text on the file name and click OK to continue

</div> 

  
<script>placeDatafillName()</script>

<script>

    let jquerypath = path.join(__dirname, './js/jquery');
    window.jQuery = window.$ = require(jquerypath);

</script>
<script src="./js/popper.min.js"></script>
<script src="./js/bootstrap.min.js"></script>`;



getFileName(htmlBodyObject)


}
