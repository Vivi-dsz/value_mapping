from scipy.ndimage import gaussian_filter
import numpy as np
import plotly.express as px


def make_blur(blur):
    def post_process(heatmap):
        heatmap = np.sqrt(heatmap)
        heatmap = gaussian_filter(heatmap, sigma=blur)
        return heatmap
    return post_process


def kw_count_heatmap(data,
            leftXcoor: int = -5,
            leftYcoor: int = -5,
            xwidth: int = 10,
            ywidth: int = 10,
            color_scale: str = 'Blues',
            x: str = "x",
            y: str = "y",
            z: str = "count",
            px_per_meter: float =100):
    """
    Generates a heatmap based on count of keywords in the text
    data = Dataframe with number of keywords and their reduced (x,y) coordinates
    leftXcoor, leftYcoor = lower left placement of the frame that heatmap will be fit in
    xwidth, ywidth = size of the frame that heatmap will be fit in
    color_scale = one of Plotly's defined continuous color scale to be used for heatmap
    x, y = (x,y) coordinates from reduced Word2Vec word vectors
    z = number of keywords found in the text
    px_per_meter = number of pixels to use for a clear heatmap
    """
    # Steps needed for heatmap
    n_x = int(np.ceil(xwidth * px_per_meter))
    n_y = int(np.ceil(ywidth * px_per_meter))
    blur = px_per_meter

    # Initialize heatmap
    heatmap = np.zeros((n_x, n_y), dtype=int)

    # Assign x,y,z from dataframe to heatmap
    if data is not None and len(data) > 0:
        xs = np.round((data[x] - (leftXcoor)) / xwidth * (n_x -1)).astype(int).values
        ys = np.round((data[y] - (leftYcoor)) / ywidth * (n_y -1)).astype(int).values
        zs = data[z].values

        for i in range(len(xs)):
            i_x = xs[i]
            if i_x<0 or i_x>=n_x:
                continue

            i_y = ys[i]
            if i_y<0 or i_y>=n_y:
                continue

            heatmap[i_x, i_y] += zs[i]

        post_process = make_blur(blur)
        heatmap = post_process(heatmap)

    # Create the map
    colormap = (
        'rgba(255, 255, 255, 0)', #white
        'rgba(139, 0, 0, 1)' #red
    )
    x_ticks = np.linspace(leftXcoor, leftXcoor+xwidth, n_x)
    y_ticks = np.linspace(leftYcoor, leftYcoor+ywidth, n_y)

    fig = px.imshow(heatmap.T, x=x_ticks, y=y_ticks, color_continuous_scale = color_scale)

    fig.update_yaxes(autorange=None)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(
        hovermode=False,
        xaxis={"constrain": None, "title": "x", "visible": False},
        yaxis={"constrain": None, "title": "y", "visible": False},
        uirevision="constant",
        plot_bgcolor="white",
        margin={"t": 0, "b": 0, "r": 0, "l": 0, "pad": 0},
    )

    return fig
