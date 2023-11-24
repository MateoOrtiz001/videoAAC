from manim import *

class section_3(Scene):

    def construct(self):
        conv_cuad_exp = Tex("Convergencia Cuadrática / Exponencial").scale(1.5)
        conv_cuad_exp.move_to(UP*2)

        conv_cuad = MathTex(r"\lvert a_{n+1} - L \rvert \leq c_1 \lvert a_n - L \rvert^2")
        conv_cuad.move_to(DOWN*0.5)
        conv_exp = MathTex(r"\lvert a_{n} - L \rvert \leq c_2^{-2^n}")
        conv_exp.move_to(DOWN*2)

        self.play( Write(conv_cuad_exp), FadeIn(conv_cuad, shift=DOWN) )
        self.wait(15)
        self.play( FadeIn(conv_exp, shift=DOWN) )
        self.wait(10)