{
    'name': 'Invoice Follow-up Management',
    'version': '1.0',
    'author': 'Shanid V V',
    'category': 'Invoice Management',
    'summary': 'Invoice Follow-up Management',
    'description': "",
    'license': 'LGPL-3',
    'application': True,
    'depends': ['base', 'sale'],
    'data': [
        'views/account_move_view.xml',
        'views/search_view_account_move.xml',
        'report/account_move_report.xml',
        'report/report_invoice_inherit.xml'
    ]
}