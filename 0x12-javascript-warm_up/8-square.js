#!/user/bin/node 
const size = parseInt(process.argv[2]);
if (Number.isInteger(size)) {
    for(i = 0; i < size; i++){
        let x = '';
        for(j = 0; j < size; j++) {
            x+= 'x';
        }
        console.log(x);
        }
} else {
    console.log('Missing size');
}