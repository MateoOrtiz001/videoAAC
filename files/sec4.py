from manim import *

class Aproximacion_pi_1(Scene):
    def construct(self):
        x = self.camera.frame_width/2
        y = self.camera.frame_height/2

        titulo = MathTex("\\text{Otras formas de aproximar $\pi$ usando AGM}",font_size=70)
        pi_1 =  MathTex("\\left| \\frac{2}{\\pi} - \\left[ \\frac{10^n}{AG(1,10^{-n})}-\\frac{10^n}{AG(1,10^{-n}+10^{-2n})}\\right]\\right| \\leq 10^{1-n}")
        comp_box_1 = SurroundingRectangle(pi_1, buff=0.3)
        pi_2 = MathTex("\\pi = \\frac{\\left[ 2AG(1,2^{-\\frac{1}{2}})\\right]^2}{1-\\sum_{n=1}^{\\infty} 2^{n+1}c_n^2}").move_to([0,-0.3*y,0])
        comp_box_2 = SurroundingRectangle(pi_2, buff=0.3)
        
        self.wait(1)
        self.play(Write(titulo),run_time=0.75)
        self.wait(1)
        self.play(titulo.animate.move_to([0,0.7*y,0]))
        self.wait(0.5)
        self.play(Write(pi_1),run_time=0.75)
        self.wait(1.4)
        self.play(Create(comp_box_1),run_time=0.75)
        self.wait(1)
        self.play(pi_1.animate.move_to([0,0.3*y,0]),comp_box_1.animate.move_to([0,0.3*y,0]))
        self.play(Write(pi_2),run_time=0.75)
        self.wait(1.4)
        self.play(Create(comp_box_2),run_time=0.75)
        self.wait(3)
        self.play(FadeOut(pi_2,comp_box_2),run_time=0.5) #16s
        self.wait(6)
        
        pi_1_text = Text("Se puede obtener a partir de: ",font_size=30).move_to([0,-0.1*y,0])
        pi_1_6 = MathTex("|\\Delta(k) - \\Delta(h)| \\leq 2\\pi |k-h|").move_to([-0.5*x,-0.4*y,0])
        pi_1_4= MathTex("I(a_0, b_0) = \\frac{\\pi}{2} AG(a_0, b_0)").move_to([0.5*x,-0.4*y,0])
        pi_1_latex = MathTex("\\text{para $k=10^{-n}$ y $h=10^{-2n}+10n$}").move_to([0,-0.7*y,0])
        
        self.play(FadeIn(pi_1_text)) #22s 
        self.wait(1)
        self.play(FadeIn(pi_1_6))
        self.wait(1.5)
        self.play(FadeIn(pi_1_4)) #26s
        self.wait(7)
        self.play(FadeIn(pi_1_latex)) #38s
        self.wait(4)

        grafica = xfunction().scale(0.5).move_to([-0.4*x,-0.5*y,0])
        self.play(FadeOut(pi_1_text, pi_1_6, pi_1_4, pi_1_latex))
        self.wait(3) 
        self.play(FadeIn(grafica),run_time=2) #46s
        self.wait(9)

        pi_1_bigo = MathTex("O(n)").move_to([0.4*x,-0.5*y,0])
        self.play(FadeIn(pi_1_bigo)) #54s
        self.wait(2)
        self.play(FadeOut(pi_1_bigo,grafica,pi_1,comp_box_1))
        self.wait(0.5)

