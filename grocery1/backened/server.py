# from flask import Flask, request, jsonify
# import products_dao
# from sql_connecton import get_sql_connection
#
# app = Flask(__name__)
#
# connection = get_sql_connection()
#
#
# @app.route('/getProducts', methods=['GET'])
# def get_products():
#     products_dao.get_all_products(connection)
#
#     response = jsonify(products)
#     response.headers.add('Access-control-Allow-Origin', '*')
#     return response
#
#
# if __name__ == "__main__":
#     print("starting python flask server grocery store")
#     app.run(port=5000)

from flask import Flask, request, jsonify
import products_dao
from sql_connecton import get_sql_connection

app = Flask(__name__)

connection = get_sql_connection()


@app.route('/getProducts', methods=['GET'])
def get_products():
    try:
        products = products_dao.get_all_products(connection)
        response = jsonify(products)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Route to delete a product
@app.route('/deleteProduct/<int:product_id>', methods=['DELETE'])
def delete_product(idproducts):
    try:
        products_dao.delete_product(connection, idproducts)
        return jsonify({'message': f'Product with id {idproducts} deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run(port=5000, debug=True)
