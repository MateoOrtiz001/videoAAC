from manim import *

class pi_change_circle(Scene):

    def construct(self):
        pi = MathTex("\pi")
        self.add(pi)
        self.wait()

        transform_title1 = Tex("Aproximaciones de $\pi$")
        transform_title1.to_corner(UP+ LEFT)
        self.play(
            Transform(pi, transform_title1)
        )
        self.wait()