{
    'name': 'Employee Skills Manager',
    'version': '19.0.1.1',
    'category': 'Human Resources',
    'summary': 'Manage employee skills and skill levels',
    'description': """
        Employee Skills Manager
        =======================
        A learning project for understanding Odoo development.
    """,
    'author': 'Frank',
    'license': 'LGPL-3',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/skill_views.xml',
    ],
    'installable': True,
    'application': True,
}
