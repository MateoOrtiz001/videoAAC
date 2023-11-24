from manim import *

class section_3(Scene):

    def construct(self):
        
        Elliptic_Integral = Tex("Integrales Elípticas").scale(1.5)
        Elliptic_Integral.to_corner(LEFT + UP)

        self.play(Write(Elliptic_Integral))
        self.wait()

        Def_EllipticInt = Tex("Para $R$ función racional, y $P$ un polinomio sin raíces repetidas, una función elíptica es una expresión de la forma:").scale(0.7)
        Def_EllipticInt.move_to(UP*1.5)

        self.play( Write(Def_EllipticInt) )

        eq_Elliptic = MathTex("f(x) = \int_c^x R(t, P(t)) dt")
        
        self.play(Write(eq_Elliptic))
        self.wait()