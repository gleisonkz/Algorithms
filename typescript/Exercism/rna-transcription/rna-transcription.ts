class Transcriptor {
  private validators = [
    {
      expect: (value: string) => !this.keyValuePair[value],
      action: () => {
        throw new Error("Invalid input DNA.");
      },
    },
  ];
  private keyValuePair: { [key: string]: string } = {
    G: "C",
    C: "G",
    T: "A",
    A: "U",
  };

  private getRNA(dna: string): string {
    this.validators.find((item) => item.expect(dna))?.action();
    const value = this.keyValuePair[dna];
    return value;
  }

  toRna(dnaList: string): string {
    const newArray = [...dnaList].map((dna) => this.getRNA(dna)).join("");
    return newArray;
  }
}
export default Transcriptor;
