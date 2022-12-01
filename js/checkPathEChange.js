let path = require("path");

let filenamecheck=path.basename(__dirname);

if (filenamecheck=="CSSAutoFormFiller"){}else{
    __dirname = path.join(__dirname, '../../../../../../');

}
