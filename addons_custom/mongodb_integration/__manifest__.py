# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'MongoDB_Integration',
    'version' : '1.2',
    'summary': 'Collect pos orders and send to mongodb',
    'sequence': -4,
    'description': """Tutorial""",
    'category': 'data collection',
    'website': 'https://www.odoo.com',
    'depends' : ['base', 'point_of_sale'],
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/staff_view.xml',
    ],
    'demo': [
        # 'demo/account_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
