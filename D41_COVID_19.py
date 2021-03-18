# 載入所需要的套件

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
pd.set_option('display.max_rows', None)
from plotly.subplots import make_subplots
import seaborn as sns
import datetime

# 利用 PANDAS 讀入DATA
data = pd.read_csv('covid_19_data.csv')
# print(data.info())

# 缺失值處理(Percentage of NAN Values, 計算缺失值在資料內的比例)
NAN = [(c, data[c].isna().mean()*100) for c in data]
NAN = pd.DataFrame(NAN, columns=["column_name", "percentage"])
# print(NAN)

# 欄位Province/State有資料缺失, 所以我們要把 NAN 的值替換成 Unknown.
data["Province/State"]= data["Province/State"].fillna('Unknown')
# print(data.head(10))

# 資料型別轉換, 利於 ARRAY.把下列資料換成 INT 整數型別 : "Confirmed","Deaths" and "Recovered" 
data[["Confirmed","Deaths","Recovered"]] =data[["Confirmed","Deaths","Recovered"]].astype(int)

# 為了識別簡易, 把 "Mainland China" 用 "China" 替代
data['Country/Region'] = data['Country/Region'].replace('Mainland China', 'China')

# 原始資料集並無感染的欄位, 利用資料處理新增一項目 "Active_case".計算Active_case = Confirmed - Deaths - Recovered
data['Active_case'] = data['Confirmed'] - data['Deaths'] - data['Recovered']

# 更新INDEX
Data = data[data['ObservationDate'] == max(data['ObservationDate'])].reset_index()

# 整理資料,以表格的方式呈現
# Data_world = Data.groupby(["ObservationDate"])[["Confirmed","Active_case","Recovered","Deaths"]].sum().reset_index()
# labels = ["Last Update","Confirmed","Active cases","Recovered","Deaths"]
# fig = go.Figure(data=[go.Table(header=dict(values=labels),
#                  cells=dict(values=Data_world.loc[0,["ObservationDate","Confirmed","Active_case","Recovered","Deaths"]]))
#                      ])
# fig.update_layout(
#     title='Coronavirus in the word : ',
# )
# fig.show()
# # 繪製圓餅圖
# labels = ["Active cases","Recovered","Deaths"]
# # 繪製圓餅圖-計算數字
# values = Data_world.loc[0, ["Active_case","Recovered","Deaths"]]
# fig = px.pie(Data_world, values=values, names=labels,color_discrete_sequence=['rgb(77,146,33)','rgb(69,144,185)','rgb(77,77,77)'],hole=0.7)
# fig.update_layout(
#     title='Total cases : '+str(Data_world["Confirmed"][0]),
# )
# fig.show()

# Evolution of coronavirus over time
data_over_time= data.groupby(["ObservationDate"])[["Confirmed","Active_case","Recovered","Deaths"]].sum().reset_index().sort_values("ObservationDate",ascending=True).reset_index(drop=True)
# print(data_over_time)

# 繪製圖表[Confirmed casesd]
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=data_over_time.index, y=data_over_time['Confirmed'],
#                     mode='lines',
#                     name='Confirmed cases'))


# fig.update_layout(
#     title='Evolution of Confirmed cases over time in the word',
#         template='plotly_white',
#       yaxis_title="Confirmed cases",
#     xaxis_title="Days",

# )

# fig.show()

# 繪製圖表[Active cases]
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=data_over_time.index, y=data_over_time['Active_case'],
#                     mode='lines',marker_color='yellow',
#                     name='Active cases',line=dict( dash='dot')))

# fig.update_layout(
#     title='Evolution of Active cases over time in the world',
#         template='plotly_dark',
#       yaxis_title="Active cases",
#     xaxis_title="Days",

# )

# fig.show()

# 繪製圖表[Recovered cases]
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=data_over_time.index, y=data_over_time['Recovered'],
#                     mode='lines',
#                     name='Recovered cases',marker_color='green'))

# fig.update_layout(
#     title='Evolution of Recovered cases over time in the world',
#         template='plotly_white',
#       yaxis_title="Recovered cases",
#     xaxis_title="Days",

# )

# fig.show()

# 繪製圖表[Deaths]
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=data_over_time.index, y=data_over_time['Deaths'],name='Deaths',
#                                    marker_color='black',mode='lines',line=dict( dash='dot') ))

