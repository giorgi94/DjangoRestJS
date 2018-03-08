const fs = require('fs')

var symbols = '0123456789abcdefghijklmnopqrstuvwxyz';

var wHash = (ext, hash) => {
    fs.writeFile(`${__dirname}/hash/${ext}.hash`, hash, (err)=>{
        if(err) {
            return console.log(err);
        }
        console.log(`\n${ext}.hash is updated\n`);
    })
}

var gHash = (length, ext) => {
    var h = '';
    for(let i=0; i<length; i++) {
        h += symbols[Math.floor(Math.random()*symbols.length)];
    }
    wHash(ext, h)
    return h;
}


module.exports = {
    gHash
}
