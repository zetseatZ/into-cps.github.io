---
layout: default
title: Co-Simulation
---


# Co-Simulation

A co-simulation starts by defining the connection between FMU instances at the
system modelling level. This is then used to create a multi-model that is
passed to the COE.

1. Define connections in SysML
2. Export the SysML model to the INTO-CPS App as a connections mapping
3. Crate a multi-model from the connections in the INTO-CPS App and assign FMUs
   to it.
4. Start the COE and launch the co-simulation

This assumes that all FMUs has been developed in one of the Simulators and
exported prior to this.







