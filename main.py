from confidential import credential
import getpass # Get user info
import os # Verify directory and files
import pandas as pd # Allow dataframes
from datetime import datetime # Allow dates
from tkinter import * # Support to window


# - Start of confidential.py file ---------------------------------- #
# It was defined at confidential.py file to hidden confidential data

# def credential(user):
#     root = fr'C:\Users\{user}\[...]\Documents\hr_HourControl'
#     base = fr'{root}\database.csv'
#     return {'root': root, 'base': base}

# - End of confidential.py file ------------------------------------ #


# VARIABLES
user = credential(getpass.getuser())
root_verify = os.path.exists(user['root'])
base_verify = os.path.exists(user['base'])
sys_verify = [root_verify, base_verify]

# FUNCTIONS
def create_structure(create):
    if create:
        os.makedirs(user['root'])
    database = open(user['base'],'w+')
    header = 'id,date,enter_hour,pause_hour,return_hour,exit_hour,first_dur,pause_dur,second_dur,total_dur,extra_time,comment'
    database.write(header)
    database.close()

def update_table(moment):
    actual_date = datetime.now().strftime('%d/%m/%y')
    actual_datetime = datetime.now().strftime('%d/%m/%y %H:%M:%S')
    match moment:
        case 'enter':
            database.loc[new_id] = [f'{new_id}',f'{actual_date}',f'{actual_datetime}','','','','','','','','','']
            database.to_csv(user['base'], index=False)
            print('\n\n- HR HOURCONTROL -------------------')
            print(getpass.getuser())
            print('ENTRADA: ',database['enter_hour'][new_id])
            print('------------------------------------\n\n')
        case 'pause':
            database['pause_hour'][new_id] = actual_datetime
            database['first_dur'][new_id] = pd.to_datetime(database['pause_hour'][new_id]) - pd.to_datetime(database['enter_hour'][new_id])
            database.to_csv(user['base'], index=False)
            print('\n\n- HR HOURCONTROL -------------------')
            print(getpass.getuser())
            print('ENTRADA:          ',database['enter_hour'][new_id])
            print('PAUSA:            ',database['pause_hour'][new_id])
            print('HORAS TRABALHADAS:',database['first_dur'][new_id])
            print('------------------------------------\n\n')
        case 'return':
            database['return_hour'][new_id] = actual_datetime
            database['pause_dur'][new_id] = pd.to_datetime(database['return_hour'][new_id]) - pd.to_datetime(database['pause_hour'][new_id])
            database.to_csv(user['base'], index=False)
            print('\n\n- HR HOURCONTROL -------------------')
            print(getpass.getuser())
            print('ENTRADA:          ',database['enter_hour'][new_id])
            print('PAUSA:            ',database['pause_hour'][new_id])
            print('HORAS TRABALHADAS:',database['first_dur'][new_id])
            print('------------------------------------')
            print('TEMPO DE PAUSA:   ',database['pause_dur'][new_id])
            print('------------------------------------')
            print('RETORNO DA PAUSA: ',database['return_hour'][new_id])
            print('------------------------------------\n\n')
        case 'exit':
            database['exit_hour'][new_id] = actual_datetime
            database['second_dur'][new_id] = pd.to_datetime(database['exit_hour'][new_id]) - pd.to_datetime(database['return_hour'][new_id])
            database['total_dur'][new_id] = (pd.to_datetime(database['exit_hour'][new_id]) - pd.to_datetime(database['return_hour'][new_id])) + (pd.to_datetime(database['pause_hour'][new_id]) - pd.to_datetime(database['enter_hour'][new_id]))
            print('\n\n- HR HOURCONTROL -------------------')
            print(getpass.getuser())
            print('ENTRADA:          ',database['enter_hour'][new_id])
            print('PAUSA:            ',database['pause_hour'][new_id])
            print('HORAS TRABALHADAS:',database['first_dur'][new_id])
            print('------------------------------------')
            print('TEMPO DE PAUSA:   ',database['pause_dur'][new_id])
            print('------------------------------------')
            print('RETORNO DA PAUSA: ',database['return_hour'][new_id])
            print('SAÍDA:            ',database['exit_hour'][new_id])
            print('HORAS TRABALHADAS:',database['second_dur'][new_id])
            print('------------------------------------')
            print('TOTAL TRABALHADO :',database['total_dur'][new_id])
            print('------------------------------------\n\n')
            if input('Deseja adicionar algum comentário?') != 'n':
                comment = input('O que deseja destacar?\n')
                database['comment'][new_id] = comment
            database.to_csv(user['base'], index=False)


# PROCESSES
# VERIFY IF PATH AND FILES NEEDED EXISTS
match sys_verify:
    case [True, True]:
        pass
    case [True, False]:
        create_structure(False)
    case _:
        create_structure(True)

# TESTE JANELA
# window = Tk()
# window.title('HR HourControl')
# window.mainloop()
# exit()

# WHEN RUN, SET START HOUR
database = pd.DataFrame(pd.read_csv(user['base']))
new_id = database.shape[0] + 1
update_table('enter')
pause = 'n'
while pause == 'n':
    pause = input('Deseja realizar a sua pausa? (Y/n)')
update_table('pause')
back = 'n'
while back == 'n':
    back = input('Deseja retornar da pausa? (Y/n)')
update_table('return')
finish = 'n'
while finish == 'n':
    finish = input('Deseja finalizar o expediente? (Y/n)')
update_table('exit')
kronos_today = database.loc[new_id]
print(kronos_today)