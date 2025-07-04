from manim import *


class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(
            square.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()

class happybirthday(Scene):
    def construct(self):
        self.wait(1)
        source = Text("Happy 50th Birthday Dad!!", font_size= 50, line_spacing= 1).set_color_by_gradient(GREEN).shift(UP)
        self.play(Write(source,run_time = 3))
        self.wait(3)
        path = VMobject()
        group = VGroup(Dot(LEFT),Dot(RIGHT)).shift(DOWN * 0.5)
        self.play(Create(group))
        self.wait()
        mob = ArcBetweenPoints(start= 1.5 * LEFT, end=1.5 *RIGHT, stroke_color=WHITE,angle = TAU/4).shift(DOWN)
        self.play(Create(mob))
        self.wait()






 
