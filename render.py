#!/usr/bin/env python3
# StaticJinja
# MIT License
# Albert Huang
import os
import sys
import traceback
import json
import shutil
from jinja2 import Environment, PackageLoader, select_autoescape

def render_file(jinja2_env, src, dst):
    try:
        template = jinja2_env.get_template(src)
        final_dst = os.path.join("publish", dst)
        
        relative_resource_path = ""
        dst_parts = dst.split("/")
        
        if len(dst_parts) > 1:
            relative_resource_path = "/".join([".."] * (len(dst_parts) - 1)) + "/"
        
        if os.path.dirname(final_dst) and not os.path.isdir(os.path.dirname(final_dst)):
            os.mkdir(os.path.dirname(final_dst))
        with open(final_dst, "w") as dst_fh:
            dst_fh.write(template.render(relative_resource_path = relative_resource_path))
    except:
        print("ERROR: Could not render %s to %s!" % (src, dst))
        traceback.print_exc()
        sys.exit(1)

def main():
    env = Environment(
        loader=PackageLoader('render', 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    
    try:
        with open("config.json") as config_fh:
            config = json.loads(config_fh.read())
    except:
        print("ERROR: Could not load configuraton!")
        traceback.print_exc()
        sys.exit(1)
    
    if not os.path.isdir("publish"):
        os.mkdir("publish")
    
    for page_entry in config["files"]:
        print("Rendering: %s -> %s" % (page_entry["src"], page_entry["dst"]))
        render_file(env, page_entry["src"], page_entry["dst"])
    
    for static_dir in ["css", "js"]:
        print("Copying: %s" % static_dir)
        shutil.copytree(static_dir, os.path.join("publish", static_dir))

if __name__ == "__main__":
    main()
