# from sql_connecton import get_sql_connection
#
#
# def get_all_products(connection):
#     cursor = connection.cursor()
#     query = ("SELECT * "
#              "FROM grocerystore.products "
#              "INNER JOIN grocerystore.uom ON products.uom_id = uom.iduom "
#              "LIMIT 10;")
#
#     cursor.execute(query)
#
#     response = []
#
#     for (idproducts, productName, uom_id, Rate, uom_name) in cursor:
#         response.append(
#             {
#                 'productid': idproducts,
#                 'name': productName,
#                 'uomid': uom_id,
#                 'rate': Rate,
#                 'uom_name': uom_name
#
#             }
#
#         )
#
#     return response
#
#
# if __name__ == '__main__':
#     connection = get_sql_connection()
#     print(get_all_products(connection))
from mysql.connector import Error

from sql_connecton import get_sql_connection


def get_all_products(connection):
    cursor = connection.cursor()
    query = ("SELECT products.idproducts, products.productName, products.uom_id, products.Rate, uom.uom_name "
             "FROM grocerystore.products "
             "INNER JOIN grocerystore.uom ON products.uom_id = uom.iduom "
             "LIMIT 10;")

    cursor.execute(query)

    response = []

    for (idproducts, productName, uom_id, Rate, uom_name) in cursor:
        response.append(
            {
                'productid': idproducts,
                'name': productName,
                'uomid': uom_id,
                'rate': Rate,
                'uom_name': uom_name
            }
        )

    cursor.close()
    return response


def select_all_products(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM grocerystore.products;")
        result = cursor.fetchall()
        for row in result:
            print(row)
        cursor.close()
    except Error as e:
        print(f"Error while executing SELECT query: {e}")


def insert_product(connection, idproducts, productName, uom_id, Rate):
    try:
        cursor = connection.cursor()
        insert_query = ("INSERT INTO grocerystore.products (idproducts,productName, uom_id, Rate) "
                        "VALUES (%s,%s, %s, %s);")
        cursor.execute(insert_query, (idproducts, productName, uom_id, Rate))
        connection.commit()
        print("Product inserted successfully")
        cursor.close()
    except Error as e:
        print(f"Error while executing INSERT query: {e}")


def delete_product(connection, idproducts):
    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM products WHERE idproducts = %s"
        cursor.execute(delete_query, (idproducts,))
        connection.commit()
        print(f"Product with id {idproducts} deleted successfully")
        cursor.close()
    except Error as e:
        print(f"Error while executing DELETE query: {e}")


if __name__ == '__main__':
    connection = get_sql_connection()
    if connection:
        print("Initial Products:")
        select_all_products(connection)

        print("\nInserting New Product:")
        product_id = int(input("Enter Product ID: "))
        product_name = input("Enter Product Name: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
        insert_product(connection, product_id, product_name, quantity, price)
        select_all_products(connection)

        # print("\nDeleting Product with ID 11:")
        # delete_product(connection, 11)
        # select_all_products(connection)

        connection.close()
    else:
        print("Failed to connect to the database.")


