class Transcriptor {
    keyValuePair: { [key: string]: string } = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U',
    }

    private getRNA(c: string): string {

        const value = this.keyValuePair[c]
        if (!value) { throw new Error('Invalid input DNA.') }
        return value;
    }

    toRna(amostras: string): string {

        const newArray = [...amostras].map(c => this.getRNA(c)).join('');
        return newArray
    }
}
export default Transcriptor