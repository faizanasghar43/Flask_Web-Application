from flask import Flask, render_template, request, flash, redirect


from database_design import *
from database_design import get_all_customers
from database_design import delete_order




@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form.get('submit1') == 'SUBMIT':
            email = request.form.get("Login")
            pass_ = request.form.get("password")
            print(email, pass_)
            if pass_ == "LQdapsl" and email == "ayz@pvt.ltd.com":
                print("it worked")
                return render_template("index.html")
            else:
                return render_template("Visit_Home.html")
    elif request.method == 'GET':
        return render_template('Login.html')


@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/')
def Visit_Home():
    return render_template('Visit_Home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



@app.route('/Visit_contact')
def Visit_contact():
    return render_template('Visit_Contact.html')




@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/Visit_about')
def Visit_about():
    return render_template('Visit_About.html')


@app.route('/product')
def product():
    return render_template('products.html')


@app.route('/Visit_product')
def Visit_product():
    return render_template('Visit_Products.html')


@app.route('/customer_form')
def customer_form():
    return render_template('Customer.html')


@app.route('/Order_list')
def order_list():
    return render_template('Order_List_Entry.html')


@app.route("/form2", methods=['GET', 'POST'])
def order_form_entry():
    if request.method == 'POST':
        if request.form.get('submit1') == 'SUBMIT':
            name = request.form.get('name')
            phone_number = request.form.get('phone')
            cus_id = request.form.get('id')
            _type = request.form.get('Type_sel')
            collars = request.form.get('Collars')
            plates = request.form.get('Plates')
            _len = request.form.get('len_id')
            side_cuts = request.form.get('cuts')
            shoulder = request.form.get('sh_id')
            neck = request.form.get('neck_id')
            chest = request.form.get('chest_id')
            waist = request.form.get('waist_id')
            cross = request.form.get('cross_id')
            pant_length = request.form.get('pant_len_id')
            pant_waist = request.form.get('pant_waist_id')
            knee = request.form.get('knee_id')
            rise = request.form.get('rises_id')
            order_id = request.form.get('order_id')
            employee = request.form.get('empid')
            deli_date = request.form.get('delivery')
            booking_dat = request.form.get('booking')
            advanced_ = request.form.get('adv')
            payment_ = request.form.get('pay')


            if cus_id == "":
                return redirect("/Order_List_Entry.html")
            else:
                add_customer(name, phone_number, cus_id, _type, collars, side_cuts, plates, _len, shoulder, neck, chest,
                             waist, cross,
                             pant_length, pant_waist, knee, rise)
                add_order(cus_id, order_id, employee, deli_date, booking_dat, advanced_, payment_)
                return render_template("index.html")
        else:
            pass  # unknown
    elif request.method == 'GET':
        return render_template('index.html')


@app.route("/Table", methods=['GET', 'POST'])
def show_customer_entries():
    result = get_all_customers()
    return render_template('Table.html', books=result)


@app.route("/Show_orders", methods=['GET', 'POST', 'DELETE'])
def show_order_entries():
    result = get_all_orders()
    return render_template('Order_show.html', books=result)



if __name__ == '__main__':
    app.run(host='localhost', port=5000)
