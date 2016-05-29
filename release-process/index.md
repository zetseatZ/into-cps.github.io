---
layout: default
title: Release Process
---

# Release Process
The INTO-CPS release process is quite simple. The new INTO-CPS App supports downloading the various tools and the download URLs are all looked up on the release site.

## Note to tool suppliers
The download URLs are public so in case of non-free you might want to take this fact into consideration.

## Release JSON format
The first file that is looked up by the download manager part of the INTO-CPS App is simple JSON file listing all currently available INTO-CPS. I might look something like this.

```
{
    "0.0.6": "http://overture.au.dk/into-cps/site/download/0.0.6.json",
    "0.0.5": "http://overture.au.dk/into-cps/site/download/0.0.5.json"
}
```

Each specific version JSON contains all the relevant information about each tool, and has the following format:
```
{
    "version": "<INTO_CPS_VERSION>",
    "tools": {
        "<SHORT_TOOL_NAME>": {
            "name": "<FULL_TOOL_NAME>",
            "version": "<TOOL_VERSION>",
            "description": "<TOOL_DESCRIPTION>",
            "platforms": {
                "PLATFORM": {
                    "url": "<TOOL_DOWNLOAD_URL>",
                    "filename": "<FILE_NAME>",
                    "md5sum": "<MD5_SUM>",
                    "action": "<INSTALLATION_ACTION>"
                },
                ...
            }
        },
        ...
    }
}
```

* INTO_CPS_VERSION: The INTO-CPS release version.
* SHORT_TOOL_NAME: A short form of the tool name.
* FULL_TOOL_NAME: The full name of the tool.
* TOOL_VERSION: The tool version.
* PLATFORM: One of: linux32, linux64, windows32, windows64, osx
* TOOL_DOWNLOAD_URL: The tool download URL
* FILE_NAME: The file name of the file the TOOL_DOWNLOAD_URL points to. The file name is not necessarily part of the URL and badly configured sites might not include the name in the header.
* MD5_SUM: The md5sum of the tool installation file.
* INSTALLATION_ACTION: One of: unpack, launch. *unpack* means that file being downloaded is expected to be a zip-file and it well get unpacked into a selected installation directory. *launch* means that the file being downloaded is an executable that simple needs to be launched in order to start the installation.


