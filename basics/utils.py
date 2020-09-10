from time import sleep


class Utils:
    @staticmethod
    def showMessage(message):
        for index in range(8):
            dots = [
                f'{message}   ', f'{message}.', f'{message}..', f'{message}...',
                f'{message}   ', f'{message}.', f'{message}..', f'{message}...',
            ]
            print(f"{dots[index]}", end="\r")
            sleep(0.2)
        print('\n')

    @staticmethod
    def inputToInt(message):
        try:
            return int(input(message))
        except ValueError:
            print("You must be input a integer value.")
            return Utils.inputToInt(message)
