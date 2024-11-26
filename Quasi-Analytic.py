import numpy as np
from manim import *


class Convexer(Scene):
    def construct(self):
        axes1 = Axes([-5,  5], [- 2,  2],
                     axis_config={"include_numbers": True})
        self.play(Create(axes1))




if __name__ == "__main__":
    from manim import config

    config["output_file"] = "Quasi-Analytic"  # 指定保存路径
    config.format = "gif"  # 直接生成 GIF
    config.quality = "medium_quality"
    # 渲染视频
    scene = Convexer()

    scene.render()
