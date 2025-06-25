def format_name(f_name, l_name):
    if f_name == '' or l_name == '':
        return 'You did not provide valid input'
    name_formatted = f_name + ' ' + l_name
    return name_formatted.title()

f_name = input('What is your first name? ')
l_name = input('What is your last name? ')
print(format_name(f_name, l_name))