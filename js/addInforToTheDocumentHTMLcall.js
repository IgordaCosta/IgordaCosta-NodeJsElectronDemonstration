function GetImageWithLocations(){
    // let process = require("process");
    
    // let path = require("path")
  
    // const currentWorkingDirectory=process.cwd()
  
  
    // const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));
  
  
  
    // let filename = 'PlaceAboutImage.py'
  
    // let callback =GetImageCoordinatesImage0
  
  
    // RunPythonFile(filename, callback)
  
  
    GetImageCoordinatesImage0()
  
  }
  
  async function GetImageCoordinatesImage0(){
  
  
    let process = require("process");
    
    let path = require("path")
    
    const currentWorkingDirectory=process.cwd()
    
    
    const { getDbDataSimple } = require(path.join(currentWorkingDirectory, './js/getDbDataSimple'));
    
    
    let AwaitProveData="getting Db Data"
      
    let TableName=''
      
    let Database=''
    
    let DataGotten = await getDbDataSimple(AwaitProveData,TableName,Database) 
    
    let newFileLocation = await DataGotten['LocationToPlaceOnWebPage']
  
    // console.log(newFileLocation)
  
    // console.log('newFileLocation after function above')
  
    // console.log(__dirname)
  
    // console.log('__dirname above')
  
  
    CreateImageWithMarkerReturn3(newFileLocation)
  
  
  }
  
  
  
  
  function CreateImageWithMarkerReturn3(newFileLocation){
  
  
    // let process = require("process");
    
    // let path = require("path")
    
    // const currentWorkingDirectory=process.cwd()
    
    
    // const { addInforToTheDocumentHTMLcall } = require(path.join(currentWorkingDirectory,"./js/addInforToTheDocumentHTMLcall"));
  
  
  
  
  
  
    // console.log(newFileLocation)
  
    // console.log("newFileLocation inside new function")
  
    document.body.innerHTML = `
    
  
  
  
      <div class="wrapper scrollON">
  
          <img class='ScrollImage' id="DocumentToClick" src="${newFileLocation}" alt="Document Image" >
  
      </div>
  
      <div class="row col-xs-4"></div>
          <button type="button" class="btn optionsbtn left btn-secondary" onclick="getRowColumnData1()">Description</button>         
          <button type="button" class="btn optionsbtn right btn-secondary" onclick="Cancel()">OK</button>   
      </div>
  
  
      
    
  
      <script>
  
          GetImageWithLocations()
  
      </script>
  
    <script>
  
      let path = require("path");
      let jquerypath = path.join(__dirname, './js/jquery');
      window.jQuery = window.$ = require(jquerypath);
      
    </script>
  
    <script src="./js/popper.min.js"></script>
    <script src="./js/bootstrap.min.js"></script>
  
  
  
  `
  
  }
  
  
  
  








function addInforToTheDocumentHTMLcall() {

    document.body.innerHTML = `
    
    <div class=text>

        <h1>This is the Identifier,</h1>
        <h1>Column and Row information</h1>
        <h1>for the <span id="datafillNameID"></span> Job</h1>

    </div>

    <div id="foreGroundImage" class="containingArea centered MainLogo noClickImg">

        <img src="_images/LogInImg.png" onclick="hideImage()" alt="MainLogo" >

    </div>

    <form class="needs-validation" novalidate>
    
        <div class="screen parentofOverflow">

            <div class="container-fluid topPartSize scrolloff">

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


        <div class="row bottom">

            <div class="col-xs-4"></div>

                <button type="button" class="btn buttons optionsbtn right btn-secondary" onclick="Cancel()">OK</button> 
                <button type="button" class="btn buttons optionsbtn left btn-secondary" onclick="GetImageWithLocations()">Image</button>   
                
                  
            </div>
      
        </div>



    </form>

  <script>

    let path = require("path");
    let jquerypath = path.join(__dirname, './js/jquery');
    window.jQuery = window.$ = require(jquerypath);
    
  </script>

  <script src="./js/popper.min.js"></script>
  <script src="./js/bootstrap.min.js"></script>
  
    `;


}


exports.addInforToTheDocumentHTMLcall = addInforToTheDocumentHTMLcall;
