# # Imports

'''
When using the [`bokeh.plotting`](http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html) interface, here are a few of the most common ones we will use:
* Use the [`figure`](http://bokeh.pydata.org/en/latest/docs/reference/plotting.html#bokeh.plotting.figure) function to  create new plot objects to work with.
* Call the functions [`output_file`](http://bokeh.pydata.org/en/latest/docs/reference/resources_embedding.html#bokeh.io.output_file), [`output_notebook`](http://bokeh.pydata.org/en/latest/docs/reference/resources_embedding.html#bokeh.io.output_notebook), and [`output_server`](http://bokeh.pydata.org/en/latest/docs/reference/resources_embedding.html#bokeh.io.output_server) (possibly in combination) to tell Bokeh how to display or save output.
* Execute [`show`](http://bokeh.pydata.org/en/latest/docs/reference/resources_embedding.html#bokeh.io.show) and  [`save`](http://bokeh.pydata.org/en/latest/docs/reference/resources_embedding.html#bokeh.io.save) to display or save plots and layouts.
'''

import bokeh.plotting

bokeh.plotting.output_html('01-plotting.html')

'''
Bokeh incorporates many [palettes](http://bokeh.pydata.org/en/latest/docs/reference/palettes.html#bokeh-palettes) for presenting your data.  The following import method makes it easy to switch out which palette you are using.
'''
from bokeh.palettes import Category10_10 as palette
# # switching palettes is as easy as replacing which you import
# from bokeh.palettes import Colorblind_7 as palette


# Palettes are simply a list of color hex strings.
print(palette)

# You can also use many color names, e.g., `'blue'`, `'red'`, `'yellow'`, `'firebrick'`, etc.  Feel free to explore.


# We will use NumPy and SciPy to create some sample data.
import numpy as np
import scipy.stats

'''
## Sample plot

Bokeh expects data as either a **single value**, or a **series of values**, e.g., list, set, NumPy array, Pandas DataFrame column.  We will often use NumPy arrays.

Lets create some sample data.  Throughout this tutorial, we will use the [normal (or Gaussian) distribution](https://en.wikipedia.org/wiki/Normal_distribution) for out sample data.  The Gaussian distribution is defined as

$$f(x | \mu, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}} \,\exp\left({-\frac{(x-\mu)^2}{2\sigma^2}}\right)$$

where $\mu$ is the mean value, and $\sigma$ is the standard deviation.

SciPy provides [`scipy.stats.norm`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html) which include many functions related to the Gaussian distribution.  Here is a simple wrapper of the probability density function (pdf).
'''

def gaussian(x_array, mu, sigma):
    pdf = scipy.stats.norm.pdf(x_array, loc=mu, scale=sigma)
    return pdf


# We will define 3 Gaussian distributions:
# 1. $\mu=10$, $\sigma=4$
# 2. $\mu=15$, $\sigma=1$
# 3. $\mu=8$, $\sigma=2$

x = np.linspace(0, 20, 100)
y1 = gaussian(x, 10, 4)
y2 = gaussian(x, 15, 1)
y3 = gaussian(x, 8, 2)



# Plot one of these

p = bokeh.plotting.figure()
p.diamond(x, y1)
bokeh.plotting.show(p)

'''
After just 3 lines of code, we have a reasonable plot of our data with several interactions availble by default.  ### Explore
Go through each of the tools on the right side figuring out what each does.

# Quiz
1\. What do each of the tools on the side of the plot do?
2\. Where do you go to learn about configuring plot tools?
3\. Name one additional tool that is not one of the default tools?
'''

# In addition to `tools`, `figure()` and `diamond()` have several other `kwargs` you can use to adjust the plotting results.  Lets see some of these in use.
p = bokeh.plotting.figure(
    title='Demo Plot',
    x_axis_label='x',
    y_axis_label='f(x)',
    width=500, height=350,
    x_range=(0, 20),
    y_range=(-0.05, 0.12),
)

p.diamond(x, y1,
          line_color=palette[0],
          fill_color=palette[1],
          line_alpha=y1/y1.max(), # oscillate from 0 to 1 (y min to max)
          fill_alpha=(1-y1/y1.max()), # oscillate from 1 to 0 (y min to max)
          legend='m=10, s=4',
          size=x/1.5)

bokeh.plotting.show(p)


# Note that you can use `color` to set both the `line_color` and `fill_color`.  Similarly, `alpha` sets both the `line_alpha` and `fill_alpha`.
p = bokeh.plotting.figure(
    title='Demo Plot',
    x_axis_label='x',
    y_axis_label='f(x)',
    width=500, height=350,
    x_range=(0, 20),
    y_range=(-0.05, 0.12),
)

p.diamond(
    x, y1,
    color=palette[0],
    alpha=y1/y1.max(), # oscillate from 0 to 1 (y min to max)
    legend='m=10 s=4',
    size=x/1.5)

bokeh.plotting.show(p)

