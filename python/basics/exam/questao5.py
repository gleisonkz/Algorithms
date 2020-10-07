def printIfIsPalindrome(word: str) -> None:
    word = word.lower()
    reversedWord = word[::-1]
    if(reversedWord == word):
        print(f"The word: {word} is a palindrome ")


printIfIsPalindrome("ana")
printIfIsPalindrome("Carlos")
printIfIsPalindrome("Ele")
printIfIsPalindrome("Teste")
