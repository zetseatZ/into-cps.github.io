---
layout: default
title: FMI Support for the Overture Tool
---

## FMI support for Overture

The support for FMI in Overture is based on the Crescendo Tool and an automated export is avaliable when annotating the specification with FMI specific information.

The entry point used by the FMU wrapper is: `new World().run()` so make sure it is present on export.

* Note that FMUs running **VDM require variable step size**. If a fixed step size is selected then it may introduce errors. Thus if fixed stepsize is selected make sure that the interval is close to that of the control loop. (Internally VDM runs with nano seconds resolution where each expression is assigned a time cost)*

Overture (VDM) specification can be annotated with interface annotations allowing the modeller to specify which *values* should be *parameters*, and which *instance variables* should be *inputs* or *outputs*.

The annotation format is as follows:

```
-- @ interface: type = [input/output/parameter], name="...";
```
it must be located exactly above a value or instance variable.


## Installing the FMI Exporter for Overture

Open Overture and follow these steps:

- 1. Go to `Help->Install New Software...`
- 2. Click `Add...`
- 3. Enter:
 - Name: `Overture FMU`
 - Location: `http://overture.au.dk/into-cps/vdm-tool-wrapper/development/latest`
- 4. Click `Ok`
- 5. Check `Overture FMU Export`
- 6. Click Next / Finish follow the usual stuff to accept and install.


## Updating / Checking for new versions

- 1. Go to `Help->Installation Details
- 2. Select `Overture FMU Export`
- 3. Click `Update...`
- 4. Complete the wizard and restart

# Importing a `ModelDescription.xml` file

- 1. Right click on the project and select `Overture FMU->Import Model Description`

![alt text](OvertureFMU_ctxt.png "Overture FMU")


- 2. Select the model description file
- 3. Check the console for errors

If import is done on a clean project, the following files will be created:

- `System.vdmrt`
- `World.vdmrt`
- `HardwareInterface.vdmrt`

If these files already exist in the project, the `HardwareInterface.vdmrt` will be updated, the import will check for an instance thereof in the system and check for the `run` operation in `World`.


# Exporting an FMU

- 1. Right click on the project and select `Overture FMU->Export FMU`

![alt text](overture-fmi-export-menu.png "Overture FMI Export Menu")


The export fill place a `.fmu` in the project folder on completion and list the export progress in the console as follows: 

```
---------------------------------------
|             FMU Export              |
---------------------------------------
Starting FMU export for project: 'watertankController'
Found annotated definition 'HardwareInterface.minlevel' with type 'parameter' and name 'minlevel'
Found annotated definition 'HardwareInterface.maxlevel' with type 'parameter' and name 'maxlevel'
Found annotated definition 'HardwareInterface.level' with type 'input' and name 'level'
Found annotated definition 'HardwareInterface.valveState' with type 'output' and name 'valveState'
Found system class: 'System'
Setting generation data to: 2016-04-26T15:36:08
```

This is followed by a printout of the `modelDescription.xml` file it generates.


# Annotations

### Parameter Annotations

A parameter annotation can only be used with VDM values as shown here: 

```
values
-- Hardware IO parameters aka - Shared Design Parameters
-- @ interface: type = parameter, name="maxlevel1";
public maxlevel1 : real = 2.0; -- {m}
```
The annotation can be used on any value in any class.

### Input & Output Annotations

An input or output annotation can only be used on instance variables in the `HardwareInterface` class as shown here:


```
system HardwareInterface

-- Hardware IO definitions
instance variables
	
-- @ interface: type = input, name="level1";
    public static upperlevel   : real := 0.0;
 
-- @ interface: type = output, name="valveState1";   
    public static upperValveState : bool := false;
```


## Manual Export

See this page for [manual](overture.html) export.

## Example

The following example is a *WaterTank* controller that seeks to keep the water level in the tank between *min* and *max* by opening and closing a valve. It has a fixed inflow.

Extract from `modelDescription.xml`

```xml
<ScalarVariable name="minlevel" 
				valueReference="0" 
				causality="parameter" 
				variability="fixed" 
				initial="exact">
		<Real start="1.0" />
</ScalarVariable>

<ScalarVariable name="level" 
				valueReference="1" 
				causality="input" 
				variability="continuous">
		<Real start="0.0" />
</ScalarVariable>

