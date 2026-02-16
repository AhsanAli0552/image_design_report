{
    'name': "cyb_sku_product_report",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': """
Long description of module's purpose
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['sale'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'report/report.xml',
        'report/sku_sale_report.xml',
    ],
}

