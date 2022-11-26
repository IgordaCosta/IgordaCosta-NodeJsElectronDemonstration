path = require("path");

let filenamecheck=path.basename(__dirname);
// console.log(filenamecheck);
// console.log("filename check above");

if (filenamecheck=="CSSAutoFormFiller"){}else{
    __dirname = path.join(__dirname, '../../../../../../');

}
// console.log(__dirname)
// console.log("new above __dirname")