# fig.update_layout(
#     title='Evolution of Deaths over time in the world',
#         template='plotly_white',
#      yaxis_title="Deaths",
#     xaxis_title="Days",

# )

# fig.show()

# 繪製圖表[ObservationDate V.S. Confirmed]
# fig = go.Figure(go.Bar(
#             x=data_over_time['ObservationDate'],
#             y=data_over_time['Confirmed'],
#            ))
# fig.update_layout(
#     title='Confirmed Cases In Each Day',
#     template='plotly_white',
#      xaxis_title="Confirmed Cases",
#     yaxis_title="Days",
# )
# fig.show()

# # 繪製圖表[ObservationDate V.S. Active_case]
# fig = go.Figure(go.Bar(
#             x=data_over_time['ObservationDate'],
#             y=data_over_time['Active_case'],
#     marker_color='rgb(253,187,132)'
#            ))
# fig.update_layout(
#     title='Active Cases In Each Day',
#     template='plotly_dark',
#      xaxis_title="Active Cases",
#     yaxis_title="Days",
# )
# fig.show()

# # 繪製圖表[ObservationDate V.S. Recovered]
# fig = go.Figure(go.Bar(
#             x=data_over_time['ObservationDate'],
#             y=data_over_time['Recovered'],
#     marker_color='rgb(178,24,43)'
#            ))
# fig.update_layout(
#     title='Recovered Cases In Each Day',
#     template='plotly_white',
#      xaxis_title="Recovered Cases",
#     yaxis_title="Days",
# )
# fig.show()

# # 繪製圖表[ObservationDate V.S. Deaths]
# fig = go.Figure(go.Bar(
#             x=data_over_time['ObservationDate'],
#             y=data_over_time['Deaths'],
#     marker_color='rgb(13,48,100)'
#            ))
# fig.update_layout(
#     title='Deaths In Each Day',
#     template='plotly_white',
#      xaxis_title="Deaths",
#     yaxis_title="Days",
# )
# fig.show()

# 整理資料,以國家為單位
Data_per_country = Data.groupby(["Country/Region"])[["Confirmed","Active_case","Recovered","Deaths"]].sum().reset_index().sort_values("Confirmed",ascending=False).reset_index(drop=True)
# headerColor = 'grey'
# rowEvenColor = 'lightgrey'
# rowOddColor = 'white'

# fig = go.Figure(data=[go.Table(
#   header=dict(
#     values=['<b>Country</b>','<b>Confirmed Cases</b>'],
#     line_color='darkslategray',
#     fill_color=headerColor,
#     align=['left','center'],
      
#     font=dict(color='white', size=12)
#   ),
#   cells=dict(
#     values=[
#       Data_per_country['Country/Region'],
#       Data_per_country['Confirmed'],
#       ],
#     line_color='darkslategray',
#     # 2-D list of colors for alternating rows
#     fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*len(Data_per_country)],
#     align = ['left', 'center'],
#     font = dict(color = 'darkslategray', size = 11)
#     ))
# ])
# fig.update_layout(
#     title='Confirmed Cases In Each Country',
# )
# fig.show()

# # 繪製圖表[Confirmed V.S. Country/Region]
# fig = go.Figure(go.Bar(
#             x=Data_per_country['Confirmed'],
#             y=Data_per_country['Country/Region'],
#             orientation='h'))
# fig.update_layout(
#     title='Confirmed Cases In Each Country',
#     template='plotly_white',
#      xaxis_title="Confirmed Cases",
#     yaxis_title="Countries",
# )
# fig.show()

# # 繪製圖表[Active_case V.S. Country/Region]
# fig = go.Figure(go.Bar(
#             x=Data_per_country['Active_case'],
#             y=Data_per_country['Country/Region'],
#             orientation='h',
#             marker_color='#DC3912',))
# fig.update_layout(
#     title='Active Cases In Each Country',
#     template='plotly_white',
#     xaxis_title="Active Cases",
#     yaxis_title="Countries",
# )
# fig.show()

# # 繪製圖表[Recovered V.S. Country/Region]
# fig = go.Figure(go.Bar(
#             x=Data_per_country['Recovered'],
#             y=Data_per_country['Country/Region'],
#             orientation='h',
#             marker_color='#2CA02C',))
# fig.update_layout(
#     title='Recovered Cases In Each Country',
#     template='plotly_white',
#      xaxis_title="Recovered Cases",
#     yaxis_title="Countries",
# )
# fig.show()

