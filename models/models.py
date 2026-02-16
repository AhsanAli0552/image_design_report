# from odoo import models, fields, api


# class cyb_sku_product_report(models.Model):
#     _name = 'cyb_sku_product_report.cyb_sku_product_report'
#     _description = 'cyb_sku_product_report.cyb_sku_product_report'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

