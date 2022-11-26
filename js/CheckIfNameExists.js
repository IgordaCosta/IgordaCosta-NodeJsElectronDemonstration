// const { ifError } = require("assert");
// const { MyDocumentsDatabasePath } = require("./MyDocumentsDatabasePath");





function LocationVariableExist (){

    location.replace("LocationVariableExist.html");
};




function Cancel (){

    location.replace("index.html");
};

function FindCoordinateInImage (){

    location.replace("FindCoordinateInImage.html");
};




function MarkExcellSheet (){

    location.replace("MarkExcellSheet.html");
};

function OpenedPdfFiles (){

    location.replace("OpenedPdfFiles.html");
};




function TypeJobNameReload (){
    document.body.innerHTML =`
    <div id="FileExists" class="alert hidden">
        
        <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
        This job name already exist! Try a new name!
        
    </div> 

    <div id="OpenExcelError" class="alert hidden">
        
        <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
        There is a program dependent document that is currently opened and altered. Save or close this document and click OK to continue or click CANCEL to cancel the operation.
        
    </div> 

    <div class="text">
        
            <h1>Name the Job and click OK or </h1>
            <h1>Press Cancel to quit this process. </h1>
            
    </div>

    <div id="foreGroundImage" class="containingArea centered MainLogo noClickImg">

        <img src="_images/LogInImg.png" onclick="hideImage()" alt="MainLogo" >

    </div>

    <div class="spinner spinner-border text-secondary hidden" role="status">
        <span class="sr-only">Loading...</span>

    </div>

    <div class="spinner down hidden">
        <h1>Loading...</h1>
    </div>


    <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="Job Name" aria-label="Job Name" aria-describedby="button-addon2">
        <div class="input-group-append">
          <button class="btn btn-outline-secondary" type="button" id="button-addon2" onclick="getTextValue()">OK</button>
        </div>
    </div>

    <div>
        <button type="button" class="btn optionsbtn left btn-secondary" onclick="Cancel()" >Cancel</button>
    </div>
    
    <script>

        let jquerypath = path.join(__dirname, './js/jquery');
        window.jQuery = window.$ = require(jquerypath);

    </script>
    
    <script src="./js/popper.min.js"></script>
    <script src="./js/bootstrap.min.js"></script>
    `;
    
};


// function gotResults(){
    
//     document.body.innerHTML =`<div class="spinner spinner-border text-secondary" role="status">
//                         <span class="sr-only">Loading...</span>
    
//                     </div>
//                     <div class="spinner down">
//                         <h1>Loading...</h1>
//                     </div>

//                     <div id="foreGroundImage" class="containingArea centered MainLogo noClickImg">

//                         <img src="_images/LogInImg.png" onclick="hideImage()" alt="MainLogo" >
                
//                     </div>`
// }




// function getTextValue(){

//     getTextValueAsync()

//     // var process = require("process");

//     // var path = require("path")

//     // const currentWorkingDirectory=process.cwd()


//     // const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));
//     // const { insertIntoDatabase } = require(path.join(currentWorkingDirectory, "./js/insertIntoDatabase"));
//     // const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory, "./js/MyDocumentsDatabasePath"));


    

//     // // var x = document.getElementById("myText").value;

//     // let jobName = document.getElementsByClassName("form-control")[0].value;
//     // // console.log(jobName);
//     // document.getElementsByClassName("form-control")[0].value=''

    
//     // if (jobName==''){}else{

//     // document.getElementsByClassName("input-group")[0].classList.add('hidden');
//     // document.getElementsByClassName("spinner")[0].classList.remove('hidden');
    
//     // let filename='CheckJobNameRedo.py';
//     // // data=jobName

//     // let callback=AddDataCheckIfExists




//     // let data=jobName;

//     // let dataName='datafillName';

//     // const MyDocumentsDatabasePath = await MyDocumentsDatabasePath(currentWorkingDirectory)


//     // let TableName=''

//     // let Database=''


//     // Done= await insertIntoDatabase(data, dataName, MyDocumentsDatabasePath,currentWorkingDirectory,TableName,Database)

//     // console.log(Done)

