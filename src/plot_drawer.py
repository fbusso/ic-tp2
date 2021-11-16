import plotly
from plotly.graph_objs import *


class PlotDrawer:

    @staticmethod
    def drawPlot(plot_title, generations, average_results, max_results, min_results):
        generations_rev = generations[::-1]

        min_results = min_results[::-1]

        max_and_min_trace = Scatter(
            x=generations + generations_rev,
            y=max_results + min_results,
            fill='tozerox',
            fillcolor='rgb(0,100,80)',
            line=Line(color='rgb(0,80,80)'),
            showlegend=True,
            name='Máximo y Mínimo',
        )

        average_trace = Scatter(
            x=generations,
            y=average_results,
            line=Line(color='rgb(200,80,80)'),
            mode='lines',
            name='Promedio',
        )

        data = Data([max_and_min_trace, average_trace])

        layout = Layout(
            title=plot_title,
            paper_bgcolor='rgb(255,255,255)',
            plot_bgcolor='rgb(229,229,229)',
            xaxis=XAxis(
                gridcolor='rgb(255,255,255)',
                showgrid=True,
                showline=False,
                showticklabels=True,
                tickcolor='rgb(127,127,127)',
                ticks='outside',
                zeroline=False
            ),
            yaxis=YAxis(
                gridcolor='rgb(255,255,255)',
                showgrid=True,
                showline=False,
                showticklabels=True,
                tickcolor='rgb(127,127,127)',
                ticks='outside',
                zeroline=False
            ),
        )
        fig = Figure(data=data, layout=layout)
        plotly.offline.plot(fig, filename='plot_' + plot_title + '.html')
