"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
class Transcriptor {
    constructor() {
        this.keyValuePair = {
            'G': 'C',
            'C': 'G',
            'T': 'A',
            'A': 'U',
        };
    }
    getRNA(c) {
        const value = this.keyValuePair[c];
        if (!value) {
            throw new Error('Invalid input DNA.');
        }
        return value;
    }
    toRna(amostras) {
        const newArray = amostras.split('').map(c => this.getRNA(c)).join('');
        return newArray;
    }
}
exports.default = Transcriptor;
//# sourceMappingURL=rna-transcription.js.map