//     // RunPythonFile(filename,callback)

//     // // runPythonFile(filename,data);




//     // }
// }





async function getTextValue2(results){

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory=process.cwd();

    const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, "./js/AddtoTablePromise"));

    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));

    // console.log(results)


    // let ReturnedData = results[results.length - 1].trim();

    // console.log(ReturnedData)

    // console.log('ReturnedData above')

    // if (ReturnedData == ''){





    // }else{

    // let data=ReturnedData;

    // let dataName='datafillName';


    
    // let callback = getTextValue2

 

    
    // // let data=['jobName1','jobName2','jobName3','jobName4','jobName5']

    // // let dataName=['datafillName1','datafillName2','datafillName3','datafillName4','datafillName5'];

    // let AwaitProveData=data;

    // let TableName=''

    // let Database=''


    // // let DoneValue= await AddToTable(AwaitProveData,data, dataName, TableName,Database)

    // let DoneValue = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);


    // console.log(DoneValue)

    // console.log('DoneValue above')


    // let filename='CheckJobNameRedo.py';

    // let callback2=AddDataCheckIfExists

    

    // RunPythonFile(filename,callback2, gotResultsFuction=false)





    };



async function getTextValue(){


    let jobName = await document.getElementsByClassName("form-control")[0].value;

    document.getElementsByClassName("form-control")[0].value='';


    // console.log(jobName)

    // console.log('jobName above')
    
    if (jobName==''){}else{


    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory=process.cwd();
  
    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));
    const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, "./js/AddtoTablePromise"));


    document.getElementsByClassName("input-group")[0].classList.add('hidden');
    document.getElementsByClassName("spinner")[0].classList.remove('hidden');

    

       


    let data=jobName;

    let dataName='datafillName';


    
    // let callback = getTextValue2


    // let filename = 'RunRegularExpressionTextOrList.py'


    // RunPythonFile(filename, callback, dataUsed = data, NoArgs=true)
    

    // }











    
    // let data=['jobName1','jobName2','jobName3','jobName4','jobName5']

    // let dataName=['datafillName1','datafillName2','datafillName3','datafillName4','datafillName5'];

    let AwaitProveData=data;

    let TableName='';

    let Database='';


    // let DoneValue= await AddToTable(AwaitProveData,data, dataName, TableName,Database)

    let DoneValue = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);


    // console.log(DoneValue)

    // console.log('DoneValue above')


    let filename='CheckJobNameRedo.py';

    let callback=AddDataCheckIfExists;



    RunPythonFile(filename,callback, gotResultsFuction=false);



    };


};





