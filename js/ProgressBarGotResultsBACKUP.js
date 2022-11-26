function createTimer(newtimeInMliSeconds){


    var countDownDate = new Date(newtimeInMliSeconds).getTime(); //it uses miliseconds instead of seconds
    
    
    
    // document.getElementById("demo").innerHTML =countDownDate;
    
    
    // Update the count down every 1 second
    var x = setInterval(function() {
    
      // Get today's date and time
      var now = new Date().getTime();
    
      // Find the distance between now and the count down date
      var distance = countDownDate - now;
    
      // Time calculations for days, hours, minutes and seconds
      var days = Math.floor(distance / (1000 * 60 * 60 * 24));
      var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
      // Display the result in the element with id="demo"
      document.getElementById("demo").innerHTML = days + "d " + hours + "h "
      + minutes + "m " + seconds + "s ";
    
      // If the count down is finished, write some text
      if (distance < 0) {
        clearInterval(x);
        document.getElementById("demo").innerHTML = "Almost Done";
      }
    }, 1000);
    
    
    
    };
    






function ProgressBarGotResults(FinalSaveLocation, rw, numberOfRows, percentDone) {

        
    let rwOutput = rw-1;

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
        <h1>by trying this Shortcuts. </h1>
        <h1>(just don't use the used files)</h1>

        
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
        <h7>${rwOutput}/${numberOfRows} completed</h7>
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



}
exports.ProgressBarGotResults = ProgressBarGotResults;
