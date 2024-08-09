import pandas as pd
import networkx as nx
import plotly.graph_objects as go
from itertools import chain

# Loading data
file_path = 'output_with_clusters_auto.csv'
data = pd.read_csv(file_path)

# Data extraction and processing
cluster_keywords = (
    data.groupby('cluster_title')['keywords']
    .apply(lambda x: set(chain.from_iterable(kw.split(', ') for kw in x)))
    .reset_index()
)

# Creating a graph
G = nx.Graph()
for _, row in cluster_keywords.iterrows():
    cluster_node = row['cluster_title'].strip('"')
    G.add_node(cluster_node, size=20, style='bold')  
    
    for keyword in row['keywords']:
        G.add_node(keyword, size=10, style='normal')
        G.add_edge(cluster_node, keyword)

# Node positioning using the algorithm
pos = nx.spring_layout(G, k=0.5, iterations=50) 

# Node data
node_x = []
node_y = []
text = []
text_styles = []
for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    text.append(node)
    text_styles.append(G.nodes[node]['style'])

# Data for edges
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

# Creating graphical objects
edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    text=text,
    marker=dict(
        showscale=True,
        colorscale='YlGnBu',
        size=[G.nodes[node]['size'] * 5 for node in G.nodes],
        color=[len(list(G.neighbors(node))) for node in G.nodes],
        colorbar=dict(
            thickness=15,
            title='Number of Connections',
            xanchor='left',
            titleside='right'
        ),
        line_width=2),
    textfont=dict(
        size=[10 if style == 'bold' else 10 for style in text_styles],  
        color='#000',
        family=['Arial Black' if style == 'bold' else 'Arial' for style in text_styles]))  


fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=0, l=0, r=0, t=0),
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )


fig.show()