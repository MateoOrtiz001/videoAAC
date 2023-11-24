from manim import *

class pi_change_circle(Scene):

    def construct(self):

        transform_title1 = Tex("Aproximaciones de $\pi$")
        transform_title1.to_corner(UP+ LEFT)
        
        john_machin_title = Tex("John Machin $(1680 - 1752)$").scale(0.7)
        john_machin_image = ImageMobject(r"John_machin.jpg").scale(2)
        john_machin_image.move_to(LEFT*4)
        john_machin_title.next_to(john_machin_image, UP)


        math_tex_approx = MathTex(r"\pi = 16 \tan^{-1} \left( \frac{1}{5} \right) - 4 \tan^{-1} \left( \frac{1}{239} \right)").scale(0.7)
        math_tex_approx.move_to(RIGHT*2.5 + UP*1.5)

    

        image_add_info = Text("Leonhard Euler, Johann Dase e IBM usaron\n aproximaciones similares con la función\n tangente inversa").scale(0.3)
        image_add_img = ImageMobject(r"foto_1abc.jpg").scale(0.4)
        image_add_img.move_to(RIGHT*0.2 + DOWN)
        #image_add_info.width = 5
        image_add_info.next_to(image_add_img, RIGHT)

        
        self.add(john_machin_image, john_machin_title, image_add_img, image_add_info, math_tex_approx,transform_title1)
        self.wait()
        self.play( FadeOut(john_machin_image, john_machin_title, image_add_img, image_add_info, math_tex_approx) )
        self.wait()

        math_tex_approx2 = MathTex(r"\pi = 24 \tan^{-1} \left( \frac{1}{8} \right) + 8 \tan^{-1} \left( \frac{1}{57} \right) + 4 \tan^{-1} \left( \frac{1}{239} \right)")
        math_tex_approx2.move_to(UP*0.5)
        self.play(Write(math_tex_approx2))
        self.wait()

        ibm_info = Tex("Usado por IBM en $1962$, Calcular $100000$ decimales de $\pi$!").scale(0.7)
        ibm_info.move_to(DOWN*0.5)
        self.play(Write(ibm_info))
        self.wait()