p = bokeh.plotting.figure(
    title='Exercise Plot',
    x_axis_label='x',
    y_axis_label='f(x)',
    width=700, height=350,
    x_range=(0, 20),
    # y_range=(-0.05, 0.12),
)

# plot y1
p.circle_cross(
    x, y1,
    line_color=palette[0],
    fill_color=palette[1],
    line_alpha=y1/y1.max(), # oscillate from 0 to 1 (y min to max)
    fill_alpha=(1-y1/y1.max()), # oscillate from 1 to 0 (y min to max)
    legend='m=10, s=4',
    size=7
)

# plot y2
p.inverted_triangle(
    x, y2,
    line_color=palette[2],
    fill_color=palette[3],
    line_alpha=0.4,
    fill_alpha=0.6,
    legend='m=5, s=1',
    size=10
)

# plot y3
p.line(
    x, y3,
    color=palette[4],
    alpha=0.7,
    legend='m=12, s=2',
    line_width=4,
)

#reposition the legend
p.legend.location = "top_left"

bokeh.plotting.show(p)