export class ResistorColor {
  private colors: string[];
  private validations = [
    {
      key: () => this.colors.length < 2,
      value: () => {
        throw new Error("At least two colors need to be present");
      },
    },
  ];
  constructor(colors: string[]) {
    this.colors = colors;
    this.validations.find((validation) => validation.key())?.value();
  }
  value = (): number => {
    const keyValuePairColors: { [key: string]: number } = {
      black: 0,
      brown: 1,
      red: 2,
      orange: 3,
      yellow: 4,
      green: 5,
      blue: 6,
      violet: 7,
      grey: 8,
      white: 9,
    };

    return +this.colors
      .map((c) => keyValuePairColors[c])
      .slice(0, 2)
      .join("");
  };
}
