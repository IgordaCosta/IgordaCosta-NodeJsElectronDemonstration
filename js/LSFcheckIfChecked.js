

// function ItemChecked(){

//     location.replace("LSFItemChecked.html");

// }

// function ItemNOTchecked(){

//     location.replace("LSFItemNOTChecked.html");

// }


// function Cancel (){
//     location.replace("index.html");
// }




// function validate(documentID) {

//     let checked=false
    
//     if (document.getElementById(documentID).checked) {
//         checked=true;

//         // console.log("checkbox is checked");

//     } else {

//         // console.log("checkbox NOT checked");

//     }
//     return checked
// }


// function getRowNumberInTableByClass(tableClass){

//     let tablesize = document.getElementsByClassName(tableClass)[0].rows.length;

//     console.log('tablesize',tablesize)

//     numberOfRows=tablesize-1

//     console.log('numberOfRows',numberOfRows)

//     return numberOfRows

// }



// function LoadSingleFile(){

//     tableClass="table";

//     getRowNumberInTableByClass(tableClass);

//     numberOfRows=getRowNumberInTableByClass(tableClass);

    

//     let AnyChecked=false;

//     let checkedNumber=0;

//     let NeedWait=true;

//     if (numberOfRows>0){

//     documentIDInitiral="customRadio"

//     let isChecked=false;

//     for (i = 0; i < numberOfRows; i++) { 

//         documentID="customRadio"+String(i)
//         isChecked=validate(documentID)
//         if (isChecked==true){

//             checkedNumber=i;

//             AnyChecked=true;

//         }

//     }

//     if (AnyChecked==true){

//         console.log('ItemChecked');

//         console.log('checkedNumber',checkedNumber)

//         let datafillName=document.getElementById("tableData").rows[checkedNumber].cells[2].innerHTML;

//         console.log('datafillName',datafillName);

//         FilesInDatabaseLocation='FilesInDatabase';

//         columnsFileinDatabase=['Job Name', 'File KEY', 'File Saved Location'];
        
//         let obj = {"datafillName":datafillName};
//         localStorage.setItem('datafillNameLocation', JSON.stringify(obj));

//         NeedWait=false;

//         ItemChecked();

//     }else{

//         console.log('ItemNOTchecked');

//         NeedWait=false;

//         ItemNOTchecked();

//     }

// }else{
//     console.log("wait to load");



    

// }

// console.log([AnyChecked, checkedNumber,NeedWait])

// // return [AnyChecked, checkedNumber,NeedWait]

// }





// function getDatafillName(){

//     let obj = JSON.parse(localStorage.getItem('datafillNameLocation'));

//     datafillName=obj.datafillName

//     return datafillName

// }

// function placeDatafillName(){

//     datafillName=getDatafillName()

//     document.getElementById("datafillNameID").innerHTML = datafillName;

// }

function Cancel (){
    location.replace("index.html");
}


function placeDatafillName(){

    let CurrentWorkingDirectory = process.cwd();

    // console.log(CurrentWorkingDirectory);

    // console.log('CurrentWorkingDirectory is above');

    const { getDatafillName } = require(path.join(CurrentWorkingDirectory,"./js/getDatafillName"));

    htmlBodyObject = `<div class="text">
        
    <h1>Are you sure you want to</h1> 
    <h1>continue with the Job Name bellow?</h1>
    <h1 id="datafillNameID"></h1>
     
</div>

<div id="foreGroundImage" class="containingArea centered MainLogo noClickImg">

    <img src="_images/LogInImg.png" onclick="hideImage()" alt="MainLogo" >

</div>
<div>
    <button type="button" class="btn optionsbtn right btn-secondary" onclick="LoadSingFileJason()" >YES</button>
</div>
<div>
    <button type="button" class="btn optionsbtn left btn-secondary" onclick="Cancel()" >NO</button>
</div>
  
<script>placeDatafillName()</script>

<script>

    let jquerypath = path.join(__dirname, './js/jquery');
    window.jQuery = window.$ = require(jquerypath);

</script>
<script src="./js/popper.min.js"></script>
<script src="./js/bootstrap.min.js"></script>`;



getDatafillName(htmlBodyObject)


}
