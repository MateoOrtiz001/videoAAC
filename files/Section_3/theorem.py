from manim import *

class section_3(Scene):

    def construct(self):

        main_thm = Tex("Teorema central sección 3")
        main_thm.to_corner(UP + LEFT)
        self.play( Write(main_thm) )

        pref1 = Tex(r"Sea $Q_n$ y $P_n$ definidas:").scale(0.7)
        pref1.move_to(LEFT*2 + UP*2)
        self.play(Write(pref1))

        eq1 = MathTex(r"P_n (k) = \left(  \frac{4 a_n}{c_n} \right)^{2^{1-n}}")
        eq1.move_to(LEFT*2 + UP)
        self.play(Write(eq1))
        
        eq2 = MathTex(r"Q_n (k) = \frac{a_n}{a_n^{\prime}  }").scale(0.7)
        eq2.move_to(RIGHT*2 + UP)
        self.play(Write(eq2))

        pref2 = Tex(r"tal que $P(k) = \lim_{n \rightarrow \infty} P_n(k)$, $Q(k) = \lim_{n \rightarrow \infty} Q_n(k)$, $a = \lim_{n \rightarrow \infty} a_n$ y $a^{\prime} = \lim_{n \rightarrow \infty} a_n^{\prime}$. Al menos una se tiene:").scale(0.7)
        pref2.move_to(DOWN*0.5)
        self.play(Write(pref2))

        equiva = Tex(r"a) $P(k) = e^{\pi Q(k)}$").scale(0.7)
        equivb = Tex(r"b) $0 \leq P_n(k) - P(k) \leq \frac{16}{1-k^2} \left( \frac{a_n - a}{a} \right)$").scale(0.7)
        equivc = Tex(r"c) $ \lvert Q_n(k) - Q(k) \leq  \frac{ a^{\prime} \lvert a - a_n \rvert + a \lvert a^{\prime} - a_n^{\prime} \rvert }{(a^{\prime})^2} \rvert $").scale(0.7)
        
        equiva.move_to(DOWN*1.25)
        equivb.move_to(DOWN*1.8)
        equivc.move_to(DOWN*2.35)

        self.play(Write(equiva), Write(equivb), Write(equivc))

        self.wait(3)
