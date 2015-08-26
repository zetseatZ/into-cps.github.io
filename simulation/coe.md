---
layout: default
title: Overview
---




# COE

### Starting the COE:

1. Download the coe, we call it `coe.jar`
2. Start the COE

```
java -jar coe.jar
```

This will print:

```
Now running on port 8082
Hit Enter to stop.
```

### Obtaining the API documentation

The COE responds to http so simply fetch the API documentation by:

```
curl -o api.pdf http://localhost:8082/api/pdf
```

Now the file api.pdf should be avaliable.




