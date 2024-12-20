# -*- coding: utf-8 -*-
{
    'name' : 'Factura Electronica Impulsa IT Odoo 17',
    'summary':"""
        Implementacion Factura Electronica FEL XIM
    """,
    'author':'XIM ODOO',
    'category': 'General',
    'version' : '1.0.0',
    'depends': [
        "account",
        "account_debit_note"
    ],
    'data': [
        "security/fel_security.xml",
        "security/ir.model.access.csv",
        "views/account_move.xml",
        "views/account_journal.xml",
        "views/res_partner.xml",
        "views/res_company.xml",
        "report/report_invoice.xml",
    ]
}