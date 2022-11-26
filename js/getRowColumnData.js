

function addInforToTheDocumentHTMLcall(){

    document.body.innerHTML = `
    
    <!-- <div id="MissingData" class="alert hidden"> -->
    <div id="MissingData" class="positionAndLocation" >
          
      <!-- <span class="closebtn" onclick="this.parentElement.classList.add('hidden');">&times;</span>
      There are Identifiers missing! All Identifiers must be filled! -->

            
    </div>


    <div class=text>

        <h1>Fill the Identifier column with information</h1>
        <h1>and press OK to continue or press Cancel </h1>
        <h1>to cancel the operation</h1>

    </div>

    <div id="foreGroundImage" class="containingArea centered MainLogo noClickImg">

      <img src="_images/LogInImg.png" onclick="hideImage()" alt="MainLogo" >

    </div>

  <form class="needs-validation" novalidate>
 
    <div class="screen parentofOverflow">

        <div class="container-fluid topPartSize scrolloff">

          <!-- <div id="foreGroundImage" class="containingArea centered MainLogo ">

              <img src="_images/LogInImg.png" onclick="hideImage()" alt="MainLogo" >

          </div> -->
          <div class="content-wrapper">
            
              <table id= "table" class="table table-dark table-striped scrollableArea" onclick="UnhideScroll()">
                <thead>
                  <tr>
                    <th scope="col">#</th>
                    <th scope="col">Row Position</th>
                    <th scope="col">Column Position</th>
                    <th scope="col">Identifier</th>
                                        
                  </tr>
                </thead >
                <tbody id="tableData">

                  <script>getRowColumnData();</script>  
                  
                </tbody>
                
              </table>
            
          </div>
        </div>                   
    </div>

    <div class= "buttons container-fluid">
      
      <div class="row bottom">

        <div class="col-xs-4"></div>
          <button type="button" class="btn optionsbtn left btn-secondary" onclick="Cancel()">Cancel</button>
          <button id="waitFunction" type="button" class="btn optionsbtn right btn-secondary" onclick="checkIfAllInputsFilled()">OK</button>   
        </div>
      
        
      </div>
      
    </div>  

  </form>

    <!-- <div class= "buttons container-fluid">
      
      <div class="row bottom">

        <div class="col-xs-4"></div>
          <button type="button" class="btn optionsbtn left btn-secondary" onclick="Cancel()">Cancel</button>
          <button type="button" class="btn optionsbtn right btn-secondary" onclick="">OK</button>   
        </div>
      
        
      </div>
      
    </div>   -->
  </div>
  <script>

    let path = require("path");
    let jquerypath = path.join(__dirname, './js/jquery');
    window.jQuery = window.$ = require(jquerypath);
    
  </script>

  <script src="./js/popper.min.js"></script>
  <script src="./js/bootstrap.min.js"></script>
  
    `


}




async function getRowColumnData(){

    // text = localStorage.getItem("RowColumn");
    
    // obj = JSON.parse(text);

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()


    const { getDbDataSimple } = require(path.join(currentWorkingDirectory,"./js/getDbDataSimple"));

    const { gotResults } = require(path.join(currentWorkingDirectory,"./js/gotResults"));


    gotResults()


    let resultDatabase="it has started"

    let TableName=''

    let Database=''
    
  



    let DbDataGotten = await getDbDataSimple(resultDatabase,TableName,Database)

    // console.log(DbDataGotten)





    listOfRows=DbDataGotten.listOfRows;
    listOfColumns=DbDataGotten.listOfColumns;

    // console.log('listOfRows 1',listOfRows);

    // console.log('listOfColumns 1',listOfColumns);

    listOfRows=listOfRows.slice(1, -1);

    listOfColumns=listOfColumns.slice(1, -1);

    // console.log('listOfRows 2',listOfRows);

    // console.log('listOfColumns 2',listOfColumns);

    listOfRows=listOfRows.split(",");

    listOfColumns=listOfColumns.split(", ");

    // console.log('listOfRows 3',listOfRows);

    // console.log('listOfColumns 3',listOfColumns);

    let i;
    for (i = 0; i < listOfRows.length; i++) {

        listOfRows[i]=listOfRows[i].trim();
        
        listOfColumns[i]=listOfColumns[i].trim();

    } 

    // console.log('listOfRows 4',listOfRows);

    // console.log('listOfColumns 4',listOfColumns);




    j=0;


    codeBlock =
    '<tr>'+
        '<th scope="row center">'+[j+1]+'</th>'+              
        '<td>'+listOfRows[j]+'</td>'+
        '<td>'+listOfColumns[j]+'</td>'+
        '<td>'+
            '<form class="needs-validation" novalidate>'+
            '<div class="form-row">'+
            '<div class="col-12">'+
                '<input type="text" class="form-control" id="validationTooltip0'+j+'" placeholder="Type here something that identifies this position" value="" required>'+
                '<div class="valid-tooltip">'+
                'Looks good!'+
                '</div>'+
            '</div'+
        '</td>'

    '</tr>'
            
    for (j = 1; j < listOfColumns.length; j++) {
        codeBlock1=codeBlock;
        codeBlock =
        '<tr>'+
            '<th scope="row center">'+[j+1]+'</th>'+              
            '<td>'+listOfRows[j]+'</td>'+
            '<td>'+listOfColumns[j]+'</td>'+
            '<td>'+
                '<form class="needs-validation" novalidate>'+
                '<div class="form-row">'+
                '<div class="col-12">'+
                    '<input type="text" class="form-control" id="validationTooltip0'+j+'" placeholder="Type here something that identifies this position" value="" required>'+
                    '<div class="valid-tooltip">'+
                    'Looks good!'+
                    '</div>'+
                '</div'+
            '</td>'

        '</tr>'
            codeBlock=codeBlock1+codeBlock;

            // console.log(codeBlock);
    }

    // console.log("done loading html");


    // addInfoToTheDocument();
    

    addInforToTheDocumentHTMLcall()


    document.getElementById("tableData").innerHTML = codeBlock;


}