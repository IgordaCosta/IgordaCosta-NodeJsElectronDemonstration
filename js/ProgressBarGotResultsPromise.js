function ProgressBarGotResultsPromise(StartCommandToPrint,FinalSaveLocation, rw, numberOfRows, percentDone) {

    // console.log(StartCommandToPrint)

    return new Promise((resolve, _reject) => {

    // console.log(FinalSaveLocation, rw, numberOfRows, percentDone)

    document.body.innerHTML = `
    <script src="./js/fontawesome.js"></script>

    <div class="spinner2 down2 awesome">
        <h1>Loading...</h1>
    </div>
    <div class="progressLocation2">
        <div class="progress">
            <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" aria-valuenow="${percentDone}" aria-valuemin="0" aria-valuemax="100" style="width: ${percentDone}%"></div>
        </div>
    </div>
    
    <div class="spinner2 circleSpiner2 spinner-border text-secondary" role="status">
        <span class="sr-only">Loading...</span>
    </div>

    <div class="text2">

        <h1>While you wait, </h1>
        <h1>continue using your Windows Machine</h1>
        <h1>by trying this Shortcuts.</h1>

        
        <h1 class="important" >
            <i class="fa fas fa-exclamation-triangle" aria-hidden="true"></i>
            Take a picture of this 
        </h1>

        <h1 class="important rightImportant" >
            shortcuts before you start!
            <i class="fa fas fa-exclamation-triangle" aria-hidden="true"></i>
        </h1>   
        

    </div>

    <div class="orderedList2">
        
        <ul>
            <li>
                <h4>Windows + Ctrl + D – Open new virtual desktop</h4>
            </li>
            
            <li>
                <h4>Windows + Ctrl + F4 – Close virtual desktop</h4>
            </li>

            <li>
                <h4>Windows + Ctrl + arrow keys – Navigate between virtual desktops</h4>
            </li>

        </ul>
        

        

    </div>
    
    <div class="TopProgressLeft">
        <h7>${FinalSaveLocation}</h7>
    </div>

    <div class="TopProgressRight">
        <h7>${rw}/${numberOfRows} completed</h7>
    </div>

    <div class="BottomProgressRight">
        <h7>${percentDone}% completed</h7>
    </div>
    

    <div id="foreGroundImage" class="containingArea centered MainLogo noClickImg">

        <img src="_images/LogInImg.png" onclick="hideImage()" alt="MainLogo" >

    </div>
    
    <script>

        let jquerypath = path.join(__dirname, './js/jquery');
        window.jQuery = window.$ = require(jquerypath);

    </script>
    <script src="./js/popper.min.js"></script>
    <script src="./js/bootstrap.min.js"></script>

    `;


    Done="html changed"

    resolve(Done)

    }


    

    )
}
exports.ProgressBarGotResultsPromise = ProgressBarGotResultsPromise;
