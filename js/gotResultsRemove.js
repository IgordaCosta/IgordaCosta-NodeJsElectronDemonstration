function gotResultsRemove() {

    let myobj = document.getElementById('ResultsObj');
    myobj.remove(); 

    document.getElementById("AllNormalItems").classList.remove('hidden')

}
exports.gotResultsRemove = gotResultsRemove;
