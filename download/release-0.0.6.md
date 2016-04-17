---
layout: default
title: INTO-CPS Release 0.0.6
---

# INTO-CPS TOOL BUNDLE - Release 0.0.6

[Download bundle](http://staff.iha.dk/pgl/into-cps-release-0.0.6-2016-04-17.zip)


**IMPORTANT: This bundle is only intended for use by the INTO-CPS consortium
members and contains software that requires you to own a valid license!**


The release documentation, and tool descriptions and guides can be found at the
INTO-CPS Release Site:
http://overture.au.dk/into-cps/site/


##Requirements
You need a 64 bit Microsoft Windows system with a 64 bit Java Run-Time
Environment ([download](https://www.java.com/en/download/manual.jsp)) installed
to run all the tools in this bundle.


##This bundle includes:

- 20-sim-4.6.1.6846-intocps-win32.exe:
  20-sim 4.6 - Modeling and simulation tool

- 20sim4C.exe:
  20-sim 4C 2.1.9 - Tool for rapid prototyping for control engineers.

- install_Python27_gcc49.exe
  Python 2.7 and GCC 4.9 bundle installer. Requiremented by the VSI tools (VSI_bundle.exe)

- VSI_bundle.exe
  The RT-Tester and the RT-Tester UI installer

- coe-0.0.4-jar-with-dependencies.jar
  Latest version of COE

- modelio-open-201512081403-win32.win32.x86_64.zip
  Latest version of OpenModelio (UML/BPMN modelling tool).

- modelio_modules.zip:
  INTO-CPS App and FMU export module along with other essential Modelio
  modules.
  Guide for installation of Modelio modules:
  <http://forge.modelio.org/projects/modelio3-usermanual-english-330/wiki/Modeler-_modeler_modelio_settings_modules_catalog>
  Guide for deploying modules into a Modelio project:
  <http://forge.modelio.org/projects/modelio3-usermanual-english-330/wiki/Modeler-_modeler_managing_projects_configuring_project_modules>

- OpenModelica-v1.10.0-dev-440-gd0581ff-64bit.exe
  Latest nightly build of OpenModelica. A Modelica-based modelling and
  simulation tool.

- Overture-2.3.4-win32.win32.x86_64.zip
  Latest version of the Overture tool. A tool for modelling control systems
  using The Vienna Development Method (VDM).

- README.md: You are currently reading it! ;)

- vdm-tool-wrapper.zip
  The latest version of the VDM Tool Wrapper.


# FMU Examples

To get the latest FMU examples please visit:
<https://github.com/into-cps/public-fmu-examples>

The latest FMU builds are directly available at:
<http://overture.au.dk/into-cps/examples/public-fmu-examples/latest/>


# Download manager

Tired of downloading a huge bundle ZIP-file and manually installing each and
every tool? Then try out the new download manager. Unfortunately not all tools
are available via this but we hope to change that soon!

You can find the pre-release of download manager here:
<https://github.com/into-cps/download-manager/releases>

The download manager is currently only released for Windows (64-bit) but it is fully
cross-platform and more platform releases will be made available if requested.


# Known issues:

1. Anti-Virus erroneously detects COE as a possible threat:
   This is a known issue with anti-virus software. You can read more about the
   on the Release Site,
   [here](http://overture.au.dk/into-cps/site/simulation/antivirus.html). A
   guide on how to exclude applications/processes can be found
   [here](http://www.tenforums.com/tutorials/5924-windows-defender-exclusions-add-remove-windows-10-a.html).
