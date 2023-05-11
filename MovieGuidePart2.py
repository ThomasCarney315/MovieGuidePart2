# Thomas Careny
# CIS261
# Movie Guide Part 2

FILENAME = 'movies.txt'

def create_movies():
    with open(FILENAME,'w') as file:
        file.write('Good Will Hunting\n')
        file.write('O Brother, Where Art Thou?\n')
        file.write('Pulp Fiction\n')
        file.close()

def show_commands():
    print('The Movie List program\n')
    print('COMMAND MENU')
    print('list - List all movies')
    print('add  - Add a movie')
    print('del  - Delete a movie')
    print('exit - Exit program')

def read_to_list():
    movies = []
    with open(FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            movies.append(line)
    return movies

def write_movies(movies):
    with open(FILENAME, 'w') as file:
        for movie in movies:
            file.write(f'{movie}\n')

def list(l):
    for pos, item in enumerate(l,1):
        print(f'{pos}. {item}')

def add(l, li):
    l.append(li)
    write_movies(l)
    print(f'{li} was added.')

def delete(l, index):
    print(f'{l[index]} was delted.')
    l.pop(index)
    write_movies(l)

def main():
    create_movies()
    show_commands()
    movies = read_to_list()
    command = ''
    while command != 'exit':
        command = input('\nCommand:  ').lower()
        if command == 'list':
            list(movies)
        elif command == 'add':
            title = input('Name/Title:  ')
            if len(title) > 0:
                add(movies, title)
            else:
                print('No input recieved.')
        elif command == 'del':
            index = int(input('Number:  ')) - 1
            if index in range(len(movies)):
                delete(movies, index)
            else:
                print('Invalid movie number.')
        elif command == 'exit':
            print('Goodbye!')
        else:
            print('Not a valid command.  Please try agian.')

if __name__ == "__main__":
    main()
