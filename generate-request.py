#!/usr/bin/python3
import sys
import os
import json

if len(sys.argv) != 5:
    print(f"Usage: {sys.argv[0]} pipeline test_name artifact version")
    sys.exit(1)

pipeline,test_name,artifact,version = sys.argv[1:7]

req = {
    "type": "Run Test",
    "user": pipeline,
    "test": test_name,
    "desired_version_override": {
        artifact: version
    }
}

print(json.dumps(req))


