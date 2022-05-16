# bc_engine   ʕ •ᴥ•ʔゝ□
A [ursina](https://github.com/pokepetter/ursina) fork for my [Backrooms](https://github.com/Chateauvisionn/The-Backrooms) game.

## Getting Started
1) Install Python 3.7 or newer. https://www.python.org/downloads/
2) Open cmd/terminal and type:

```
pip install git+https://github.com/Chateauvisionn/bc_engine.git
```


If you want to easily edit the source, it's recommended to clone the git
repo and install as develop like this. Make sure you have git installed. https://git-scm.com/

```
git clone https://github.com/Chateauvisionn/bc_engine.git
python setup.py develop
```

On some systems you might have to use pip3 instead of pip in order to use Python 3 and not the old Python 2.


## Dependencies
  * python 3.7+
  * panda3d
  * screeninfo, for detecting screen resolution
  * pillow, for texture manipulation
  * psd-tools, for converting .psd files
  * blender, for converting .blend files
  * pyperclip, for copy/pasting


## Project Structure

```
📁bc_engine                # the actual bc_engine module.
    📁audio                 # built-in audio clips.
    📁editor                # the 3d level editor for bc_engine.
    📁fonts                 # built-in fonts.
    📁models                # .blend files, source files, for built-in 3d models.
        📁procedural            # classes for generating 3d models, like Cylinder, Quad and Terrain.
    📁models_compressed     # .blend files converted to .ursinamesh.
    📁prefabs               # higher level classes like Draggable, Slider, Sprite, etc.

    📃__init__.py
    📃application.py
    📃audio.py
    ...
        # bc_engine base modules, like code for Entity, input_handler, Text, window and so on.
```
