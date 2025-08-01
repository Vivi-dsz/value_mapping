import plotly.express as px
import pandas as pd
import numpy as np

def kw_count_polar_plot(df, kw_dict, brand_text, color_scale=px.colors.qualitative.G10):
    groupdf = df.groupby(['category', 'brand']).agg({'count':'sum'}).reset_index()

    modgroupdf = pd.DataFrame()
    for cat in kw_dict.keys():
        temp = groupdf[groupdf['category'] == cat].reset_index(drop=True)
        for brand in brand_text.keys():
            # If the brand does not have a keyword in the category,
            # add a placeholder value of 0.1 for visualization
            if brand not in set(temp['brand']):
                temp = pd.concat([temp, pd.DataFrame({'category': [cat], 'brand': [brand], 'count':[0.1]})])

        modgroupdf = pd.concat([modgroupdf, temp]).reset_index(drop=True)

    totcountdict = {}
    for brand in brand_text.keys():
        totcountdict[brand] = np.floor(modgroupdf[modgroupdf['brand'] == brand]['count'].sum())

    modgroupdf['totkwcount'] = modgroupdf['brand'].map(totcountdict)
    modgroupdf['catcountperc'] = 100*modgroupdf['count']/modgroupdf['totkwcount']

    fig = px.line_polar(modgroupdf,
                    r='catcountperc',
                    theta='category',
                    color='brand',
                    line_close=True,
                    color_discrete_sequence=color_scale,
                    range_theta=[0,360], start_angle=0,
                    width=800,
                    height=800)

    fig.update_layout(
        template=None,
        polar = dict(
            radialaxis = dict(showticklabels=False, ticks='', showline=False),
            #angularaxis = dict(showticklabels=False, ticks='')
        )
    )
    fig.update_traces(fill='toself')
    fig.update_polars(bgcolor='lightgray')

    return fig
