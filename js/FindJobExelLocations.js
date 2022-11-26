
function FindJobExcelLocationsImage(){

    location.replace("FindJobExcelLocationsImage.html");
  
  }







async function getRowColumnData(){


let process = require("process");
  
let path = require("path")

const currentWorkingDirectory=process.cwd()


const { RunPythonFile } = require(path.join(currentWorkingDirectory, './js/RunPythonFile'));



let filename = 'PlaceAboutImage.py'

// let callback =GetImageCoordinatesImage0

let callback =getRowColumnData1

// getRowColumnData1


RunPythonFile(filename, callback)


}




async function getRowColumnData1(results){

    // console.log(results)
    

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()


    // const { getDbDataSimple } = require(path.join(currentWorkingDirectory,"./js/getDbDataSimple"));


    const { RunPythonFile } = require(path.join(currentWorkingDirectory,"./js/RunPythonFile"));

    
    filename="GetItemAddressAndDescription.py"

    callback=GetItemAddressAndDescriptionReturn


    RunPythonFile(filename, callback, gotResultsFuction=true)


    


    // let resultDatabase="it has started"

    // let TableName=''

    // let Database=''
    
  



    // let DbDataGotten = await getDbDataSimple(resultDatabase,TableName,Database)

    // console.log(DbDataGotten)





    // listOfRows=DbDataGotten.listOfRows;
    // listOfColumns=DbDataGotten.listOfColumns;

    // // console.log('listOfRows 1',listOfRows);

    // // console.log('listOfColumns 1',listOfColumns);

    // listOfRows=listOfRows.slice(1, -1);

    // listOfColumns=listOfColumns.slice(1, -1);

    // // console.log('listOfRows 2',listOfRows);

    // // console.log('listOfColumns 2',listOfColumns);

    // listOfRows=listOfRows.split(",");

    // listOfColumns=listOfColumns.split(", ");

    // // console.log('listOfRows 3',listOfRows);

    // // console.log('listOfColumns 3',listOfColumns);

    // let i;
    // for (i = 0; i < listOfRows.length; i++) {

    //     listOfRows[i]=listOfRows[i].trim();
        
    //     listOfColumns[i]=listOfColumns[i].trim();

    // } 

    // // console.log('listOfRows 4',listOfRows);

    // // console.log('listOfColumns 4',listOfColumns);














    // j=0;


    // codeBlock =
    // '<tr>'+
    //     '<th scope="row center">'+[j+1]+'</th>'+              
    //     '<td>'+listOfRows[j]+'</td>'+
    //     '<td>'+listOfColumns[j]+'</td>'+
    //     '<td>'+
    //         '<form class="needs-validation" novalidate>'+
    //         '<div class="form-row">'+
    //         '<div class="col-12">'+
    //             '<input type="text" class="form-control" id="validationTooltip0'+j+'" placeholder="Type here something that identifies this position" value="" required>'+
    //             '<div class="valid-tooltip">'+
    //             'Looks good!'+
    //             '</div>'+
    //         '</div'+
    //     '</td>'

    // '</tr>'
            
    // for (j = 1; j < listOfColumns.length; j++) {
    //     codeBlock1=codeBlock;
    //     codeBlock =
    //     '<tr>'+
    //         '<th scope="row center">'+[j+1]+'</th>'+              
    //         '<td>'+listOfRows[j]+'</td>'+
    //         '<td>'+listOfColumns[j]+'</td>'+
    //         '<td>'+
    //             '<form class="needs-validation" novalidate>'+
    //             '<div class="form-row">'+
    //             '<div class="col-12">'+
    //                 '<input type="text" class="form-control" id="validationTooltip0'+j+'" placeholder="Type here something that identifies this position" value="" required>'+
    //                 '<div class="valid-tooltip">'+
    //                 'Looks good!'+
    //                 '</div>'+
    //             '</div'+
    //         '</td>'

    //     '</tr>'
    //         codeBlock=codeBlock1+codeBlock;

    //         // console.log(codeBlock);
    // }

    // // console.log("done loading html");


    // // addInfoToTheDocument();
    

    // addInforToTheDocumentHTMLcall()


    // document.getElementById("tableData").innerHTML = codeBlock;


}




