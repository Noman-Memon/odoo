from odoo import models, fields


# create wizard folder in project
# create __init__.py file
# create wizard.py file or any other name as we want
# to create its view
# define path in manifest.py
# Note : Do all things same as creation of models and its fields, views, actions_ids everything only two fields extra create in
# wizard action_id that is
# <field name="target">new</field>
#         <field name="view_id" ref="tutorial_project.rest_staff_wizard_view_form"/>

# after this create action button where ever we want and define this wizard's xml file action_id with project name '
class RestStaffWizard(models.TransientModel):
    _name = 'rest.staff.wizard'
    _description = 'This wizard will update information of staff'

    name = fields.Char(string='Name', size=50)
    age = fields.Integer(string='Age')
    dob = fields.Date(string='Date_Of_Birth')
    mobile = fields.Char(string='Mobile_Number')
    email = fields.Char(string="Email")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    country_id = fields.Many2one('res.country',
                                 string="Country")  # when we want to get 1 record from multiple records of other models or objects
    country_ids = fields.Many2many('res.country', string="Countries")
    country_code = fields.Char(string="Country_code",
                               related="country_id.code")  # if we want to get related data of any field of many2one object then...
    staff_line_ids = fields.One2many('rest.staff.wizard.lines', 'connecting_field', string="Staff Line")
    image = fields.Binary(string="Image")
    hand_salary = fields.Float(string="In Hand Salary")
    epf_efi = fields.Float(string="EPF+ESI")
    ctc_salary = fields.Float(string="CTC")


class RestStaffWizardLines(models.TransientModel):
    _name = 'rest.staff.wizard.lines'
    _description = 'This model store line data of staff'

    name = fields.Char(string="Name", size=50, required=True)
    connecting_field = fields.Many2one('rest.staff.wizard', string="staff ID")
    product_id = fields.Many2one('product.product', string="Products")
    sequence = fields.Integer(string="Seq.")
