mu_x1, mu_y1, mu_x2, mu_y2 = np.random.randint(-40, 40, 4)
sigma_x1, sigma_y1, sigma_x2, sigma_y2 = np.random.randint(1, 25, 4)


my_fig = bokeh.plotting.figure(
    plot_width=400,
    plot_height=400,
    x_axis_label='x',
    y_axis_label='y',
    x_range=(-100, 100),
    y_range=(-100, 100),
)

data1 = bokeh.models.sources.ColumnDataSource(data=dict(x=[], y=[]))
data2 = bokeh.models.sources.ColumnDataSource(data=dict(x=[], y=[]))

circle1 = my_fig.circle(
    "x", "y",
    source=data1,
    color=palette[0],
    alpha=0.2,
)

circle2 = my_fig.circle(
    "x", "y",
    source=data2,
    color=palette[1],
    alpha=0.2,
)

handle = bokeh.io.show(my_fig, notebook_handle=True)

new_data1=dict(x=[], y=[])
new_data2=dict(x=[], y=[])

step = 0
max_step = 1000  # arbitrary stop point for example

while step < max_step:
    new_data1['x'] = [np.random.normal(loc=mu_x1, scale=sigma_x1)]
    new_data1['y'] = [np.random.normal(loc=mu_y1, scale=sigma_y1)]
    new_data2['x'] = [np.random.normal(loc=mu_x2, scale=sigma_x2)]
    new_data2['y'] = [np.random.normal(loc=mu_y2, scale=sigma_y2)]

    data1.stream(new_data1)
    data2.stream(new_data2)

    bokeh.io.push_notebook(handle=handle)
    step += 1
