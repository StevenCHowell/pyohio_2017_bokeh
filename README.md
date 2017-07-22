# Bokeh tutorial at [PyOhio 2017](https://pyohio.org/)

## Brief Description

Bokeh is a powerful library for creating interactive data visualizations in the style of D3.js without writing JavaScript.  In this tutorial, you will learn to use Bokeh to

  - create simple interactive plots, both from scripts and Jupyter notebooks
  - link interactive visualizations to a running python instance
  - plot streamed data
  - interactively view large datasets with Datashader

## Detailed Abstract

"A picture is worth a thousand words." Data visualization is key to understanding the information contained in data.  Interactive visualizations provide a valuable means for students, data journalist, engineers, and scientist to explore their data.  Bokeh provides a Python API for creating elegant plots, dashboards, and data applications in the style of D3.js, without having to write any JavaScript.

This tutorial will introduce students to the basics of using Bokeh, demonstrate different aspects of the library, and teach students how to get the answers to questions that arise as they apply what they have learned to their own data.  We will cover the following four examples:

  - using Bokeh to create simple interactive plots, both from a script and from a Jupyter notebook
  - using Bokeh server to link interactive visualizations to a running python instance
  - steaming data to a Bokeh plot
  - partnering Bokeh with Datashader to interactively view large datasets

For each of these topics, students will be given exercises to apply what they have learned and further explore the Bokeh API.

## Resources
  - Official [Bokeh Tutorial](http://nbviewer.jupyter.org/github/bokeh/bokeh-notebooks/blob/master/tutorial/00%20-%20intro.ipynb)

## Setup
### Step 1: Clone the [pyohio_2017_bokeh](https://github.com/StevenCHowell/pyohio_2017_bokeh) repository

- You can should be able to use any Linux, Mac OS X, or Windows computer with a web browser for this tutorial.  I recommend using Chrome, but the code should also work in Firefox and Safari.
- Clone this repository, e.g. using `git clone https://github.com/StevenCHowell/pyohio_2017_bokeh`.
- Open a terminal window inside the repository.

Please *do a `git pull`* on this cloned repository either *in the evening of Friday July 28 or in the morning of Saturday July 29*.

### Step 2: Create a conda environment from `environment.yml`

The easiest way to get an environment set up for the tutorial is installing it using the `environment.yml` provided. If you do not already have it, install [`conda`](https://www.continuum.io/downloads), and then create the `bk_tutorial` environment by executing:
```
conda env create -f environment.yml
```

When installation is complete you may activate the environment by running the command:
```
activate bk_tutorial
```
(for Windows) or:
```
$ source activate bk_tutorial
```
(for Linux and Mac).

Later, when you are ready to exit the environment after the tutorial, you can type:
```
deactivate
```
(for Windows) or:
```
$ source deativate
```
(for Linux and Mac).  

If for some reason you want to remove the environment entirely, you can do so by writing:
```
conda env remove --name bk_tutorial
```
