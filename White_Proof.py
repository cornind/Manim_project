from copy import deepcopy
from tracemalloc import start
from typing_extensions import runtime
import numpy as np
from manim import *
import scipy.signal

class CopyrightLabel(VMobject):
    def __init__(self, copyright_text="© 2024 Cornind", font_size=24, color=BLACK, **kwargs):
        super().__init__(**kwargs)
        self.text = MarkupText(
            f'<span color="{color.to_hex()}"> {copyright_text}</span>',
            font_size=font_size
        )
        self.text.to_corner(UP + RIGHT)
        self.add(self.text)

class SmoothIteration(Scene):
    def construct(self):
        copyright = CopyrightLabel()
        self.add(copyright)


        MathTex.set_default(color=BLACK)
        Arrow.set_default(color = BLACK)
        self.camera.background_color = WHITE


        Gongshi1 = MathTex('u^{(','0',')}').to_corner(DL).shift(RIGHT*1.5);
        
        Arrow1 = Arrow(start = 2*LEFT, end =2*RIGHT).next_to(Gongshi1,RIGHT)
        ShowTau1 = MathTex(r'\tau_{a_1}').next_to(Arrow1,UP)

        Gongshi2 = MathTex(r'\tau_{a_1}','u^{(','0',')}').next_to(Arrow1,RIGHT)

        Arrow2 = Arrow(start = DOWN, end =UP).next_to(Gongshi1,UP)
        ShowH1 = MathTex(r'H_{a_1}*a_1').next_to(Arrow2,RIGHT)

        Gongshi3 = MathTex(r'H_{a_1}*a_1','u^{(','1',')}').next_to(Arrow2,UP)

        self.add
        self.play(Write(Gongshi1),runtime = 1)
        self.play(Write(Arrow1),
                  Write(ShowTau1),
                  Write(Arrow2),
                  Write(ShowH1),
                  runtime = 1)
        self.play(TransformMatchingTex(VGroup(Gongshi1,Gongshi1.copy(),ShowTau1,ShowH1)
                                       ,VGroup(Gongshi2,Gongshi3))
                                       ,runtime = 1)

        
        
        Arrow3 = Arrow(start = LEFT, end =RIGHT).next_to(Gongshi2,RIGHT)
        ShowTau2 = MathTex(r'\tau_{a_1}').next_to(Arrow3,UP)

        Gongshi4 = MathTex(r'\tau_{a_1}',r'\tau_{a_1}','u^{(','0',')}').next_to(Arrow3,RIGHT)

        Arrow4 = Arrow(start = DOWN, end =UP).next_to(Gongshi2,UP)
        ShowH1 = MathTex(r'H_{a_1}*a_1').next_to(Arrow4,RIGHT)

        Gongshi5 = MathTex(r'H_{a_1}*a_1',r'\tau_{a_1}','u^{(','1',')}').next_to(Arrow4,UP)


        self.play(Write(Arrow3),
                  Write(ShowTau2),
                  Write(Arrow4),
                  Write(ShowH1),
                  runtime = 1)
        self.play(TransformMatchingTex(VGroup(Gongshi2,Gongshi2.copy(),ShowTau2,ShowH1)
                                       ,VGroup(Gongshi4,Gongshi5))
                                       ,runtime = 1)

        Arrow5 = Arrow(start = LEFT, end =RIGHT).next_to(Gongshi3,RIGHT)
        ShowTau1 = MathTex(r'\tau_{a_2}').next_to(Arrow5,UP)
        Gongshi5new = MathTex(r'H_{a_1}*a_1\tau_{a_1}u^{(1)}').next_to(Arrow4,UP)
        Gongshi6 = MathTex(r'H_{a_1}*a_1\tau_{a_1}u^{(1)}',
                           '+',r'\tau_{a_2}',r'H_{a_1}*a_1','u^{(','1',')}').next_to(Arrow5,RIGHT)
        ShowTau1Gongshi3 = MathTex(r'\tau_{a_2}',r'H_{a_1}*a_1','u^{(','1',')}').next_to(Arrow5,UP)
        Arrow6 = Arrow(start = DOWN, end =UP).next_to(Gongshi3,UP)
        ShowH2 = MathTex(r'H_{a_2}*a_2').next_to(Arrow6,RIGHT)

        Gongshi7 = MathTex(r'H_{a_2}*a_2',r'H_{a_1}*a_1','u^{(','2',')}').next_to(Arrow6,UP)


        self.play(Write(Arrow5),
                  Write(ShowTau1),
                  Write(Arrow6),
                  Write(ShowH2),
                  TransformMatchingTex(Gongshi5,Gongshi5new),
                  runtime = 1)
        self.play(TransformMatchingTex(VGroup(Gongshi3.copy(),ShowTau1)
                                       ,ShowTau1Gongshi3)
                  ,runtime = 1)
        self.play(TransformMatchingTex(VGroup(ShowTau1Gongshi3,Gongshi5new)
                                       ,VGroup(Gongshi6))
                  ,runtime = 1)
        self.play(TransformMatchingTex(VGroup(Gongshi3,ShowH2)
                                       ,VGroup(Gongshi7)),
                  runtime = 1)

        self.wait(1)
        
        

    




def main():
    
    
    # Configure Manim settings
    config["media_dir"] = "./media"
    config["output_file"] = "SmoothIteration"
    config["write_to_movie"] = True
    config["format"] = "gif"
    config["quality"] = "medium_quality"
    # Parse the command line or directly run the scene
    ani = SmoothIteration();
    ani.render();


if __name__ == "__main__":
    main()