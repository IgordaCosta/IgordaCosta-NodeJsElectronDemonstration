function hideImage(){

    // console.log("hide image init ran")
        
    hideImageFunction()

    sleep(15000).then(() => UnHideImageFunction() );

}


function hideImageFunction(){


    // console.log("hide image inititated");

    try {
        document.getElementsByClassName("MainLogo")[0].classList.add('hidden');
     }
     catch (e) {
        if (e instanceof TypeError) {
        
        // console.log("user asked to go to the new window witout it finished hidding, its ok");
        // console.log(e);
     }else{
        //  console.log("SOME OTHER ERROR HAPPENED!");
        //  console.log(e);
     }
    }

    // console.log("hide image terminated");

    
}


function UnHideImageFunction(){

    // console.log("UNhide image inititated!!!!!!");


    try {
        document.getElementsByClassName("MainLogo")[0].classList.remove('hidden');
     }
     catch (e) {
        if (e instanceof TypeError) {
        
        // console.log("user asked to go to the new window witout it finished hidding, its ok");
        // console.log(e);
     }else{
        //  console.log("SOME OTHER ERROR HAPPENED!");
        //  console.log(e);
     }
    }

    // console.log("UNhide image terminated!!!!!!");

}














function sleep1(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  function sleep2(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }



function UnhideScroll1(){

    // console.log("unhide scroll init ran")
        
    showScrollfunction1()

    sleep1(15000).then(() => hideScroll1() );

}


function hideScroll1(){


    // console.log("hide scroll inititated");

    try {

        document.getElementsByClassName("topPartSize1")[0].classList.add('scrolloff');
        document.getElementsByClassName("topPartSize1")[0].classList.remove('scrollON');
       
     }
     catch (e) {
        if (e instanceof TypeError) {
        
        // console.log("user asked to go to the new window witout it finished hidding, its ok");
        // console.log(e);
     }else{
        //  console.log("SOME OTHER ERROR HAPPENED!");
        //  console.log(e);
     }
    }

    // console.log("hide scroll terminated");


}

function showScrollfunction1(){


    // console.log("UNhide scroll inititated!!!!!!");

    try {
        document.getElementsByClassName("topPartSize1")[0].classList.add('scrollON');
        document.getElementsByClassName("topPartSize1")[0].classList.remove('scrolloff');
     }
     catch (e) {
        if (e instanceof TypeError) {
        
        // console.log("user asked to go to the new window witout it finished hidding, its ok");
        // console.log(e);
     }else{
        //  console.log("SOME OTHER ERROR HAPPENED!");
        //  console.log(e);
     }
    }

    // console.log("UNhide scroll terminated!!!!!!");
}













function UnhideScroll2(){

    // console.log("unhide scroll init ran")
        
    showScrollfunction2()

    sleep2(15000).then(() => hideScroll2() );

}


function hideScroll2(){


    // console.log("hide scroll inititated");

    try {

        document.getElementsByClassName("topPartSize2")[0].classList.add('scrolloff');
        document.getElementsByClassName("topPartSize2")[0].classList.remove('scrollON');
       
     }
     catch (e) {
        if (e instanceof TypeError) {
        
        // console.log("user asked to go to the new window witout it finished hidding, its ok");
        // console.log(e);
     }else{
        //  console.log("SOME OTHER ERROR HAPPENED!");
        //  console.log(e);
     }
    }

    // console.log("hide scroll terminated");


}

function showScrollfunction2(){


    // console.log("UNhide scroll inititated!!!!!!");

    try {
        document.getElementsByClassName("topPartSize2")[0].classList.add('scrollON');
        document.getElementsByClassName("topPartSize2")[0].classList.remove('scrolloff');
     }
     catch (e) {
        if (e instanceof TypeError) {
        
        // console.log("user asked to go to the new window witout it finished hidding, its ok");
        // console.log(e);
     }else{
        //  console.log("SOME OTHER ERROR HAPPENED!");
        //  console.log(e);
     }
    }

    // console.log("UNhide scroll terminated!!!!!!");
}