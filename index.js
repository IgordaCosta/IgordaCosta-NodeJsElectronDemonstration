// Modules to control application life and create native browser window


// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.


let {app, protocol, BrowserWindow} = require("electron");
let {readFile} = require("fs");
let {extname} = require("path");
let {URL} = require("url");


let createProtocol = (scheme, normalize = true) => {
  protocol.registerBufferProtocol(scheme,
    (request, respond) => {
      let pathName = new URL(request.url).pathname;
      pathName = decodeURI(pathName); // Needed in case URL contains spaces
    
      readFile(__dirname + "/" + pathName, (error, data) => {
        let extension = extname(pathName).toLowerCase();
        let mimeType = "";

        if (extension === ".js") {
          mimeType = "text/javascript";
        }
        else if (extension === ".html") {
          mimeType = "text/html";
        }
        else if (extension === ".css") {
          mimeType = "text/css";
        }
        else if (extension === ".svg" || extension === ".svgz") {
          mimeType = "image/svg+xml";
        }
        else if (extension === ".json") {
          mimeType = "application/json";
        }

        respond({mimeType, data}); 
      });
    },
    (error) => {
      if (error) {
        // console.error(`Failed to register ${scheme} protocol`, error); // this is a default error message
      }
    }
  );
}



let mainWindow

// let valueMultiply=1.2;

// let widthvalue=800*valueMultiply;
// let heightvalue=600*valueMultiply;    // this is how the height and width if found

const widthvalue=960;
const heightvalue=720;

function createWindow(){

  createProtocol("app");

  let browserWindow = new BrowserWindow({
    
    width: widthvalue,
    height: heightvalue,
    resizable:false,
    useContentSize: true,
    // autoHideMenuBar: true,    // after testing and building the app change this to true, it must be done to fix resizing without being asked to
    icon: __dirname + '/_images/python-icon.ico',
    webPreferences: {
      nodeIntegration: true,
      preload: `${__dirname}/preload.js`
    }
 
  });
  
  browserWindow.setAlwaysOnTop(true, 'floating');

  browserWindow.loadFile("index.html");

  // browserWindow.loadFile("index.html");
  browserWindow.on('closed', function () {
        // Dereference the window object, usually you would store windows
        // in an array if your app supports multi windows, this is the time
        // when you should delete the corresponding element.
        browserWindow = null


})
}


//   // Emitted when the window is closed.
//   mainWindow.on('closed', function () {
//     // Dereference the window object, usually you would store windows
//     // in an array if your app supports multi windows, this is the time
//     // when you should delete the corresponding element.
//     mainWindow = null
//   })
// }

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
// app.on('ready', createWindow)

// Quit when all windows are closed.
app.on('window-all-closed', function () {
  // On macOS it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
    app.quit()
})


// Standard scheme must be registered before the app is ready
protocol.registerStandardSchemes(["app"], { secure: true });

app.on("ready", () => {

  createWindow()
  
});


app.on('activate', function () {
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (mainWindow === null) {
    createWindow()
  }
})