async function AddDataCheckIfExists(results){

    let process = require("process");

    let path = require("path");

    const currentWorkingDirectory = process.cwd();

    const { getDbDataSimple } = require(path.join(currentWorkingDirectory, './js/getDbDataSimple'));

    const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, "./js/AddtoTablePromise"));

    // const { GetValueFromKey } = require(path.join(currentWorkingDirectory, "./js/GetValueFromKey"));


    


    // console.log('this is run python function this should appear last')


  

    let ifExists = await results[results.length - 1];

    // console.log(ifExists);

    // console.log(ifExists);
      

    if(ifExists=="True"){

        TypeJobNameReload();

        // console.log("variable is TRUE");

        // console.log("back to old window to try again")

        // document.getElementsByClassName("spinner")[0].classList.add('hidden');


        // // document.getElementsByClassName("spinner")[0].classList.add('hidden');
        // document.getElementsByClassName("input-group")[0].classList.remove('hidden');

        document.getElementById("FileExists").classList.remove('hidden');
        

    }else if(ifExists=="False"){

        // console.log("variable is False.... continue to next part from here");


        //  this is the location where the datatype diferentiates where the program
        // will run next 

        // bellow is for excel, the other datatype options must be listed here to guide the user
        // to the location the datatype will work as it should

        let AwaitProveData = 'Starting to check type of data';
        
        let TableName = '';
        
        let Database  = '';

        let DatabaseDataGotten = await getDbDataSimple(AwaitProveData,TableName,Database);

        // console.log(DatabaseDataGotten)

        // console.log('DatabaseDataGotten above')

        let ExtensionType = await DatabaseDataGotten['ExtensionType'];


        // console.log(ExtensionType);

        // console.log("ExtensionType above in javascript")
        

        let datafillName =  await DatabaseDataGotten['datafillName'];


        // console.log('this should apear before the value inbetween')

        // console.log(await DatabaseDataGotten['datafillName'])

        // console.log('this should apear after the value inbetween')

        // let datafillName =  await DatabaseDataGotten['datafillName'];









        let PDFfile0 = await DatabaseDataGotten['PDFfile'];

        let PDFfile = String(PDFfile0);

        // console.log(ExtensionType);


        if (ExtensionType=='excel'){
            // this is for excel 



            let dataName='InPDFdatafillName';

            let data= '';
        
            let AwaitProveData=data;
        
            let TableName='';
        
            let Database='';
        
        
            // let DoneValue= await AddToTable(AwaitProveData,data, dataName, TableName,Database)

            let DoneValue = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);

        
            // console.log(DoneValue)




            OpenExcelDocument();


        }else if (ExtensionType=='image'){
            // this is for image document 



            if (PDFfile  == 'false'){ 


            let dataName='InPDFdatafillName';

            let data= '';
        
            let AwaitProveData=data;
        
            let TableName='';
        
            let Database='';
        
        
            // let DoneValue= await AddToTable(AwaitProveData,data, dataName, TableName,Database)

            let DoneValue = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);
        
            // console.log(DoneValue)



            }else if(PDFfile == 'true'){
                
            }else{


                // console.log('Something is wrong PDFfile can only be true or false')


            }


            FindCoordinateInImage();
            

        }else if(ExtensionType=='pdf'){
            // this is for pdf document 




            let dataName='InPDFdatafillName';

            let data= datafillName;
        
            let AwaitProveData=data;
        
            let TableName='';
        
            let Database='';
        
        
            // let DoneValue= await AddToTable(AwaitProveData,data, dataName, TableName,Database)

            let DoneValue = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);
        
            // console.log(DoneValue)






            OpenedPdfFiles();


        }else if(ExtensionType=='word'){
            // this is for word document 



            let dataName='InPDFdatafillName';

            let data= '';
        
            let AwaitProveData=data;
        
            let TableName='';
        
            let Database='';
        
        
            // let DoneValue= await AddToTable(AwaitProveData,data, dataName, TableName,Database)

            let DoneValue = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);
        
            // console.log(DoneValue)




            // OpenWordDocument()

        }else{
            
            // console.log("there is something wrong with the extension value")
            // console.log('ExtensionType= ' + ExtensionType)
    }
      



    }else{

        // TypeJobNameReload();
        // console.log("Last Variable must be either True or False and it is neither. Check last Python function output!");
        
        
        // document.getElementsByClassName("spinner")[0].classList.add('hidden');
        // document.getElementsByClassName("input-group")[0].classList.remove('hidden');
        
    
    };
    

    // document.getElementsByClassName("input-group")[0].classList.remove('hidden');

    // document.getElementsByClassName("spinner")[0].classList.add('hidden');

    // console.log("Finished Python File after check if file exists");

};



// function runPythonFile(filename,data){

//     gotResults()

//     let path = require("path");

//     let filenamecheck=path.basename(__dirname);
//     // console.log(filenamecheck);
//     // console.log("filename check above");

//     // console.log(fileLocation);
//     // console.log('fileLocation above')

//     if (filenamecheck=="CSSAutoFormFiller"){}else{
//         __dirname = path.join(__dirname, '../../../../../../');

//     }
    
//     // console.log(__dirname)
//     // console.log("__dirname")
    
    

//     let {PythonShell} = require("python-shell");

//     let opcoes = {
//         scriptPath : path.join(__dirname, './_engine/'),
//         pythonPath: 'C:\\ProgramData\\Anaconda3\\python',
//         args : [data]
//     };

//     // console.log(path.join(__dirname, './_engine/'));
//     // console.log("startprint");

