from odoo import models, fields


class RestStaff(models.Model):
    _name = 'rest.staff'
    _description = 'This model store data of staff'
    _rec_name = 'name'  # rec_name is used to show records according to specidief field like age,dob,email, etc...
    _order = 'age'  # _order is used to show list or tree according to specified filed , bydefault its shows by id , we canalso specified asc or desc

    name = fields.Char(string='Name', size=50)
    age = fields.Integer(string='Age')
    dob = fields.Date(string='Date_Of_Birth')
    mobile = fields.Char(string='Mobile_Number')
    email = fields.Char(string="Email")
    gender = fields.Selection([('male','Male'),('female','Female')], string="Gender")
    country_id = fields.Many2one('res.country',
                                 string="Country")  # when we want to get 1 record from multiple records of other models or objects
    country_ids = fields.Many2many('res.country', string="Countries")
    country_code = fields.Char(string="Country_code",
                               related="country_id.code")  # if we want to get related data of any field of many2one object then...
    staff_line_ids = fields.One2many('rest.staff.lines', 'connecting_field', string="Staff Line")
    sequence = fields.Integer(string="seq.")
    status = fields.Selection([('active','Active'),('resigned','Resigned')], string="status", readonly=True, default='active')


    def new_function(self):
        print("Hello!.")

    # this function is used to delete all rows of current record line items.
    def delete_one2many(self):
        for record in self:
            if record.staff_line_ids:
                record.staff_line_ids = [(5, 0, 0)]
                # if we want to return some messages with rainbow effect
                return {
                    'effect': {
                        'fadeout': 'slow',
                        'type': 'rainbow_man',
                        'message': 'record has been deleted',
                    }
                }
    def changestatus(self):
        for record in self:
            if record.status == 'active':
                record.status = 'resigned'
            else:
                record.status = 'active'

class RestStaffLines(models.Model):
    _name = 'rest.staff.lines'
    _description = 'This model store line data of staff'

    name = fields.Char(string="Name", size=50)
    connecting_field = fields.Many2one('rest.staff', string="staff ID")
    product_id = fields.Many2one('product.product', string="Products")
    sequence = fields.Integer(string="seq.")
