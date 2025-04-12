import PySimpleGUI as sg

layout = [[sg.Input(key='-IN-'), sg.FileBrowse()],
          [sg.Button('Go'), sg.Button('Exit')]]

window = sg.Window('File Browse Example', layout)
event, values = window.read()
print(f'File chosen: {values["-IN-"]}')
window.close()