//     PythonShell.run(filename, opcoes, function (err, results) {
//         if (err) throw err;

    
        // console.log(results);

        // let ifExists = results[results.length - 1];
        

        


        // if(ifExists=="True"){

        //     TypeJobNameReload();

        //     // console.log("variable is TRUE");

        //     // console.log("back to old window to try again")

        //     // document.getElementsByClassName("spinner")[0].classList.add('hidden');


        //     // // document.getElementsByClassName("spinner")[0].classList.add('hidden');
        //     // document.getElementsByClassName("input-group")[0].classList.remove('hidden');

        //     document.getElementById("FileExists").classList.remove('hidden');
            

        // }else if(ifExists=="False"){

        //     // console.log("variable is False.... continue to next part from here");

        //     OpenExcelDocument();

        // }else{

        //     TypeJobNameReload();
        //     // console.log("Last Variable must be either True or False and it is neither. Check last Python function output!");
            
            
        //     // document.getElementsByClassName("spinner")[0].classList.add('hidden');
        //     // document.getElementsByClassName("input-group")[0].classList.remove('hidden');
            
        
        // };
        

        // // document.getElementsByClassName("input-group")[0].classList.remove('hidden');

        // // document.getElementsByClassName("spinner")[0].classList.add('hidden');

        // // console.log("Finished Python File after check if file exists");
        
//     });
// }


function OpenExcelDocument(){


    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory=process.cwd();


    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));
    // const { insertIntoDatabase } = require(path.join(currentWorkingDirectory, "./js/insertIntoDatabase"));
    // const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory, "./js/MyDocumentsDatabasePath"));



    let filename="OpenExcelDocument.py";

    let callback=AddDataOpenExcelDocumentReturn;


    RunPythonFile(filename,callback);






    // let path = require("path");

    // let filenamecheck=path.basename(__dirname);
    // // console.log(filenamecheck);
    // // console.log("filename check above");


    // if (filenamecheck=="CSSAutoFormFiller"){}else{
    //     __dirname = path.join(__dirname, '../../../../../../');

    // }
    
    // // console.log(__dirname)
    // // console.log("__dirname")
       

    // let {PythonShell} = require("python-shell");

    // let opcoes = {
    //     scriptPath : path.join(__dirname, './_engine/'),
    //     pythonPath: 'C:\\ProgramData\\Anaconda3\\python',
        
    // };

    // // console.log(path.join(__dirname, './_engine/'));
    // // console.log("startprint");

    // PythonShell.run(filename, opcoes, function (err, results) {
    //     if (err) throw err;

        // // console.log(results)

        // IfError=(results[results.length -1]).trim()

        // // console.log(IfError);

        // // console.log(IfError=="AllOk");

        // // console.log('IfError=="AllOk above"');


        // if(IfError=="ERROR"){

        //     TypeJobNameReload();

        //     // console.log("There is an error opening the excel sheet");

        //     document.getElementById("OpenExcelError").classList.remove('hidden');
        //     // AlteredOrOpenedDocument() // use the red alert instead, its more professional


        // }else if(IfError=="AllOk"){

        //     // console.log("All is ok to continue from here");


        //     GetOldStamp();

        //     // MarkExcellSheet();

        //     // here is where the user copy and pastes a special code into 
        //     // his excel sheet and press ok for the location of the sheet to
        //     // be recognized by the program



        // }else{
        //     TypeJobNameReload();

        //     // console.log("IfError is a different value from the accepted check last python program print");


        // }

        

        

        // JSON.stringify(ifError) === JSON.stringify('ERROR')

        // if(ifError=="ERROR"){

        // if(JSON.stringify(ifError) === JSON.stringify('ERROR')){

        //     console.log("error happend it must run the self.InicioSalveDocumento() function then try again");
            
        //     // OpenExcelDocument()

        // }
        // // else if(ifError=="All Ok"){
        // else if (JSON.stringify(ifError) === JSON.stringify('AllOk')){

        //     console.log("continue");

        // }else{

        //     console.log("check last function print statemente it must be one of the above");

        // };

}
// )
// }

function AddDataOpenExcelDocumentReturn(results){

    AddDataOpenExcelDocumentReturnfunction(results);

};


