#!/user/bin/node
if (process.argv.length <= 3) {
    console.log(0);
} else {
    int_args = process.argv.map(Number);
    const sec_biggest = int_args.sort(function (a, b){ return b-a})[3];
    console.log(sec_biggest);
}