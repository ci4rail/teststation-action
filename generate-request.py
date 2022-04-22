#!/usr/bin/python3
import sys
import os
import json

if len(sys.argv) != 4:
    print(f"Usage: {sys.argv[0]} pipeline test_name artifact_override")
    sys.exit(1)

pipeline,test_name,artifact_override = sys.argv[1:4]

print("artifact_override='%s", artifact_override)

req = {
    "type": "Run Test",
    "user": pipeline,
    "test": test_name,
    "desired_version_override": {
        artifact_override
    }
}

print(json.dumps(req))