async function AddDataOpenExcelDocumentReturnfunction(results){


    let IfError=await (results[results.length -1]).trim();

        // console.log(IfError);

        // console.log(IfError=="AllOk");

        // console.log('IfError=="AllOk above"');


    if(IfError=="SheetIsOpenAndHasChanges"){

        TypeJobNameReload();

        // console.log("There is an error opening the excel sheet");

        document.getElementById("OpenExcelError").classList.remove('hidden');
        // AlteredOrOpenedDocument() // use the red alert instead, its more professional


    }else if(IfError=="AllOK"){

        // console.log("All is ok to continue from here");


        GetOldStamp();

        // MarkExcellSheet();

        // here is where the user copy and pastes a special code into 
        // his excel sheet and press ok for the location of the sheet to
        // be recognized by the program



    }else{
        // TypeJobNameReload();


        // console.log("IfError is a different value from the accepted check last python program print");


    };


};

function AddDataOpenWordDocumentReturn(results){

    AddDataOpenWordDocumentReturnfunction(results);

}


async function AddDataOpenWordDocumentReturnfunction(results){

    const currentWorkingDirectory=process.cwd();

    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));


    let IfError=await (results[results.length -1]).trim();

        // console.log(IfError);

        // console.log(IfError=="AllOk");

        // console.log('IfError=="AllOk above"');


    if(IfError=="SheetIsOpenAndHasChanges"){

        // TypeJobNameReload();  //This oprion was selected in case of Excel

        // console.log("There is an error opening the excel sheet");

        document.getElementById("OpenExcelError").classList.remove('hidden');  // this option is written to acodate word also
        

    }else if(IfError=="AllOK"){

        // console.log("All is ok to continue from here");


        // the word document opened here without problem
        // now the program needs to check to see if the 
        // words chossen as a reference to location are already
        // in the document and take precautions on each case

        // after the above the a function like (but not the same)
        // as GetOldStap is Run

        // please note the above step needs to be done as well
        // for the excel part of the program
        
        let filename="CheckIfLocationWordinDoc.py";

        let callback = CheckIfLocationWordinDocReturn ;


        RunPythonFile(filename,callback);
    
    



        // GetOldStamp();   // this was the option to continue in case of Excel

        

        // here is where the user copy and pastes a special code into 
        // his excel sheet and press ok for the location of the sheet to
        // be recognized by the program



    }else{
        // TypeJobNameReload();


        // console.log("IfError is a different value from the accepted check last python program print");


    };


};


async function CheckIfLocationWordinDocReturn(){

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory=process.cwd();

    const { getDbDataSimple } = require(path.join(currentWorkingDirectory, './js/getDbDataSimple'));
    // const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));

    const { GetOldWordStamp } = require(path.join(currentWorkingDirectory, "./js/GetOldWordStamp"));

    // const { insertIntoDatabase } = require(path.join(currentWorkingDirectory, "./js/insertIntoDatabase"));
    // const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory, "./js/MyDocumentsDatabasePath"));

    let AwaitProveData="getting Db Data";
  
    let TableName='';
  
    let Database='';

    let DataGotten = await getDbDataSimple(AwaitProveData,TableName,Database);

    let ValueInText = await DataGotten['ValueInText'];


    if (ValueInText == 'ValueIsInText'){

        // console.log('the value is inside text')

        // in this option the program will go in a new screen
        // where the user will choose what to do

        LocationVariableExist();


    }else if(ValueInText == 'ValueNOTinText'){

        // console.log('the value NOT inside text')

        GetOldWordStamp();

        // in this option the program will run as normal

        // the user will be guided to the next step where the 

        // the user will be presented with the text to copy already
        // in his clipboard but he can press a button to put it there 
        // if he wishes or in the case that he copies another text by
        // mistake and he needs that value ready to copy again

        // after the user is satisfied with what he copied he will
        // save the document and click ok to continue
        // the program will check if there were changes to the document
        // meaning the user clicked save after making his changes (if done so)

        // if so the user can then name the locations for easy recognition
        // after that the program concludes this section 

    }else{

        // console.log('something went wrong, result ValueInText:')
        // console.log(ValueInText)
    };




};



