from manim import *

class Iteracion(Scene):
    def construct(self):
        x = self.camera.frame_width/2
        y = self.camera.frame_height/2

        titulo_1 = MathTex(r"\text{Asumamos} $a>b>0$")
        titulo_2 = Tex(r"Sea $a_0 = a$ y $b_0=b0$, definimos la iteración:")
        an1 = MathTex("a_{n+1} = \\frac{1}{2} (a_n + b_n)")
        bn1 = MathTex("b_{n+1} = \\sqrt{a_n b_n}")
        titulo_3 =  MathTex("\\text{Para todo} $n \\in \\N$, a_{n+1} \\geq b_{n+1}$")
        titulo_4 = MathTex("a_n \\geq a_{n+1} \\geq b_{n+1} \\geq b_{n}")
        titulo_5 = Tex("Mientras $n \\rightarrow \\infty$, $(a_n) \\rightarrow L$ y $(b_n) \\rightarrow L$")
        
        agm = MathTex("AG(a,b) = L")
        cn = MathTex("\\sqrt{a_n^2 - b_n^2}")
        titulo_6 = MathTex("\\text{ $(C_n)$ converge cuadráticamente a 0}")
        cn1 = MathTex("c_{n+1} = \\frac{1}{2}(a_n - b_n) = \\frac{c_n^2}{4 a_{n+1}} \\leq \\frac{c_n^2}{4L}")

        titulo_7 = MathTex("\\text{Definamos $a_n$, $b_n$ y $c_n$ para $n$ negativo}")
        anneg = MathTex("a_n = a_{n+1} + c_{n+1}")
        bnneg = MathTex("b_n = a_{n+1} - c_{n+1}")

        #prop1 = MathTex("\\lim_{k \\rightarrow 0^+} \\left[ \\log \\left(\\frac{4}{k} \\right) - I(1,k) \\right] = 0")
        #prop1_a = Tex(r"Denotamos por $\Delta (k) = \log \left(  \frac{4}{k} \right) - I(1, k)$")
        #prop2_a = Tex("\\text{Para $k \in (0, 1]$")
        #prop2 = MathTex("\\lvert \\Delta(k) \\rvert \\leq \\left\\lvert \\log \\left(  \\frac{4}{k} \\right) - I(1, k) \\right\\rvert \\leq 4k^2 I(1,k) \\leq 4k^2 (8 + \\lvert \\log k \\rvert)")
        
        #prop3 = Tex("La AGM satisface la siguiente identidad (Para todos los valores iniciales)")
        #prop3_a = MathTex("\\lim_{n \\rightarrow \\infty} 2^{-n} \\frac{a_n^\\prime}{a_n} \\log \\left( \\frac{4a_n}{c_n} \\right) = \\frac{\\pi}{2}")
        #prop3_b = MathTex("\\text{donde $a_n^{\prime}$ es la sucesión definida como $a_n^{\prime} = 2^{-n} a_{-n}$}")
        
        self.wait(1)
        self.play(Write(titulo_1.move_to([0.5*x,0.5*y,0])),run_time=0.75)
        # self.wait(1)
        # self.play(titulo.animate.move_to([0,0.7*y,0]))
        # self.wait(0.5)
        # self.play(Write(pi_1),run_time=0.75)
        # self.wait(1.4)
        # self.play(Create(comp_box_1),run_time=0.75)
        # self.wait(1)
        # self.play(pi_1.animate.move_to([0,0.3*y,0]),comp_box_1.animate.move_to([0,0.3*y,0]))
        # self.play(Write(pi_2),run_time=0.75)
        # self.wait(1.4)
        # self.play(Create(comp_box_2),run_time=0.75)
        # self.wait(3)
        # self.play(FadeOut(pi_2,comp_box_2),run_time=0.5) #16s
        # self.wait(6)
        
        # pi_1_text = Text("Se puede obtener a partir de: ",font_size=30).move_to([0,-0.1*y,0])
        # pi_1_6 = MathTex("|\\Delta(k) - \\Delta(h)| \\leq 2\\pi |k-h|").move_to([-0.5*x,-0.4*y,0])
        # pi_1_4= MathTex("I(a_0, b_0) = \\frac{\\pi}{2} AG(a_0, b_0)").move_to([0.5*x,-0.4*y,0])
        # pi_1_latex = MathTex("\\text{para $k=10^{-n}$ y $h=10^{-2n}+10n$}").move_to([0,-0.7*y,0])
        
        # self.play(FadeIn(pi_1_text)) #22s 
        # self.wait(1)
        # self.play(FadeIn(pi_1_6))
        # self.wait(1.5)
        # self.play(FadeIn(pi_1_4)) #26s
        # self.wait(7)
        # self.play(FadeIn(pi_1_latex)) #38s
        # self.wait(4)

