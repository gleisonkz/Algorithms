import PySimpleGUI as sg


class SimpleScreen:
    def __init__(self):
        layout = [
            [sg.Text('Video URL', size=(9, 0)), sg.InputText(key='videoURL')],
            [sg.Text('E-mail', size=(9, 0)), sg.InputText(key='email', size=(35, 0),default_text="")],
            [sg.Text('Password', size=(9, 0)), sg.InputText(key='password', size=(35, 0), password_char='*',default_text="")],
            [sg.InputOptionMenu(('Passive Listening', 'Active Listening'), key='option')],
            [sg.Button('Ok', size=(9, 0))]
        ]

        sg.theme('DarkAmber')
        self.window = sg.Window('Login info', layout)
        self.button, self.values = self.window.Read()
        self.optionClassNameOnPage = {
            'Passive Listening': 'ul.nav.nav-list.conteudoItemLista.__tab-campo > li:nth-child(2)',
            'Active Listening': 'ul.nav.nav-list.conteudoItemLista.__tab-campo > li:nth-child(1)'
        } 

    def closeWindow(self):    
        self.window.Close()

    def openScreen(self):        
        return [
            self.values['videoURL'],
            self.values['email'],
            self.values['password'],
            self.optionClassNameOnPage[self.values['option']],
        ]