# # 繪製圖表[Deaths V.S. Country/Region]
# fig = go.Figure(go.Bar(
#             x=Data_per_country['Deaths'],
#             y=Data_per_country['Country/Region'],
#             orientation='h',
#             marker_color='black',))
# fig.update_layout(
#     title='Deaths In Each Country',
#     template='plotly_white',
#     xaxis_title="Deaths",
#     yaxis_title="Countries",
# )

# fig.show()

# # 繪製圖表[Confirmed V.S. Country/Region]
# fig = px.choropleth(Data_per_country, locations=Data_per_country['Country/Region'],
#                     color=Data_per_country['Confirmed'],locationmode='country names', 
#                     hover_name=Data_per_country['Country/Region'], 
#                     color_continuous_scale=px.colors.sequential.Tealgrn,template='plotly_dark', )
# fig.update_layout(
#     title='Confirmed Cases In Each Country',
# )
# fig.show()

# # 繪製圖表[Active_case V.S. Country/Region]
# fig = px.choropleth(Data_per_country, locations=Data_per_country['Country/Region'],
#                     color=Data_per_country['Active_case'],locationmode='country names', 
#                     hover_name=Data_per_country['Country/Region'], 
#                     color_continuous_scale=px.colors.sequential.Tealgrn,template='plotly_white', )
# fig.update_layout(
#     title='Active Cases In Each Country',
# )
# fig.show()

# # 繪製圖表[Recovered V.S. Country/Region]
# fig = px.choropleth(Data_per_country, locations=Data_per_country['Country/Region'],
#                     color=Data_per_country['Recovered'],locationmode='country names', 
#                     hover_name=Data_per_country['Country/Region'], 
#                     color_continuous_scale=px.colors.sequential.Tealgrn,template='plotly_white', )
# fig.update_layout(
#     title='Recovered Cases In Each Country',
# )
# fig.show()

# # 繪製圖表[Deaths V.S. Country/Region]
# fig = px.choropleth(Data_per_country, locations=Data_per_country['Country/Region'],
#                     color=Data_per_country['Deaths'],locationmode='country names', 
#                     hover_name=Data_per_country['Country/Region'], 
#                     color_continuous_scale=px.colors.sequential.Tealgrn,template='plotly_dark', )
# fig.update_layout(
#     title='Deaths In Each Country',
# )
# fig.show()

data_per_country = data.groupby(["Country/Region","ObservationDate"])[["Confirmed","Active_case","Recovered","Deaths"]].sum().reset_index().sort_values("ObservationDate",ascending=True).reset_index(drop=True)
# # 繪製圖表[ObservationDat :Confirmed V.S. Country/Region]
# fig = px.choropleth(data_per_country, locations=data_per_country['Country/Region'],
#                     color=data_per_country['Confirmed'],locationmode='country names', 
#                     hover_name=data_per_country['Country/Region'], 
#                     color_continuous_scale=px.colors.sequential.deep,
#                     animation_frame="ObservationDate")
# fig.update_layout(

#     title='Evolution of confirmed cases In Each Country',
# )
# fig.show()

# # 繪製圖表[ObservationDat :Active_cas V.S. Country/Region]
# fig = px.choropleth(data_per_country, locations=data_per_country['Country/Region'],
#                     color=data_per_country['Active_case'],locationmode='country names', 
#                     hover_name=data_per_country['Country/Region'], 
#                     color_continuous_scale=px.colors.sequential.Tealgrn,
#                     animation_frame="ObservationDate")
# fig.update_layout(

#     title='Evolution of active cases In Each Country',
#     template='plotly_dark'
# )
# fig.show()

# # 繪製圖表[ObservationDat :Recovered V.S. Country/Region]
# fig = px.choropleth(data_per_country, locations=data_per_country['Country/Region'],
#                     color=data_per_country['Recovered'],locationmode='country names', 
#                     hover_name=data_per_country['Country/Region'], 
#                     color_continuous_scale=px.colors.sequential.deep,
#                     animation_frame="ObservationDate")
# fig.update_layout(
#     title='Evolution of recovered cases In Each Country',
# )
# fig.show()

