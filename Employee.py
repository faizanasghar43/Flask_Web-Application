from settings import *
import json
from OrderList import *
db = SQLAlchemy(app)


class Employee(db.Model):
    __Tablename__ = 'Employees'
    Emp_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Emp_name = db.Column(db.String(30), nullable=False)
    phone_no = db.Column(db.String(15), nullable=False)

    def json(self):
        return {'Emp_id': self.Emp_id,
                'Emp_name': self.Emp_name,
                'phone_no': self.phone_no}


def add_employee(_emp_id, _emp_name, _phone_no):
    new_employee = Employee(Emp_id=_emp_id, Emp_name=_emp_name, phone_no=_phone_no)
    db.session.add(new_employee)
    db.session.commit()


def get_employee(_id):
    return [Employee.json(Employee.query.filter_by(Emp_id=_id).first())]


def get_all_employees():
    return [Employee.json(Employee) for employee in Employee.query.all()]


def update_employee(_emp_id, _emp_name, _phone_no):
    emp_to_update = Employee.query.filter_by(id=_emp_id).first()
    emp_to_update.name = _emp_name
    emp_to_update.phone_no = _phone_no
    db.session.commit()


def delete_employee(_emp_id):
    Employee.query.filter_by(id=_emp_id).delete()
    db.session.commit()
