import numpy as np
from manim import *

class CopyrightLabel(VMobject):
    def __init__(self, copyright_text="© 2024 Cornind", font_size=24, color=GRAY, **kwargs):
        super().__init__(**kwargs)
        self.text = MarkupText(
            f'<span color="{color.to_hex()}"> {copyright_text}</span>',
            font_size=font_size
        )
        self.text.to_edge( RIGHT)
        self.add(self.text)


class Convexer(Scene):
    def construct(self):
        # 设置相机为方形
        self.camera.background_color = WHITE
        MathTex.set_default(color=BLACK)
        Tex.set_default(color=BLACK)
        Text.set_default(color=BLACK)
        copyright = CopyrightLabel()
        self.add(copyright)
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=8,
            y_length=8,
            axis_config={"include_numbers": True,
                         "color":BLACK}
        )
        x_numbers = axes.get_x_axis().numbers
        y_numbers = axes.get_y_axis().numbers
        x_numbers.set_color(RED)
        y_numbers.set_color(BLUE)

        self.play(Create(axes))

        graph = axes.plot(lambda x: x, color=BLACK)
        self.play(Create(graph))

        points = VGroup(
            *[Dot(axes.coords_to_point(-4/i/i, 4/i/i), color=BLUE_E,stroke_width=2)
                  for i in np.arange(1,8)]
        )


        # Create an ellipse
        ellipse = Ellipse(width=3, height=2, color=BLUE)
        ellipse.move_to(axes.coords_to_point(0, 0))
        self.play(Create(points))
        self.wait(3)


if __name__ == "__main__":
    from manim import config


    config["output_file"] = "Partition"  # 指定保存路径
    config.format = "gif"  # 直接生成 GIF
    # 渲染视频
    scene = Convexer()

    scene.render()