# # 繪製圖表[Confirmed V.S. Country/Region,Mode=Bar Charts]
# fig = go.Figure(data=[go.Bar(
#             x=Data_per_country['Country/Region'][0:10], y=Data_per_country['Confirmed'][0:10],
#             text=Data_per_country['Confirmed'][0:10],
#             textposition='auto',
#             marker_color='black',
            

#         )])
# fig.update_layout(
#     title='Most 10 infected Countries',
#     xaxis_title="Countries",
#     yaxis_title="Confirmed Cases",
#         template='plotly_white'

# )
# fig.show()

# # 繪製圖表[Confirmed V.S. Country/Region,Mode=Bubble Scatter Plots]
# fig = go.Figure(data=[go.Scatter(
#     x=Data_per_country['Country/Region'][0:10],
#     y=Data_per_country['Confirmed'][0:10],
#     mode='markers',
    
#     marker=dict(
#         color=100+np.random.randn(500),
#         size=(Data_per_country['Confirmed'][0:10]/25000),
#         showscale=True
#         )
# )])

# fig.update_layout(
#     title='Most 10 infected Countries',
#     xaxis_title="Countries",
#     yaxis_title="Confirmed Cases",
#     template='plotly_dark'
# )
# fig.show()

Recovered_per_country = Data.groupby(["Country/Region"])["Recovered"].sum().reset_index().sort_values("Recovered",ascending=False).reset_index(drop=True)

# # 繪製圖表[Recovered V.S. Country/Region]
# headerColor = 'grey'
# rowEvenColor = 'lightgrey'
# rowOddColor = 'white'

# fig = go.Figure(data=[go.Table(
#   header=dict(
#     values=['<b>Country</b>','<b>Confirmed Cases</b>'],
#     line_color='darkslategray',
#     fill_color=headerColor,
#     align=['left','center'],      
#     font=dict(color='white', size=12)
#   ),
#   cells=dict(
#     values=[
#       Recovered_per_country['Country/Region'],
#       Recovered_per_country['Recovered'],
#       ],
#     line_color='darkslategray',
#     # 2-D list of colors for alternating rows
#     fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*len(Data_per_country)],
#     align = ['left', 'center'],
#     font = dict(color = 'darkslategray', size = 11)
#     ))
# ])
# fig.update_layout(
#     title='Recovered Cases In Each Country',
# )
# fig.show()

# # 繪製圖表[Recovered V.S. Country/Region,Mode=Pie Charts]
# fig = px.pie(Recovered_per_country, values=Recovered_per_country['Recovered'], names=Recovered_per_country['Country/Region'],
#              title='Recovered cases',
#             )
# fig.update_traces(textposition='inside', textinfo='percent+label')
# fig.update_layout(
#     template='plotly_white'
# )
# fig.show()

# # 繪製圖表[Recovered V.S. Country/Region,Mode=Bar Charts]
# fig = go.Figure(data=[go.Bar(
#             x=Recovered_per_country['Country/Region'][0:10], y=Recovered_per_country['Recovered'][0:10],
#             text=Recovered_per_country['Recovered'][0:10],
#             textposition='auto',
#             marker_color='green',

#         )])
# fig.update_layout(
#     title='Most 10 infected Countries',
#     xaxis_title="Countries",
#     yaxis_title="Recovered Cases",
#     template='plotly_white'
# )
# fig.show()

#  # 繪製圖表[Recovered V.S. Country/Region,Mode=Bubble Scatter]
# fig = go.Figure(data=[go.Scatter(
#     x=Recovered_per_country['Country/Region'][0:10],
#     y=Recovered_per_country['Recovered'][0:10],
#     mode='markers',
#     marker=dict(
#         color=100+np.random.randn(500),
#         size=(Data_per_country['Recovered'][0:10]/20000),
#         showscale=True
#         )
# )])
# fig.update_layout(
#     title='Most 10 infected Countries',
#     xaxis_title="Countries",
#     yaxis_title="Recovered Cases",
#     template='plotly_white'

# )
# fig.show()

Active_per_country = Data.groupby(["Country/Region"])["Active_case"].sum().reset_index().sort_values("Active_case",ascending=False).reset_index(drop=True)
# headerColor = 'grey'
# rowEvenColor = 'lightgrey'
# rowOddColor = 'white'

