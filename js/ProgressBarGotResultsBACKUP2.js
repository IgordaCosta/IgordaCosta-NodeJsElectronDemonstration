const { configureRequestOptions } = require("builder-util-runtime");



function createTimer(NewEndTimeOfCompletion, AproxTotalTimeComplete, JsInitTimeInMliSeconds, CompareTimeNow){


    // let NewEndTimeOfCompletion1 = parseInt(NewEndTimeOfCompletion);

    let AproxTotalTimeComplete1 = parseInt(AproxTotalTimeComplete);

    // let JsInitTimeInMliSeconds1 = parseInt(JsInitTimeInMliSeconds)


    let CompareTimeNow1 = parseInt(CompareTimeNow);

    // let DifferenceToAdd = CompareTimeNow1 - NewEndTimeOfCompletion1

    // let NewEndTimeOfCompletion1AddedDiff = NewEndTimeOfCompletion1 + DifferenceToAdd

    let NewEndTimeOfCompletion1AddedDiff = CompareTimeNow1 + AproxTotalTimeComplete1

    console.log(NewEndTimeOfCompletion1AddedDiff)

    console.log('NewEndTimeOfCompletion1AddedDiff')

    // console.log(CompareTimeNow1);

    // console.log('CompareTimeNow1');

    // console.log(NewEndTimeOfCompletion1);

    // console.log('NewEndTimeOfCompletion1');

    // console.log(NewEndTimeOfCompletion1AddedDiff);

    // console.log('NewEndTimeOfCompletion1AddedDiff');

    // let nowtest = new Date().getTime();

    // console.log(nowtest)

    // console.log('nowtest')




    // let countDownDate = new Date(NewEndTimeOfCompletion1AddedDiff).getTime(); //it uses miliseconds instead of seconds

    let countDownDate = NewEndTimeOfCompletion1AddedDiff


    
    
    
    
    // document.getElementById("Timer").innerHTML =countDownDate;
    
    
    // Update the count down every 1 second
    let x = setInterval(function() {
    
      // Get today's date and time
      let now = new Date().getTime();


    //   let distanceFromStart = now - JsInitTimeInMliSeconds;

    //   let percentage = Math.floor(distanceFromStart/AproxTotalTimeComplete) * 100;
        

    //   console.log(countDownDate);
    //   console.log('countDownDate above')

      console.log(now);
      console.log('now above')

      console.log(countDownDate);

      console.log('countDownDate above');


    
      // Find the distance between now and the count down date
    //   let distance = countDownDate - now;

    // let distance = now - countDownDate;

    let distance = countDownDate - now;


    let percentage = parseInt(now/NewEndTimeOfCompletion1AddedDiff);

    print(percentage);

    print('percentage');


    // let distance = now - (AproxTotalTimeComplete1);

      console.log(distance);
      console.log('distance above')
    
      // Time calculations for days, hours, minutes and seconds
      let days = Math.floor(distance / (1000 * 60 * 60 * 24));
      let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      let seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
      // Display the result in the element with id="Timer"
      document.getElementById("Timer").innerHTML = "Less then: " + days + "d " + hours + "h "
      + minutes + "m " + seconds + "s ";

    //   document.getElementById("PercentMark").innerHTML = percentage + ' %';

    //   document.getElementById("progressBarUsed").ariaValueNow = percentage;

    //   document.getElementById("progressBarUsed").style.width = percentage +'%';


      
    
      // If the count down is finished, write some text
      if (distance < 0) {
        clearInterval(x);
        document.getElementById("Timer").innerHTML = "Almost Done";
      }
    }, 1000);
    
    
    
    };
    




function ProgressBarGotResults(NewEndTimeOfCompletion, AproxTotalTimeComplete, JsInitTimeInMliSeconds, CompareTimeNow) {

    createTimer(NewEndTimeOfCompletion, AproxTotalTimeComplete, JsInitTimeInMliSeconds, CompareTimeNow);

        
    // let rwOutput = rw-1;

    // <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" aria-valuenow="${percentDone}" aria-valuemin="0" aria-valuemax="100" style="width: ${percentDone}%"></div>

    document.body.innerHTML = `

    <script src="./js/fontawesome.js"></script>

    <script src="./js/ProgressBarGotResults.js"></script>

    <div class="spinner2 down2 awesome">
        <h1>Loading...</h1>
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
        <h7 id="Timer" ></h7>    
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



function ProgressBarGotResultsBACKUP(NewEndTimeOfCompletion, AproxTotalTimeComplete, JsInitTimeInMliSeconds) {

    createTimer(NewEndTimeOfCompletion, AproxTotalTimeComplete, JsInitTimeInMliSeconds);

        
    // let rwOutput = rw-1;

    // <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" aria-valuenow="${percentDone}" aria-valuemin="0" aria-valuemax="100" style="width: ${percentDone}%"></div>

    document.body.innerHTML = `

    <script src="./js/fontawesome.js"></script>

    <div class="spinner2 down2 awesome">
        <h1>Loading...</h1>
    </div>
    <div class="progressLocation2">
        <div class="progress">
            <div id="progressBarUsed" class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" aria-valuemin="0" aria-valuemax="100"></div>
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
        <h7 id="Timer" ></h7>    
    </div>

    <div class="TopProgressRight">
        <h7 id="PercentMark" ></h7>  
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

