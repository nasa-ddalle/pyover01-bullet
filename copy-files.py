#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Standard library modules
import os
import shutil


# This folder
fdir = os.path.dirname(os.path.realpath(__file__))
# Name of working folder
fwork = os.path.join(fdir, "work")

# Files list
fnames = [
    "pyOver.json",
    "inputs/matrix.csv",
    "inputs/bullet-mach.lay",
    "common/grid.in",
    "common/overflow.inp",
    "common/xrays.in",
    "common/fomo/mixsur.i",
    "common/fomo/grid.ibi",
    "common/fomo/grid.nsf",
    "common/fomo/grid.ptv",
    "common/fomo/mixsur.fmp",
    "dcf/GlobalDefs.tcl",
    "dcf/inputs.tcl",
    "dcf/config.tcl",
    "dcf/geom/bullet.lr8.crv",
    "dcf/geom/bullet.i.tri",
    "dcf/geom/bullet.stp",
    "dcf/bullet/BuildBullet.tcl",
    "dcf/bullet/localinputs.tcl",
    "dcf/bullet/Makefile"
]

# Check if working folder exists
if not os.path.isdir(fwork):
    # Create it
    os.mkdir(fwork)

# Loop through files
for fname in fnames:
    # System independence
    f1 = fname.replace("/", os.sep)
    # Source file
    fsrc = os.path.join(fdir, f1)
    # Destination file
    fdest = os.path.join(fwork, f1)
    # Check if output file already exists
    if os.path.isfile(fdest):
        # Skip
        continue
    # Break out folder names (if any)
    fparts = fname.split("/")[:-1]
    # Create cumulative subfolder name
    fsub = fwork
    # Loop through subfolder names
    for fpart in fparts:
        # Add to subfolder name
        fsub = os.path.join(fsub, fpart)
        # Check if folder exists
        if os.path.isdir(fsub):
            continue
        # Create folder
        os.mkdir(fsub)
    # Copy file
    shutil.copy(fsrc, fdest)

