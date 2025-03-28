#!/usr/bin/env python3
import sys
import yaml


def printit(disk):
    print(
        f'    {" ".join(disk["tags"]):<15} {int(disk["size"])/(1000000000):<10.1f}',
        disk["id_path"],
    )


def read_yaml_from_stdin():
    try:
        yaml_content = sys.stdin.read()
        data = yaml.safe_load(yaml_content)[0]

    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"\n{data['hostname']}\n")

    bootdisk = data["boot_disk"]
    print("  Bootdisk")
    printit(bootdisk)
    blockdevs = data["blockdevice_set"]
    print("  Devices")
    for bd in blockdevs:
        printit(bd)


if __name__ == "__main__":
    read_yaml_from_stdin()
