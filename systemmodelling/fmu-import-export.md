---
layout: default
title: FMU Import Export
---

Two commands have been implemented in order to link SysML modelling and FMI definition i.e. the modeldescription.xml file defined inside the [FMI 2.0 specification][3].

# FMI Import

* This command imports the `modelDescription.xml` document describing the interface of a FMI and created an corresponding SysML Block under Modelio.
* Importing is easily done via the right click content menu, under a Package, as shown on the screenshot below.

![1]


# FMI Export

* This only exports the `modelDescription.xml` document describing the interface of a FMI and not its behavior.
* Exporting is easily done via the right click content menu, under a SysML Block, as shown on the screenshot below.

![2]

[1]: importfmi.png

[2]: reversefmi.png

[3]: https://www.fmi-standard.org/downloads