class Aproximacion_pi_2(Scene):
    def construct(self):
        x = self.camera.frame_width/2
        y = self.camera.frame_height/2

        titulo = MathTex("\\text{Otras formas de aproximar $\pi$ usando AGM}",font_size=70).move_to([0,0.7*y,0])
        pi_2 = MathTex("\\pi = \\frac{\\left[ 2AG(1,2^{-\\frac{1}{2}})\\right]^2}{1-\\sum_{n=1}^{\\infty} 2^{n+1}c_n^2}").move_to([0,-0.3*y,0])
        comp_box_2 = SurroundingRectangle(pi_2, buff=0.3)

        self.add(titulo)
        self.wait(1)
        self.play(Write(pi_2))
        self.wait(1.4)
        self.play(Create(comp_box_2))
        self.wait(1)
        self.play(pi_2.animate.move_to([0,0.3*y,0]),comp_box_2.animate.move_to([0,0.3*y,0]))
        self.wait(1)

        image_path1 = "img/Brent.jpg"
        image_path2 = "img/Salamin.jpg"

        # Crear un objeto de imagen a partir de la ruta
        image_Brent= ImageMobject(image_path1).move_to([0.2*x,-0.4*y,0])
        image_Brent.scale(0.5)
        brent = Text("Richard Brent",font_size=20).next_to(image_Brent, DOWN)

        image_Salamin = ImageMobject(image_path2).move_to([-0.2*x,-0.4*y,0])
        salamin = Text("Eugene Salamin",font_size=20).next_to(image_Salamin, DOWN)

        self.play(FadeIn(image_Salamin,salamin)) #8s
        self.wait(0.3)
        self.play(FadeIn(image_Brent,brent))
        self.wait(7)
        self.play(FadeOut(image_Salamin,salamin,image_Brent,brent))
        self.wait(1)

        pi_1_text = Text("Se puede obtener a partir de: ",font_size=30).move_to([0,-0.1*y,0])
        legendre_text = Text("relación de legendre:",font_size=30).move_to([0,-0.4*y,0])
        legendre = MathTex("I(1,k)J(1,k') + I(1,k')J(1,k) - I(1,k)I(1,k') = \\frac{\\pi}{2}").move_to([0,-0.6*y,0])
        pi_2_j = MathTex("J(a,b) := \\int_{0}^{\\frac{\\pi}{2}} \\sqrt{a^2\\cos^2\\theta + b^2\\sin^2\\theta} \\, d\\theta").move_to([0,-0.65*y,0])
        pi_2_elipticas = MathTex("J(a_0,b_0) = \\left( a_0^2-\\frac{1}{2}\\sum_{n=0}^{\\infty} 2^nc_n^2\\right)I(a_0,b_0)").move_to([0,-0.7*y,0])
        pi_2_igualdad = MathTex("\\text{donde $c_n^2 = a_n^2- b_n^2$").move_to([-0.5*x,-0.65*y,0])
        pi_2_condicion = MathTex("\\text{y tomando $k=2^{-\\frac{1}{2}}$ y $k'=k$}").move_to([-0.5*x,-0.8*y,0])
    
        

        self.play(FadeIn(pi_1_text)) #17s
        self.wait(0.7)
        self.play(FadeIn(legendre_text))
        self.wait(0.3)
        self.play(FadeIn(legendre))
        self.wait(1.5)
        self.play(legendre.animate.scale(0.6).move_to([-0.5*x,-0.4*y,0]),legendre_text.animate.scale(0.7).move_to([-0.5*x,-0.3*y,0]))
        self.wait(0.5)
        self.play(FadeIn(pi_2_j))
        self.wait(3)
        self.play(pi_2_j.animate.scale(0.6).move_to([0.5*x,-0.4*y,0]))
        self.wait(0.4)
        self.play(FadeIn(pi_2_elipticas))
        self.wait(1.6)
        self.play(pi_2_elipticas.animate.scale(0.6).move_to([0.5*x,-0.7*y,0]))
        self.wait(1)
        self.play(FadeIn(pi_2_igualdad))
        self.wait(4)
        self.play(FadeIn(pi_2_condicion))
        self.wait(3)
        self.play(FadeOut(titulo,pi_2_condicion,pi_1_text,pi_2,pi_2_elipticas,pi_2_igualdad,pi_2_j,legendre,legendre_text,comp_box_2))
        self.wait(1)


def xfunction():
    axes = Axes(
        x_range=[0, 10, 1],
        y_range=[0, 20, 2],
        axis_config={"color": GREEN},
        x_axis_config={
            "numbers_to_include": list(range(0, 11, 2)),
            "numbers_with_elongated_ticks": list(range(0, 11, 2)),
        },
        y_axis_config={
            "numbers_to_include": list(range(0, 20, 4)),
            "numbers_with_elongated_ticks": list(range(0, 20, 4)),
        },
        tips=False,
    )
    axes_labels = axes.get_axis_labels(x_label="n", y_label="Operaciones")
    graph = axes.plot(lambda n: 2*n, color=BLUE)

    fn_label = axes.get_graph_label(
        graph, "f(n)=2n", x_val=5, direction=2*UP
    )

    plot = VGroup(axes, graph)
    labels = VGroup(axes_labels, fn_label)
    
    return VGroup(plot, labels)

