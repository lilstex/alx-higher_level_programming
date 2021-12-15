#!/user/bin/node
const list = require('./100-data.js').list;

map_list = list.map((el, index) => el * index);
console.log(list);
console.log(map_list);