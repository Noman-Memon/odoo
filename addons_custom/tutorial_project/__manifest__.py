# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Tutorial Project',
    'version' : '1.2',
    'summary': 'Tutorial for Learning',
    'sequence': -3,
    'description': """Tutorial""",
    'category': 'For Study',
    'website': 'https://www.odoo.com',
    'depends' : ['base', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/staff_view.xml',
        'views/menu_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
