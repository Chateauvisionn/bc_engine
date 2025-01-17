from bc_engine import *
from bc_engine.prefabs.button import Button
from bc_engine.models.procedural.quad import Quad

class Panel(Entity):

    def __init__(self, **kwargs):
        super().__init__()
        self.parent = camera.ui
        self.model = Quad()
        self.color = Button.color

        for key, value in kwargs.items():
            setattr(self, key, value)

if __name__ == '__main__':
    app = Ursina()
    p = Panel()
    app.run()
