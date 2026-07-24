import json
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
schema = json.loads((ROOT / "schemas" / "station-registration.schema.json").read_text())
validator = Draft202012Validator(schema)

valid = json.loads((ROOT / "examples" / "station-controlled.example.json").read_text())
validator.validate(valid)

invalid = json.loads((ROOT / "examples" / "invalid-verified-without-endpoint.json").read_text())
errors = list(validator.iter_errors(invalid))
assert errors, "verified registration without endpoint unexpectedly validated"

print("station registration fixtures: valid accepted; invalid rejected")
