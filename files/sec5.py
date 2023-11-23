from manim import *
import numpy as np

class Previo(Scene):
    def construct(self):
        # Ruta de la imagen (puedes cambiarla por la ruta de tu propia imagen)
        image_path1 = "img/PETER1SMALL.png"
        image_path2 = "img/jborwein.jpg"

        # Crear un objeto de imagen a partir de la ruta
        imageJB = ImageMobject(image_path2).move_to(2.8*LEFT)
        #imageJB.scale(0.5)
        jonatan = Text("Jonatan Borwein",font_size=20).next_to(imageJB, DOWN)

        imagePB = ImageMobject(image_path1).next_to(imageJB)
        imagePB.scale(0.5)
        peter = Text("Peter Borwein",font_size=20).next_to(imagePB, DOWN)

        # Añadir la imagen a la escena
        self.wait(1)
        self.add(imageJB,imagePB)
        self.play(Write(peter),Write(jonatan))

        # Mostrar la escena
        self.wait(2)

        self.play(
            imageJB.animate.shift( 2.8 * LEFT),
            imagePB.animate.shift( 2.8 * LEFT),
            jonatan.animate.shift( 2.8 * LEFT),
            peter.animate.shift( 2.8 * LEFT),
        )
        self.wait(1)
        formula = MathTex("\\pi = \\frac{\\left[2AG(1,2^{-1/2})  \\right]^2}{1- \\sum_{n=1}^{\\infty}2^{n+1}c_n^2}").move_to(2.5*RIGHT)
        formtexto = MarkupText(f'<u>Gauss-Legendre</u>').next_to(formula,UP)
        self.play(Write(formula),Write(formtexto))

        # Mostrar la escena
        self.wait(2)
        self.play(
            FadeOut(imageJB),
            FadeOut(imagePB),
            FadeOut(jonatan),
            FadeOut(peter),
        )
        self.wait(1)
        self.play(
            FadeOut(formula),
            FadeOut(formtexto),
            run_time=0.8
        )

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

class Complejidad(Scene):
    def construct(self):
        pregunta = Text("¿Cuál es la complejidad computacional?")
        complejidad = MathTex("O(\\log n)")

        self.wait(1)
        self.play(Write(pregunta),run_time=0.75)
        self.wait(1)
        self.play(pregunta.animate.shift(2.5*UP))
        self.wait(0.5)
        self.play(Write(complejidad))

        self.wait(1.4)
        comp_box = SurroundingRectangle(complejidad, buff=0.3)
        self.play(Create(comp_box))

        self.wait(1)
        beta = MathTex("\\beta_n = \\alpha_{n-1}^{1/2}\\left( \\frac{\\beta_{n-1}+1}{ \\beta_{n-1} + \\alpha_{n-1}} \\right)").shift(2*LEFT)
        alfa = MathTex("\\alpha_n = \\frac{1}{2}\\left( \\alpha_{n-1}^{1/2} + \\alpha_{n-1}^{-1/2} \\right)").next_to(beta,UP)
        pi = MathTex("\\pi_n = \\pi_{n-1}\\beta_n \\left( \\frac{1+\\alpha_n}{1+\\beta_n} \\right)").next_to(beta,DOWN)

        self.play(Write(beta),Write(alfa),Write(pi),comp_box.animate.shift(3*RIGHT),complejidad.animate.shift(3*RIGHT))
        
        self.wait(3)
        self.play(FadeOut(beta),FadeOut(alfa),FadeOut(pi),FadeOut(complejidad),FadeOut(comp_box),run_time=0.5)
        self.wait(0.5)
        texto = Text("Se requieren de ",font_size=30).move_to(1.1*UP+4.75*LEFT)
        form1 = MathTex("\\log_2 n").next_to(texto,RIGHT)
        texto2 = Text("iteraciones para obtener un error del orden",font_size=30).next_to(form1,RIGHT)
        form2 = MathTex("2^n e^{-\\pi 2^{n+1}}").scale(1.25)
        self.play(FadeIn(texto),Write(form1),FadeIn(texto2),Write(form2))

        self.wait(2)        
        texto3 = Text("el cual es el verdadero error producido por el algoritmo",font_size=30).move_to(1.4*DOWN)
        self.play(FadeIn(texto3))
        self.wait(3)

