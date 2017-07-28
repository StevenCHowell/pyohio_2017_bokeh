# hello_server.py

# 0. imports
from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models.widgets import TextInput, Button, Paragraph, Select

# 1. create some widgets
button = Button(label="Say HI")
input = TextInput(value="Bokeh")
output = Paragraph()
select = Select(
    title="Greeting",
    value="Hello ",
    options=["Hola ", "Guten tag ", "Bonjour ",
             "Hey ", "Hello ", "Tungjatjeta"]
)


# 2. add a callback to a widget
def update():
    output.text = select.value + input.value
button.on_click(update)

# 3. create a layout for everything
layout = column(select, button, input, output)

# 4. add the layout to curdoc
curdoc().add_root(layout)
