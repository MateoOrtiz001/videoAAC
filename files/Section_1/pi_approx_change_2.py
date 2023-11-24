from manim import *

class pi_change_circle(Scene):

    def construct(self):

        #myBaseTemplate = TexTemplate(
        #    documentclass="\documentclass[preview]{standalone}"
        #)
        #myBaseTemplate.add_to_preamble(r"\usepackage{ragged2e}")

        transform_title1 = Tex("Aproximaciones de $\pi$")
        transform_title1.to_corner(UP+ LEFT)
        

        circle = Circle(radius = 2, color = TEAL_D)
        circle.move_to(LEFT*4)


        poly1 = RegularPolygon(n=93, fill_opacity=0.5).scale(2)
        poly1.move_to(LEFT*4)
        text_nside = MathTex(f"n = 93")
        text_nside.next_to(poly1, UP)

        math_tex_approx = MathTex(r"3.1405 \cdots = \frac{6336}{2017.25} < \pi < \frac{14688}{4673.5} = 3.1428").scale(0.7)
        math_tex_approx.move_to(RIGHT*2.5)

        self.add(transform_title1, circle, poly1, text_nside, math_tex_approx)
        self.wait()
        self.play( FadeOut(circle, poly1, text_nside, math_tex_approx) )
        self.wait()

        john_machin_title = Tex("John Machin $(1680 - 1752)$").scale(0.7)
        john_machin_image = ImageMobject(r"John_machin.jpg").scale(2)
        john_machin_image.move_to(LEFT*4)
        john_machin_title.next_to(john_machin_image, UP)

        self.play(Write(john_machin_title))
        self.play(FadeIn(john_machin_image))
        self.wait()

        math_tex_approx = MathTex(r"\pi = 16 \tan^{-1} \left( \frac{1}{5} \right) - 4 \tan^{-1} \left( \frac{1}{239} \right)").scale(0.7)
        math_tex_approx.move_to(RIGHT*2.5 + UP*1.5)

        self.play(Write(math_tex_approx))
        self.wait()

        image_add_info = Text("Leonhard Euler, Johann Dase e IBM usaron\n aproximaciones similares con la función\n tangente inversa").scale(0.3)
        image_add_img = ImageMobject(r"foto_1abc.jpg").scale(0.4)
        image_add_img.move_to(RIGHT*0.2 + DOWN)
        #image_add_info.width = 5
        image_add_info.next_to(image_add_img, RIGHT)

        
        self.play(FadeIn(image_add_img))
        self.play(Write(image_add_info))
        self.wait(2)