class Prueba(Scene):
    def construct(self):
        texto1 = Text("Corriendo el algoritmo tenemos").shift(2.4*UP+2*LEFT)
        pi1 = MathTex("|\\pi - \\pi_1 | = 0.00101410 ").next_to(texto1,DOWN)
        pi2 = MathTex("|\\pi - \\pi_2 | = 7.37625099\\times 10^{-9}").next_to(pi1,DOWN)
        pi3 = MathTex("|\\pi - \\pi_3 | = 1.83130608\\times 10^{-19}").next_to(pi2,DOWN)
        pi4 = MathTex("|\\pi - \\pi_4 | = 5.47210915\\times 10^{-41}").next_to(pi3,DOWN)
        pi5 = MathTex("|\\pi - \\pi_5 | = 2.40612213 \\times 10^{-84}").next_to(pi4,DOWN)

        p1 = MathTex("\\pi_1: 3").move_to(3.8*LEFT+1.65*UP).scale(0.65)
        t1 = Text(" dígitos  correctos",font_size=20).next_to(p1,RIGHT)
        p2 = MathTex("\\pi_2: 8").next_to(p1,DOWN).scale(0.65)
        t2 = Text(" dígitos  correctos",font_size=20).next_to(p2,RIGHT)
        p3 = MathTex("\\pi_3: 19").next_to(p2,DOWN).scale(0.65)
        t3 = Text(" dígitos  correctos",font_size=20).next_to(p3,RIGHT)
        p4 = MathTex("\\pi_4: 40").next_to(p3,DOWN).scale(0.65)
        t4 = Text(" dígitos  correctos",font_size=20).next_to(p4,RIGHT)
        p5 = MathTex("\\pi_5: 84").next_to(p4,DOWN).scale(0.65)
        t5 = Text(" dígitos  correctos",font_size=20).next_to(p5,RIGHT)
        p6 = MathTex("\\pi_6: 171").move_to(2.4*RIGHT+1.65*UP).scale(0.65)
        t6 = Text(" dígitos  correctos",font_size=20).next_to(p6,RIGHT)
        p7 = MathTex("\\pi_7: 345").next_to(p6,DOWN).scale(0.65)
        t7 = Text(" dígitos  correctos",font_size=20).next_to(p7,RIGHT)
        p8 = MathTex("\\pi_8: 694").next_to(p7,DOWN).scale(0.65)
        t8 = Text(" dígitos  correctos",font_size=20).next_to(p8,RIGHT)
        p9 = MathTex("\\pi_9: 1392").next_to(p8,DOWN).scale(0.65)
        t9 = Text(" dígitos  correctos",font_size=20).next_to(p9,RIGHT)
        p10 = MathTex("\\pi_{10}: 2789").next_to(p9,DOWN).scale(0.65)
        t10 = Text(" dígitos  correctos",font_size=20).next_to(p10,RIGHT)

        text2 = Text("Lo  que  sería:",font_size=22).move_to(1.35*DOWN+4.5*LEFT)
        image_path = "img/pi10.png"
        imagen = ImageMobject(image_path).move_to(2.65*DOWN).scale(0.5)
        self.play(FadeIn(texto1))
        self.wait(1)
        self.play(Write(pi1),Write(pi2),Write(pi3),Write(pi4),Write(pi5))
        self.wait(3)
        self.play(FadeOut(pi1),FadeOut(pi2),FadeOut(pi3),FadeOut(pi4),FadeOut(pi5))
        self.wait(0.5)
        self.play(Write(p1),Write(p2),Write(p3),Write(p4),Write(p5),Write(p6),Write(p7),Write(p8),Write(p9),Write(p10),Write(t1),Write(t2),Write(t3),Write(t4),Write(t5),Write(t6),Write(t7),Write(t8),Write(t9),Write(t10))
        self.wait(3)
        self.play(Write(text2),FadeIn(imagen))
        self.wait(2)
        self.play(FadeOut(p1),FadeOut(t1),FadeOut(p2),FadeOut(t2),FadeOut(p3),FadeOut(t3),FadeOut(p4),FadeOut(t4),FadeOut(p5),FadeOut(t5),FadeOut(p6),FadeOut(t6),FadeOut(p7),FadeOut(t7),FadeOut(p8),FadeOut(t8),FadeOut(p9),FadeOut(t9),FadeOut(p10),FadeOut(t10),FadeOut(text2),FadeOut(imagen))
        
        image_path3 = "img/grafica.png"
        imagen2 = ImageMobject(image_path3).scale(0.7).move_to(1.125*DOWN)
        self.wait(0.3)
        self.play(FadeIn(imagen2))
        self.wait(3)