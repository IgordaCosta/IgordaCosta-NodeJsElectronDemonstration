function CreateImageWithMarkerStep5Return2(newFileLocation, FontSize, tableTitles, tableData) {

    // var process = require("process");

    // var path = require("path")

    // const currentWorkingDirectory=process.cwd()

    // const { gotResultsAdd } = require(path.join(currentWorkingDirectory, "./js/gotResultsAdd"));

    

    // console.log('newFileLocation: ', newFileLocation);

    // console.log('FontSize: ', FontSize);

    // console.log("newFileLocation inside new function");

    document.body.innerHTML =
    // document.documentElement.innerHTML=
    `

    <div id="alert MissingData" class="positionAndLocation" >
          
        <div id= "identifiersMissingAlert" class="alert alert-dismissible hidden">
            <button type="button" class="close" data-dismiss="alert">&times;</button>
            There are Identifiers missing! All Identifiers must be filled!
        </div>

            
    </div>
    <div id = "createImageGetData" >    
        <div>
            <div class=text>

                <h1>Fill in an identifier for every </h1>
                <h1>number in the document.</h1>
                <h1>When done click OK to continue</h1>
                <h1>or click Cancel to cancel the operation</h1>
            
            </div>

            <div class="screen parentofOverflow">

                <div class="container-fluid topPartSize scrolloff">


                    <div class="content-wrapper">

                        <table class="table table-dark table-striped scrollON" onclick="UnhideScroll()">
                            <thead>
                                <tr id = "tableTitles" >

                                    ${tableTitles}


                                    
                                <!-- <th scope="col">1*</th>
                                    <th scope="col">2*</th>
                                    <th scope="col">3*</th>
                                    <th scope="col">4*</th> -->
                                    

                                </tr>
                            </thead >

                            <tbody>

                                <tr id = "tableData" >

                                    ${tableData}
                                    
                                <!-- <td>
                                        <div class="form-group thirdsize">
                                            <input type="text" class="form-control" id="identifier1" placeholder="Type here the identifier">
                                        </div>
                                    </td>
                                    <td>
                                        <div class="form-group thirdsize">
                                            <input type="text" class="form-control" id="identifier2" placeholder="Type here the identifier">
                                        </div>
                                    </td>
                                    <td>
                                        <div class="form-group thirdsize">                              
                                            <input type="text" class="form-control" id="identifier3" placeholder="Type here the identifier">
                                        </div>
                                    </td>
                                    <td>
                                        <div class="form-group thirdsize">                              
                                            <input type="text" class="form-control" id="identifier4" placeholder="Type here the identifier">
                                        </div>
                                    </td> -->
                                    


                                </tr>

                                
                            
                            </tbody>
                            
                        </table>
                    </div>

                </div>


            </div>

            <form class="needs-validation" novalidate>
        
                <div class= "buttons container-fluid">

                    <div class="row bottom">
                
                        <div class="col-xs-4"></div>

                            <button type="button" class="btn optionsbtn left btn-secondary" onclick="Cancel()">Cancel</button>              
                            <button id="waitFunction" type="button" class="btn optionsbtn right btn-secondary" onclick="checkIfAllInputsFilled()">OK</button> 

                        </div>
                    
                    </div>
                
                </div>  

            </form>
        
        </div>

            <div id="ImageDocument" class="wrapper scrollON ">

                <img class='ScrollImage' id="DocumentToClick" src="${newFileLocation}" alt="Document Image" >

            </div>

    </div>

    <script>

            GetImageCoordinates5()

    </script>

  `
//   gotResultsAdd()
  
  
  
  





}
exports.CreateImageWithMarkerStep5Return2 = CreateImageWithMarkerStep5Return2;




{/* <script>getDatabaseData();</script> */}