import requests
requests.packages.urllib3.disable_warnings()

import plotly

from plotly.graph_objs import Histogram, Layout, Figure
from utils.read_samples import read_timing_samples

x0 = read_timing_samples('token-timing.db', 'db_init', '224a93060c0dd4fb931d05083b4cb7b6a8000000')
x1 = read_timing_samples('token-timing.db', 'db_init', '224a93060c0dd4fb931d05083b4cb7b6a9000000')

sample_ok = Histogram(
    x=x0,
    name='Success (takes longer)',
    histnorm='count',
    opacity=0.75
)

sample_fail = Histogram(
    x=x1,
    name='Fail',
    histnorm='count',
    opacity=0.75
)

data = [sample_ok, sample_fail]
layout = Layout(
    barmode='overlay',
    xaxis=dict(
        title='Response time (ms)'
    ),
    yaxis=dict(
        title='Count'
    ),
    bargap=0.0,
    bargroupgap=0.0
)

fig = Figure(data=data, layout=layout)
plotly.offline.plot(fig)
