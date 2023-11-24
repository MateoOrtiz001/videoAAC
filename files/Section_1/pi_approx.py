from manim import *

class CreateText(Scene):

    def construct(self):
        txt = MathTex("\pi")
        self.play(Create(txt))
        self.wait()

        