'''
# Quiz

### 1. Which settings, both args and kwargs, did we see for `bokeh.plotting.figure`?
[Your answer here]
### 2. Which settings, both args and kwargs, did we see for `diamond`?
[Your answer here]
### 3. In the above plots, which settings used a single value and which used a series of values?
[Your answer here]

# See the file `solutions/01_quiz.txt` for the solution


# </table><p>There are many marker types available in Bokeh, you can see details and
# example plots for all of them in the reference guide by clicking on entries in the list below:</p>
# <table class="hlist" style="float:left"><tr><td><ul>
# <li><a href="http://bokeh.pydata.org/en/latest/docs/reference/plotting.html#bokeh.plotting.Figure.asterisk" title="bokeh.plotting.Figure.asterisk"><code class="xref py py-func docutils literal"><span class="pre">asterisk()</span></code></a></li>
# <li><a href="http://bokeh.pydata.org/en/latest/docs/reference/plotting.html#bokeh.plotting.Figure.circle" title="bokeh.plotting.Figure.circle"><code class="xref py py-func docutils literal"><span class="pre">circle()</span></code></a></li>
# <li><a href="http://bokeh.pydata.org/en/latest/docs/reference/plotting.html#bokeh.plotting.Figure.circle_cross" title="bokeh.plotting.Figure.circle_cross"><code class="xref py py-func docutils literal"><span class="pre">circle_cross()</span></code></a></li>
# <li><a href="http://bokeh.pydata.org/en/latest/docs/reference/plotting.html#bokeh.plotting.Figure.circle_x" title="bokeh.plotting.Figure.circle_x"><code class="xref py py-func docutils literal"><span class="pre">circle_x()</span></code></a></li>
# <li><a href="http://bokeh.pydata.org/en/latest/docs/reference/plotting.html#bokeh.plotting.Figure.cross" title="bokeh.plotting.Figure.cross"><code class="xref py py-func docutils literal"><span class="pre">cross()</span></code></a></li>
# </ul>
# </td><td><ul>
# <li><a href="http://bokeh.pydata.org/en/latest/docs/reference/plotting.html#bokeh.plotting.Figure.diamond" title="bokeh.plotting.Figure.diamond"><code class="xref py py-func docutils literal"><span class="pre">diamond()</span></code></a></li>
# <li><a href="http://bokeh.pydata.org/en/latest/docs/reference/plotting.html#bokeh.plotting.Figure.diamond_cross" title="bokeh.plotting.Figure.diamond_cross"><code class="xref py py-func docutils literal"><span class="pre">diamond_cross()</span></code></a></li>
# <li><a href="http://bokeh.pydata.org/en/latest/docs/reference/plotting.html#bokeh.plotting.Figure.inverted_triangle" title="bokeh.plotting.Figure.inverted_triangle"><code class="xref py py-func docutils literal"><span class="pre">inverted_triangle()</span></code></a></li>
# <li><a href="http://bokeh.pydata.org/en/latest/docs/reference/plotting.html#bokeh.plotting.Figure.square" title="bokeh.plotting.Figure.square"><code class="xref py py-func docutils literal"><span class="pre">square()</span></code></a></li>
# </ul>
# </td><td><ul>
# <li><a href="http://bokeh.pydata.org/en/latest/docs/reference/plotting.html#bokeh.plotting.Figure.square_cross" title="bokeh.plotting.Figure.square_cross"><code class="xref py py-func docutils literal"><span class="pre">square_cross()</span></code></a></li>
# <li><a href="http://bokeh.pydata.org/en/latest/docs/reference/plotting.html#bokeh.plotting.Figure.square_x" title="bokeh.plotting.Figure.square_x"><code class="xref py py-func docutils literal"><span class="pre">square_x()</span></code></a></li>
# <li><a href="http://bokeh.pydata.org/en/latest/docs/reference/plotting.html#bokeh.plotting.Figure.triangle" title="bokeh.plotting.Figure.triangle"><code class="xref py py-func docutils literal"><span class="pre">triangle()</span></code></a></li>
# <li><a href="http://bokeh.pydata.org/en/latest/docs/reference/plotting.html#bokeh.plotting.Figure.x" title="bokeh.plotting.Figure.x"><code class="xref py py-func docutils literal"><span class="pre">x()</span></code></a></li>
# </ul>
# </td></tr></table>

# Also, there is a similar command to draw a `line()`, with the added kwarg: `line_width`.

# # Exercise
# Plot all three data sets, `y1`, `y2`, and `y3`, each as a function of the `x` array.  For each data set, use a different entry for each of the following:
# - `color` (or `line_color` and `fill_color` separately)
# - `alpha` (or `line_alpha` and `fill_alpha` separately)
# - `legend`
#
# Also, try using the `line()` option for one of the data sets and two different marker types for the other two data sets (e.g. `diamond()`, `asterisk()`, `circle()`, etc).
#
# Try using a mix of single values and series of values.




# [enter your code here]


# Run the following cell to see one possible solution.




get_ipython().magic('load solutions/01_exercise.py')


# # Read the [Docs](http://bokeh.pydata.org)
#   - [Plotting with Basic Glyphs](http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html)
#   - [Styling Visual Attributes](http://bokeh.pydata.org/en/latest/docs/user_guide/styling.html)

# ---
# Return to [00-introduction.ipynb](00-introduction.ipynb)
# Proceed to [02-streaming.ipynb](02-streaming.ipynb)
