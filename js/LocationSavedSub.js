
function Cancel (){
    location.replace("index.html");
}


function placeDatafillName(){

    let CurrentWorkingDirectory = process.cwd();

    // console.log(CurrentWorkingDirectory);

    // console.log('CurrentWorkingDirectory is above');

    const { getLocationSaved } = require(path.join(CurrentWorkingDirectory,"./js/getLocationSaved"));

    htmlBodyObject = `
    
    <div class = 'text'>
        <div class="screen parentofOverflow">      
                <div class="content-wrapper">
                    
                    <h1>The document was saved on</h1>
                    <h1>the following subfolders:</h1>

                    <div class="container-fluid topPartSize1 scrolloff StraightLine" onclick="UnhideScroll1()">
                            
                                                       
                    




                        <table class="table table-dark table-striped " >
                                <thead>
                                    <tr id = "tableTitles" >
                                                                        

                                    </tr>
                                </thead >

                                <tbody>

                                    <tr id="SaveNameID" >

                                        
                                        
                                    <!-- <td>
                                            <div class="form-group thirdsize">
                                                <h1 id="SaveNameID"></h1>
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

        <br>

        <div class="screen parentofOverflow">      
                <div class="content-wrapper">
                    
                    <h1>In the following location:</h1>

                    <div class="container-fluid topPartSize2 StraightLine2 scrolloff" onclick="UnhideScroll2()">
                            
                        <h1 id="SaveLocationID"></h1>
                                    
                    </div>
                </div>            
        </div>
    </div>






<div id="foreGroundImage" class="containingArea centered MainLogo noClickImg">

    <img src="_images/LogInImg.png" onclick="hideImage()" alt="MainLogo" >

</div>

<div>
        <button type="button" class="btn optionsbtn right btn-secondary" onclick="OperationComplete()" >OK</button>
</div>




<script>placeDatafillName()</script>

<script>

let jquerypath = path.join(__dirname, './js/jquery');
window.jQuery = window.$ = require(jquerypath);

</script>
<script src="./js/popper.min.js"></script>
<script src="./js/bootstrap.min.js"></script>

`;



getLocationSaved(htmlBodyObject)


}






