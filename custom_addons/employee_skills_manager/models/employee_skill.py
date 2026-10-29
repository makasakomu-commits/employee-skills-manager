
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class EmployeeSkill(models.Model):
    _name = 'employee.skill'
    _description = 'Employee Skill'
    _rec_name = 'name'
    _order = 'employee_id, name'

    name = fields.Char(
        string='Skill Name',
        required=True,
    )

    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Employee',
        ondelete='cascade',
    )

    level = fields.Selection(
        selection=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
            ('expert', 'Expert'),
        ],
        string='Skill Level',
        default='beginner',
        required=True,
    )

    @api.constrains('employee_id', 'name')
    def _check_duplicate_employee_skill(self):
        for record in self:
            if not record.employee_id or not record.name:
                continue

            skill_name = record.name.strip()

            if not skill_name:
                raise ValidationError(
                    "Skill Name cannot contain only spaces."
                )

            duplicate = self.search([
                ('id', '!=', record.id),
                ('employee_id', '=', record.employee_id.id),
                ('name', '=ilike', skill_name),
            ], limit=1)

            if duplicate:
                raise ValidationError(
                    "This employee already has this skill recorded."
                )
