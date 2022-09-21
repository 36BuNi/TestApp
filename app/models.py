from app import db


# Создаем массив пользователей.
class Employee_table(db.Model):
    __tablename__ = 'employee_table'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(), nullable=False)
    position_held = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"Employee_table {self.id} - {self.full_name}"


# Создаем массив задач пользователей .
class Task_table(db.Model):
    __tablename__ = 'task_table'

    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    parent_task_id = db.Column(db.Integer, db.ForeignKey('task_table.id'), nullable=False)
    parent_task = db.relationship('Task_table', remote_side=id, backref='')
    executor_id = db.Column(db.Integer, db.ForeignKey('employee_table.id'), nullable=False)
    executor = db.relationship('Employee_table', backref=db.backref('tasks_table', lazy=True))
    deadline = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Boolean(), default=False, nullable=False)

    def __repr__(self):
        return f"Task_table {self.task_name}"
