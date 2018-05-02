import grpc

import todo_pb2
import todo_pb2_grpc


def status_name(status_code):
    return todo_pb2.TodoResponse.Status.Name(status_code)

def print_response(response):
    print('Status: %s --> Messaage: %s' % (status_name(response.status_code), response.message))
    if(response.todo is not None and response.status_code == 1):
        print('Details:\n%s' % (response.todo))

def addToDo(stub):
    print('-----Add Todo-----')
    todo_desc = raw_input('Todo desc: ')
    response = stub.AddTodo(todo_pb2.Todo(todo=todo_desc, status=1))
    print_response(response)

def listToDo(stub):
    print('-----List Todo-----')
    response = stub.ListTodos(todo_pb2.ListRequest(count=3))
    for todo in response.data:
        print(todo)

def updateToDoDesc(stub):
    print('-----Update Todo-----')
    id = int(raw_input('Todo ID: '))
    todo_desc = raw_input('Todo desc: ')
    response = stub.UpdateTodo(todo_pb2.Todo(id=id, todo=todo_desc))
    print_response(response)

def updateToDoStatus(stub):
    print('-----Update Todo Status-----')
    id = int(raw_input('Todo ID: '))
    todo_status = -1
    while 0 > todo_status or todo_status > 3:
        print('----- Todo Statuses -----')
        print('0 --> INITIAL,    1 --> DRAFT,  2 --> IN_PROGRESS, 3 --> COMPLETED')
        todo_status = int(raw_input('Select a Todo Status: '))
        if(0 > todo_status or todo_status > 3):
            print " Error: Invalid Status."
    response = stub.UpdateTodo(todo_pb2.Todo(id=id, status=todo_status))
    print_response(response)


def deleteToDo(stub):
    print('-----Delete Todo-----')
    id = int(raw_input('Todo ID: '))
    response = stub.DeleteTodo(todo_pb2.Todo(id=id))
    print_response(response)
    # print('Status: %s\nMessaage: %s' % (status_name(response.status_name), response.message))


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = todo_pb2_grpc.TodosStub(channel)
    print('-----> Welcome To ToDo Aplication <-----')

    while True:
        print('----------> Select an Option: <------------')
        print('1 ---> Add a Todo')
        print('2 ---> List all Todo')
        print('3 ---> Update a Todo Description')
        print('4 ---> Update a Todo Status')
        print('5 ---> Delete a Todo')
        print('6 ---> Exit ToDo')
        print('------------------------------------------')

        option = int(raw_input('Your Option: '))
        if(option==1):
            addToDo(stub)

        elif(option==2):
            listToDo(stub)

        elif(option==3):
            updateToDoDesc(stub)

        elif (option == 4):
            updateToDoStatus(stub)

        elif(option==5):
            deleteToDo(stub)
        else:
            print('Bye. Exit.')
            break


if __name__ == '__main__':
    run()

