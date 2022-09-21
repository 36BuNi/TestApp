from marshmallow import Schema, fields

parameter_marshaller = {
    "flag": fields.String,
    "value": fields.String
}


class EmployeeSchema(Schema):
    """
    Схема сотрудника, которая определяет поля, их типы.
    """
    id = fields.Str(dump_only=True)
    full_name = fields.Str()
    position_held = fields.Str()


class TaskSchema(Schema):
    """
    Схема задач, которая определяет поля, их типы
    """
    id = fields.Str(dump_only=True)
    full_surname = fields.Str()
    position_held = fields.Str()
    parent_task = fields.Nested(lambda: TaskSchema(only=("id",)))
    executor = fields.Nested(EmployeeSchema)
    deadline = fields.DateTime()
    status = fields.Bool()


class EmployeesTaskSchema(EmployeeSchema):
    """
    Схема занятых сотрудников и задач.
    """
    tasks = fields.List(fields.Nested(lambda: TaskSchema()))

