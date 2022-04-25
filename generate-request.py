#!/usr/bin/python3
import sys
import os
import json

if len(sys.argv) != 4:
    print(f"Usage: {sys.argv[0]} pipeline test_name artifact_override")
    sys.exit(1)

pipeline,test_name,artifact_override_json = sys.argv[1:4]

artifact_override=json.loads(artifact_override_json)

req = {
    "type": "Run Test",
    "user": pipeline,
    "test": test_name,
    "desired_version_override": artifact_override
}

print(json.dumps(req))


