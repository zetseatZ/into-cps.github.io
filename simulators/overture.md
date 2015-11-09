---
layout: default
title: Overview
---

# Overture

The Overture community supports the modelling method *The Vienna Development Method (VDM)* which is a set of modelling techniques that have a long and successful history in both research and industrial application in the development of computer-based systems.

The *Overture Tool* is an open-source integrated development environment (IDE) for developing and analysing VDM models. The tool suite is written entirely in Java and built on top of the Eclipse platform.

## FMI support for Overture

The Overture tool currently does not have build-in support for FMI. However a prototype is available that is based on the Overture simulator made for the crescendo tool.

* Note that FMUs running **VDM require variable step size**. If a fixed step size is selected then it may introduce errors. Thus if fixed stepsize is selected make sure that the interval is close to that of the control loop. (Internally VDM runs with nano seconds resolution where each expression is assigned a time cost)*

### Components required to create an FMU

* the VDM model `*.vdmrt`
* a copy of the vdm tool wrapper [(last release)](http://overture.au.dk/into-cps/vdm-tool-wrapper/development/Build-30_2015-10-21_10-47/vdm-tool-wrapper.zip) | [(link to development download site)](http://overture.au.dk/into-cps/vdm-tool-wrapper/development/)

### Supported Platforms
* Windows 32 and 64 bit + Java 32/64
* Linux 64 bit + Java x64
* Mac OSX 64 bit + Java x64

### FMU layout

The FMU is a 7z library with the following layout:

```
binaries
	linux64
		<FMU name>.so
	darwin64
		<FMU name>.dylib
	win32
		<FMU name>.dll
	win64
		<FMU name>.dll

sources
	*.vdmrt
resources
	config.txt
	crescendo-fmi-2.0.7-SNAPSHOT-jar-with-dependencies.jar
modelDescription.xml
```
The VDM Tool wrapper includes the folders `binaries` and `resources` and a `modelDescription.xml` file that can be used as a template.

### FMU Creation Procidure
To create the FMU do the following:

1. Download the VDM tool wrapper (link shown above)
2. Extract is and create the directory structure as shown above
4. Rename the binaries/{*.so/*.dll/*.dylib} such that they match the FMU name
5. Copy the VDM source files (*.vdmrt) into the `sources` directory
6. Update the model description (example shown below)
7. Compress the directories `binaries`, `sources`, `resources` and the `modelDescription.xml` file into a 7z archive named `<FMU name>.fmu`

### Example model description

The scalar variable names used in the `modelDescription.xml` must be the fully qualified names of the VDM instance variables. The name format must match the naming used in the link file of the Crescendo tool.
 The names are currently used to lookup VDM values at run-time. This will in futher versions be change to use the `valueReference` as described in the FMI standard.
 
```Xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<fmiModelDescription 
    fmiVersion="2.0" 
    modelName="<FMU name>" 
    guid="{8c4e810f-3df3-4a00-8276-176fa3c9f003}" 
    numberOfEventIndicators="0">

  <CoSimulation modelIdentifier="tankcontroller" needsExecutionTool="true"
                canHandleVariableCommunicationStepSize="true" />

  <ModelVariables>
		
    <!-- INDEX 1-->
    <ScalarVariable name="Controller.maxLevel" 
        valueReference="0" 
        description="the max tank level" 
        causality="parameter" 
        variability="fixed" 
        initial="exact">
      <Real start="5"/>
    </ScalarVariable>

    <!-- INDEX 2-->
    <ScalarVariable name="System.levelSensor.level" 
        valueReference="3" 
        description="the tank level" 
        causality="input" 
        variability="continuous">
      <Real start="1" />
    </ScalarVariable>

    <!-- INDEX 3-->
    <ScalarVariable name="System.valveActuator.valveState" 
        valueReference="4" 
        description="the tank valve state" 
        causality="output" 
        variability="discrete" 
        initial="calculated">
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


## Name Mapping

The name of the scalar variable which is used by the VDM interpreter to locate it during runtime is desired to be different than the VDM lookup path then this can be achieved using the following element in the model description:

```Xml
<Overture>
  <link valueReference="0" name="Controller.maxLevel"/>
  <link valueReference="3" name="System.levelSensor.level"/>
  <link valueReference="4" name="System.valveActuator.valveState"/>
</Overture>
```
The VDM interpreter will read this section first and ignore the scalar variable `name` attribute if found in this element. The value reference is the link to the scalar variable.
