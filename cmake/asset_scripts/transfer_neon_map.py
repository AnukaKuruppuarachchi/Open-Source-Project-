#!/usr/bin/env python3
"""
Transfer neon map settings from a project map JSON to an official .meta.json file.

Usage: transfer_neon_map.py map.json target.meta.json

Derives the resource name from the target filename (e.g., metropolis_torso_corpse_head.meta.json
-> metropolis_torso_corpse_head), looks it up in map.json's external_resources, and transfers
neon_map fields to extra_loadables.generate_neon_map in the target.
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

    neon_map = resource.get("neon_map", None)
    if neon_map is None:
        print(f"No neon_map for '{resource_name}' in {map_path}")
        sys.exit(1)

    with open(target_path) as f:
        target_data = json.load(f)

    if "extra_loadables" not in target_data:
        target_data["extra_loadables"] = {}
    if "generate_neon_map" not in target_data["extra_loadables"]:
        target_data["extra_loadables"]["generate_neon_map"] = {}

    neon_target = target_data["extra_loadables"]["generate_neon_map"]

    if "light_colors" in neon_map:
        neon_target["light_colors"] = neon_map["light_colors"]

    if "amplification" in neon_map:
        neon_target["amplification"] = neon_map["amplification"]

    if "standard_deviation" in neon_map:
        neon_target["standard_deviation"] = neon_map["standard_deviation"]

    if "radius" in neon_map:
        neon_target["radius"] = neon_map["radius"]

    if "alpha_multiplier" in neon_map:
        neon_target["alpha_multiplier"] = neon_map["alpha_multiplier"]

    with open(target_path, "w") as f:
        json.dump(target_data, f, indent=4)

    n_colors = len(neon_map.get("light_colors", []))
    print(f"Transferred neon map for '{resource_name}': {n_colors} light colors")


if __name__ == "__main__":
    main()
