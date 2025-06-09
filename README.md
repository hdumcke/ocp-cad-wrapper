# ocp-cad-wrapper

*This is a very early version under development*

## Installation

Create a Python virtual environment and run

```
  pip install git+https://github.com/hdumcke/ocp-cad-wrapper.git
```

## Run

Open a terminal session, activate your Python virtual environment and run OCP CAD Viewer in stand alonne mode:

```
  python -m ocp_vscode
```

Open a new terminal session, activate your Python virtual environment and run OCP CAD Wrapper:

```
  wrapper <filename>
```

You can now edit <filename> with your favorite editor. Each time you save the file OCP CAD Viewer will be refreshed

## Run with screen

The tools directory contains two scripts that uses screen to start all session in the background. The script in it's current state has the location of the Python virtual environment hard coded as ~/.virtualenvs/build123d

Copy these two scripts into your execution path (like /usr/local/bin for example)

Example session:

```
  # start processes in background
  wrapper_start.sh <path to build123d file>
  # edit <path to build123d file> and save to disk. Each time you save the web page with the rendering will be refreshed
  # to tear down the environment
  wrapper_stop.sh
  
