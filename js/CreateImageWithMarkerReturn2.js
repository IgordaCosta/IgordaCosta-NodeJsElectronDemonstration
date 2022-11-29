
function CreateImageWithMarkerReturn2(newFileLocation, FontSize) {


    

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()

    const { fontSelect } = require(path.join(currentWorkingDirectory, "./js/fontSelect"));

    

    // console.log('newFileLocation: ', newFileLocation);

    // console.log('FontSize: ', FontSize);

    // console.log("newFileLocation inside new function");

    // document.body.innerHTML = `

    document.getElementById("AllNormalItems").innerHTML = `

    <div id = "createImageGetData" class= 'hidden'">    
        <div>
            <div class=text>

                <h1>Choose a Word size and font then</h1>
                <h1>click Try configuration to see how it will look.</h1>
                <h1>Click OK when you are happy with your choice</h1>
                <h1>or click Cancel to cancel the operation</h1>
            
            </div>

            <form class= 'row WordSizeForm'>

                <div class= "container-fluid">

                    <div class="row">
                    
                        <div class="col-xs-4">

                            <label for="wordSize">Word size (${FontSize}):</label>
                            <input id="wordSize" class="btn optionsbtn SmallerButton left btn-secondary" type="number" name="wordSize"  min="1" max="1000" required>
                            <span class="validity"></span>

                        </div>

                        <div class="col-xs-4">

                            <p id = "ShowFontTypeHere" class= "right" >This is how the font looks when it is changed</p>

                        </div>
                            
                    </div>
                    
                </div> 
      
            
            </form>

            <form id = "FontSelector" class="needs-validation" novalidate>
    
                <div class= "container-fluid">
            

                    <div class="row">
                
                        <div class="col-xs-4"></div>

                            <input class= "btn optionsbtn left" id="font4" type="text">

                    </div>

                        <div class="col-xs-4">

                            <button id= "FontSelector" type="button" class="btn optionsbtn right btn-secondary" onclick="PlaceChoosenSizeInDb()">Try configuration</button>
                    
                        </div>
                
                </div>


               

            </form>


            <form class="needs-validation" novalidate>
        
                <div class= "buttons container-fluid">

                    <div class="row bottom">
                
                        <div class="col-xs-4"></div>

                            <button type="button" class="btn optionsbtn left btn-secondary" onclick="Cancel()">Cancel</button>              
                            <button type="button" class="btn optionsbtn right btn-secondary" onclick="GetImageCoordinates4CheckClick()">OK</button> 

                        </div>
                    
                    </div>
                
                </div>  

            </form>
        
        </div>

        <div id="ImageDocument" class="wrapper scrollON hidden">

            <img class='ScrollImage' id="DocumentToClick" src="${newFileLocation}" alt="Document Image" >

        </div>

    </div>
  

  `


  window.onload = fontSelect()

//   fontSelect()
// console.log('went up to create image marker return 2');


//   gotResultsAdd()
  
  
  
//   ;





}
exports.CreateImageWithMarkerReturn2 = CreateImageWithMarkerReturn2;
