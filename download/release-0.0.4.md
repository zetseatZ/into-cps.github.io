---
layout: default
title: INTO-CPS Release 0.0.4
---

# INTO-CPS TOOL BUNDLE - Release 0.0.4

[Download bundle](http://overture.au.dk/into-cps/release-bundles/0.0.4.zip)


**IMPORTANT: This bundle is only intended for use by the INTO-CPS consortium
members and contains software that requires you to own a valid license!**


The release documentation, and tool descriptions and guides can be found at the
INTO-CPS Release Site:
http://overture.au.dk/into-cps/site/


##Requirements
You need a 64 bit Microsoft Windows system with a 64 bit Java Run-Time
Environment ([download](https://www.java.com/en/download/manual.jsp)) installed to run all the
tools in this bundle.


##This bundle includes:

- fmu-examples (folder):
  The cross-platform test FMUs.

- 20sim.exe:
  20-sim 4.6 - Modeling and simulation tool

- 20sim4C.exe:
  20-sim 4C 2.1.8 - Tool for rapid prototyping for control engineers.
  If you wish to use 20-sim 4C 2.1.8 with 20-sim 4.6, please follow the steps described here: http://www.20sim4c.com/news/81-using4cin20sim46.html

- 2016-02-02.VSI-TOOLCHAIN.zip:
  Entire toolchain for RT-Tester and the RT-Tester UI. Installation
  instructions can be found in the README inside the zip-file.

- coe-0.0.1-SNAPSHOT-jar-with-dependencies.jar:
  Latest version of COE

- modelio-open-201512081403-win32.win32.x86_64.zip:
  Latest version of OpenModelio (UML/BPMN modelling tool).

- modelio_modules.zip:
  INTO-CPS App and FMU export module along with other essential Modelio modules.

- OpenModelica-v1.9.4-dev.beta1-27-g8b53e78.exe:
  Latest nightly build of OpenModelica. A Modelica-based modelling and simulation tool.

- Overture-2.3.0-win32.win32.x86.zip:
  Latest version of the Overture tool. A tool for modelling control systems using The Vienna Development Method (VDM).

- RELEASE_NOTES.txt: This text file.

- vdm-tool-wrapper.zip:
  The latest version of the VDM Tool Wrapper.


# Known issues:
1. Anti-Virus erroneously detects COE as a possible threat:
   This is a known issue with anti-virus software. You can read more about the
   on the Release Site,
   [here](http://overture.au.dk/into-cps/site/simulation/antivirus.html). A
   guide on how to exclude applications/processes can be found
   [here](http://www.tenforums.com/tutorials/5924-windows-defender-exclusions-add-remove-windows-10-a.html).
