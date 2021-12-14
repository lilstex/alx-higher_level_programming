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

    rotate() {
        [this.width, this.height] = [this.height, this.width];
    }

    double() {
        [this.width, this.height] = [this.width * 2, this.height * 2];
    }
}