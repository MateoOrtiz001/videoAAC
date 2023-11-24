from manim import *

class introduction(Scene):

    def construct(self):

        transform_title1 = Tex("Aproximaciones de $\pi$")
        transform_title1.to_corner(UP+ LEFT)

        math_tex_approx2 = MathTex(r"\pi = 24 \tan^{-1} \left( \frac{1}{8} \right) + 8 \tan^{-1} \left( \frac{1}{57} \right) + 4 \tan^{-1} \left( \frac{1}{239} \right)")
        math_tex_approx2.move_to(UP*0.5)


        ibm_info = Tex("Usado por IBM en $1962$, Calcular $100000$ decimales de $\pi$!").scale(0.7)
        ibm_info.move_to(DOWN*0.5)
        
        self.add(math_tex_approx2, ibm_info, transform_title1)
        self.wait()
        self.play( FadeOut(math_tex_approx2, ibm_info, transform_title1) )
        self.wait()


        main_title = Tex("La media geométrica y cómputos rápidos de funciones elementales").scale(0.8)
        main_title.move_to(UP*1.5)
        self.play(Write(main_title))

        Alqui = Tex("David Alejandro Alquichire Rincón").scale(0.5)
        Mateo = Tex("Mateo Sebastián Ortíz Higuera").scale(0.5)
        Leo = Tex("David Leonardo Ortíz Uribe").scale(0.5)
        Mateo.move_to(DOWN*0.5)
        Leo.move_to(DOWN*1)

        self.play(Write(Alqui))
        self.play(Write(Mateo))
        self.play(Write(Leo))

        book_img = ImageMobject("book.jpg").scale(2)
        book_img.move_to(LEFT*4 + DOWN*1.5)

        self.play(FadeIn(book_img))

        self.wait(10)
        self.play(FadeOut(main_title, Alqui,Mateo,Leo, book_img))
        self.wait()

