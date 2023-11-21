from manim import *
import numpy as np

class Teorema2(Scene):
    def construct(self):
        # Definir objetos matemáticos iniciales
        alpha_n = MathTex("\\alpha_n").move_to(LEFT)
        beta_n = MathTex("\\beta_n")
        pi_n = MathTex("\\pi_n").move_to(RIGHT)
        teorema = Text("Teorema 2.",slant=ITALIC).to_edge(UP)

        # Mostrar objetos iniciales
        self.play(Write(teorema),Write(alpha_n), Write(beta_n), Write(pi_n))
        self.wait(1)

        # Transformación 1
        self.play(Transform(alpha_n, MathTex("\\alpha_0=\\sqrt{2}").shift(3 * LEFT)),
                  Transform(beta_n, MathTex("\\beta_0=0")),
                  Transform(pi_n, MathTex("\\pi_0=2+\\sqrt{2}").shift(3 * RIGHT)))
        self.wait(1)

        # Transformación 2
        self.play(Transform(alpha_n, MathTex("\\alpha_n = \\frac{1}{2}\\left( \\alpha_{n-1}^{1/2} + \\alpha_{n-1}^{-1/2} \\right)").shift(1.6*UP+ 2*LEFT)),
                  Transform(beta_n, MathTex("\\beta_n = \\alpha_{n-1}^{1/2}\\left( \\frac{\\beta_{n-1}+1}{ \\beta_{n-1} + \\alpha_{n-1}} \\right)").shift(2*LEFT)),
                  Transform(pi_n, MathTex("\\pi_n = \\pi_{n-1}\\beta_n \\left( \\frac{1+\\alpha_n}{1+\\beta_n} \\right)").shift(1.6*DOWN+2*LEFT)))
        self.wait(1)

        error = Text("Además", font_size=30).move_to(3*RIGHT)
        error2 = MathTex("| \\pi - \\pi_n | \\leq \\frac{1}{10^{2^n}}}").move_to(3.25*RIGHT+1.1*DOWN)
        convergencia = MathTex("\\pi_n \\longrightarrow \\pi").move_to(3*RIGHT+1.1*UP)
        self.play(Write(convergencia))

        self.wait(1)
        convergencia_box = SurroundingRectangle(convergencia, buff=0.3)
        self.play(Create(convergencia_box))
        self.wait(1)

        self.play(Write(error),Write(error2))
        # Mostrar la escena final
        self.wait(3)
