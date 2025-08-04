import plotly.express as px
import pandas as pd
import numpy as np

def kw_count_polar_plot(df, kw_dict, brand_text,
                        brand_name_list: list,
                        color_scale=px.colors.qualitative.G10):

    selected_df = df[df['brand'].isin(brand_name_list)].reset_index(drop=True)

    groupdf = selected_df.groupby(['category', 'brand']).agg({'count':'sum'}).reset_index()

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
                    range_theta=[0,360], start_angle=0)
                    #width=800,height=800)

    if len(brand_name_list) == 1:
        fig.update_layout(showlegend=False)

    for trace in fig['data']:
        if (not trace['name'] in brand_name_list):
            trace['showlegend'] = False

    fig.update_layout(
        template=None,
        polar = dict(
            radialaxis = dict(showticklabels=False, ticks='', showline=False),
            angularaxis = dict(labelalias={'quality_usability': 'quality<br>usability',
                                           'innovation_technology': 'innovation<br>technology',
                                           'trust_ethics': 'trust<br>ethics',
                                           'empowerment_control': 'empowerment<br>control',
                                           'user_centricity_support': 'user centricity<br>support',
                                           'community_belonging': 'community<br>belonging',
                                           'growth_ambition': 'growth<br>ambition'})
        )
    )
    fig.update_traces(fill='toself')
    fig.update_polars(bgcolor='lightgray')

    return fig
