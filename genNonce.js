const crypto = require('crypto');
let nonce = crypto.randomBytes(16).toString('base64');

console.log(nonce)

// change to index.js on package.json after running this and getting the nonce value
// then add the nonce value to manifest.json file