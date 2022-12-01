

// function ChoosenImage(IdChoosen){


//     let node = document.getElementById(IdChoosen);
//     let ImageName  = node.textContent || node.innerText;

//     console.log(ImageName)





// }





function OPFSelectImageFile4(tableTitles, tableData) {

    // var process = require("process");

    // var path = require("path")

    // const currentWorkingDirectory=process.cwd()

    // const { gotResultsAdd } = require(path.join(currentWorkingDirectory, "./js/gotResultsAdd"));

    // console.log(tableTitles)

    ResultsObj =
    // document.documentElement.innerHTML=
    `

    <div id="foreGroundImage" class="containingArea centered MainLogo noClickImg">

        <img src="_images/LogInImg.png" onclick="hideImage()" alt="MainLogo" >

    </div>

    <div id = "createImageGetData" >    
        <div>
            <div class=text>

                <h1>Select an image file below</h1>
                <h1>to add it to the database</h1>
                <h1>or click Cancel to cancel the operation</h1>
            
            </div>

            <div class="screen parentofOverflow">

                <div class="container-fluid topPartSize scrolloff">


                    <div class="content-wrapper">

                        <table class="table table-dark table-striped scrollON" onclick="UnhideScroll()">
                                <thead>
                                    <tr id = "tableTitles" >

                                        ${tableTitles}

                                    </tr>
                                </thead >
                            <tbody>

                                <tr id = "tableData" >

                                    ${tableData}

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
                            
                        </div>
                    
                    </div>
                
                </div>  

            </form>
        
        </div>

    </div>

    <script>

        OPFSelectImageFile()

    </script>

  `;

let  d1 = document.getElementById('AllNormalItems');
    d1.insertAdjacentHTML('afterbegin', ResultsObj);

}
exports.OPFSelectImageFile4 = OPFSelectImageFile4;