async function GetItemAddressAndDescriptionReturn(results){

    // console.log(results)

    var iconv = require('iconv-lite');

    var process = require("process");

    var path = require("path")

    const currentWorkingDirectory=process.cwd()


    const { getDbDataSimple } = require(path.join(currentWorkingDirectory,"./js/getDbDataSimple"));



    const { addInforToTheDocumentHTMLcall } = require(path.join(currentWorkingDirectory,"./js/addInforToTheDocumentHTMLcall"));


    let resultDatabase="it has started"

    let TableName=''

    let Database=''
    
    
 



    let DbDataGotten = await getDbDataSimple(resultDatabase,TableName,Database)





    let itemDescription = await results[results.length - 1];

    let itemAddress = await results[results.length - 2];


    let fontName = await results[results.length - 3];

    let fontSize = await results[results.length - 4];

    

    let InPDFdatafillName = await results[results.length - 5];

    let PdfUsed0 = await results[results.length - 6];

    let FromPdf = await results[results.length - 7];

    let ExtensionType = await results[results.length - 8];




    



    let datafillName = await results[results.length - 9];




    let buff = Buffer.from(PdfUsed0, 'utf8');


    let PdfUsed = iconv.decode(buff, 'utf8');
    



    // console.log(itemAddress)

    // console.log('itemAddress above')

    // console.log(itemDescription)

    // console.log('itemDescription above')

    itemDescription0 = itemDescription.slice(2, -2); 



    let itemDescriptionList = itemDescription0.split("', '");

    // console.log(itemDescriptionList)

    // console.log('itemDescriptionList above')


    itemAddress0 = itemAddress.slice(3, -3); 

    itemAddress1= itemAddress0.split("]', '[");

    // console.log(itemAddress0)

    // console.log('itemAddress0 above')

    // console.log(itemAddress1)

    // console.log('itemAddress1 above')

    let tempListValue;

    let listOfRows=[]

    let listOfColumns=[]

    for (i = 0; i < itemAddress1.length; i++) { 


        tempListValue= itemAddress1[i].split(", ");

        listOfRows[i]=tempListValue[0]

        listOfColumns[i] =tempListValue[1]


        // console.log(itemAddressList[i])

        // console.log('itemAddressList[i]')

        // console.log(i)
    }

    // console.log(listOfRows)

    // console.log('listOfRows above')

    // console.log(listOfColumns)

    // console.log('listOfColumns above')

    

    // console.log(itemAddressList)

    // console.log('itemAddressList above')


    


    // +listOfRows[j]+'</td>'+
    // '<td>'+listOfColumns[j]+'</td>'+
    // '<td>'+itemDescriptionList[j]+'</td>

    // let fontName = results[results.length - 3];

    // let fontSize = results[results.length - 4];


   
    // listOfRows.push.apply(listOfRows, ['-', '-', '-'])

    // listOfColumns.push.apply(listOfColumns, [fontSize, fontName , '-'])

    // itemDescriptionList.push.apply(itemDescriptionList,  ['Font Name', 'Font Size', '-'])


    // let ExtensionType = DbDataGotten['ExtensionType']

    // let PDFfile = DbDataGotten['PDFfile']


    if (ExtensionType =='image'){

        if (FromPdf == 'No'){


            // listOfRows.push.apply(listOfRows, ['-', 'Font Name', 'Font Size','Pdf Used?'])

            // listOfColumns.push.apply(listOfColumns, ['-', fontName , fontSize, FromPdf])

            // itemDescriptionList.push.apply(itemDescriptionList,  ['-', '-', '-','-'])


            // listOfRows.push.apply(listOfRows, ['-', 'Font Name', 'Actual Font Size', 'Font Size Chosen', 'Pdf Used?'])

            listOfRows.push.apply(listOfRows, ['-', 'Font Name', 'Font Size', 'Pdf Used?'])

            // listOfColumns.push.apply(listOfColumns, ['-', fontName , fontSize, FontSizeShow, FromPdf])

            listOfColumns.push.apply(listOfColumns, ['-', fontName , fontSize, FromPdf])

            itemDescriptionList.push.apply(itemDescriptionList,  ['-', '-', '-', '-','-'])



        }else if(FromPdf == 'Yes'){


            // listOfRows.push.apply(listOfRows, ['-', 'Font Name', 'Actual Font Size', 'Font Size Chosen' ,'Pdf Used?', 'Pdf', 'Pdf Identifier'])

            listOfRows.push.apply(listOfRows, ['-', 'Font Name', 'Font Size','Pdf Used?', 'Pdf', 'Pdf Identifier'])

            // listOfColumns.push.apply(listOfColumns, ['-', fontName , fontSize, FontSizeShow, FromPdf, PdfUsed,InPDFdatafillName])

            listOfColumns.push.apply(listOfColumns, ['-', fontName , fontSize, FromPdf, PdfUsed,InPDFdatafillName])

            itemDescriptionList.push.apply(itemDescriptionList,  ['-', '-', '-', '-','-', '-', '-'])


        }else{


            // console.log('something is wrong, values are suposed to be only Yes or No')


        }


    }

        




    // let InPDFdatafillName = results[results.length - 5];

    // let PdfUsed = results[results.length - 6];







    j=0;


    codeBlock =
    '<tr>'+
        '<th scope="row center">'+[j+1]+'</th>'+              
        '<td>'+listOfRows[j]+'</td>'+
        '<td>'+listOfColumns[j]+'</td>'+
        '<td>'+itemDescriptionList[j]+'</td>'+
    '</tr>'

            
    for (j = 1; j < listOfColumns.length; j++) {
        codeBlock1=codeBlock;
        codeBlock =
        '<tr>'+
            '<th scope="row center">'+[j+1]+'</th>'+              
            '<td>'+listOfRows[j]+'</td>'+
            '<td>'+listOfColumns[j]+'</td>'+
            '<td>'+itemDescriptionList[j]+'</td>'+            
        '</tr>'
            codeBlock=codeBlock1+codeBlock;

            // console.log(codeBlock);
    }

    // console.log("done loading html");


    // addInfoToTheDocument();
    

    addInforToTheDocumentHTMLcall()


    document.getElementById("tableData").innerHTML = codeBlock;


    document.getElementById("datafillNameID").innerHTML = datafillName;



}