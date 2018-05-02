from concurrent import futures
import time
import grpc
import todo_pb2
import todo_pb2_grpc

_ONE_DAY_IN_SECONDS = 30

TODO = []

def get_todo(id):
    for todo in TODO:
        if todo.id == id:
            return todo
    return None

class Todo(todo_pb2_grpc.TodosServicer):
    count = 0
    def AddTodo(self, request, context):
        print('-----Add Todo server side-----')
        if request.todo == '':
            response=todo_pb2.TodoResponse(todo=request)
            response.status_code= 2
            response.message= 'Required fields missing'
        else:
            self.count = self.count+1
            request.id = self.count
            TODO.append(request)
            response=todo_pb2.TodoResponse(todo=get_todo(self.count))
            response.status_code= 1
            response.message='New Todo created!'
            print('-----new Todo Added-----')
        return response

    def ListTodos(self, request, context):
        return todo_pb2.ListResponse(data=TODO)

    def UpdateTodo(self, request, context):
        response=todo_pb2.TodoResponse(todo=request)
        todo = get_todo(request.id)
        print('UpdateTodo: '+ str(request.id))
        if todo is None:
            response.message='Error: No Todo with id %s exists' % request.id
            response.status_code=2
        elif request.todo == '' and request.status == 0:
            response.message='Error: Required fields missing'
            response.status_code=2
        else:
            todo_old = todo.todo
            index = TODO.index(todo)
            if request.todo != '':
                TODO[index].todo = request.todo
            if request.status != None and request.status != 0:
                TODO[index].status = request.status
            response.status_code = 1
            response=todo_pb2.TodoResponse(todo=TODO[index], status_code=1, message='Todo "%s" is updated to ' % (todo_old))
        return response

    def DeleteTodo(self, request, context):
        todo = get_todo(request.id)
        print('DeleteTodo: '+ str(request.id))
        if todo is None:
            return todo_pb2.TodoResponse(status_code=2, message='No Todo with id %s exists' % request.id)
        else:
            index = TODO.index(todo)
            del TODO[index]
            return todo_pb2.TodoResponse(status_code=1, message='Todo removed!')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodosServicer_to_server(Todo(), server)
    server.add_insecure_port('localhost:50051')
    print ' Server started at localhost:50051 ...'
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
            print ' Server is not sleeping... It\'s day dreaming..'
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
