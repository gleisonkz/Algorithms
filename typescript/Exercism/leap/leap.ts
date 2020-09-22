function isLeapYear(year: number) {
  const divisibleBy = (operand: number) => year % operand === 0;
  return (divisibleBy(4) && !divisibleBy(100)) || divisibleBy(400);
}

export default isLeapYear;
