function gotResultsAdd() {

   

    let ResultsObj = `
                <div id="ResultsObj OntopOfAll">
                    <div id='OntopOfAll' class="spinner spinner-border text-secondary" role="status">
                        <span id='OntopOfAll' class="sr-only">Loading...</span>
    
                    </div>
                    <div id='OntopOfAll' class="spinner down">
                        <h1>Loading...</h1>
                    </div>

                    <div id="foreGroundImage" class="containingArea centered MainLogo noClickImg">
                        <img id='OntopOfAll' src="_images/LogInImg.png" alt="Img" >
                        <img id="FullBlackBackground OntopOfAll" class="blackBackground" src="_images/FullBlackBackground.png"  >
                    </div>
                </div>`;

    let  d1 = document.getElementById('BellowBody');
    d1.insertAdjacentHTML('afterbegin', ResultsObj);

    try{
    document.getElementById("AllNormalItems").classList.add('hidden')
    }catch{};


}
exports.gotResultsAdd = gotResultsAdd;
