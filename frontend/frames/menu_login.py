import PySimpleGUI as sg
from menu_cadastro import criar_tela_cadastro
#from UsuarioDAO import UsuarioDAO

sg.theme('dark blue 14')
logo_path = r'assets\logo_fundo.png'
def criar_login():
    '''Função que leva a criação do menu de login'''
    login_layout = [
                [sg.Button(key='-SAIR-', button_color=('#cd2323', sg.theme_background_color), size=(3, 3), button_text='Sair', font=('Arial', 30, 'bold'), border_width=0), 
                sg.Button(key='-BUSCAR-', button_color=('white', sg.theme_background_color), size=(10, 3), button_text='Buscar', font=('Arial', 35, 'bold'), border_width=0, ), 
                sg.Text('|', font=('Arial', 30, 'bold')), 
                sg.Button(key='-PRATO_DO_DIA-', button_color=('white', sg.theme_background_color), size=(10, 3), button_text='Pratos do dia', font=('Arial', 35, 'bold'), border_width=0), \
                sg.Text('|', font=('Arial', 30, 'bold')), 
                sg.Button(key='-MAPA-', button_color=('white', sg.theme_background_color), size=(10, 3), button_text='Mapa', font=('Arial', 35, 'bold'), border_width=0), 
                sg.Text(''), 
                sg.Text('|', font=('Arial', 30, 'bold')), 
                sg.Button(key='-LOGIN-', button_color=('gray', sg.theme_background_color), size=(10, 3), button_text='Login', font=('Arial', 30, 'bold'), border_width=0)], 
                [sg.Image(filename=logo_path, enable_events=True)], 
                [sg.Text('Login', font=('Arial', 20, 'bold'), justification='center')], 
                [sg.Input(key='-LOGIN_USUARIO-')], 
                [sg.Text('Senha', font=('Arial', 20, 'bold'), justification='center')], 
                [sg.Input(key='-PASSWORD-', password_char='*')],
                [sg.Button(key='-ENTRAR-', button_color=('#23cd4b', sg.theme_background_color), button_text='Entrar', font=('Arial', 30, 'bold'), border_width=0)], 
                [sg.Button(key='-CADASTRAR-', button_color=('#cd2323', sg.theme_background_color), button_text='Não tem login? Fazer cadastro!', font=('Arial', 20, 'bold'), border_width=0)]]

    menu_login = sg.Window('Food Finder', login_layout, finalize=True, 
                               element_justification='center')
    menu_login.maximize()
    while True:
        event, values = menu_login.read()
        if event==sg.WINDOW_CLOSED or event=='Não quero comer nada' or event=='-SAIR-':
            break

        elif event == '-ENTRAR-':
            login = values['-LOGIN_USUARIO-']
            senha = values['-PASSWORD-']
            
            resultado = UsuarioDAO().login_usuario(login, senha)

            print(resultado)

        elif event == '-CADASTRAR-':
            criar_tela_cadastro()

        if event=='-SAIR-':
            for window in list(sg.Window):
                sg.Window(window).close()
                