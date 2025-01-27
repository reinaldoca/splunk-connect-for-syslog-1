#! /usr/bin/env python3

import os
import shutil
import jinja2

plugin_path = os.path.dirname(os.path.abspath(__file__))

templateLoader = jinja2.FileSystemLoader(searchpath=plugin_path)
templateEnv = jinja2.Environment(loader=templateLoader)
tm = templateEnv.get_template("plugin.jinja")

msg = tm.render(
    stats_freq=os.getenv(f"SC4S_GLOBAL_OPTIONS_STATS_FREQ", 30),
    stats_level=os.getenv(f"SC4S_GLOBAL_OPTIONS_STATS_LEVEL", 1),
    log_fifo=os.getenv(f"SC4S_GLOBAL_OPTIONS_LOG_FIFO", 10000),
)

print(msg)
