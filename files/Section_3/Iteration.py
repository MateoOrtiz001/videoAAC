from manim import *

class section_3(Scene):

    def construct(self):
        
        Elliptic_Integral = Tex("Integrales Elípticas").scale(1.5)
        Elliptic_Integral.to_corner(LEFT + UP)
        Def_EllipticInt = Tex("Para $R$ función racional, y $P$ un polinomio sin raíces repetidas, una función elíptica es una expresión de la forma:").scale(0.7)
        Def_EllipticInt.move_to(UP*1.5)
        eq_Elliptic = MathTex("f(x) = \int_c^x R(t, P(t)) dt")
        
        self.add(Elliptic_Integral, Def_EllipticInt, eq_Elliptic)
        self.wait()
        self.play(FadeOut(Elliptic_Integral, Def_EllipticInt, eq_Elliptic))
        self.wait()

        iter_a = MathTex(r"a_{n+1} = \frac{1}{2}(a_n + b_n)").scale(0.7)
        iter_b = MathTex(r"b_{n+1} = \sqrt{a_n b_n}").scale(0.7)

        iter_a.move_to(LEFT*2 + UP*2)
        iter_b.move_to(RIGHT*2 + UP*2)



        self.play(Write(iter_a))
        self.play(Write(iter_b))

        self.wait(10)

        text_AGM1 = Tex(r"Por la desigualdad de la medio geométrica aritmética, tenemos que $a_{n+1} \geq b_{n+1}$, y en general $a_n \geq a_{n+1} \geq b_{m+1} \geq b_m$. Así, las sucesiones $(a_n)$ y $(b_n)$ tienden a un mismo valor, denotado, $AG(a,b)$").scale(0.7)    
        text_AGM1.move_to(UP*0.8)
        self.play(Write(text_AGM1))
        self.wait(5)

        limit_an = Tex(r"Observar límite de $(a_n)$ :").scale(0.7)
        integral_elliptic = MathTex(r"I(a,b) = \int_0^{\frac{\pi}{2}} \frac{d \theta}{\sqrt{ a^2 \cos^2 \theta + b^2 \sin^2 \theta }} ").scale(0.7)
        limit_an.move_to(LEFT*2.5 + DOWN)
        integral_elliptic.move_to(RIGHT*2.5 + DOWN)
        self.play( Write(limit_an), Write(integral_elliptic) )
        self.wait(10)