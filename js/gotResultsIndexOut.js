function gotResultsIndexOut() {


    document.body.innerHTML = `<div class="spinner3 spinner-border text-secondary" role="status">
                        <span class="sr-only">Loading...</span>
    
                    </div>
                    <div class="spinner3 down3">
                        <h1>Loading...</h1>
                    </div>

                    <div id="foreGroundImage" class="containingArea centered MainLogo noClickImg">
                        <img src="_images/LogInImg.png" id="LogoImg3" alt="Img" >
                        <img src="_images/FullBlackBackground.png" id="FullBlackBackground3" >
                    </div>`;
}
exports.gotResultsIndexOut = gotResultsIndexOut;
