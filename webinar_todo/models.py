from odoo import models,fields

class Todo(models.Model):
    _name = "wb.todo"

    name = fields.Char("Nombre")
    status = fields.Selection(selection=[("borrador","Borrador"),("hecho","Hecho")])