# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Tutorial Project',
    'version': '1.2',
    'summary': 'Tutorial for Learning',
    'sequence': -3,
    'description': """Tutorial""",
    'category': 'For Study',
    'website': 'https://www.odoo.com',
    'depends': ['base', 'product', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'wizard/staff_wizard_view.xml',
        'views/staff_view.xml',
        'views/department_view.xml',
        'views/menu_view.xml',
        'reports/staff_report.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
