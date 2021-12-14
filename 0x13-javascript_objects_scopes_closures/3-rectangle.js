#!/user/bin/node
module.exports = class Rectangle {
    constructor(w, h) {
        if(w > 0 && h > 0) {
            this.width = w;
            this.height = h;
        }
    };

    print() {
        for(i=0; i < this.height; i++){
            let row = 0;
            for(j=0; j < this.width; j++){
                row+= 'x';
            }
            console.log(row);
        }
    }
}