# fig = go.Figure(data=[go.Table(
#   header=dict(
#     values=['<b>Country</b>','<b>Active Cases</b>'],
#     line_color='darkslategray',
#     fill_color=headerColor,
#     align=['left','center'],
#     font=dict(color='white', size=12)
#   ),
#   cells=dict(
#     values=[
#       Active_per_country['Country/Region'],
#       Active_per_country['Active_case'],
#       ],
#     line_color='darkslategray',
#     # 2-D list of colors for alternating rows
#     fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*len(Data_per_country)],
#     align = ['left', 'center'],
#     font = dict(color = 'darkslategray', size = 11)
#     ))
# ])
# fig.update_layout(
#     title='Active Cases In Each Country',
# )
# fig.show()

# # 繪製圖表[Active_case V.S. Country/Region,Mode=Bar Charts]
# fig = go.Figure(data=[go.Bar(
#             x=Active_per_country['Country/Region'][0:10], y=Active_per_country['Active_case'][0:10],
#             text=Active_per_country['Active_case'][0:10],
           
#         )])
# fig.update_layout(
#     title='Most 10 infected Countries',
#     xaxis_title="Countries",
#     yaxis_title="Active Cases",
#     template='plotly_white'
# )
# fig.show()

# # 繪製圖表[Active_case V.S. Country/Region,Mode=Bubble Scatter]
# fig = go.Figure(data=[go.Scatter(
#     x=Active_per_country['Country/Region'][0:10],
#     y=Active_per_country['Active_case'][0:10],
#     mode='markers',
#     marker=dict(
#         color=10+np.random.randn(200),

#         size=Active_per_country['Active_case'][0:10]/15000,
#         showscale=True
#         )
# )])
# fig.update_layout(
#     title='Most 10 infected Countries',
#     xaxis_title="Countries",
#     yaxis_title="Active Cases",
#         template='plotly_white'

# )
# fig.show()


Deaths_per_country = Data.groupby(["Country/Region"])["Deaths"].sum().reset_index().sort_values("Deaths",ascending=False).reset_index(drop=True)
# print(Deaths_per_country.head(10))

# headerColor = 'grey'
# rowEvenColor = 'lightgrey'
# rowOddColor = 'white'

# fig = go.Figure(data=[go.Table(
#   header=dict(
#     values=['<b>Country</b>','<b>Deaths</b>'],
#     line_color='darkslategray',
#     fill_color=headerColor,
#     align=['left','center'],
#     font=dict(color='white', size=12)
#   ),
#   cells=dict(
#     values=[
#       Deaths_per_country['Country/Region'],
#       Deaths_per_country['Deaths'],
#       ],
#     line_color='darkslategray',
#     # 2-D list of colors for alternating rows
#     fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*len(Data_per_country)],
#     align = ['left', 'center'],
#     font = dict(color = 'darkslategray', size = 11)
#     ))
# ])
# fig.update_layout(
#     title='Deaths In Each Country',
# )
# fig.show()

# # 繪製圖表[Death V.S. Country/Region,Mode=Bar Charts]
# fig = go.Figure(data=[go.Bar(
#             x=Deaths_per_country['Country/Region'][0:10], y=Deaths_per_country['Deaths'][0:10],
#             text=Deaths_per_country['Deaths'][0:10],
#             textposition='auto',
#             marker_color='black'

#         )])
# fig.update_layout(
#     title='Most 10 infected Countries',
#     xaxis_title="Countries",
#     yaxis_title="Deaths",
#         template='plotly_white'

# )
# fig.show()

# # 繪製圖表[Death V.S. Country/Region,Mode=Bubble Scatter]
# fig = go.Figure(data=[go.Scatter(
#     x=Deaths_per_country['Country/Region'][0:10],
#     y=Deaths_per_country['Deaths'][0:10],
#     mode='markers',
#     marker=dict(
#         color=[145, 140, 135, 130, 125, 120,115,110,105,100],
#         size=Deaths_per_country['Deaths'][0:10]/1000,
#         showscale=True
#         )
# )])
# fig.update_layout(
#     title='Most 10 infected Countries',
#     xaxis_title="Countries",
#     yaxis_title="Deaths",
#         template='plotly_white'

# )
# fig.show()


