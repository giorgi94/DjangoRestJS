const fs = require('fs')

var symbols = '0123456789abcdefghijklmnopqrstuvwxyz';

var write_hash = (hash, name) => {

    if(name) {
        name += '-hash'
    }
    else {
        name += 'hash'
    }

    fs.writeFile(`${__dirname}/../../context/hash/${name}.txt`, hash, (err)=>{
        if(err) {
            return console.log(err);
        }
        console.log(`\n${name} is updated\n`);
    })
}

var make_hash = (length, name) => {
    var h = '';
    for(let i=0; i<length; i++) {
        h += symbols[Math.floor(Math.random()*symbols.length)];
    }
    write_hash(h, name)
    return h;
}


module.exports = make_hash;
