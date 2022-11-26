function EmpyFieldsHtmlCodehiddenReverced() {


    // var process = require("process");

    // var path = require("path");

    // const currentWorkingDirectory = process.cwd();

    // const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));



    document.body.innerHTML = `<div id="EmptyFields" class="alert">
        
    <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
    There are empty fields or the Excel file was not saved! Try again!
    
</div> 

<div class="text">
    
        <h1>Add information to the document.</h1>
        <h1>Save the document and click OK to continue</h1>
        <h1>or CANCEL to cancel the operation.</h1>
        
 
</div>

<div id="foreGroundImage" class="containingArea centered MainLogo noClickImg">

    <img src="_images/LogInImg.png" onclick="hideImage()" alt="MainLogo" >

</div>

<div>
    <button type="button" class="btn optionsbtn right btn-secondary" onclick="LMFAddInfoExcel()" >OK</button>
</div>
<div>
    <button type="button" class="btn optionsbtn left btn-secondary" onclick="Cancel()" >Cancel</button>
</div>





<script>

    let jquerypath = path.join(__dirname, './js/jquery');
    window.jQuery = window.$ = require(jquerypath);

</script>
<script src="./js/popper.min.js"></script>
<script src="./js/bootstrap.min.js"></script>`;




// let filename = 'LMFAddInfoExcel.py';
// let callback = '';
    
// RunPythonFile(filename, callback);

}
exports.EmpyFieldsHtmlCodehiddenReverced = EmpyFieldsHtmlCodehiddenReverced;
