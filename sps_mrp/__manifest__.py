# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'MRP Base',
    'category': 'Production',
    'summary': 'MRP Base',
    'description': "",
    "author": "Yustaf Pramsistya",
    'version': '1.0',
    'depends': ['stock','mrp','mrp_account'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/mrp_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
