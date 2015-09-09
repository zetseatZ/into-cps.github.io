---
layout: default
title: Overview
---


OpenModelica
============

[OpenModelica](http://openmodelica.org) is an open-source
[Modelica](http://modelica.org)-based modeling and simulation environment
intended for industrial and academic usage. Its short-term and long-term goals
are:
-  The short-term goal is to develop an efficient interactive
       computational environment for the Modelica language, as well as a
       rather complete implementation of the language. It turns out that
       with support of appropriate tools and libraries, Modelica is very
       well suited as a computational language for development and
       execution of both low level and high level numerical algorithms,
       e.g. for control system design, solving nonlinear equation
       systems, or to develop optimization algorithms that are applied
       to complex applications.

-  The longer-term goal is to have a complete reference implementation
       of the Modelica language, including simulation of equation based
       models and additional facilities in the programming environment,
       as well as convenient facilities for research and experimentation
       in language design or other research activities. However, our
       goal is not to reach the level of performance and quality
       provided by current commercial Modelica environments that can
       handle large models requiring advanced analysis and optimization
       by the Modelica compiler.


Documentation
-------------

The OpenModelica users guide [as pdf or epub](https://openmodelica.org/doc/OpenModelicaUsersGuide/)
or as [html](https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/).
The OpenModelica [API documentation](https://build.openmodelica.org/Documentation/OpenModelica.Scripting.html).
More documentation can be found [here](https://openmodelica.org/useresresources/userdocumentation).


Export an FMU from OpenModelica
-------------------------------


To export an FMU from a Modelica model one can use a exportFMU.mos script:

    // start exportFMU.mos script
    loadModel(Modelica); getErrorString();
    // loadModel(AnotherLibraryIfNeeded); getErrorString();
    // loadFile("SomeMOFileContainingYourModel.mo"); getErrorString();
    translateModelFMU(ModelName, "2.0", "cs"); getErrorString();
    // end exportFMU.mos

One can run the exportFMU.mos script via the omc[.exe] executable.
On Windows:

    %OPENMODELICAHOME%\bin\omc exportFMU.mos

On Linux (if OpenModelica is installed via apt-get):

    omc exportFMU.mos

On MacOS X:

    omc exportFMU.mos

Documentation of the function [translateModelFMU](https://build.openmodelica.org/Documentation/OpenModelica.Scripting.translateModelFMU.html).


Link to OpenModelica latest binaries
-------------------------------------

The latest release binaries for [Windows](https://openmodelica.org/download/download-windows) can be found [here](https://build.openmodelica.org/omc/builds/windows/releases/1.9.3/).
The latest nightly-builds binaries for Windows can be found [here](https://build.openmodelica.org/omc/builds/windows/nightly-builds/).

We also support [Linux](https://openmodelica.org/download/download-linux) and
[Mac OS](https://openmodelica.org/download/download-mac) installations.

