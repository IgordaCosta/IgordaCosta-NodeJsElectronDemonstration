

function GetHtmlFromPage(StartVariable){

    return new Promise((resolve, _reject) => {

        window.onload = function() {

        // console.log(StartVariable)

        let htmlBodyObject = document.documentElement.innerHTML

        resolve(htmlBodyObject)
            
        }

        

    }

    )

}

async function LMFgetFileNames(){

    // window.onload = function() {

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()

    const { getDbData } = require(path.join(currentWorkingDirectory, './js/getDbData'));

    const { gotResults } = require(path.join(currentWorkingDirectory, './js/gotResults'));

    // const { readHTMLTextFile } = require(path.join(currentWorkingDirectory,"./js/readHTMLTextFile"));

    // const { gotResultsRemove } = require(path.join(currentWorkingDirectory, './js/gotResultsRemove'));

    const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory, './js/MyDocumentsDatabasePath'));

    const { AddAnyDataToHtml } = require(path.join(currentWorkingDirectory, './js/AddAnyDataToHtml'));

    // let htmlBodyObject = document.documentElement.innerHTML

    // console.log(htmlBodyObject)


    gotResults()


    // StartVariable="it has started"

    // htmlBodyObject= await GetHtmlFromPage(StartVariable)


    let MydocumentsDbPath = await MyDocumentsDatabasePath(currentWorkingDirectory)

    let CurrentWorkingPath = currentWorkingDirectory

    let Database=''

    let TableName=''

    let resultDatabase = MydocumentsDbPath

    let DbDataGotten =await getDbData(resultDatabase,TableName,Database,CurrentWorkingPath,MydocumentsDbPath)

    let ListofInlist=DbDataGotten.ListofInlist



    let spacedComa =  "', '"
    // console.log(ListofInlist.length)

    // console.log('above is ListofInlist.length')

    // console.log(ListofInlist)
    // console.log('ListofInlist string is above')

    let CorrectedText=ListofInlist.slice(1, -1);
          
    ListofInlist=CorrectedText.split(spacedComa);

    // console.log(ListofInlist)

    // console.log('ListofInlist as a list is above')

    let j=0;


    if (ListofInlist.constructor === Array){

    codeBlock =
    '<tr>'+
        '<th scope="row center">'+[j+1]+'</th>'+   
    
        // '<td>'+jobNameList[0][j]+'</td>'+
        '<td>'+ListofInlist[j]+'</td>'+
    
    '</tr>'

    
    for (j = 1; j < ListofInlist.length; j++) {



        codeBlock1=codeBlock;
        codeBlock =
        '<tr>'+
            '<th scope="row center">'+[j+1]+'</th>'+   
        
            // '<td>'+jobNameList[0][j]+'</td>'+
            '<td>'+ListofInlist[j]+'</td>'+
        
        '</tr>'


            codeBlock=codeBlock1+codeBlock;

    }

}else{

    codeBlock =
    '<tr>'+
        '<th scope="row center">'+[j+1]+'</th>'+   
    
        // '<td>'+jobNameList[0][j]+'</td>'+
        '<td>'+ListofInlist+'</td>'+
    
    '</tr>'

}
    


    // var process = require("process");

    // var path = require("path")

    // const currentWorkingDirectory=process.cwd()

    // const { getDbData } = require(path.join(currentWorkingDirectory, './js/getDbData'));

    // const { MyDocumentsDatabasePath } = require(path.join(currentWorkingDirectory, './js/MyDocumentsDatabasePath'));


    // let MydocumentsDbPath = await MyDocumentsDatabasePath(currentWorkingDirectory)

    // let CurrentWorkingPath = currentWorkingDirectory

    // let Database=''

    // let TableName=''

    // let resultDatabase = MydocumentsDbPath

    // let DbDataGotten =await getDbData(resultDatabase,TableName,Database,CurrentWorkingPath,MydocumentsDbPath)

    // let codeBlock = DbDataGotten.codeBlock
                
    // document.getElementById("tableData").innerHTML = codeBlock;

    let HtmlID="tableData"

    let DataToAdd=codeBlock

    // file=path.join(currentWorkingDirectory, './LMFNotValidFileNames.html')
    // console.log(file)
    // console.log("file loaded name above")


    // let htmlBodyObject=await readHTMLTextFile(file)

    // console.log(htmlBodyObject)

    // console.log('htmlBodyObject above')

    let htmlBodyObject= await LMFNotValidNamesHtml()

    AddAnyDataToHtml(htmlBodyObject,DataToAdd,HtmlID)

    try{
        document.getElementById("WholeHtml").classList.remove('hidden');
    }catch(e){
        // console.log(e)
        // console.log("if it is the second time loading this page its ok")
    }
    


    // gotResultsRemove()


    // file=path.join(currentWorkingDirectory, './LMFNotValidFileNames.html')


    // let HtmlRead=await readTextFile(file)

    // console.log(HtmlRead)

    // console.log('HtmlRead above')

    

    


    // }
}

function LMFNotValidNamesHtml(){

    return new Promise((resolve, _reject) => {

        HtmlObj=`
        <div class="text">
        
            <h1>Above is listed invalid file name(s)</h1>
            <h1>Change the name(s) of the listed file(s)</h1>
            <h1>and click OK to try again or</h1>
            <h1>click CANCEL to quit this process.</h1>
                    
    </div>

    
    <div class="screen parentofOverflow">

        <div class="container-fluid topPartSize scrolloff">

        <div id="foreGroundImage" class="containingArea centered MainLogo noClickImg">

            <img src="_images/LogInImg.png" onclick="hideImage()" alt="MainLogo" >
    
        </div>
          <div class="content-wrapper">

              <table class="table table-dark table-striped scrollableArea" onclick="UnhideScroll()">
                <thead>
                  <tr>

                    <th scope="col">#</th>
                    <th scope="col">File_Saved_Location</th>
                    
                  </tr>
                </thead >
                <tbody id="tableData">

                  <script>LMFgetFileNames();</script>  
                  
                </tbody>
                
              </table>
          </div>
        </div>                   
    </div>

    <div>
        <button type="button" class="btn optionsbtn right btn-secondary" onclick="LMFAddInfoExcel()" >OK</button>
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
        `

        resolve(HtmlObj)


    }


    )
    

}