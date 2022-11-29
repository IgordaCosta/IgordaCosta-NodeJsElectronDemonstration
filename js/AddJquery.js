function AddJqueryToHtml(){


    var path = require("path")
    var process = require("process")
    const CurrrentWorkingDirectory=process.cwd()


    try{
      let path = require("path");
      let jquerypath = path.join(CurrrentWorkingDirectory, './js/jquery');
      window.jQuery = window.$ = require(jquerypath);
    } catch (e){
      console.log(e);
      path = require("path");
      let jquerypath = path.join(CurrrentWorkingDirectory, './js/jquery');
      window.jQuery = window.$ = require(jquerypath);
    }
    
    





};

try{
exports.AddJquery = AddJquery;
}catch{}