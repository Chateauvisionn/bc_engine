# do imports here so I can do a single line import
import sys
from pathlib import Path
from textwrap import dedent
import time
import random
from copy import copy, deepcopy
from math import floor, ceil, inf

from bc_engine.window import instance as window
from bc_engine.camera import instance as camera
from bc_engine.mouse import instance as mouse
from bc_engine.main import Ursina
from bc_engine.ursinamath import *
from bc_engine.ursinastuff import *
from bc_engine import input_handler
from bc_engine.input_handler import held_keys, Keys
from bc_engine.string_utilities import *
from bc_engine.mesh_importer import load_model, load_blender_scene
from bc_engine.texture import Texture
from bc_engine.texture_importer import load_texture
from bc_engine import color
from bc_engine.color import Color, hsv, rgb
from bc_engine.sequence import Sequence, Func, Wait
from bc_engine.entity import Entity
from bc_engine.collider import *
from bc_engine.raycaster import raycast, boxcast
from bc_engine.trigger import Trigger
from bc_engine.audio import Audio
from bc_engine.duplicate import duplicate
from panda3d.core import Quat
from bc_engine.vec2 import Vec2
from bc_engine.vec3 import Vec3
from bc_engine.vec4 import Vec4
from bc_engine.shader import Shader
from bc_engine.lights import *

from bc_engine.text import Text
from bc_engine.mesh import Mesh, MeshModes

from bc_engine.prefabs.sprite import Sprite
from bc_engine.prefabs.button import Button
from bc_engine.prefabs.panel import Panel
from bc_engine.prefabs.animation import Animation
from bc_engine.prefabs.frame_animation_3d import FrameAnimation3d
from bc_engine.prefabs.animator import Animator
from bc_engine.prefabs.sky import Sky
from bc_engine.prefabs.cursor import Cursor

from bc_engine.models.procedural.quad import Quad
from bc_engine.models.procedural.plane import Plane
from bc_engine.models.procedural.circle import Circle
from bc_engine.models.procedural.pipe import Pipe
from bc_engine.models.procedural.cone import Cone
from bc_engine.models.procedural.cube import Cube
from bc_engine.models.procedural.cylinder import Cylinder
from bc_engine.models.procedural.grid import Grid
from bc_engine.models.procedural.terrain import Terrain

from bc_engine.scripts.terraincast import terraincast
from bc_engine.scripts.smooth_follow import SmoothFollow
from bc_engine.scripts.position_limiter import PositionLimiter
from bc_engine.scripts.noclip_mode import NoclipMode, NoclipMode2d
from bc_engine.scripts.grid_layout import grid_layout
from bc_engine.scripts.scrollable import Scrollable
from bc_engine.scripts.colorize import get_world_normals

from bc_engine.prefabs.tooltip import Tooltip
from bc_engine.prefabs.text_field import TextField
from bc_engine.prefabs.input_field import InputField, ContentTypes
from bc_engine.prefabs.draggable import Draggable
from bc_engine.prefabs.slider import Slider, ThinSlider
from bc_engine.prefabs.button_group import ButtonGroup
from bc_engine.prefabs.window_panel import WindowPanel, Space
from bc_engine.prefabs.button_list import ButtonList
from bc_engine.prefabs.file_browser import FileBrowser
# from ursina.prefabs import primitives

from bc_engine.prefabs.debug_menu import DebugMenu
from bc_engine.prefabs.editor_camera import EditorCamera
from bc_engine.prefabs.hot_reloader import HotReloader
