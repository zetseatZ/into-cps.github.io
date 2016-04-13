---
layout: default
title: Overview
---


# RT-Tester (Core)
RT-Tester is a test automation tool for automatic test generation, test
execution and real-time test evaluation. Key features include a strong
C/C++-based test script language, high performance multi-threading, and
hard real-time capability.
The tool has been successfully applied in avionics, rail automation, and
automotive test projects. 
More information is available on the product web site
[here](https://www.verified.de/products/rt-tester/).


# RT-Tester Model Based Extension (RTT-MBT)
RT-Tester Model Based Test Case and Test Data Generator (RTT-MBT) supports
model-based testing (MBT), that is, automated generation of test cases, test
data, and test procedures from UML/SysML models. A number of common modelling
tools can be used as front-end for this. 
The derived test procedures use the RT-Tester Core as a back-end, allowing the
system under test to be provided on real hardware, software only, or even
just simulation to aid test model development.
RTT-MBT includes requirement tracing from test models down to test executions
and allows for powerful status reporting in large scale testing projects.
More information is available on the product web site
[here](https://www.verified.de/products/model-based-testing/).


## FMI/FMU support for RT-Tester / RTT-MBT
The RTT-MBT component is catering for FMI/FMU by a specialised feature
release that allows to cast a test procedures to an FMI2-compliant FMU.
That FMU is in input to the COE.

## Downloads
In order to operate properly, it is necessary to first obtain the prerequisite
tools Python-2.7 and gcc-4.9.
An installer collection is available [for Windows] (https://secure.verified.de/f5x1hks4/into-cps/one-click/install_Python27_gcc49.exe).

RT-Tester Core, RTT-MBT, RTTUI3, and prepared example projects can be downloaded and 
installed by one click
  [for Windows] (https://secure.verified.de/f5x1hks4/into-cps/one-click/VSI_bundle.exe)

Updates of the installers will be available at the same URL.
