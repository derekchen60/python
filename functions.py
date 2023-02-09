def get_todos():
    with open('todo.txt', 'r') as myfile:
        return myfile.readlines()

def write_todos(todos):
    with open('todo.txt', 'w') as myfile:
        myfile.writelines(todos)

if __name__ == '__main__':
    print(get_todos())

print(get_todos())