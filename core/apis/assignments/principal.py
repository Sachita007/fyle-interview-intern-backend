from flask import Blueprint
from pprint import pprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment

from .schema import AssignmentSchema, AssignmentGradeSchema
principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)

@principal_assignments_resources.route("/assignments",methods=['GET'],strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of assignments"""
    submitted_filter = Assignment.state == 'SUBMITTED'
    graded_filter = Assignment.state == 'GRADED'
    filtered_assignments = Assignment.filter(submitted_filter | graded_filter).all()
    print(filtered_assignments)
    students_assignments_dump = AssignmentSchema().dump(filtered_assignments, many=True)
    return APIResponse.respond(data=students_assignments_dump)

@principal_assignments_resources.route("/assignments/grade",methods=['POST'],strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(p, incoming_payload):
    """Grade an assignment"""
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)
    graded_assignment = Assignment.mark_grade(
        _id=grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
        auth_principal=p
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)