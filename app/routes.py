from flask import request, jsonify
from flask_apispec import FlaskApiSpec, doc, marshal_with

from app import app, db, schemas
from app.models import EmployeeTable, TaskTable

# Начало создания документации.
docs = FlaskApiSpec(app)


# CRUD
@app.route('/employees', methods=['GET'])
@marshal_with(schemas.EmployeeSchema(many=True), 200, description='Получение массива всех сотрудников ')
@doc(description='Получение массива всех сотрудников', tags=['Employees'])
def get_manage_employee():
    """
    Получение массива всех сотрудников.
    :return:
    """
    employees = EmployeeTable.query.all()
    results = [
        {
            "full_name": employee.full_name,
            "position": employee.position_held,
        } for employee in employees]
    return jsonify({"count": len(results), "employees": results})


@app.route('/employees', methods=['POST'])
@marshal_with(schemas.EmployeeSchema(many=True), 200, description='Создание нового сотрудника ')
@doc(description='Создание нового сотрудника', tags=['Employees'])
def post_manage_employee():
    """
    Создание нового сотрудника.
    :return:
    """
    data = request.get_json()
    new_employee = EmployeeTable(full_name=data['full_name'], position=data['position'])
    db.session.add(new_employee)
    db.session.commit()
    return {
        "message": f"employee {new_employee.full_name} "
                   f"Массив успешно создан."}


@app.route('/employee/<int:id>/', methods=['GET'])
@marshal_with(schemas.EmployeeSchema(many=True), 200, description='Получение данных сотрудника')
@doc(description='Получить данные сотрудника', tags=['Employees'])
def get_employee(id):
    """
    Получение данных сотрудника
    :param id: id сотрудника.
    :return:
    """
    employee = EmployeeTable.query.filter_by(id=id).first()
    results = {"full_name": employee.full_name,
               "position": employee.position_held}
    return jsonify(results)


@app.route('/employee/<int:id>/', methods=['PUT'])
@marshal_with(schemas.EmployeeSchema(many=True), 200, description='Обновление данных одного сотрудника')
@doc(description='Обновление данных одного сотрудника', tags=['Employees'])
def put_employee(id):
    """
    Обновление данных одного сотрудника.
    :param id:
    :return:
    """
    data = request.get_json()
    employee = EmployeeTable.query.filter_by(id=id).first()
    employee.full_name = data['name']
    employee.position_held = data['model']
    db.session.add(employee)
    db.session.commit()
    return jsonify({"message": f"Employee {employee.full_name} "
                               f"Успешно обновлено."})


@app.route('/employee/<int:id>/', methods=['DELETE'])
@marshal_with(schemas.EmployeeSchema(many=True), 200, description='Удаление работника')
@doc(description='Удаление работника', tags=['Employees'])
def delete_employee(id):
    """
    Удаление работника.
    :param id:
    :return:
    """
    employee = EmployeeTable.query.filter_by(id=id).first()
    db.session.delete(employee)
    db.session.commit()
    return {"message": f"Employee {employee.full_name} "
                       f"Успешно удалено."}


delete_employee.provide_automatic_options = False
delete_employee.methods = ['DELETE']

app.add_url_rule('/', delete_employee)


@app.route('/tasks', methods=['POST'])
@marshal_with(schemas.TaskSchema(many=True), 200, description='Создание новой задачи')
@doc(description='Создание новой задачи', tags=['Task'])
def post_tasks():
    """
    Создание новой задачи.
    :return:
    """
    data = request.get_json()
    new_task = TaskTable(title=data['title'],
                         parent_task_id=data['parent_task_id'],
                         employee_id=data['employee_id'],
                         deadline=data['deadline'],
                         status=data['status'])
    db.session.add(new_task)
    db.session.commit()
    return {"message": f"Task {new_task.title} "
                       f"Успешно создано."}


@app.route('/tasks', methods=['GET'])
@marshal_with(schemas.TaskSchema(many=True), 200, description='Получение списка всех задач')
@doc(description='Получение списка всех задач', tags=['Task'])
def get_tasks():
    """
    Получение списка всех задач.
    :return:
    """
    tasks = TaskTable.query.all()
    results = [
        {
            "id": task.id,
            "title": task.task_name,
            "parent_task_id": task.parent_task_id,
            "employee_id": task.employee_id,
            "deadline": task.deadline,
            "status": task.status
        } for task in tasks]
    return jsonify({"count": len(results), "tasks": results})


