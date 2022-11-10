from confidential import credential
import getpass
import os # Verify directory and files


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
    header = 'id,enter_hour,pause_hour,return_hour,exit_hour,first_dur,pause_dur,second_dur,total_dur,extra_time'
    first_content = list()
    first_content.append(header)
    first_content.append('\n1,,,,,,,,,')
    database.writelines(first_content)
    database.close()

# PROCESS
match sys_verify:
    case [True, True]:
        pass
    case [True, False]:
        create_structure(True)
    case _:
        create_structure(False)

print('FIM')