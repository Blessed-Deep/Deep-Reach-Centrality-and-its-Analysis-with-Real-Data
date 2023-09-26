import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def corr_func(x, y, **kwargs):
    corr_coef = x.corr(y)
    ax = plt.gca()
    ax.annotate(f"{corr_coef:.2f}", xy=(0.5, 0.5), xycoords=ax.transAxes, fontsize=35, ha='center', va='center')

# Load your DataFrame
corona_scaled = pd.read_excel("outputs/centrality_measures/corona_data_for_analysis/corona_centrality_scaled_data.xlsx")

corona_scaled = corona_scaled.drop(['Node', 'corona_nodes'], axis=1)

# Rename the large name for better visualition 
corona_scaled.rename(columns={'closeness_centrality': 'clo'}, inplace=True)
corona_scaled.rename(columns={'harmonic_centrality': 'har'}, inplace=True)
corona_scaled.rename(columns={'degree_centrality': 'deg'}, inplace=True)
corona_scaled.rename(columns={'decay_centrality': 'dec'}, inplace=True)
corona_scaled.rename(columns={'eccentricity': 'ecc'}, inplace=True)
corona_scaled.rename(columns={'radiality_centrality': 'rad'}, inplace=True)
corona_scaled.rename(columns={'load_centrality': 'load'}, inplace=True)
corona_scaled.rename(columns={'approximate_current_flow_betweenness_centrality': 'aprx_cfb'}, inplace=True)
corona_scaled.rename(columns={'betweenness_centrality': 'bet'}, inplace=True)
corona_scaled.rename(columns={'current_flow_closeness_centrality': 'cfc'}, inplace=True)
corona_scaled.rename(columns={'information_centrality': 'info'}, inplace=True)
corona_scaled.rename(columns={'current_flow_betweenness_centrality': 'cfb'}, inplace=True)
corona_scaled.rename(columns={'reach_centrality': 'rc'}, inplace=True)
corona_scaled.rename(columns={'deep_reach_centrality': 'drc'}, inplace=True)


dis_deg = ['clo',
           'har',
           'deg',
           'dec',
           'ecc',
           'rad',
           'load',
           'aprx_cfb',
           'bet',
           'cfc',
           'info',
           'cfb',
           'rc',
           'drc']


def increase_font_size(*args, **kwargs):
    kwargs['fontsize'] = 35  # Adjust the fontsize as needed
    ax = plt.gca()
    ax.tick_params(axis='both', labelsize=20)  # Increase font size for ticks
    ax.set_xlabel(ax.get_xlabel(), **kwargs)
    ax.set_ylabel(ax.get_ylabel(), **kwargs)

# Create a PairGrid with scatterplots and correlation values

# Distance and Degree based
g = sns.PairGrid(corona_scaled, vars=dis_deg)
g.map_upper(corr_func)  
g.map_diag(sns.violinplot) 
g.map_lower(sns.scatterplot)
g.map(increase_font_size)

g_filename = "figures/pearson_corr_values_dis_deg.png"
g.savefig(g_filename, dpi=300, bbox_inches='tight')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
