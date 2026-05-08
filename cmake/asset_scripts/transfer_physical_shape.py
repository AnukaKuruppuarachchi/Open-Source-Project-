#!/usr/bin/env python3
"""
Transfer physical shape from a project map JSON to an official .meta.json file.

Usage: transfer_physical_shape.py map.json target.meta.json

Derives the resource name from the target filename (e.g., resistance_torso_corpse.meta.json
-> resistance_torso_corpse), looks it up in map.json's external_resources, and transfers
as_physical.custom_shape to offsets.non_standard_shape in the target.
"""

import json
import sys
import os


def find_resource(map_data, resource_name):
    for res in map_data.get("external_resources", []):
        path = res.get("path", "")
        name = os.path.splitext(os.path.basename(path))[0]
        if name == resource_name:
            return res

        res_id = res.get("id", "")
        if res_id == f"@{resource_name}":
            return res

    return None


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} map.json target.meta.json")
        sys.exit(1)

    map_path = sys.argv[1]
    target_path = sys.argv[2]

    basename = os.path.basename(target_path)
    resource_name = basename.replace(".meta.json", "")

    with open(map_path) as f:
        map_data = json.load(f)

    resource = find_resource(map_data, resource_name)
    if resource is None:
        print(f"Resource '{resource_name}' not found in {map_path}")
        sys.exit(1)

    custom_shape = resource.get("as_physical", {}).get("custom_shape", None)
    if custom_shape is None:
        print(f"No custom_shape for '{resource_name}' in {map_path}")
        sys.exit(1)

    with open(target_path) as f:
        target_data = json.load(f)

    if "offsets" not in target_data:
        target_data["offsets"] = {}

    shape_data = {
        "source_polygon": custom_shape.get("source_polygon", []),
        "convex_partition": custom_shape.get("convex_partition", [])
    }

    target_data["offsets"]["non_standard_shape"] = shape_data

    with open(target_path, "w") as f:
        json.dump(target_data, f, indent=4)

    n_verts = len(shape_data["source_polygon"])
    n_parts = len(shape_data["convex_partition"])
    print(f"Transferred physical shape for '{resource_name}': {n_verts} vertices, {n_parts} partition indices")


if __name__ == "__main__":
    main()
