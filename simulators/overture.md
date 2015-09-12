---
layout: default
title: Overview
---

# Overture

The Overture community supports the modelling method *The Vienna Development Method (VDM)* which is a set of modelling techniques that have a long and successful history in both research and industrial application in the development of computer-based systems.

The *Overture Tool* is an open-source integrated development environment (IDE) for developing and analysing VDM models. The tool suite is written entirely in Java and built on top of the Eclipse platform.

## FMI support for Overture

The Overture tool currently does not have build-in support for FMI. However a prototype is available that is based on the Overture simulator made for the crescendo tool.

### Components required to create an FMU

* the VDM model `*.vdmrt`
* the native FMI library that provides a bridge between FMI and the Crescendo simulator [`libgrpcfmu.so`](http://overture.au.dk/into-cps/test/fmu/libgrpcfmu.so)
* the crescendo simulator build for FMI [`crescendo-fmi-2.0.7-SNAPSHOT-jar-with-dependencies.jar`](http://overture.au.dk/into-cps/test/fmu/crescendo-fmi-2.0.7-SNAPSHOT-jar-with-dependencies.jar)
* a model description file (like the one shown below). `modelDescription.xml`
* a config file specifying how the FMI bridge is launched [`config.txt`](http://overture.au.dk/into-cps/test/fmu/config.txt)


### FMU layout

The FMU is a 7z library with the following layout:

```
binaries
	linux64
		<FMU name>.so
sources
	*.vdmrt
	modelDescription.xml
resources
	config.txt
	crescendo-fmi-2.0.7-SNAPSHOT-jar-with-dependencies.jar
modelDescription.xml

```
Note the duplication of the `modelDescription.xml`.

### Example model description

The scalar variable names used in the `modelDescription.xml` must be the fully qualified names of the VDM instance variables. The name format must match the naming used in the link file of the Crescendo tool.
 The names are currently used to lookup VDM values at run-time. This will in futher versions be change to use the `valueReference` as described in the FMI standard.
 
```Xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<fmiModelDescription fmiVersion="2.0" modelName="<FMU name>" guid="{8c4e810f-3df3-4a00-8276-176fa3c9f003}" numberOfEventIndicators="0">

	<CoSimulation modelIdentifier="tankcontroller" canHandleVariableCommunicationStepSize="true" />

	<ModelVariables>
		
		<!-- INDEX 1-->
		<ScalarVariable name="Controller.maxLevel" valueReference="0" description="the max tank level" causality="parameter" variability="fixed" initial="exact">
			<Real start="5"/>
		</ScalarVariable>

		<!-- INDEX 2-->
		<ScalarVariable name="System.levelSensor.level" valueReference="3" description="the tank level" causality="input" variability="continuous">
			<Real start="1" />
		</ScalarVariable>

		<!-- INDEX 3-->
		<ScalarVariable name="System.valveActuator.valveState" valueReference="4" description="the tank valve state" causality="output" variability="discrete" initial="calculated">
			<Boolean />
		</ScalarVariable>

	</ModelVariables>

	<ModelStructure>
		<Outputs>
			<Unknown index="4" dependencies="2" />
		</Outputs>

	</ModelStructure>

</fmiModelDescription>

```