@app.route('/task/<int:id>/', methods=['GET'])
@marshal_with(schemas.TaskSchema(many=True), 200, description='Получить данные задачи')
@doc(description='Данные задачи', tags=['Task'])
def get_task(id):
    """
    Получение данных одной задачи
    :param id:
    :return:
    """
    task = TaskTable.query.filter_by(id=id).first()
    results = {"id": task.id,
               "title": task.title,
               "parent_task_id": task.parent_task_id,
               "employee_id": task.employee_id,
               "deadline": task.deadline,
               "status": task.status}
    return jsonify(results)


@app.route('/task/<int:id>/', methods=['PUT'])
@marshal_with(schemas.TaskSchema(many=True), 200, description='Изменение данных задачи')
@doc(description='Изменение данных задачи', tags=['Task'])
def put_task(id):
    """
    Изменение данных задачи.
    :param id:
    :return:
    """
    task = TaskTable.query.filter_by(id=id).first()
    data = request.get_json()
    task.title = data['title']
    task.parent_task_id = data['parent_task_id']
    task.employee_id = data['employee_id']
    task.deadline = data['deadline']
    task.status = data['status']
    db.session.add(task)
    db.session.commit()
    return jsonify({"message": f"Task {task.title} "
                               f"Успешно изменено."})


@app.route('/task/<int:id>/', methods=['DELETE'])
@marshal_with(schemas.TaskSchema(many=True), 200, description='Удаление задачи')
@doc(description='Удаление задачи', tags=['Task'])
def delete_task(id):
    """
    Удаление задачи.
    :param id:
    :return:
    """
    task = TaskTable.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return {"message": f"Employee {task.title} "
                       f"Успешно удалено."}


@app.route('/busy-employees', methods=['GET'])
@marshal_with(schemas.EmployeesTaskSchema(many=True), 200, description='Получение массива сотрудников и задач')
@doc(description='Список занятых сотрудников и задач', tags=['Busy'])
def get_busy_employees():
    """
    Получение массива сотрудников и задач.
    :return:
    """
    employees = EmployeeTable.query.outerjoin(TaskTable). \
        group_by(EmployeeTable.id).filter(EmployeeTable.tasks). \
        order_by(db.func.count().filter(TaskTable.status).desc())
    results = [
        {
            "id": employee.id,
            "full_name": employee.full_name,
            "position_held": employee.position_held,
            "tasks": [
                {
                    "id": task.id,
                    "task_name": task.task_name,
                    "parent_task_id": task.parent_task_id,
                    "executor_id": task.employee_id,
                    "deadline": task.deadline,
                    "status": task.status
                }
                for task in employee.tasks],
        } for employee in employees]
    return jsonify({"count": len(results), "employees": results})


@app.route('/important-task', methods=['GET'])
@marshal_with(schemas.EmployeesTaskSchema(many=True), 200,
              description='Получить список важных задач и сотрудников которые могу взять эти задачи')
@doc(description='Список важных задач и сотрудников которые могу взять эти задачи', tags=['Important_task'])
def get_important_task():
    """
    Получить список важных задач и сотрудников которые могу взять эти задачи.
    :return:
    """

    tasks = TaskTable.query.filter(TaskTable.employee_id == None,
                                   TaskTable.parent_task != None).all()
    employees = EmployeeTable.query.all()
    minimal_tasks_count = min(
        [(len(employee.tasks)) for employee in employees])
    least_busy_employees = [
        employee.full_name for employee in employees if
        (len(employee.tasks)) == minimal_tasks_count]
    result = []
    for task in tasks:
        task_list = {
            'title': task.title,
            'deadline': task.deadline,
            'employee': []
        }
        result.append(task_list)
        for employee in employees:
            employee_less_busy = len(employee.tasks) < (
                    minimal_tasks_count + 2)
            for sub_task in employee.tasks:
                employee_busy_on_parent = sub_task.id == task.parent_task_id
                if employee_less_busy and employee_busy_on_parent:
                    list_emp = employee.full_name
                    task_list['employee'].append(list_emp)
        task_list['employee'].extend(least_busy_employees)
    return jsonify(result)


# Окончание создания документации.
docs.register_existing_resources()
