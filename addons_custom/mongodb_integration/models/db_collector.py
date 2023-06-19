# import pymongo
from pymongo import MongoClient
from odoo import models, fields, api

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['mydb']
collection = db['pos_orders']


class CustomPosOrder(models.Model):
    _name = 'custom.pos.order'

    name = fields.Char(string='Order Name')
    # Add more fields as per your requirements


class CustomPosLine(models.Model):
    _name = 'custom.pos.line'

    product_id = fields.Many2one('product.product', string='Product')
    quantity = fields.Float(string='Quantity')
    price = fields.Float(string='Price')
    order_id = fields.Many2one('custom.pos.order', string='Order')


class PosOrder(models.Model):
    _inherit = 'pos.order'

    def create():
        # import psycopg2


        # # PostgreSQL configuration
        # postgres_host = 'localhost'
        # postgres_port = 5432
        # postgres_db = 'database_15'
        # postgres_user = 'postgres'
        # postgres_password = 'admin'

        # # MongoDB configuration
        # mongo_host = 'localhost'
        # mongo_port = 27017
        # mongo_db = 'mydb'
        # mongo_collection = 'pos_orders'

        # Connect to PostgreSQL
        # postgres_conn = psycopg2.connect(
        #     host=postgres_host,
        #     port=postgres_port,
        #     database=postgres_db,
        #     user=postgres_user,
        #     password=postgres_password
        # )
        # postgres_cursor = postgres_conn.cursor()

        # Connect to MongoDB
        # mongo_client = MongoClient(mongo_host, mongo_port)
        # mongo_db = mongo_client[mongo_db]
        # mongo_collection = mongo_db[mongo_collection]

        # Retrieve data from PostgreSQL
        postgres_cursor.execute('SELECT * FROM "pos_order"')
        orders = postgres_cursor.fetchall()

        postgres_cursor.execute('SELECT * FROM "pos_order_line"')
        order_lines = postgres_cursor.fetchall()

        # Retrieve existing order IDs from MongoDB collection
        existing_order_ids = set(mongo_collection.distinct('id'))

        # Transform and insert data into MongoDB
        for order in orders:
            order_id = order[0]

            # Skip insertion if order is already in MongoDB
            if order_id in existing_order_ids:
                continue

            order_data = {
                'id': order_id,
                'customer_id': order[1],
                'order_lines': []
            }
            for order_line in order_lines:
                print(order_line[0])
                if order_line[0] == order_id or order_line[12] == order_id:
                    order_line_data = {
                        'id': order_line[0],
                        'product_id': order_line[2],
                        # Add more fields as necessary
                    }
                    order_data['order_lines'].append(order_line_data)

            mongo_collection.insert_one(order_data)

        # Close connections
        # postgres_cursor.close()
        # postgres_conn.close()
        mongo_client.close()
        # Retrieve only updated POS orders and collect data
        # updated_orders = [vals for vals in vals_list if vals.get(['update_existing'])]
        # for order in updated_orders:
            # Extract the necessary data from the order
            # order_data = {
            #     'name': order['name'],
            #     # Add more fields as per your requirements
            # }

            # Create a new record in the custom model
        #     custom_order = self.env['custom.pos.order'].create(order_data)
        #
        #     # Process POS order lines
        #     for order_line in order['lines']:
        #         # Extract the data from the POS order line
        #         line_data = {
        #             'product_id': order_line[2]['product_id'],
        #             'quantity': order_line[2]['qty'],
        #             'price': order_line[2]['price_unit'],
        #             'order_id': custom_order.id,
        #         }
        #
        #         # Create a new record in the custom line model
        #         custom_line = self.env['custom.pos.line'].create(line_data)
        #
        #         # Send data to MongoDB
        #         collection.insert_one(line_data)
        #
        # # Proceed with the regular creation of POS orders
        # return super(PosOrder, self).create(vals_list)

