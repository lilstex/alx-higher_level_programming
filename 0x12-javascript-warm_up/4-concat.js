#!/user/bin/node
if(typeof(process.argv[3]) === 'undefined'){
    console.log(process.argv[2] + ' is undefined');
} else {
    console.log(process.argv[2] + ' is ' + process.argv[3]);
}