# -*- coding: utf-8 -*-

from copy import deepcopy
import numpy as np
from manim import *
import scipy.signal

class CopyrightLabel(VMobject):
    def __init__(self, copyright_text="© 2024 Cornind", font_size=24, color=WHITE, **kwargs):
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


    
        a_values = [1 
                    for i 
                    in np.arange(10)]  # Example sequence

        num_iterations = len(a_values)
        x_range_max = sum(a_values) 
        dx = 0.001  # Increased resolution for convolution

        # Calculate convolutions iteratively
        u_functions = []
        current_convolution = None

        x_values = np.arange(0,x_range_max,dx)

        for k in range(num_iterations):
            
            h_k = np.array((0 <= x_values) & (x_values < a_values[k]),
                           dtype=np.double
                           )/a_values[k]
            
            if k == 0:
                current_convolution =deepcopy(h_k)
            else:
                current_convolution = self.convolve(current_convolution,h_k,dx)
                    
                

            u_functions.append(current_convolution)

        # Create axes (adjust y_range dynamically)
        x_values = np.arange(0, x_range_max, dx)
        axes = Axes(
            x_range=[0, x_range_max, 0.5],  # Add x-axis ticks
            y_range=[0, 1, 0.5],  # Add y-axis ticks
            axis_config={"include_tip": False,
                        "include_numbers": True},  # Show numbers
        )
        self.play(Create(axes))

        # Animate the convolutions
        graphs = []
        labels = []
        for k, u_k in enumerate(u_functions):
            # 绘制当前函数的图形
            graph = axes.plot_line_graph(
                x_values,
                [u_k[i] for i in np.arange(np.size(x_values))],
                line_color=BLUE,
                add_vertex_dots=False
            )
            graphs.append(graph)

            # 创建标签
            label = MathTex(f"u_{k}=","{(H_1)}^{*",f"{k+1}","}").to_edge(RIGHT)  # 将标签放置在图形上方
            labels.append(label)  # 存储标签

            if k == 0:
                self.play(Create(graph), Write(label))  # 同时绘制图形和标签
            else:
                self.play(Transform(graphs[k-1], graph),
                         Transform(labels[k-1], label),
                         run_time=0.5)
                
                
                self.remove(graphs[k-1])
                self.remove(labels[k-1])
        self.wait(0.5)

    def convolve(self, f, g, dx):
        """Approximate convolution using numerical integration (iterative)."""
        
        h = scipy.signal.convolve(f,g)*dx
        return h[np.arange(np.size(f))]




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
