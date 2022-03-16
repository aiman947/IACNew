# -*- coding: utf-8 -*-
{
    'name': "CMS Notifications",

    'version': '13.0.1.0.1',
    'summary': """Academic Module for UMS""",
    'description': 'Academic Module of Educational Institutes (University Level)',
    'category': 'OdooCMS',
    'sequence': 34,
    'author': "GlobalXS",
    'company': 'GlobalXS Technology Solutions',
    'website': "https://www.globalxs.co",

    # any module necessary for this one to work correctly
    'depends': ['base','odoocms'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/odoocms_notification_security.xml',
        'views/views.xml',
        'views/menu_cms_notifications.xml',
        'wizard/create_notifications.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
