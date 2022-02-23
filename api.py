from database_design import *


# route to get all movies
@app.route('/Customer', methods=['GET'])
def get_customers():
    return jsonify({'Customers': Customer.get_all_movies()})

@app.route('/Customer/<int:id>', methods=['GET'])
def get_customer_by_id(id):
    return_value = Customer.get_movie(id)
    return jsonify(return_value)


@app.route('/Customer', methods=['POST'])
def add_customer():
    request_data = request.get_json()  # getting data from client
    Customer.add_movie(request_data["name"], request_data["phone_no"])
    response = Response("Customer added", 201, mimetype='application/json')
    return response


@app.route('/Customer/<int:id>', methods=['PUT'])
def update_Customer(id):
    request_data = request.get_json()
    Customer.update_movie(id, request_data['name'], request_data['phone_no'])
    response = Response("Customer Updated", status=200, mimetype='application/json')
    return response

@app.route('/Customer/<int:id>', methods=['DELETE'])
def remove_movie(id):
    Customer.delete_movie(id)
    response = Response("Customer Deleted", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(port=1234, debug=True)