Data_China = data [(data['Country/Region'] == 'China') ].reset_index(drop=True)
# print(Data_China.head(10))

Data_china_last = Data_China[Data_China['ObservationDate'] == max(Data_China['ObservationDate'])].reset_index()
# print(Data_china_last.head(10))
# 取得確診率
Data_china_per_state= Data_china_last.groupby(["Province/State"])[["Confirmed","Active_case","Recovered","Deaths"]].sum().reset_index().sort_values("Confirmed",ascending=False).reset_index(drop=True)
# print(Data_china_per_state)

# # 繪製圖表[Confirmed V.S. Chain,Mode=Pie Charts]
# fig = px.pie(Data_china_per_state, values=Data_china_per_state['Confirmed'], names=Data_china_per_state['Province/State'],
#              title='Confirmed cases in China',
#             hole=.2)
# fig.update_traces(textposition='inside', textinfo='percent+label')
# fig.show()

# # 繪製圖表[Active_case V.S. Province/State=Chain,Mode=Bar Charts]
# fig = go.Figure(go.Bar(
#             x=Data_china_per_state['Active_case'],
#             y=Data_china_per_state['Province/State'],
#             orientation='h',
#             marker_color='#DC3912',))
# fig.update_layout(
#     title='Active Cases In Each Province/State',
#     template='plotly_white',
#     xaxis_title="Active Cases",
#     yaxis_title="Province/State",
# )
# fig.show()

# # 繪製圖表[Recovered V.S. Province/State=Chain,Mode=Bar Charts]
# fig = go.Figure(go.Bar(
#             x=Data_china_per_state['Recovered'],
#             y=Data_china_per_state['Province/State'],
#             orientation='h',
#             marker_color='green',))
# fig.update_layout(
#     title='Active Cases In Each Province/State',
#     template='plotly_white',
#     xaxis_title="Recovered Cases",
#     yaxis_title="Province/State",
# )
# fig.show()

# # 繪製圖表[Deaths V.S. Province/State=Chain,Mode=Bar Charts]
# fig = go.Figure(go.Bar(
#             x=Data_china_per_state['Deaths'],
#             y=Data_china_per_state['Province/State'],
#             orientation='h',
#             marker_color='black',))
# fig.update_layout(
#     title='Deaths In Each Province/State',
#     template='plotly_white',
#     xaxis_title="Deaths",
#     yaxis_title="Province/State",
# )
# fig.show()

# Country/Region=Chain 境內統計
Data_china_total= Data_china_last.groupby(["Country/Region"])[["Confirmed","Deaths","Recovered","Active_case"]].sum().reset_index().reset_index(drop=True)
# print(Data_china_total)

# # 繪製圖表["Active_case","Recovered","Deaths V.S. Chain,Mode=Pie Charts]
# labels = ["Active cases","Recovered","Deaths"]
# values = Data_china_total.loc[0, ["Active_case","Recovered","Deaths"]]
# df = px.data.tips()
# fig = px.pie(Data_china_total, values=values, names=labels, color_discrete_sequence=['green','royalblue','darkblue'], hole=0.5)
# fig.update_layout(
#     title='Total cases in China : '+str(Data_china_total["Confirmed"][0]),
# )
# fig.show()

Data_china_op= Data_China.groupby(["ObservationDate","Country/Region"])[["Confirmed","Deaths","Recovered","Active_case"]].sum().reset_index().reset_index(drop=True)
# print(Data_china_op.head(10))

# # 繪製圖表[Confirmed","Deaths","Recovered","Active_case" V.S. ObservationDate,Mode=Line and Scatter]
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=Data_china_op['ObservationDate'], y=Data_china_op['Confirmed'],
#                     mode='lines',
#                     name='Confirmed cases'))


# fig.add_trace(go.Scatter(x=Data_china_op['ObservationDate'], y=Data_china_op['Active_case'],
#                     mode='lines',
#                     name='Active cases',line=dict( dash='dot')))
# fig.add_trace(go.Scatter(x=Data_china_op['ObservationDate'], y=Data_china_op['Deaths'],name='Deaths',
#                                    marker_color='black',mode='lines',line=dict( dash='dot') ))
# fig.add_trace(go.Scatter(x=Data_china_op['ObservationDate'], y=Data_china_op['Recovered'],
#                     mode='lines',
#                     name='Recovered cases',marker_color='green'))

