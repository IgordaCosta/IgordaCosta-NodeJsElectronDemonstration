function gotResultsRemove() {


    let Ani = document.getElementById('AllNormalItems')

    try{

        Ani.insertAdjacentHTML('afterbegin', ResultsObj);
        }catch{}

    Ani.classList.remove('hidden');
    
       


    try{

        let spn = document.getElementsByClassName("spinner");
        spn[0].classList.add('hidden');
        spn[1].classList.add('hidden');
    
    }catch{};

    try{

        let spn2 = document.getElementsByClassName("MainLogo");
        spn2[0].classList.add('hidden');
    
    }catch{};

    

}
exports.gotResultsRemove = gotResultsRemove;
