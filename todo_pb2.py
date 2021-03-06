# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='todo.proto',
  package='todo',
  syntax='proto3',
  serialized_pb=_b('\n\ntodo.proto\x12\x04todo\"\x96\x01\n\x04Todo\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04todo\x18\x02 \x01(\t\x12!\n\x06status\x18\x04 \x01(\x0e\x32\x11.todo.Todo.Status\"Q\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05\x44RAFT\x10\x01\x12\x0b\n\x07INITIAL\x10\x01\x12\x0f\n\x0bIN_PROGRESS\x10\x02\x12\r\n\tCOMPLETED\x10\x03\x1a\x02\x10\x01\"\x98\x01\n\x0cTodoResponse\x12.\n\x0bstatus_code\x18\x01 \x01(\x0e\x32\x19.todo.TodoResponse.Status\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x18\n\x04todo\x18\x03 \x01(\x0b\x32\n.todo.Todo\"-\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\t\n\x05\x45RROR\x10\x02\"\x1c\n\x0bListRequest\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\"(\n\x0cListResponse\x12\x18\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\n.todo.Todo2\xca\x01\n\x05Todos\x12+\n\x07\x41\x64\x64Todo\x12\n.todo.Todo\x1a\x12.todo.TodoResponse\"\x00\x12\x34\n\tListTodos\x12\x11.todo.ListRequest\x1a\x12.todo.ListResponse\"\x00\x12.\n\nDeleteTodo\x12\n.todo.Todo\x1a\x12.todo.TodoResponse\"\x00\x12.\n\nUpdateTodo\x12\n.todo.Todo\x1a\x12.todo.TodoResponse\"\x00\x62\x06proto3')
)



_TODO_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='todo.Todo.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DRAFT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INITIAL', index=2, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IN_PROGRESS', index=3, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETED', index=4, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=_descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\020\001')),
  serialized_start=90,
  serialized_end=171,
)
_sym_db.RegisterEnumDescriptor(_TODO_STATUS)

_TODORESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='todo.TodoResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=281,
  serialized_end=326,
)
_sym_db.RegisterEnumDescriptor(_TODORESPONSE_STATUS)


_TODO = _descriptor.Descriptor(
  name='Todo',
  full_name='todo.Todo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='todo.Todo.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='todo', full_name='todo.Todo.todo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='todo.Todo.status', index=2,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TODO_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=171,
)


_TODORESPONSE = _descriptor.Descriptor(
  name='TodoResponse',
  full_name='todo.TodoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status_code', full_name='todo.TodoResponse.status_code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='todo.TodoResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='todo', full_name='todo.TodoResponse.todo', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TODORESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=174,
  serialized_end=326,
)


_LISTREQUEST = _descriptor.Descriptor(
  name='ListRequest',
  full_name='todo.ListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='todo.ListRequest.count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=328,
  serialized_end=356,
)


_LISTRESPONSE = _descriptor.Descriptor(
  name='ListResponse',
  full_name='todo.ListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='todo.ListResponse.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=358,
  serialized_end=398,
)

_TODO.fields_by_name['status'].enum_type = _TODO_STATUS
_TODO_STATUS.containing_type = _TODO
_TODORESPONSE.fields_by_name['status_code'].enum_type = _TODORESPONSE_STATUS
_TODORESPONSE.fields_by_name['todo'].message_type = _TODO
_TODORESPONSE_STATUS.containing_type = _TODORESPONSE
_LISTRESPONSE.fields_by_name['data'].message_type = _TODO
DESCRIPTOR.message_types_by_name['Todo'] = _TODO
DESCRIPTOR.message_types_by_name['TodoResponse'] = _TODORESPONSE
DESCRIPTOR.message_types_by_name['ListRequest'] = _LISTREQUEST
DESCRIPTOR.message_types_by_name['ListResponse'] = _LISTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Todo = _reflection.GeneratedProtocolMessageType('Todo', (_message.Message,), dict(
  DESCRIPTOR = _TODO,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.Todo)
  ))
_sym_db.RegisterMessage(Todo)

TodoResponse = _reflection.GeneratedProtocolMessageType('TodoResponse', (_message.Message,), dict(
  DESCRIPTOR = _TODORESPONSE,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.TodoResponse)
  ))
_sym_db.RegisterMessage(TodoResponse)

ListRequest = _reflection.GeneratedProtocolMessageType('ListRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTREQUEST,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.ListRequest)
  ))
_sym_db.RegisterMessage(ListRequest)

ListResponse = _reflection.GeneratedProtocolMessageType('ListResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTRESPONSE,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.ListResponse)
  ))
_sym_db.RegisterMessage(ListResponse)


_TODO_STATUS.has_options = True
_TODO_STATUS._options = _descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\020\001'))

_TODOS = _descriptor.ServiceDescriptor(
  name='Todos',
  full_name='todo.Todos',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=401,
  serialized_end=603,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddTodo',
    full_name='todo.Todos.AddTodo',
    index=0,
    containing_service=None,
    input_type=_TODO,
    output_type=_TODORESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListTodos',
    full_name='todo.Todos.ListTodos',
    index=1,
    containing_service=None,
    input_type=_LISTREQUEST,
    output_type=_LISTRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteTodo',
    full_name='todo.Todos.DeleteTodo',
    index=2,
    containing_service=None,
    input_type=_TODO,
    output_type=_TODORESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateTodo',
    full_name='todo.Todos.UpdateTodo',
    index=3,
    containing_service=None,
    input_type=_TODO,
    output_type=_TODORESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TODOS)

DESCRIPTOR.services_by_name['Todos'] = _TODOS

# @@protoc_insertion_point(module_scope)
