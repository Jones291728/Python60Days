
# Case_01_利用 Source 建立字典, 再用figure 輸出 BAR 圖 source = ColumnDataSource(data=dict(fruits=fruits, counts=counts, color=Spectral6))import numpy as np
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, HoverTool,FactorRange
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

output_file("colormapped_bars.html")
fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
counts = [5, 3, 4, 2, 4, 6]
source = ColumnDataSource(data=dict(fruits=fruits, counts=counts, color=Spectral6))
p = figure(x_range=fruits, plot_height=250, toolbar_location=None, title="Fruit Counts")
p.vbar(x="fruits",top="counts",width=0.7,source=source,color="color",legend="fruits")

p.xgrid.grid_line_color =None
p.y_range.end = 9
p.legend.orientation = "horizontal"
p.legend.location = "top_center"
show(p)

# Case_02_Grouped(vbar+factor_cmap)
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, HoverTool,FactorRange
from bokeh.transform import factor_cmap
from bokeh.plotting import figure

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
years = ['2015', '2016', '2017']

data = {'fruits' : fruits,
        '2015'   : [2, 1, 4, 3, 2, 4],
        '2016'   : [5, 3, 3, 2, 4, 6],
        '2017'   : [3, 2, 4, 4, 5, 3]}

# this creates [ ("Apples", "2015"), ("Apples", "2016"), ("Apples", "2017"), ("Pears", "2015), ... ]

x = [(fruit, year) for fruit in fruits for year in years]
counts = sum(zip(data["2015"], data["2016"], data["2017"]), ())
source = ColumnDataSource(data=dict(fruits_year=x, counts=counts)) 
p = figure(x_range=FactorRange(*x), plot_height=250, plot_width=800, title="Fruit Counts by Year")
p.vbar(x='fruits_year', top='counts', width=0.9, source=source, line_color="white",fill_color=factor_cmap('fruits_year', palette=["#c9d9d3", "#718dbf", "#e84d60"], factors=years, start=1, end=3))
p.y_range.start = 0
p.x_range.range_padding = .05
p.xaxis.major_label_orientation = .5
p.xgrid.grid_line_color = None
show(p)


# Case_03_使用HoverTool(游標滑過時顯示資料); Click_policy (藉由標籤控制數值顯示)
# Download the Bokeh sample data sets to local disk(example_bokeh sampledata)
import bokeh.io
from bokeh.resources import INLINE
from bokeh.models import HoverTool
from bokeh.palettes import Spectral4
from bokeh.plotting import figure, output_file, show, output_notebook,ColumnDataSource
from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT
import pandas as pd

# 環境 settings
bokeh.io.reset_output()
bokeh.io.output_notebook(INLINE)
# set hover
## HoverTool
# 游標滑過時顯示資料,date格式需要轉換，不然會是timestamp
hover = HoverTool(
    tooltips = [
        ("date", "@date"),
        ("close", "@open"),
        ("close", "@close"),
        ("high", "@high"),
        ("low", "@low"),
        ("volume","@volume")
    ], 
    formatters={"@date":"datetime"}
)

# set figure
p = figure(plot_width=1000, plot_height=400, x_axis_type="datetime",tools=[hover,"pan,box_zoom,reset,save"],)
p.title.text = 'Stock_Price--Click on legend entries to mute the corresponding lines and show daily details in hover'

# use ColumnDataSource to control
# click_policy
# 藉由標籤控制數值顯示
# hide為隱藏，mute為切換自訂顯示模式
# 可在muted_color控制顏色, muted_alpha控制顏色濃淡
for data, name, color in zip([AAPL, IBM, MSFT, GOOG], ["AAPL", "IBM", "MSFT", "GOOG"], Spectral4):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    source = ColumnDataSource(df)
    p.line(x="date",y="close", line_width=2, color=color, alpha=0.8,muted_color=color, muted_alpha=0.2, legend_label=name,source=source)

p.legend.location = "top_left"
# use hide or mute
p.legend.click_policy="mute"
output_file("interactive_legend.html", title="interactive_legend.py example")
show(p)
output_notebook() 


# 參考資料
# https://docs.bokeh.org/en/latest/docs/user_guide/categorical.html
