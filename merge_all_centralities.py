import pandas as pd

corona = pd.read_excel("datasets/corona_nodes.xlsx")

corona_clo = pd.read_excel("outputs/centrality_measures/closeness_centrality.xlsx")
corona_clo = corona_clo.sort_values(by=['Node'],ascending=True)

corona_har = pd.read_excel("outputs/centrality_measures/harmonic_centrality.xlsx")
corona_har = corona_har.sort_values(by=['Node'],ascending=True)

corona_deg = pd.read_excel("outputs/centrality_measures/degree_centrality.xlsx")
corona_deg = corona_deg.sort_values(by=['Node'],ascending=True)

corona_dec = pd.read_excel("outputs/centrality_measures/decay_centrality.xlsx")
corona_dec = corona_dec.sort_values(by=['Node'],ascending=True)

corona_ecc = pd.read_excel("outputs/centrality_measures/eccentricity.xlsx")
corona_ecc = corona_ecc.sort_values(by=['Node'],ascending=True)

corona_rad = pd.read_excel("outputs/centrality_measures/radiality_centrality.xlsx")
corona_rad = corona_rad.sort_values(by=['Node'],ascending=True)

corona_lc = pd.read_excel("outputs/centrality_measures/load_centrality.xlsx")
corona_lc = corona_lc.sort_values(by=['Node'],ascending=True)

corona_acf = pd.read_excel("outputs/centrality_measures/approximate_current_flow_betweenness_centrality.xlsx")
corona_acf = corona_acf.sort_values(by=['Node'],ascending=True)

corona_bet = pd.read_excel("outputs/centrality_measures/betweenness_centrality.xlsx")
corona_bet = corona_bet.sort_values(by=['Node'],ascending=True)

corona_cfc = pd.read_excel("outputs/centrality_measures/current_flow_closeness_centrality.xlsx")
corona_cfc = corona_cfc.sort_values(by=['Node'],ascending=True)

corona_info = pd.read_excel("outputs/centrality_measures/information_centrality.xlsx")
corona_info = corona_info.sort_values(by=['Node'],ascending=True)

corona_cfb = pd.read_excel("outputs/centrality_measures/current_flow_betweenness_centrality.xlsx")
corona_cfb = corona_cfb.sort_values(by=['Node'],ascending=True)

corona_rc = pd.read_excel("outputs/centrality_measures/reach_centrality.xlsx")
corona_rc = corona_rc.sort_values(by=['Node'],ascending=True)

corona_drc = pd.read_excel("outputs/centrality_measures/deep_reach_centrality.xlsx")
corona_drc = corona_drc.sort_values(by=['Node'],ascending=True)



corona_dt = corona.merge(corona_clo)
corona_dt = corona_dt.merge(corona_har)
corona_dt = corona_dt.merge(corona_deg)
corona_dt = corona_dt.merge(corona_dec)
corona_dt = corona_dt.merge(corona_ecc)
corona_dt = corona_dt.merge(corona_rad)
corona_dt = corona_dt.merge(corona_lc)
corona_dt = corona_dt.merge(corona_acf)
corona_dt = corona_dt.merge(corona_bet)
corona_dt = corona_dt.merge(corona_cfc)
corona_dt = corona_dt.merge(corona_info)
corona_dt = corona_dt.merge(corona_cfb)
corona_dt = corona_dt.merge(corona_rc)
corona_dt = corona_dt.merge(corona_drc)

corona_dt.to_excel('outputs/centrality_measures/corona_data_for_analysis/corona_centrality_data.xlsx',index=False)
corona_dt.head()