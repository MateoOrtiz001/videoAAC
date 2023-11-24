from manim import *

class pi_change_circle(Scene):

    def construct(self):
        transform_title1 = Tex("Aproximaciones de $\pi$")
        transform_title1.to_corner(UP+ LEFT)
        self.add(
            transform_title1
        )
        self.wait()

        circle = Circle(radius = 2, color = TEAL_D)
        circle.move_to(LEFT*4)
        self.play( Create(circle))
        self.wait()

        for i in [8, 16, 28, 93]:
        
            poly1 = RegularPolygon(n=i, fill_opacity=0.5).scale(2)
            poly1.move_to(LEFT*4)
            text_nside = MathTex(f"n = {i}")
            text_nside.next_to(poly1, UP)
            
            self.play( Create(poly1) )
            self.play( Write(text_nside))
            self.wait(duration=1.5)

            if i < 93: self.play(FadeOut(poly1, text_nside))
        
        math_tex_approx = MathTex(r"3.1405 \cdots = \frac{6336}{2017.25} < \pi < \frac{14688}{4673.5} = 3.1428").scale(0.7)
        math_tex_approx.move_to(RIGHT*2.5)
        self.play(Write(math_tex_approx))
        self.wait(4)