---
layout: default
title: Overview
---




# Simulation Example

To perform a simulation we need the following:

1. A collection of FMU's
2. A COE configuration listing:
 * the path to all FMU's
 * their connections
 * any parameters
 * the step size configuration
3. The COE
4. A suitable tool and language for assisting in calling the COE (we use Shell and curl)

### Fetch FMUs
These FMU's are cross compiles to all supported platforms:

* [automatic build site](http://overture.au.dk/into-cps/examples/fmus/)

Also fetch the COE, see the download page.

### File structure
This is just a proposed file structure, chose what you like.

* coe - place the `coe.jar` here
* fmus - place all FMU's here

### Make the configuration

Create a file named `config.json` with the following content:

```json
{
	"fmus":[
		"{fmu1}":"../fmus/tankcontroller.fmu",
		"{fmu2}":"../fmus/tank.fmu"
	],
	"connections":{
		"{fmu1}.controller.valve":
		    ["{fmu2}.tank.valve"],
		"{fmu2}.tank.level":
		    ["{fmu1}.controller.level"]
	},
	"parameters":{
		"{fmu1}.controller.maxLevel":8,
		"{fmu1}.controller.minLevel":2
	},
	"algorithm":{
		"type":"fixed-step",
		"size":0.1
	}
}

```

Note that the connections is Output to Inputs i.e. a map from String -> Set of String. So here `"a":["b","c"]` means that input `b` and `c` is provided by `a`.

### Perform the simulation

1. Start the COE:

```bash
cd coe
java -jar coe.jar 
```

2. (New terminal, or use &) Initialize the simulation

```bash
curl -s -H "Content-Type: application/json" --data @config.json http://localhost:8082/initialize
```

3. Find the session id in the response
4. Start the simulation

```bash
sessionId=1234
endTime=4
curl -s -H "Content-Type: application/json" --data '{"startTime":0.0, "endTime":'$endTime'}' http://localhost:8082/simulate/$sessionId
```

note that the above json string must be expressed as follows on windows platforms:
```bash
--data "{\"startTime\":0.0, \"endTime\":%endTime%}" 
```


5. Fetch the result

```bash
curl -s http://localhost:8082/result/$sessionId
```







