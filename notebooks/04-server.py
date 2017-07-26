'''
Present a scatter plot with linked histograms on both axes.

Use the ``bokeh serve`` command to run the example by executing:

    bokeh serve --show selection_histogram.py

at your command prompt. This will open the URL

    http://localhost:5006/selection_histogram

in your browser.

'''

import numpy as np

import bokeh.plotting
import bokeh.layouts
from bokeh.models import BoxSelectTool, LassoSelectTool, Spacer

from bokeh.palettes import Category10_10 as palette


# ~~~~~~~~~~~~~~ create dataset ~~~~~~~~~~~~~~ #
# create three Gaussian distributions
x1 = np.random.normal(loc=5.0, size=400) * 100
y1 = np.random.normal(loc=10.0, size=400) * 10

x2 = np.random.normal(loc=5.0, size=800) * 50
y2 = np.random.normal(loc=5.0, size=800) * 10

x3 = np.random.normal(loc=55.0, size=200) * 10
y3 = np.random.normal(loc=4.0, size=200) * 10

x = np.concatenate((x1, x2, x3))
y = np.concatenate((y1, y2, y3))

# ~~~~~~~~~~ define a fitting function ~~~~~~~~ #
def fit_pdf(x_min=0, x_max=1000):
    # fit the data within input bounds
    mask = (data[:, 0] > x_min) & (data[:, 0] < x_max)
    mu_guess = data[mask, 0].mean()
    sigma_guess = (data[mask, 0].max() - data[mask, 0].min()) / 4
    guess = [mu_guess, sigma_guess]
    (mu, sigma), _ = scipy.optimize.curve_fit(gauss, data[mask, 0],
                                              data[mask, 1], p0=guess,
                                              bounds=([x_min, 0], [x_max, np.inf]))

    # output the fit results
    print('mu: {:0.1f}, sigma: {:0.1f}'.format(mu, sigma))

    # fit_pdf guassian fit
    pdf = gauss(data[:, 0], mu, sigma)
    fit.data_source.data['y'] = pdf

    # fit_pdf limits lines
    x_min_line.data_source.data['x'] = [x_min] * 2
    x_max_line.data_source.data['x'] = [x_max] * 2

    bokeh.io.push_notebook()

# ~~~~~~~~~~~~~ setup the figures ~~~~~~~~~~~~~ #
TOOLS="pan,wheel_zoom,box_select,lasso_select,reset"

# create the scatter plot
p = bokeh.plotting.figure(
    tools=TOOLS,
    plot_width=600, plot_height=600,
    toolbar_location="above",
    title="Linked Histograms",
)
p.select(LassoSelectTool).select_every_mousemove = False  # wait to update until mouse released

r = p.circle(
    x, y,
    size=3,
    alpha=0.6,
    color=palette[1],
)

n_bins = 100

# setup the horizontal histogram
hhist, hedges = np.histogram(x, bins=n_bins)
hzeros = np.zeros(n_bins)
hmax = max(hhist)*1.1

ph = bokeh.plotting.figure(
    toolbar_location=None,
    plot_height=200,
    plot_width=p.plot_width,
    x_range=p.x_range,
    y_range=(-hmax, hmax),
    y_axis_location="right",
)

# horizontal histogram
ph.quad(
    top=hhist,
    bottom=0,
    left=hedges[:-1],
    right=hedges[1:],
    alpha=0.2,
    line_color=None,
    color=palette[0],
)
hh1 = ph.quad(
    top=hzeros,
    bottom=0,
    left=hedges[:-1],
    right=hedges[1:],
    alpha=0.9,
    line_color=None,
    color=palette[1],
)
hh2 = ph.quad(
    top=hzeros,
    bottom=0,
    left=hedges[:-1],
    right=hedges[1:],
    alpha=0.2,
    line_color=None,
    color=palette[0],
)

# setup the vertical histogram
vhist, vedges = np.histogram(y, bins=n_bins)
vzeros = np.zeros(n_bins)
vmax = max(vhist)*1.1

pv = bokeh.plotting.figure(
    toolbar_location=None,
    plot_width=200,
    plot_height=p.plot_height,
    y_range=p.y_range,
    x_range=(-vmax, vmax),
    y_axis_location="right"
)

# vertical histogram
pv.quad(
    top=vedges[1:],
    bottom=vedges[:-1],
    left=0,
    right=vhist,
    alpha=0.2,
    line_color=None,
    color=palette[0],
)
vh1 = pv.quad(
    top=vedges[1:],
    bottom=vedges[:-1],
    left=0,
    right=vzeros,
    alpha=0.9,
    line_color=None,
    color=palette[1],
)
vh2 = pv.quad(
    top=vedges[1:],
    bottom=vedges[:-1],
    left=0,
    right=vzeros,
    alpha=0.2,
    line_color=None,
    color=palette[0],
)

# ~~~~~~~~~~~~~~ arrange the figures ~~~~~~~~~~~~~~ #
layout = bokeh.layouts.column(
    bokeh.layouts.row(p, pv),
    bokeh.layouts.row(ph, Spacer(width=200, height=200)),
)

# ~~~~~~~~~~~~~~ create the application ~~~~~~~~~~~~~~ #
bokeh.plotting.curdoc().add_root(layout)
bokeh.plotting.curdoc().title = "Selection Histogram"

# ~~~~~~~~~~~~~~ define how application updates ~~~~~~~~~~~~~~ #
def update(attr, old, new):
    inds = np.array(new['1d']['indices'])
    if len(inds) == 0 or len(inds) == len(x):
        hhist1, hhist2 = hzeros, hzeros
        vhist1, vhist2 = vzeros, vzeros
    else:
        neg_inds = np.ones_like(x, dtype=np.bool)
        neg_inds[inds] = False
        hhist1, _ = np.histogram(x[inds], bins=hedges)
        vhist1, _ = np.histogram(y[inds], bins=vedges)
        hhist2, _ = np.histogram(x[neg_inds], bins=hedges)
        vhist2, _ = np.histogram(y[neg_inds], bins=vedges)

    hh1.data_source.data["top"]   =  hhist1
    hh2.data_source.data["top"]   = -hhist2
    vh1.data_source.data["right"] =  vhist1
    vh2.data_source.data["right"] = -vhist2

r.data_source.on_change('selected', update)