<ScalarVariable name="maxlevel" 
				valueReference="2" 
				causality="parameter" 
				variability="fixed" 
				initial="exact">
		<Real start="2.0" />
</ScalarVariable>

<ScalarVariable name="valveState" 
				valueReference="3" 
				causality="output" 
				variability="discrete" 
				initial="calculated">
		<Boolean  />
</ScalarVariable>
```

The `HardwareInterface` as it will be imported or how it should be written manually. Note that the parameters (VDM values) could have been placed in other classes.

```
class HardwareInterface

values
	-- @ interface: type = parameter, name="minlevel";
	public minlevel : real = 1.0;
	-- @ interface: type = parameter, name="maxlevel";
	public maxlevel : real = 2.0;

instance variables
	-- @ interface: type = input, name="level";
	public level : real := 0.0;

instance variables
	-- @ interface: type = output, name="valveState";
	public valveState : bool := false;
	
end HardwareInterface
```

The `World` class, which is just used to start the model

```
class World

operations

public run : () ==> ()
run() ==
 (start(System`controller);
  block();
 );

private block : () ==>()
block() ==
  skip;

sync

  per block => false;

end World
```

The `system` has one special instance variable `hwi`.  This is used to auto link the FMI interface to the VDM model.

```
system System

instance variables

-- Hardware interface variable required by FMU Import/Export
public static hwi: HardwareInterface := new HardwareInterface();
    

instance variables

  public static controller : [Controller] := nil;

	cpu1 : CPU := new CPU(<FP>, 20);
operations

public System : () ==> System
System () == 
(
	let levelSensor   = new LevelSensor(lambda -:bool& hwi.level),
		 valveActuator =  new ValveActuator(lambda x: bool & 
		 				Reflect`setMember(System`hwi,"valveState",x) ) 
	in
		controller := new Controller(levelSensor, valveActuator);

	cpu1.deploy(controller,"Controller");
);

end System
```

Note the trick that's used here in the constructor. It creates function values (think of it as function pointers) for the inputs and outputs such that any object can encapsulate these. 

Why like this? because VDM is by value, in Java or C/C++ we could have parsed references for these but not in VDM. The VDM language only has function values, and since a function has to cannot have side effects, we therefore have to use the `Reflect` class. The `Reflect` class is a Java wrapper that enables side effects in functions. (and for the getter in `LevelSensor` here the type check is just not strong enough to detect this case).

The `Reflect` library can be added through the same context menu as the import/export.

The `LevelSensor` class has a function value as its handle. The parameter is not used but VDM lambdas cannot be declared without a parameter.

```
class LevelSensor

instance variables

handle : bool->real;

operations

public LevelSensor: bool->real ==> LevelSensor
LevelSensor(h) == handle := h;

public getLevel: () ==> real
getLevel()==return handle(true);

end LevelSensor
```

The `ValveActuator` class has a function value as its handle. We don't use the return value thus the don't care in the `let`.

```
class ValveActuator


instance variables

handle : bool->bool;

operations

public ValveActuator: bool->bool ==> ValveActuator
ValveActuator(h) == handle := h;

public setValve: bool ==> ()
setValve(value)==let - = handle(value) in skip;

end ValveActuator
```

Finally for completeness the `Controller`.

```
class Controller
  
instance variables

  levelSensor   : LevelSensor;
  valveActuator : ValveActuator;

operations

public Controller : LevelSensor * ValveActuator  ==> Controller
Controller(l,v)==
 (levelSensor   := l;
  valveActuator := v;
  );
  
values
open : bool = true;
close: bool = false;

operations

private loop : () ==>()
loop()==
	cycles(2)
   (
   
    let level : real = levelSensor.getLevel()
    in
    (
    
    if( level >= HardwareInterface`maxlevel)
    then valveActuator.setValve(open);
    
    if( level <= HardwareInterface`minlevel)
    then valveActuator.setValve(close);
    );
			
    
   );

thread
periodic(10E6,0,0,0)(loop);	 
		 
end Controller
```

<!--
You can download an example archive that makes use of the above annotations [here](cascading-watertank-for-overture-export.zip).

To import it in Overture:

- 1. Goto the `Project Explorer->Import`
- 2. Select `Existing Projects into Workspace`
- 3. Select `Select archiev file` and brows for the downloaded example
- 4. Follow the standard options and finally finish the wizard
-->
