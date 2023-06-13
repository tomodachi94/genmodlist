#!/usr/bin/env python3
import os
import sys
import zipfile  # For reading the contents of .jar files
import json  # For mcmod.info parsing
import argparse  # For a proper CLI

import toml  # For mods.toml parsing


def get_mod_name_from_mcmodinfo(file):
    with zipfile.ZipFile(file, "r") as zip_ref:
        try:
            with zip_ref.open("mcmod.info") as mod_info:
                mod_data = json.load(
                    mod_info,
                    strict=False,  # HACK: See https://stackoverflow.com/questions/22394235
                )
                return mod_data[0]["name"]
        except KeyError:
            pass


def get_mod_name_from_mods_toml(file):
    with zipfile.ZipFile(file, "r") as zip_ref:
        try:
            with zip_ref.open("META-INF/mods.toml") as mod_info:
                mod_data = toml.load(mod_info)

                return mod_data["mods"][0]["displayName"]
        except (KeyError, FileNotFoundError):
            pass


def extract_mod_names(directory):
    for file in os.listdir(directory):
        if file.endswith(".jar") or file.endswith(".zip"):
            file_path = os.path.join(directory, file)
            mod_name = get_mod_name_from_mcmodinfo(
                file_path
            ) or get_mod_name_from_mods_toml(file_path)
            if mod_name:
                print(mod_name)


if __name__ == "__main__":
    p = argparse.ArgumentParser(
        prog="genmodlist",
        description="Generate a list of Minecraft mods from a directory.",
    )

    p.add_argument("--directory", "-d", help="The directory to scan.")

    # Exit unsuccessfully if no arguments provided
    if len(sys.argv) == 1:
        p.print_help(sys.stderr)
        sys.exit(1)

    args = p.parse_args()
    extract_mod_names(args.directory)
