function hideImage(){
        
    hideImageFunction()

    sleep(15000).then(() => UnHideImageFunction() );

}

function UnhideScroll(){
       
    showScrollfunction()

    sleep(15000).then(() => hideScroll() );

}


function hideImageFunction(){

    try {
        document.getElementsByClassName("MainLogo")[0].classList.add('hidden');
     }
     catch (e) {
        if (e instanceof TypeError) {
        
     }else{

   }
    }
    
}

function UnHideImageFunction(){

    try {
        document.getElementsByClassName("MainLogo")[0].classList.remove('hidden');
     }
     catch (e) {
        if (e instanceof TypeError) {

      }else{

      }
    }

}


function sleep(ms) {

   return new Promise(resolve => setTimeout(resolve, ms));

}


  function hideScroll(){

    try {

        document.getElementsByClassName("topPartSize")[0].classList.add('scrolloff');
        document.getElementsByClassName("topPartSize")[0].classList.remove('scrollON');
       
     }
     catch (e) {
        if (e instanceof TypeError) {

      }else{

     }
    }

}

function showScrollfunction(){

    try {

      document.getElementsByClassName("topPartSize")[0].classList.add('scrollON');
      document.getElementsByClassName("topPartSize")[0].classList.remove('scrolloff');

   }
     catch (e) {
        if (e instanceof TypeError) {

      }else{

     }
    }

}