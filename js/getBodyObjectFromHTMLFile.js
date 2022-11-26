function getBodyObjectFromHTMLFile(HTMLfile) {

    let mySubString = HTMLfile.substring(
        HTMLfile.lastIndexOf("<body>") + 6,
        HTMLfile.lastIndexOf("</body>")
    );

    return mySubString;

}
exports.getBodyObjectFromHTMLFile = getBodyObjectFromHTMLFile;
