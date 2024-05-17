from marshmallow import Schema, EXCLUDE, fields, post_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_enum import EnumField
from core.models.teachers import Teacher
from core.libs.helpers import GeneralObject

class TeacherSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Teacher  # Associate the schema with the Teacher model
        unknown = EXCLUDE  # Exclude unknown fields from the schema

    # Define fields for serialization and deserialization
    id = auto_field(required=False, allow_none=True)  # ID field (optional and nullable)
    user_id = auto_field()  # User ID field
    created_at = auto_field(dump_only=True)  # Created timestamp (read-only)
    updated_at = auto_field(dump_only=True)  # Updated timestamp (read-only)

    # Define a method to instantiate a Teacher object after deserialization
    @post_load
    def initiate_class(self, data_dict, many, partial):
        # This method creates a Teacher object from the deserialized data
        # pylint: disable=unused-argument,no-self-use
        return Teacher(**data_dict)  # Instantiate a new Teacher object using the deserialized data
