---
layout: default
title: System Modelling with Modelio
---




# System Modelling with Modelio

## Description##

Modelio is a combined UML/BPMN modeler supporting a wide range of models and diagrams.

Modelio's main features:

* SysML support integrated with UML and BPMN
* XMI import and export
* Scripting language support (Jython)
* Extensibility: Modelio can be extended for any language, methodology or modeling technique just by adding modules. You can either use existing modules or else develop your own.


A forum is available on the [Modelio community site](http://www.modelio.org/forum/index.html).

## License##
**Modelio** is **open source** software. Most of the source code is under the **GNU GPL** license. The module runtime, used to develop extensions to Modelio, is under the **Apache license** providing a very large degree of freedom to anyone wishing to reuse and embed the code.

Full details on Modelio licensing conditions can be found [here](http://www.modelio.org/about-modelio/license.html).

## Download and installation##

**Modelio's current version is 3.3**.

Binary distribution archives for Linux and Windows are available on the [download page](http://www.modelio.org/downloads/download-modelio.html) of the Modelio community site.

Installation requirements and instructions can be found in our [Quick start guide](http://www.modelio.org/documentation/installation.html) on the community site.

Modelio version contents can be found in the [[Version history]].

### Installing FMU Export support

To be able to export n modelDescription from a SysML block into Modelio you have to first install the INTOCPS module which is available here for now:

[https://dl.dropboxusercontent.com/u/13060777/INTO-CPS/INTOCPS_0.0.1.jmdac]()

A specific project will be created into Modelio.org forge for future version.

**Key:**

1. Run the **Configuration / ![2] Modules catalog...** command.
2. To add a module, click on **Add a module to the catalog...** and use the file browser to select the modules (*.jmdac files).
3. To remove a module, select the module in question and click on the **Remove module from the catalog** button.
4. To download new versions of modules into the catalog, click on **Check for new versions...**.

#### Installing modules in a project

![3]

####Installing a module in a project

**Steps:**

* **1**. Click on [![4]] to expand the Modules catalog.
* **2**. In the Modules catalog, select the module you want to install.
* **3**. Click on [![5]] to install the module in the project.

   [1]: module_catalog.png
   [2]: modulecatalog.png
   [3]: en-installingmodules.png
   [4]: maximize.png
   [5]: add.png

## Documentation

**For end users**

* [User's manual](http://forge.modelio.org/projects/modelio3-usermanual-english-300/wiki) *(wiki)*
* [Installing a module in to Modelio](http://forge.modelio.org/projects/modelio3-usermanual-english-330/wiki/Modeler-_modeler_modelio_settings_modules_catalog)
* [Configuring Modelio project modules](http://forge.modelio.org/projects/modelio3-usermanual-english-330/wiki/Modeler-_modeler_managing_projects_configuring_project_modules)
