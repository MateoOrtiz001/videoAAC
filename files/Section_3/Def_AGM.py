from manim import *

class section_3(Scene):

    def construct(self):
        conv_cuad_exp = Tex("Convergencia Cuadrática / Exponencial").scale(1.5)
        conv_cuad_exp.move_to(UP*2)

        conv_cuad = MathTex(r"\lvert a_{n+1} - L \rvert \leq c_1 \lvert a_n - L \rvert^2")
        conv_cuad.move_to(DOWN*0.5)
        conv_exp = MathTex(r"\lvert a_{n} - L \rvert \leq c_2^{-2^n}")
        conv_exp.move_to(DOWN*2)

        self.add(conv_exp, conv_cuad, conv_cuad_exp)

        self.play( FadeOut(conv_cuad_exp, conv_cuad, conv_exp,shift=UP))
        self.wait()

        AGM = Tex("Desigualdad AGM (Arithmetic-Geometric Mean)").scale(1.2)
        AGM.move_to(UP*2)
        
        Desq_AGM = Tex(R"Dados $x,y \in \mathbb{Z}^+$, tendremos")
        Desq_AGM.move_to(UP).scale(0.7)
        desq_Eq = MathTex(r"\frac{x + y}{2} \geq \sqrt{xy}").scale(0.7)

        self.play(Write(AGM))
        self.play(Write(Desq_AGM))
        self.play(Write(desq_Eq))
        self.wait()