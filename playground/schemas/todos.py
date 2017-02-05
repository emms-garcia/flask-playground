from marshmallow import Schema, fields, validate


class TodoSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=3))
    description = fields.Str(missing=None)
    complete = fields.Bool(missing=False)

    class Meta:
        strict = True
