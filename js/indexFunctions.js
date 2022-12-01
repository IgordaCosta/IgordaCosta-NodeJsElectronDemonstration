
function getCodeBlock(results){

    getCodeBlockFuncion(results);

};


function NotAvailableItem(){


    console.log('This option is Not available in the Test Run!');

}




async function getCodeBlockFuncion(results){

    let IfFileFound = await results[results.length - (1)];

    let j;
    let codeBlock;
    let codeBlock1;
    let OutputTitleList=['JobName', 'FileKey', 'FileSavedLocation'];
    let variable;
    let SplitVariableList=[];
    let splitVariable;
    let coma=", ";

    if (IfFileFound=='file not found'){

        codeBlock= '<div class="NotFoundText">'+
        '<h1> No data was found on the database.</h1>'+
        "<h1>Add new data by clicking</h1>"+
        "<h1>'Add to Database'</h1>"+
        '</div>'

        document.getElementsByClassName("content-wrapper")[0].innerHTML=codeBlock;

    }else if(IfFileFound=='FILE FOUND'){

        for (j = 0; j < OutputTitleList.length; j++) {

            variable = await results[results.length - (j+2)];
    
            splitVariable=variable.split(coma);
    
            SplitVariableList.push(splitVariable);
    
        };
        
    
        let CorrectedText0;
        let CorrectedText;
        let CorrectedTextList;
        let ListOfCorrectedTextLists=[];
        let NewSavedLocation;
    
        let spacedComa="', '";
    
        for (k = 0; k < SplitVariableList.length; k++) {
    
            CorrectedText0=String.fromCharCode(...SplitVariableList[k]);
    
            CorrectedText=CorrectedText0.slice(2, -2);
          
            CorrectedTextList=CorrectedText.split(spacedComa);
         
            ListOfCorrectedTextLists.push([]);
            ListOfCorrectedTextLists[k].push(CorrectedTextList);
                
        };

        let jobNameList= await ListOfCorrectedTextLists[2];
        let fileSavedLocationList= await ListOfCorrectedTextLists[0];
    
        j=0;

        NewSavedLocation= await replaceAllSlashes(fileSavedLocationList[0][j]);

        codeBlock =
            '<tr>'+
                '<th scope="row center">'+[j+1]+'</th>'+   

                '<td>'+
                    '<div class="custom-control custom-radio">'+
                        '<input type="radio" id="customRadio'+j+'" name="customRadio" class="custom-control-input">'+
                        '<label class="custom-control-label" for="customRadio'+j+'">Click_Here_to_Check</label>'+
                    '</div>'+
                '</td>'+
                
                '<td>'+jobNameList[0][j]+'</td>'+
                '<td>'+NewSavedLocation+'</td>'+
    
            '</tr>';
              
        for (j = 1; j < jobNameList[0].length; j++) {

            NewSavedLocation=replaceAllSlashes(fileSavedLocationList[0][j]);

            codeBlock1=codeBlock;
            codeBlock =
            '<tr>'+
                '<th scope="row center">'+[j+1]+'</th>'+   

                '<td>'+

                    '<div class="custom-control custom-radio">'+
                        '<input type="radio" id="customRadio'+j+'" name="customRadio" class="custom-control-input">'+
                        '<label class="custom-control-label" for="customRadio'+j+'">Click_Here_to_Check</label>'+

                    '</div>'+
                '</td>'+
                
                '<td>'+jobNameList[0][j]+'</td>'+
                '<td>'+NewSavedLocation+'</td>'+
    
            '</tr>';


                codeBlock=codeBlock1+codeBlock;
   


        };
    
    
        document.getElementById("tableData").innerHTML = codeBlock;


    }else{
            
    };
      
};


function spinnerInTableLocation() {

    document.getElementById("tableData").innerHTML = ` 
    <div class="spinnerInit spinner-border text-secondary" role="status">

        <span class="sr-only">Loading...</span>
    
    </div>
    <div class="spinnerInit downInit">

        <h1>Loading...</h1>

    </div> `;

};


function getDatabaseData(){

    spinnerInTableLocation();
   
    let path = require("path");

    const currentWorkingDirectory=process.cwd();

    console.log(currentWorkingDirectory)


    let filenamecheck=path.basename(currentWorkingDirectory);







    filenameUsed=require('path').dirname(require.main.filename);


    let {PythonShell} = require("python-shell");
    
    let opcoes = {

        scriptPath : path.join(currentWorkingDirectory, './_engine/'),

        

        pythonPath: currentWorkingDirectory + '\\e564\\Scripts\\python',
    };

    
    PythonShell.run('GetDbData.py', opcoes, function (err, results) {
        if (err) throw err;

        getCodeBlock(results);
        
    });
};



function hideImage(){

        
    hideImageFunction();

    sleep(15000).then(() => UnHideImageFunction() );

}

function UnhideScroll(){

        
    showScrollfunction();

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

    
};

function UnHideImageFunction(){

    try {
        document.getElementsByClassName("MainLogo")[0].classList.remove('hidden');
     }
     catch (e) {
        if (e instanceof TypeError) {
        
     }else{

    }
    }


};


function sleep(ms) {

    return new Promise(resolve => setTimeout(resolve, ms));

};


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

};

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

};



function replaceAllSlashes(stringToReplace){

    let OldSavedLocation=String(stringToReplace);
    let OldSavedLocationCheck=OldSavedLocation;
    let NewSavedLocation=OldSavedLocation.replace("\\\\", "\\");
    let doneFix=false;
    while (doneFix==false){
    if (NewSavedLocation==OldSavedLocationCheck){
        doneFix=true;
    }else{
        OldSavedLocationCheck=OldSavedLocation;

        NewSavedLocation=OldSavedLocation.replace("\\\\", "\\");
        
        OldSavedLocation=NewSavedLocation;
    }
    }

return NewSavedLocation;

};


