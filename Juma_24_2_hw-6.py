import re

data_base = open('MOCK_DATA.txt', 'r')
content = data_base.read()
data_base.close()

while True:
    print('1 - Считать имена и фамилии')
    print('2 - Считать все емайлы')
    print('3 - Считать названия файлов')
    print('4 - Считать цвета')
    print('5 - Выход')
    command = input('Введите комманду:')
    if command == '5':
        print('Выход')
        break
    elif command == '1':
        with open('names.txt', 'w', encoding='utf-8') as full_name:
            names_list = re.findall(r'\b[A-Z][a-zA-Z\'\-\. ]+[\s]+[a-zA-Z\'\-\. ]+\b', content)
            for name in names_list:
                full_name.write(f'{name}\n')

    elif command == '2':
        with open('emails.txt', 'w', encoding='utf-8') as emails:
            emails_list = re.findall(r'(\b[\w\-]+[@][\w\-]+(\.[\w\-]+)+)', content)
            for email in emails_list:
                emails.write(f'{email}\n')

    elif command == '3':
        with open('file.txt', 'w', encoding='utf-8') as files:
            file_list = re.findall(r'[\t\s][\w]+\.[\w]+\b', content)
            for file in file_list:
                files.write(f'{file}\n')

    elif command == '4':
        with open('color.txt', 'w', encoding='utf-8') as colors:
            colors_list = re.findall('#[0-9|a-z]*', content)
            for color in colors_list:
                colors.write(f'{color}\n')

    else:
        print('\n\tКоманнда не верна.\n')

