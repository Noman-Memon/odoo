import pymongo
from odoo import models, fields, api



class PosOrder(models.Model):
    _name = 'data.collection'

    def collectData(self):
        # Connect to MongoDB
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client['mydb']
        collection = db['pos_orders']
        
        orders = self.env['pos.order'].search([])

        # Retrieve existing order IDs from MongoDB collection
        existing_order_ids = set(collection.distinct('id'))

        # Transform and insert data into MongoDB
        for order in orders:
            _id = order.id

            # Skip insertion if order is already in MongoDB
            if _id in existing_order_ids:
                continue

            order_data = {
                'id': _id,
                'customer_id': order.name,
                'date_order': order.date_order,
                'amount_tax': order.amount_tax,
                'amount_total': order.amount_total,
                'amount_return': order.amount_return,
                'state': order.state,
                'order_lines': []
            }
            order_lines = self.env['pos.order.line'].search([('order_id', '=', _id)])
            print(order_lines)
            for order_line in order_lines:
                order_line_data = {
                    'id': order_line.id,
                    'full_product_name': order_line.full_product_name,
                    'price_unit': order_line.price_unit,
                    'qty': order_line.qty,
                    'price_subtotal': order_line.price_subtotal,
                    'price_subtotal_incl': order_line.price_subtotal_incl,
                    'total_cost': order_line.total_cost,
                }
                order_data['order_lines'].append(order_line_data)

            collection.insert_one(order_data)

        client.close()
