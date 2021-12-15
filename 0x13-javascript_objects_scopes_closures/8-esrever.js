#!/user/bin/node

exports.esrever = function (list) {
    const rev = [];
    len = list.length;
    for(i=0; i < len; i++) {
        rev.push(list.pop());
    }
    return rev;
}