function GetOldStamp(){


        var process = require("process");

        var path = require("path");

        const currentWorkingDirectory=process.cwd();


        const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));
        // const { insertIntoDatabase } = require(path.join(currentWorkingDirectory, "./js/insertIntoDatabase"));
        // const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory, "./js/MyDocumentsDatabasePath"));


    // function runPythonFile(filename,fileLocation){
        let filename="GetOldStamp.py";

        let callback = MarkExcellSheet;

        RunPythonFile(filename,callback);


        // let path = require("path");
    
        // let filenamecheck=path.basename(__dirname);

        // // console.log(filenamecheck);
        // // console.log("filename check above");
    
    
        // if (filenamecheck=="CSSAutoFormFiller"){}else{
        //     __dirname = path.join(__dirname, '../../../../../../');
    
        // }
        
        // // console.log(__dirname)
        // // console.log("__dirname")
        
    
        // let {PythonShell} = require("python-shell");
    
        // let opcoes = {
        //     scriptPath : path.join(__dirname, './_engine/'),
        //     pythonPath: 'C:\\ProgramData\\Anaconda3\\python',
        // };
    
        // // console.log(path.join(__dirname, './_engine/'));
        // // console.log("startprint");

        // PythonShell.run(filename, opcoes, function (err, results) {
        //     if (err) throw err;

        //     // console.log(results);


            // MarkExcellSheet();

            
            // checkIfSavedAndFilled();

    
        }
//         )    
// };



function OpenWordDocument(){


    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory=process.cwd();


    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));


    let filename="OpenWordDocument.py";

    // let callback=AddDataOpenExcelDocumentReturn

    let callback=AddDataOpenWordDocumentReturn;

    RunPythonFile(filename,callback);






    // let path = require("path");

    // let filenamecheck=path.basename(__dirname);
    // // console.log(filenamecheck);
    // // console.log("filename check above");


    // if (filenamecheck=="CSSAutoFormFiller"){}else{
    //     __dirname = path.join(__dirname, '../../../../../../');

    // }
    
    // // console.log(__dirname)
    // // console.log("__dirname")
       

    // let {PythonShell} = require("python-shell");

    // let opcoes = {
    //     scriptPath : path.join(__dirname, './_engine/'),
    //     pythonPath: 'C:\\ProgramData\\Anaconda3\\python',
        
    // };

    // // console.log(path.join(__dirname, './_engine/'));
    // // console.log("startprint");

    // PythonShell.run(filename, opcoes, function (err, results) {
    //     if (err) throw err;

        // // console.log(results)

        // IfError=(results[results.length -1]).trim()

        // // console.log(IfError);

        // // console.log(IfError=="AllOk");

        // // console.log('IfError=="AllOk above"');


        // if(IfError=="ERROR"){

        //     TypeJobNameReload();

        //     // console.log("There is an error opening the excel sheet");

        //     document.getElementById("OpenExcelError").classList.remove('hidden');
        //     // AlteredOrOpenedDocument() // use the red alert instead, its more professional


        // }else if(IfError=="AllOk"){

        //     // console.log("All is ok to continue from here");


        //     GetOldStamp();

        //     // MarkExcellSheet();

        //     // here is where the user copy and pastes a special code into 
        //     // his excel sheet and press ok for the location of the sheet to
        //     // be recognized by the program



        // }else{
        //     TypeJobNameReload();

        //     // console.log("IfError is a different value from the accepted check last python program print");


        // }

        

        

        // JSON.stringify(ifError) === JSON.stringify('ERROR')

        // if(ifError=="ERROR"){

        // if(JSON.stringify(ifError) === JSON.stringify('ERROR')){

        //     console.log("error happend it must run the self.InicioSalveDocumento() function then try again");
            
        //     // OpenExcelDocument()

        // }
        // // else if(ifError=="All Ok"){
        // else if (JSON.stringify(ifError) === JSON.stringify('AllOk')){

        //     console.log("continue");

        // }else{

        //     console.log("check last function print statemente it must be one of the above");

        // };

};