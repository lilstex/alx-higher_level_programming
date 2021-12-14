#!/user/bin/node
const n = parseInt(process.argv[2]);

function factorial(n) {
    if (n < 0) {
        return -1;
    } else if (n == 0) {
        return 1;
    } else if (!Number.isInteger(n)) {
        return 1;
    } else {
        return n * factorial(n-1);
    }
}

const fact = factorial(n);
console.log(fact);