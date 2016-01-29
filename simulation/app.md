---
layout: default
title: Overview
---


# APP

Built on top of the Modelio tool, the INTO-CPS Application is the front-end of the INTO-CPS tool chain.
Embedded in the Browser and Editor modules,  the following screenshot shows how it looks.

![1]

Taking as input a configuration generated from an INTO-CPS Model, the INTO-CPS Application allows you to complete, 
thanks to a specific editor, the specification of the co-simulation orchestrated by the COE.

This editor is composed of four tabs:

- FMU Tab, listing the FMUs used for the simulation.
- Connection Tab, showing the specified connections.
- Parameter Tab, where parameter values are initialized.
- Algorithm Tab, for specifying the algorithm type and its different values. 

Note that the FMU and Connection tabs can not be modified from this editor (they come from the model generation).

![2]


Once the co-simulation configuration has been fully specified, it is possible to run the co-simulation. 
At the end of the simulation activity, a folder will be created inside the results folder, containing the co-simulation configuration and the results, in CSV format.

![3]

[1]: app-general-aspect.png

[2]: app-fmus.png

[3]: app-result.png

