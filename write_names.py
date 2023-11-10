def main():
    print('Введите имя трех друзей.')
    name1 = input('Друг № 1: ')
    name2 = input('Друг № 2: ')
    name3 = input('Друг № 3: ')

    myfile = open('friends.txt', 'w')

    myfile.write(name1 + '\n')
    myfile.write(name2 + '\n')
    myfile.write(name3 + '\n')

    myfile.close()
    print('Имена были записаны в friends.txt.')

if __name__ == '__main__':
    main()