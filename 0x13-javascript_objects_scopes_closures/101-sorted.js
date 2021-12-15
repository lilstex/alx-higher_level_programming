#!/user/bin/node
const dict = require('./101-data.js').dict;

let new_dict = {};
for(let key in dict) {
    new_dict[dict[key]] = [key];
}

console.log(new_dict);