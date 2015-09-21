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

Download the folowing FMU's

* [tank](http://overture.au.dk/into-cps/test/fmu/tank.fmu)
* [tankcontroller](http://overture.au.dk/into-cps/test/fmu/tankcontroller.fmu)

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
		"../fmus/tankcontroller",
		"../fmus/tank"
	],
	"connections":{
		"{8c4e810f-3df3-4a00-8276-176fa3c9f000}.controller.valve":
		    ["{8c4e810f-3df3-4a00-8276-176fa3c9f001}.tank.valve"],
		"{8c4e810f-3df3-4a00-8276-176fa3c9f001}.tank.level":
		    ["{8c4e810f-3df3-4a00-8276-176fa3c9f000}.controller.level"]
	},
	"parameters":{
		"{8c4e810f-3df3-4a00-8276-176fa3c9f000}.controller.maxLevel":8,
		"{8c4e810f-3df3-4a00-8276-176fa3c9f000}.controller.minLevel":2
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
curl -s -H "Content-Type: application/json" --data config.json http://localhost:8082/initialize
```

3. Find the session id in the response
4. Start the simulation

```bash
sessionId=1234
endTime=4
curl -s -H "Content-Type: application/json" --data '{"startTime":0.0, "endTime":'$endTime'}' http://localhost:8082/simulate/$sessionId
```

5. Fetch the result

```bash
curl -s http://localhost:8082/result/$sessionId
```







