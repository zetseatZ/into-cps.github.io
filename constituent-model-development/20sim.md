---
layout: default
title: Overview
---


# 20-Sim
20-sim is a modeling and simulation program for mechatronic systems. With
20-sim you can enter model graphically, similar to drawing an engineering
scheme. With these models you can simulate and analyze the behavior of
multi-domain dynamic systems and create control systems. You can even generate
C-code and run this code on hardware for rapid prototyping and HIL-simulation.
More information is available on the 20-sim website [here](http://www.20sim.com/).


## FMI/FMU support for 20-sim
FMI support for INTO-CPS is provided using a code generation template. For 20-sim 4.5, this template can be downloaded from our Github repository [here](https://github.com/controllab/fmi-export-20sim) and the installation instructions can be found in the included [README](https://github.com/controllab/fmi-export-20sim/blob/master/README.md) file. Starting with 20-sim 4.6, the template is available out of the box.

Instructions on how to set up automated compilation of the .fmu are given under the section *External dependencies* in the above [README](https://github.com/controllab/fmi-export-20sim/blob/master/README.md) file.
