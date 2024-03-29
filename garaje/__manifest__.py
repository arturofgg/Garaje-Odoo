# -*- coding: utf-8 -*-
{
    'name': "Gestion de garaje",

    'summary': """
        Gestión de colecciones de coches en aparcamientos""",

    'description': """
        Este es un modulo de pruebas que trata de como construir un modulo en odoo
    """,

    'author': "Arturo",
    'website': "https://solitarios-online.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/garaje_aparcamiento_report.xml',
        'data/garaje_data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],


    'application':True
}

