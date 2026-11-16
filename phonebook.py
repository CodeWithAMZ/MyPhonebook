#-----Imported Libraries-----
import sqlite3
import os

#-----Sqlite Database Connection-----
conn = sqlite3.connect('phonebook.db')
cur = conn.cursor()
cur.execute('''
    create table if not exists contacts (
        name TEXT,
        number TEXT
    )
''')

conn.commit()

#-----Menu-----
c=0
while c != 6:
    input('Press Enter to continue...')
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n----- My PhoneBook v2.0 -----')
    print('1. Add Contact')
    print('2. List Contact')
    print('3. Search Contact')
    print('4. Delete Contact')
    print('5. Edit Contact')
    print('6. Exit')
    choose = input('\nChoose an option: ')

    #-----Add Contact-----
    if choose == '1':
        name1 = input('Enter Contact Name: ')
        number1 = input('Enter Contact Number: ')
        cur.execute('''
            insert into contacts (name, number) values (?, ?)
        ''', (name1, number1))
        conn.commit()
        print('Contact Added Successfully!')

    #-----List Contact-----
    elif choose == '2':
        cur.execute('SELECT name , number FROM contacts')
        contacts = cur.fetchall()
        if contacts:
            for contact in contacts:
                print(f'Name: {contact[0]} | Number: {contact[1]}')
        else:
            print('No contacts found!')

    #-----Search Contact-----
    elif choose == '3':
        choice = input('Search by Name or Number? (name/number): ').lower().strip()
        if choice == 'name':
            name1 = input('Enter Contact Name: ')
            cur.execute('''
                select name, number from contacts where name = ?
            ''', (name1,))
        elif choice == 'number':
            number1 = input('Enter Contact Number: ')
            cur.execute('''
                select name, number from contacts where number = ?
            ''', (number1,))
        else:
            print('Invalid Search Option!')
            continue

        contacts = cur.fetchall()
        if contacts:
            for c in contacts:
                print(f'Name: {c[0]} | Number: {c[1]}')
        else:
            print('Contact Not Found!')

    #-----Delete Contact-----
    elif choose == '4':
        choice = input('Search by Name or Number? (name/number): ').lower().strip()
        if choice == 'name':
            name1 = input('Enter Contact Name: ')
            cur.execute('''
                delete from contacts where name = ?
            ''', (name1,))
        elif choice == 'number':
            number1 = input('Enter Contact Number: ')
            cur.execute('''
                delete from contacts where number = ?
            ''', (number1,))
        else:
            print('Invalid Search Option!')
            continue

        conn.commit()
        if cur.rowcount > 0:
            print('Contact Deleted!')
        else:
            print('Contact Not Found!')

    #-----Edit Contact-----
    elif choose == '5':
        name1 = input('Enter Contact Name: ')
        number1 = input('Enter New Number: ')
        cur.execute('''
            update contacts set number = ? where name = ?
        ''', (number1, name1))
        conn.commit()
        if cur.rowcount > 0:
            print('Contact Updated!')
        else:
            print('Contact Not Found!')

    #-----Exit-----
    elif choose == '6':
        print('Goodbye!')
        break
    else:
        print('Invalid Option!')


conn.close()
