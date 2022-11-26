function gotResults() {


    document.body.innerHTML = `<div class="spinner spinner-border text-secondary" role="status">
                        <span class="sr-only">Loading...</span>
    
                    </div>
                    <div class="spinner down">
                        <h1>Loading...</h1>
                    </div>

                    <div id="foreGroundImage" class="containingArea centered MainLogo noClickImg">
                        <img src="_images/LogInImg.png" id="LogoImg" alt="Img" >
                        <img src="_images/FullBlackBackground.png" id="FullBlackBackground" >
                    </div>`;
}
exports.gotResults = gotResults;
