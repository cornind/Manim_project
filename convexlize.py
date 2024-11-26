import numpy as np
from manim import *


class Convexer(Scene):
    def construct(self):
        axes1 = Axes([-0.5, 7.5], [-0.5, 7.5],
                     axis_config={"include_numbers": True})
        self.play(Create(axes1))

        # 创建点并添加标签
        points = [(i, np.floor(np.sqrt(10 * i)) - np.mod(i, 2) * i / 2) for i in range(7)]

        dots = VGroup()
        lines = VGroup()
        for i, point in enumerate(points):
            dot = Dot(axes1.c2p(point[0], point[1]), color=RED)
            label = MathTex(f"({point[0]}, {point[1]})").next_to(dot, UP)
            dot.add(label)
            dots.add(dot)

            self.play(Create(dot), run_time=0.25)
            if i < len(points) - 1:
                line = Line(axes1.c2p(point[0], point[1]),
                            axes1.c2p(points[i + 1][0], points[i + 1][1]),
                            color=BLUE_E)
                lines.add(line)

        # 添加坐标轴
        dashed_lines = VGroup()
        for i in range(len(points)):
            for j in range(i + 2, len(points)):
                line = DashedLine(
                    axes1.c2p(points[i][0], points[i][1]),
                    axes1.c2p(points[j][0], points[j][1]),
                    color=RED_E
                )
                dashed_lines.add(line)

        for line in lines:
            self.play(Create(line), run_time=0.25)

        # 添加标记的点
        self.add(dots)
        self.wait(1)

        self.play(*[Create(dashed_line) for dashed_line in dashed_lines], run_time=1.0)

        new_points = [(i + 1, 0.9 * (i + 1)) for i in range(4)]

        ndots = VGroup()
        ARROWS = VGroup()
        for i, point in enumerate(new_points):
            dot = Dot(axes1.c2p(point[0], point[1]), color=RED)
            label = MathTex(f"({point[0]}, {point[1]})").next_to(dot, UP)
            dot.add(label)
            ndots.add(dot)
            arrow = Line(start=axes1.c2p(point[0], 0), end=axes1.c2p(point[0], point[1]), color=BLUE_A, stroke_width=2)
            ARROWS.add(arrow)
            self.play(Create(arrow), Create(dot), run_time=0.35)

        self.play(*[[FadeOut(dashed_line) for dashed_line in dashed_lines]],
                  run_time=1.0)

        new_points = [(0, 0.0), *new_points, (5, 4.5), (6, 7.0)];
        new_dots = VGroup()
        new_lines = VGroup()
        for i, point in enumerate(new_points):
            dot = Dot(axes1.c2p(point[0], point[1]), color=RED)
            label = MathTex(f"({point[0]}, {point[1]})").next_to(dot, UP)
            dot.add(label)
            new_dots.add(dot)

            self.add(dot)
            if i < len(points) - 1:
                line = Line(axes1.c2p(point[0], point[1]),
                            axes1.c2p(new_points[i + 1][0], new_points[i + 1][1]),
                            color=BLUE_E)
                new_lines.add(line)

        self.play(*[*[Transform(dot, new_dots[i]) for i, dot in enumerate(dots)],
                    *[Transform(line, new_lines[i]) for i, line in enumerate(lines)]],
                  run_time=1)
        self.wait(1)


if __name__ == "__main__":
    from manim import config

    config["output_file"] = "output/video"  # 指定保存路径
    config.format = "mp4"  # 直接生成 GIF
    config.quality = "medium_quality"
    # 渲染视频
    scene = Convexer()

    scene.render()
