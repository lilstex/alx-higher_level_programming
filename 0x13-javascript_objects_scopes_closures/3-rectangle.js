#!/user/bin/node
module.exports = class Rectangle {
    constructor(w, h) {
        if(w > 0 && h > 0) {
            [this.width, this.height] = [w, h];
        }
    };

    print() {
        for(let i=0; i < this.height; i++){
            let row = 'x';
            for(let j=0; j < this.width-1; j++){
                row+= 'x';
            }
            console.log(row);
        }
    }
}