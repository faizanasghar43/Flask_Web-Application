from settings import *
import json

db = SQLAlchemy(app)


class Employee(db.Model):
    __Tablename__ = 'Employee'
    Emp_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Emp_name = db.Column(db.String(30), nullable=False)
    phone_no = db.Column(db.String(15), nullable=False)
    salary = db.Column(db.Integer)


    def json(self):
        return {'Emp_id': self.Emp_id,
                'Emp_name': self.Emp_name,
                'phone_no': self.phone_no,
                'Salary': self.salary
                }


def add_employee(_emp_id, _emp_name, _phone_no, _salary):
    new_employee = Employee(Emp_id=_emp_id, Emp_name=_emp_name, phone_no=_phone_no, salary=_salary)
    db.session.add(new_employee)
    db.session.commit()


def get_employee(_id):
    return [Employee.json(Employee.query.filter_by(Emp_id=_id).first())]


def get_all_employees():
    return [Employee.json(Employee) for employee in Employee.query.all()]


def update_employee(_emp_id, _emp_name, _phone_no, _salary):
    emp_to_update = Employee.query.filter_by(id=_emp_id).first()
    emp_to_update.name = _emp_name
    emp_to_update.phone_no = _phone_no
    emp_to_update.salary = _salary
    db.session.commit()


class Customer(db.Model):
    __Tablename__ = 'Customer'
    cus_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    phone_no = db.Column(db.String(15), nullable=False)
    Type = db.Column(db.String(15), nullable=True)
    Collars = db.Column(db.String(15), nullable=True)
    Side_cuts = db.Column(db.String(15), nullable=True)
    Plates = db.Column(db.String(15), nullable=True)
    Length = db.Column(db.String(15), nullable=True)
    Shoulder = db.Column(db.String(15), nullable=True)
    Neck = db.Column(db.String(15), nullable=True)
    Chest = db.Column(db.String(15), nullable=True)
    Waist = db.Column(db.String(15), nullable=True)
    Crosses = db.Column(db.String(15), nullable=True)
    Pant_Length = db.Column(db.String(15), nullable=True)
    Pant_Waist = db.Column(db.String(15), nullable=True)
    Knee = db.Column(db.String(15), nullable=True)
    Rises = db.Column(db.String(15), nullable=True)

    def json(self):
        return {'cus_id': self.cus_id,
                'name': self.name,
                'phone_no': self.phone_no,
                'Type': self.Type,
                'Collars': self.Collars,
                'Side_cuts': self.Side_cuts,
                'Plates': self.Plates,
                'Length': self.Length,
                'Shoulder': self.Shoulder,
                'Neck': self.Neck,
                'Chest': self.Chest,
                'Waist': self.Waist,
                'Crosses': self.Crosses,
                'Pant_Length': self.Pant_Length,
                'Pant_Waist': self.Pant_Waist,
                'Knee': self.Knee,
                'Rise': self.Rises,
                }


def add_customer(_name, _phone_no, _cus_id,  _type, _collars, _side_cuts, _plates, _length, _shoulder, _neck, _chest, _waist, _crosses,
             _pant_length, _pant_waist, _knee, _rises):
    new_customer = Customer(name=_name, phone_no=_phone_no, cus_id=_cus_id, Type=_type, Collars=_collars, Side_cuts=_side_cuts, Plates=_plates,
                             Length=_length, Shoulder=_shoulder, Neck=_neck, Chest=_chest, Waist=_waist,
                             Crosses=_crosses, Pant_Length=_pant_length, Pant_Waist=_pant_waist,
                             Knee=_knee, Rises=_rises, )
    db.session.add(new_customer)
    db.session.commit()


def get_customer(_id):
    return [Customer.json(Customer.query.filter_by(cus_id=_id).first())]


def get_all_customers():
    return [Customer.json(customer) for customer in Customer.query.all()]


def update_customer(_name, _phone_no, _cus_id,  _type, _collars, _side_cuts, _plates, _length, _shoulder, _neck, _chest, _waist, _crosses,
                _pant_length, _pant_waist,  _knee, _rises):
    cus_to_update = Customer.query.filter_by(cus_id=_cus_id).first()
    cus_to_update.name = _name
    cus_to_update.phone_no = _phone_no
    cus_to_update.Type = _type
    cus_to_update.Collars = _collars
    cus_to_update.Side_cuts = _side_cuts
    cus_to_update.Shoulder = _shoulder
    cus_to_update.Neck = _neck
    cus_to_update.Chest = _chest
    cus_to_update.Waist = _waist
    cus_to_update.Crosses = _crosses
    cus_to_update.Pant_Length = _pant_length
    cus_to_update.Pant_Waist = _pant_waist
    cus_to_update.Knee = _knee
    cus_to_update.Rises = _rises
    db.session.commit()


def delete_customer(_id):
    Customer.query.filter_by(cus_id=_id).delete()
    db.session.commit()









class Order(db.Model):
    __Tablename__ = 'Order'
    cus_id = db.Column(db.Integer, db.ForeignKey(Customer.cus_id), nullable=False)
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    emp_id = db.Column(db.Integer)
    delivery_date = db.Column(db.String(15))
    booking_date = db.Column(db.String(15))
    advanced = db.Column(db.Integer)
    payment = db.Column(db.Integer)

    def json(self):
        return {'cus_id': self.cus_id,
                'order_id': self.order_id,
                'emp_id': self.emp_id,
                'delivery_date': self.delivery_date,
                'booking_date': self.booking_date,
                'advanced': self.advanced,
                'payment': self.payment}


def add_order(_cus_id, _order_id, _employee_id, _delivery_date, _booking_date, _advanced, _payment):
    new_order = Order(cus_id=_cus_id, order_id=_order_id, emp_id=_employee_id,
                      delivery_date=_delivery_date,
                      booking_date=_booking_date, advanced=_advanced, payment=_payment)
    db.session.add(new_order)
    db.session.commit()


def get_order(_id):
    return [Order.json(Order.query.filter_by(id=_id).first())]


def get_all_orders():
    return [Order.json(order) for order in Order.query.all()]


def update_order(_cus_id, _order_id, _employee_id, _delivery_date, _booking_date, _advanced, _payment):
    order_to_update = Order.query.filter_by(order_id=_order_id).first()
    order_to_update.cus_id = _cus_id
    order_to_update.order_id = _order_id
    order_to_update.emp_id = _employee_id
    order_to_update.delivery_date = _delivery_date
    order_to_update.booking_date = _booking_date
    order_to_update.advanced = _advanced
    order_to_update.payment = _payment
    db.session.commit()


def delete_order(_id):
    Order.query.filter_by(order_id=_id).delete()
    db.session.commit()


db.create_all()
