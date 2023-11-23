from manim import *
import numpy as np

class Final(Scene):
    def construct(self):

        texto = Text("Observaciones Finales").move_to(2.5*LEFT+3*UP)
        texto2 = Text("Capacidad de Computo",font_size=24).move_to(2.5*LEFT+1.3*UP)
        texto25 = Text("+",font_size=25).move_to(1.3*UP)
        texto3 = Text("Algoritmos más eficientes",font_size=24).move_to(2.7*RIGHT+1.3*UP)
        
        imagen1 = ImageMobject("img/cuantico.png").move_to(2.5*LEFT+0.75*DOWN).scale(0.4)
        imagen2 = ImageMobject("img/algologa.png").next_to(texto3,DOWN).scale(0.6)

        self.play(Write(texto))
        self.wait(1)
        self.play(FadeIn(texto2),FadeIn(texto25),FadeIn(texto3),FadeIn(imagen1),FadeIn(imagen2),run_time=0.8)
        self.wait(4)
        self.play(Unwrite(texto2),Unwrite(texto25),Unwrite(texto3),FadeOut(imagen1),FadeOut(imagen2),run_time=0.65)
        self.wait(0.76)

        texto4= Text("1984: 4 millones de decimales de ",font_size=26).move_to(3*LEFT+1.7*UP)
        pi = MathTex("\\pi").next_to(texto4,RIGHT)
        texto5= Text("2022: 100 trillones de decimales de ",font_size=26).move_to(3.25*RIGHT+1.8*DOWN)
        pi2 = MathTex("\\pi").next_to(texto5,RIGHT)

        image_path1 = "img/100trillion.png"
        image_path2 = "img/100k.png"

        image84 = ImageMobject(image_path2).move_to(2.9*LEFT).scale(0.4)
        image22 = ImageMobject(image_path1).move_to(3.45*RIGHT).scale(0.4)


        self.play(Write(texto4),FadeIn(image84))
        self.play(Write(pi),run_time=0.25)
        self.wait(3)
        self.play(Write(texto5),FadeIn(image22))
        self.play(Write(pi2),run_time=0.25)
        self.wait(3)
        self.play(FadeOut(texto5),FadeOut(image22),FadeOut(texto4),FadeOut(image84),FadeOut(pi),FadeOut(pi2))
        self.wait(0.5)
        textofinal = Text("¿Cuántos decimales se calcularán de aquí a una década?",font_size=30)
        self.play(FadeIn(textofinal))
        self.wait(3)