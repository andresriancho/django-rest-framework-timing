import plotly

from plotly.graph_objs import Histogram, Layout, Figure


def read_samples(filename):
    samples = []

    for line in file(filename):
        line = line.strip()

        if not line:
            continue

        try:
            timing = float(line)
        except:
            continue

        samples.append(timing)

    return samples

x0 = read_samples('token-timing-224a%s.txt' % ('0' * 36,))
x1 = read_samples('token-timing-224c%s.txt' % ('0' * 36,))

sample_ok = Histogram(
    x=x0,
    name='Success (takes longer)',
    histnorm='count'
)

sample_fail = Histogram(
    x=x1,
    name='Fail',
    histnorm='count'
)
data = [sample_ok, sample_fail]
layout = Layout(
    barmode='stack',
    xaxis=dict(
        title='Value'
    ),
    yaxis=dict(
        title='Count'
    ),
    bargap=0.0,
    bargroupgap=0.0
)

fig = Figure(data=data, layout=layout)
plotly.offline.plot(fig)
