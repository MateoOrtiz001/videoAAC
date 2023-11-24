from manim import *

class section_3(Scene):

    def construct(self):

        iter_a = MathTex(r"a_{n+1} = \frac{1}{2}(a_n + b_n)").scale(0.7)
        iter_b = MathTex(r"b_{n+1} = \sqrt{a_n b_n}").scale(0.7)

        iter_a.move_to(LEFT*2 + UP*2)
        iter_b.move_to(RIGHT*2 + UP*2)



        text_AGM1 = Tex(r"Por la desigualdad de la medio geométrica aritmética, tenemos que $a_{n+1} \geq b_{n+1}$, y en general $a_n \geq a_{n+1} \geq b_{m+1} \geq b_m$. Así, las sucesiones $(a_n)$ y $(b_n)$ tienden a un mismo valor, denotado, $AG(a,b)$").scale(0.7)    
        text_AGM1.move_to(UP*0.8)


        limit_an = Tex(r"Observar límite de $(a_n)$ :").scale(0.7)
        integral_elliptic = MathTex(r"I(a,b) = \int_0^{\frac{\pi}{2}} \frac{d \theta}{\sqrt{ a^2 \cos^2 \theta + b^2 \sin^2 \theta }} ").scale(0.7)
        limit_an.move_to(LEFT*2.5 + DOWN)
        integral_elliptic.move_to(RIGHT*2.5 + DOWN)


        self.add(iter_a, iter_b, text_AGM1, limit_an, integral_elliptic)
        self.wait()
        self.play(FadeOut(iter_a, iter_b, text_AGM1, limit_an, integral_elliptic))
        self.wait()

        Gauss_Img = ImageMobject("gauss_img.jpg").scale(0.3)
        Gauss_Img.move_to(LEFT*3)

        self.play(FadeIn(Gauss_Img))

        thm_Gauss = MathTex(r"I(a_0, b_0) = \frac{\pi}{2} AG(a_0,b_0)")
        thm_Gauss.move_to(RIGHT*3)
        self.play(Write(thm_Gauss))

        self.wait(10)

        self.play(FadeOut(Gauss_Img, thm_Gauss))
        self.wait(3)