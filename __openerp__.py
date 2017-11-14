# -*- coding: utf-8 -*-

{
    'name': 'Lockdown',
    'version': '0.1',
    'category': 'System Modules',
    'sequence': 2,
    'summary': 'Remove database management and API from login screen.',
    'description': """\
Improve the security of the system by:

- removing the Manage Database link from the login page (Guewen Baconnier)
- blocking the API for database management (Andrey Kolpakov)

Original code from https://www.odoo.com/forum/help-1/question/how-to-remove-manage-databases-2615
""",
    'author': 'Van Sebille Systems',
    'depends': [
        'base',
        'auth_crypt',
        'web',
        ],
    'data': [],
    'qweb': [
        'static/src/xml/lockdown.xml',
        ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
