'''
Present a scatter plot with linked histograms on both axes.

Use the ``bokeh serve`` command to run the example by executing:

    bokeh serve --show selection_histogram.py

at your command prompt. This will open the URL

    http://localhost:5006/selection_histogram

in your browser.

'''

import numpy as np
import scipy.stats
import scipy.optimize

import bokeh.plotting
import bokeh.layouts
from bokeh.models import BoxSelectTool, LassoSelectTool, Spacer
from bokeh.models.widgets import Slider, Paragraph

from bokeh.palettes import Category10_10 as palette

def gaussian(x_array, mu, sigma):
    pdf = scipy.stats.norm.pdf(x_array, loc=mu, scale=sigma)
    return pdf

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

x_min = np.floor(x.min())
x_max = np.ceil(x.max())
y_min = np.floor(y.min())
y_max = np.ceil(y.max())

# ~~~~~~~~~~~~~ setup the figures ~~~~~~~~~~~~~ #
TOOLS="pan,wheel_zoom,box_select,lasso_select,reset"

# create the scatter plot
p = bokeh.plotting.figure(
    tools=TOOLS,
    plot_width=600, plot_height=600,
    toolbar_location="above",
    title="Fit Gaussians",
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
# Gaussian fit of histogram
hfit_x = hedges[:-1]
hfit_x += hfit_x[1] - hfit_x[0]
mu0 = hfit_x.mean()
sigma0 = (hfit_x.max() - hfit_x.min()) / 4
hfit_y = gaussian(hfit_x, mu0, sigma0)
x_fit_line = ph.line(hfit_x, hfit_y, color=palette[2])
x_min_line = ph.line([hfit_x[0], hfit_x[0]], [0, hmax], color=palette[3])
x_max_line = ph.line([hfit_x[-1], hfit_x[-1]], [0, hmax], color=palette[4])

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
vfit_y = vedges[:-1]
vfit_y += vfit_y[1] - vfit_y[0]
mu0 = vfit_y.mean()
sigma0 = (vfit_y.max() - vfit_y.min()) / 4
vfit_x = gaussian(vfit_y, mu0, sigma0)
v_fit_line = pv.line(vfit_x, vfit_y, color=palette[2])
v_min_line = pv.line([0, vmax], [vfit_y[0], vfit_y[0]], color=palette[3])
v_max_line = pv.line([0, vmax], [vfit_y[-1], vfit_y[-1]], color=palette[4])


# ~~~~~~~~~~~~~~ create the sliders ~~~~~~~~~~~~~~ #
x_low = Slider(title="x-min", value=x_min, start=300, end=x_min)  # , step=1.0)
x_high = Slider(title="x-max", value=x_max, start=x_min, end=x_min)  # , step=1.0)
x_output = Paragraph()

y_low = Slider(title="y-min", value=y_min, start=y_min, end=y_min)  # , step=1.0)
y_high = Slider(title="y-max", value=y_max, start=y_min, end=y_min)  # , step=1.0)
y_output = Paragraph()

# ~~~~~~~~~~~~~~ arrange the interface ~~~~~~~~~~~~~~ #
layout = bokeh.layouts.column(
    bokeh.layouts.row(p, pv, bokeh.layouts.widgetbox(y_low, y_high)),
    bokeh.layouts.row(ph, Spacer(width=200, height=200)),
    bokeh.layouts.widgetbox(x_low, x_high),
)

# ~~~~~~~~~~ define a fitting function ~~~~~~~~ #
def do_fit(fit_data):
    mu_guess = fit_data.mean()
    sigma_guess = (fit_data.max() - fit_data.min()) / 4
    guess = [mu_guess, sigma_guess]

    (mu, sigma), _ = scipy.optimize.curve_fit(
        gaussian,
        p0=guess,
        bounds=([x_min, 0], [x_max, np.inf]),
    )
    return mu, sigma

def update_x_fit(attr, old, new):
    # fit_pdf limits lines
    x_min_line.data_source.data['x'] = [x_low.value] * 2
    x_max_line.data_source.data['x'] = [x_high.value] * 2

    # fit the data within input bounds
    data = hh1.data_source.data["top"]
    mask = (hfit_x > x_min) & (hfit_x < x_max)
    fit_data = data[mask]
    mu, sigma = do_fit(fit_data)

    # output the fit results
    x_output.text = 'mu: {:0.1f}, sigma: {:0.1f}'.format(mu, sigma)

    # fit_pdf guassian fit
    hfit_y = gaussian(fit_data, mu, sigma)
    x_fit_line.data_source.data['y'] = hfit_y

def update_y_fit(attr, old, new):
    # fit_pdf limits lines
    y_min_line.data_source.data['y'] = [y_low.value] * 2
    y_max_line.data_source.data['y'] = [y_high.value] * 2

    # fit the data within input bounds
    data = vh1.data_source.data["right"]
    print(len(vfit_y))
    mask = (vfit_y > y_min) & (vfit_y < y_max)
    fit_data = data[mask]
    mu, sigma = do_fit(fit_data)

    # output the fit results
    y_output.text = 'mu: {:0.1f}, sigma: {:0.1f}'.format(mu, sigma)

    # fit_pdf guassian fit
    vfit_x = gaussian(fit_data, mu, sigma)
    y_fit_line.data_source.data['x'] = vfit_x

# ~~~~~~~~~~~~~~ create the application ~~~~~~~~~~~~~~ #
bokeh.plotting.curdoc().add_root(layout)
bokeh.plotting.curdoc().title = "Fit Gaussians"

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
x_low.on_change('value', update_x_fit)
x_high.on_change('value', update_x_fit)
