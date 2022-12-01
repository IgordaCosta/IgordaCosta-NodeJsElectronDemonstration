




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


    
    


                












    



    

    
























async function getTextValue2(results){

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory=process.cwd();

    const { AddtoTablePromise } = require(path.join(currentWorkingDirectory, "./js/AddtoTablePromise"));

    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));















    

 

    














    






    };



async function getTextValue(){


    let jobName = await document.getElementsByClassName("form-control")[0].value;

    document.getElementsByClassName("form-control")[0].value='';



    
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


    




    












    


    let AwaitProveData=data;

    let TableName='';

    let Database='';



    let DoneValue = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);





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



    




  

    let ifExists = await results[results.length - 1];


      

    if(ifExists=="True"){

        TypeJobNameReload();






        document.getElementById("FileExists").classList.remove('hidden');
        

    }else if(ifExists=="False"){





        let AwaitProveData = 'Starting to check type of data';
        
        let TableName = '';
        
        let Database  = '';

        let DatabaseDataGotten = await getDbDataSimple(AwaitProveData,TableName,Database);



        let ExtensionType = await DatabaseDataGotten['ExtensionType'];



        

        let datafillName =  await DatabaseDataGotten['datafillName'];














        let PDFfile0 = await DatabaseDataGotten['PDFfile'];

        let PDFfile = String(PDFfile0);



        if (ExtensionType=='excel'){



            let dataName='InPDFdatafillName';

            let data= '';
        
            let AwaitProveData=data;
        
            let TableName='';
        
            let Database='';
        
        

            let DoneValue = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);

        




            OpenExcelDocument();


        }else if (ExtensionType=='image'){



            if (PDFfile  == 'false'){ 


            let dataName='InPDFdatafillName';

            let data= '';
        
            let AwaitProveData=data;
        
            let TableName='';
        
            let Database='';
        
        

            let DoneValue = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);
        



            }else if(PDFfile == 'true'){
                
            }else{




            }


            FindCoordinateInImage();
            

        }else if(ExtensionType=='pdf'){




            let dataName='InPDFdatafillName';

            let data= datafillName;
        
            let AwaitProveData=data;
        
            let TableName='';
        
            let Database='';
        
        

            let DoneValue = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);
        






            OpenedPdfFiles();


        }else if(ExtensionType=='word'){



            let dataName='InPDFdatafillName';

            let data= '';
        
            let AwaitProveData=data;
        
            let TableName='';
        
            let Database='';
        
        

            let DoneValue = await AddtoTablePromise(AwaitProveData, data, dataName, TableName, Database);
        





        }else{
            
    }
      



    }else{

        
        
        
    
    };
    




};









    
    
    





    

        

        









            





            
            
            
        
        



        


function OpenExcelDocument(){


    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory=process.cwd();


    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));



    let filename="OpenExcelDocument.py";

    let callback=AddDataOpenExcelDocumentReturn;


    RunPythonFile(filename,callback);










    
       


        


























        

        




            






}

function AddDataOpenExcelDocumentReturn(results){

    AddDataOpenExcelDocumentReturnfunction(results);

};


async function AddDataOpenExcelDocumentReturnfunction(results){


    let IfError=await (results[results.length -1]).trim();





    if(IfError=="SheetIsOpenAndHasChanges"){

        TypeJobNameReload();


        document.getElementById("OpenExcelError").classList.remove('hidden');


    }else if(IfError=="AllOK"){



        GetOldStamp();





    }else{




    };


};

function AddDataOpenWordDocumentReturn(results){

    AddDataOpenWordDocumentReturnfunction(results);

}


async function AddDataOpenWordDocumentReturnfunction(results){

    const currentWorkingDirectory=process.cwd();

    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));


    let IfError=await (results[results.length -1]).trim();





    if(IfError=="SheetIsOpenAndHasChanges"){



        

    }else if(IfError=="AllOK"){





        
        let filename="CheckIfLocationWordinDoc.py";

        let callback = CheckIfLocationWordinDocReturn ;


        RunPythonFile(filename,callback);
    
    




        




    }else{




    };


};


async function CheckIfLocationWordinDocReturn(){

    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory=process.cwd();

    const { getDbDataSimple } = require(path.join(currentWorkingDirectory, './js/getDbDataSimple'));

    const { GetOldWordStamp } = require(path.join(currentWorkingDirectory, "./js/GetOldWordStamp"));


    let AwaitProveData="getting Db Data";
  
    let TableName='';
  
    let Database='';

    let DataGotten = await getDbDataSimple(AwaitProveData,TableName,Database);

    let ValueInText = await DataGotten['ValueInText'];


    if (ValueInText == 'ValueIsInText'){



        LocationVariableExist();


    }else if(ValueInText == 'ValueNOTinText'){


        GetOldWordStamp();






    }else{

    };




};



function GetOldStamp(){


        var process = require("process");

        var path = require("path");

        const currentWorkingDirectory=process.cwd();


        const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));


        let filename="GetOldStamp.py";

        let callback = MarkExcellSheet;

        RunPythonFile(filename,callback);


    

    
    
    
        
        
    
    
    





            

    
        }



function OpenWordDocument(){


    var process = require("process");

    var path = require("path");

    const currentWorkingDirectory=process.cwd();


    const { RunPythonFile } = require(path.join(currentWorkingDirectory, "./js/RunPythonFile"));


    let filename="OpenWordDocument.py";


    let callback=AddDataOpenWordDocumentReturn;

    RunPythonFile(filename,callback);










    
       


        


























        

        




            






};