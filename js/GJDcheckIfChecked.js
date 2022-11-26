



function Cancel (){
    location.replace("index.html");
}


function placeDatafillName(){
    
    var path = require("path")

    var process = require("process")

    let CurrentWorkingDirectory = process.cwd();

    // console.log(CurrentWorkingDirectory);

    // console.log('CurrentWorkingDirectory is above');

    const { getDatafillName } = require(path.join(CurrentWorkingDirectory,"./js/getDatafillName"));

    htmlBodyObject = `<div class="text">
        
    <h1>Are you sure you want to</h1> 
    <h1>continue with the Job Name bellow?</h1>
    <h1 id="datafillNameID"></h1>
     
</div>

<div id="foreGroundImage" class="containingArea centered MainLogo noClickImg">

    <img src="_images/LogInImg.png" onclick="hideImage()" alt="MainLogo" >

</div>
<div>
    <button type="button" class="btn optionsbtn right btn-secondary" onclick="GetJobDataJason()" >YES</button>
</div>
<div>
    <button type="button" class="btn optionsbtn left btn-secondary" onclick="Cancel()" >NO</button>
</div>
  
<script>placeDatafillName()</script>

<script>

    let jquerypath = path.join(__dirname, './js/jquery');
    window.jQuery = window.$ = require(jquerypath);

</script>
<script src="./js/popper.min.js"></script>
<script src="./js/bootstrap.min.js"></script>`;



getDatafillName(htmlBodyObject)


}