# fig.update_layout(
#     title='Evolution of cases over time in China',
#         template='plotly_white'

# )

# fig.show()


# # 資料統計(Country/Region=US)
Data_US = data [(data['Country/Region'] == 'US') ].reset_index(drop=True)
Data_us_last = Data_US[Data_US['ObservationDate'] == max(Data_US['ObservationDate'])].reset_index()
Data_us_total= Data_us_last.groupby(["Country/Region"])[["Confirmed","Deaths","Recovered","Active_case"]].sum().reset_index().reset_index(drop=True)
# print(Data_us_total)

# # 繪製圖表["Active_case","Recovered","Deaths" V.S. U.S.,Mode=Pie Charts]
# labels = ["Active cases","Recovered","Deaths"]
# values = Data_us_total.loc[0, ["Active_case","Recovered","Deaths"]]
# df = px.data.tips()
# fig = px.pie(Data_us_total, values=values, names=labels, color_discrete_sequence=['royalblue','darkblue','green'], hole=0.5)
# fig.update_layout(
#     title='Total cases in United States : '+str(Data_us_total["Confirmed"][0]),
# )
# fig.show()


Data_us_per_state= Data_us_last.groupby(["Province/State"])[["Confirmed","Active_case","Deaths"]].sum().reset_index().sort_values("Confirmed",ascending=False).reset_index(drop=True)
# print(Data_us_per_state)

# # 繪製圖表[Confirmed V.S. U.S.,Mode=Pie Charts]
# fig = px.pie(Data_us_per_state, values=Data_us_per_state['Confirmed'], names=Data_us_per_state['Province/State'],
#              title='Confirmed cases in United States',
#             hole=.2)
# fig.update_traces(textposition='inside', textinfo='percent+label')
# fig.show()

# # 繪製圖表[Active_case V.S. U.S.,Mode=Pie Charts]
# fig = px.pie(Data_us_per_state, values=Data_us_per_state['Active_case'], names=Data_us_per_state['Province/State'],
#              title='Active cases in United States',
#             hole=.2)
# fig.update_traces(textposition='inside', textinfo='percent+label')
# fig.show()

# # 繪製圖表[Deaths V.S. U.S.,Mode=Pie Charts]
# fig = px.pie(Data_us_per_state, values=Data_us_per_state['Deaths'], names=Data_us_per_state['Province/State'],
#              title='Deaths in United States',
#             hole=.2)
# fig.update_traces(textposition='inside', textinfo='percent+label')
# fig.show()

Data_US_op= Data_US.groupby(["ObservationDate","Country/Region"])[["Confirmed","Deaths","Recovered","Active_case"]].sum().reset_index().reset_index(drop=True)
# print(Data_US_op)

# # 繪製圖表[Confirmed cases V.S. U.S.,Mode=Line plot]
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=Data_US_op.index, y=Data_US_op['Confirmed'],
#                     mode='lines',
#                     name='Confirmed cases'))
# fig.update_layout(
#     title='Evolution of Confirmed cases over time in US',
#         template='plotly_white'

# )

# fig.show()

# # 繪製圖表[Active cases V.S. U.S.,Mode=Line plot]
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=Data_US_op.index, y=Data_US_op['Active_case'],
#                     mode='lines',
#                     name='Active cases',line=dict( dash='dot')))

# fig.update_layout(
#     title='Evolution of Acitive cases over time in US',
#         template='plotly_white'

# )

# fig.show()

# # 繪製圖表[Recovered cases V.S. U.S.,Mode=Line plot]
# fig = go.Figure()

# fig.add_trace(go.Scatter(x=Data_US_op.index, y=Data_US_op['Recovered'],
#                     mode='lines',
#                     name='Recovered cases',marker_color='green'))

# fig.update_layout(
#     title='Evolution of Recovered cases over time in US',
#         template='plotly_white'

# )

# fig.show()

# # 繪製圖表[Deaths V.S. U.S.,Mode=Line plot]
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=Data_US_op.index, y=Data_US_op['Deaths'],name='Deaths',
#                                    marker_color='white',mode='lines',line=dict( dash='dot') ))

# fig.update_layout(
#     title='Evolution of Deaths over time in US',
#         template='plotly_dark'

# )

# fig.show()