### Example
```
{
    "version": "0.0.6",
    "tools": {
        "20sim": {
            "name": "20-sim",
            "version": "4.5.4b6171-2015-09-28",
            "description": "Modeling and simulation tool",
            "platforms": {
                "windows32": {
                    "url": "https://dl.dropboxusercontent.com/u/7249985/controllab/20sim/20-sim-4.6.1.6846-intocps-win32.exe",
                    "filename": "20-sim-4.6.1.6846-intocps-win32.exe",
                    "md5sum": "3dbfd82ebf80499ac9ca5d5ffb53a06b",
                    "action": "launch"
                },
                "windows64": {
                    "url": "https://dl.dropboxusercontent.com/u/7249985/controllab/20sim/20-sim-4.6.1.6846-intocps-win32.exe",
                    "filename": "20-sim-4.6.1.6846-intocps-win32.exe",
                    "md5sum": "3dbfd82ebf80499ac9ca5d5ffb53a06b",
                    "action": "launch"
                }
            }
        },
        "20sim4c": {
            "name": "20-sim 4C",
            "version": "2.1.9-2016-02-19",
            "description": "Tool for rapid prototyping for control engineers",
            "platforms": {
                "windows32": {
                    "url": "http://www.20sim.com/downloads/files/20sim4C.exe",
                    "filename": "20sim4C.exe",
                    "md5sum": "02c2fea66e5fa63f50565b4140b36385",
                    "action": "launch"
                },
                "windows64": {
                    "url": "http://www.20sim.com/downloads/files/20sim4C.exe",
                    "filename": "20sim4C.exe",
                    "md5sum": "02c2fea66e5fa63f50565b4140b36385",
                    "action": "launch"
                }
            }
        },
        "open-modelica": {
            "name": "Open Modelica",
            "version": "1.10.0-dev-440-gd0581ff",
            "description": "A Modelica-based modelling and simulation tool",
            "platforms": {
                "windows32": {
                    "url": "https://build.openmodelica.org/omc/builds/windows/nightly-builds/32bit/OpenModelica-v1.10.0-dev-440-gd0581ff-32bit.exe",
                    "filename": "OpenModelica-v1.10.0-dev-440-gd0581ff-32bit.exe",
                    "md5sum": "181419521e377f88bfc33b26797301ac",
                    "action": "launch"
                },
                "windows64": {
                    "url": "https://build.openmodelica.org/omc/builds/windows/nightly-builds/64bit/OpenModelica-v1.10.0-dev-440-gd0581ff-64bit.exe",
                    "filename": "OpenModelica-v1.10.0-dev-440-gd0581ff-64bit.exe",
                    "md5sum": "0eda2c3972b2ab7399cd5234c504a990",
                    "action": "launch"
                }
            }
        },
        "modelio": {
            "name": "Modelio",
            "version": "3.4.1",
            "description": "UML/BPMN modelling tool",
            "platforms": {
                "windows32": {
                    "url": "https://www.modelio.org/modelio-download-archive/doc_download/117-modelio-341-windows-32-bit.html",
                    "filename": "modelio-open-201512081403-win32.win32.x86.zip",
                    "md5sum": "180c744b0bffd064dc349b1035ccb1ca",
                    "action": "launch"
                },
                "windows64": {
                    "url": "https://www.modelio.org/modelio-download-archive/doc_download/116-modelio-341-windows-64-bit.html",
                    "filename": "modelio-open-201512081403-win32.win32.x86_64.zip",
                    "md5sum": "fc2d84672ca45670b72185b1c044341a",
                    "action": "launch"
                }
            }
        },
        "rttester-dependencies": {
            "name": "VSI tools dependencies bundle",
            "version": "0.0.6",
            "description": "VSI tools dependencies: Python 2.7 and GCC 4.9",
            "platforms": {
                "windows32": {
                    "url": "https://secure.verified.de/f5x1hks4/into-cps/one-click/install_Python27_gcc49.exe",
                    "filename": "install_Python27_gcc49.exe",
                    "md5sum": "680950d6c176ef3718243cf201c2d66a",
                    "action": "launch"
                },
                "windows64": {
                    "url": "https://secure.verified.de/f5x1hks4/into-cps/one-click/install_Python27_gcc49.exe",
                    "filename": "install_Python27_gcc49.exe",
                    "md5sum": "680950d6c176ef3718243cf201c2d66a",
                    "action": "launch"
                }
            }
        },
        "rttester": {
            "name": "VSI tools",
            "version": "0.0.6",
            "description": "RT-Tester and examples bundle",
            "platforms": {
                "windows32": {
                    "url": "https://secure.verified.de/f5x1hks4/into-cps/one-click/VSI_bundle.exe",
                    "filename": "VSI_bundle.exe",
                    "md5sum": "0fe36e2b7427dbc2512a35e9ad618f4b",
                    "action": "launch"
                },
                "windows64": {
                    "url": "https://secure.verified.de/f5x1hks4/into-cps/one-click/VSI_bundle.exe",
                    "filename": "VSI_bundle.exe",
                    "md5sum": "0fe36e2b7427dbc2512a35e9ad618f4b",
                    "action": "launch"
                }
            }
        },
        "overture": {
            "name": "Overture",
            "version": "2.3.4",
            "description": "A tool for modelling control systems using The Vienna Development Method (VDM)",
            "platforms": {
                "windows32": {
                    "url": "https://github.com/overturetool/overture/releases/download/Release/2.3.4/Overture-2.3.4-win32.win32.x86.zip",
                    "filename": "Overture-2.3.4-win32.win32.x86.zip",
                    "md5sum": "884adf03b8e90ec3af7e8144b66e57e6",
                    "action": "unpack"
                },
                "windows64": {
                    "url": "https://github.com/overturetool/overture/releases/download/Release/2.3.4/Overture-2.3.4-win32.win32.x86_64.zip",
                    "filename": "Overture-2.3.4-win32.win32.x86_64.zip",
                    "md5sum": "54e9063b44a6b5805ace61c580aa1f84",
                    "action": "unpack"
                }
            }
        },
        "overtureToolWrapper": {
            "name": "Overture Tool Wrapper",
            "description": "Overture/VDM Tool Wrapper",
            "version": "2016-03-01T22:28",
            "platforms": {
                "linux32": {
                    "url": "http://overture.au.dk/into-cps/vdm-tool-wrapper/development/Build-87_2016-03-01_22-28/vdm-tool-wrapper.zip",
                    "filename": "vdm-tool-wrapper.zip",
                    "md5sum": "d1a2270404f4b5c6a4e515549fb488ca",
                    "action": "unpack"
                },
                "linux64": {
                    "url": "http://overture.au.dk/into-cps/vdm-tool-wrapper/development/Build-87_2016-03-01_22-28/vdm-tool-wrapper.zip",
                    "filename": "vdm-tool-wrapper.zip",
                    "md5sum": "d1a2270404f4b5c6a4e515549fb488ca",
                    "action": "unpack"
                },
                "windows32": {
                    "url": "http://overture.au.dk/into-cps/vdm-tool-wrapper/development/Build-87_2016-03-01_22-28/vdm-tool-wrapper.zip",
                    "filename": "vdm-tool-wrapper.zip",
                    "md5sum": "d1a2270404f4b5c6a4e515549fb488ca",
                    "action": "unpack"
                },
                "windows64": {
                    "url": "http://overture.au.dk/into-cps/vdm-tool-wrapper/development/Build-87_2016-03-01_22-28/vdm-tool-wrapper.zip",
                    "filename": "vdm-tool-wrapper.zip",
                    "md5sum": "d1a2270404f4b5c6a4e515549fb488ca",
                    "action": "unpack"
                },
                "osx64": {
                    "url": "http://overture.au.dk/into-cps/vdm-tool-wrapper/development/Build-87_2016-03-01_22-28/vdm-tool-wrapper.zip",
                    "filename": "vdm-tool-wrapper.zip",
                    "md5sum": "d1a2270404f4b5c6a4e515549fb488ca",
                    "action": "unpack"
                }
            }
        }
    }
}
```
