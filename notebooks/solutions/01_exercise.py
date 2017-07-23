p = bokeh.plotting.figure(
    title='Exercise Plot',
    x_axis_label='x',
    y_axis_label='f(x)',
    width=400, height=350,
    x_range=(-8, 8),
    y_range=(-1.5, 3)
)

p.circle_cross(
    x, y_sin,
    line_color=palette[0],
    fill_color=palette[1],
    line_alpha=((y_sin+1)/2), # oscillate from 0 to 1 (y min to max)
    fill_alpha=((1-y_sin)/2), # oscillate from 1 to 0 (y min to max)
    legend='Sine',
    size=5
)

p.inverted_triangle(
    x, y_cos,
    line_color=palette[2],
    fill_color=palette[3],
    line_alpha=((y_cos+1)/2), # oscillate from 0 to 1 (y min to max)
    fill_alpha=((1-y_cos)/2), # oscillate from 1 to 0 (y min to max)
    legend='Cosine',
    size=10
)

p.line(
    x, y_tan,
    color=palette[4],
    alpha=0.7,
    legend='Tangent',
    line_width=2,
)

bokeh.plotting.show(p)