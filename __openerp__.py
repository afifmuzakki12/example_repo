# -*- coding: utf-8 -*-
{
    'name': "dym_telemarketing",

    'summary': """
        Module Telemarketing""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Muhammad Afif Muzakki",
    'website': "http://www.daya-motor.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}