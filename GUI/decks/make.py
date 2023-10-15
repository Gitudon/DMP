import pickle
filepass="DMP\GUI\decks\deck0.txt"
f = open(filepass, 'wb')
deck=['gb_c_001', 'rgb_c_001', 'r_c_001', 'r_c_001', 'r_c_001', 'r_cs_001', 'gb_c_001', 'g_cs_001', 'z_c_001', 'g_cs_001', 'rg_c_001', 'rgb_c_001', 'rg_s_001', 'b_c_001', 'gb_c_001', 'rg_s_001', 'r_c_002', 'rg_c_001', 'r_cs_001', 'rg_s_001', 'rg_s_001', 'bw_cs_001', 'bw_cs_001', 'rg_c_002', 'bw_cs_001', 'b_c_001', 'g_cs_001', 'rg_c_001', 'gb_c_001', 'rgb_c_001', 'r_cs_001', 'g_cs_001', 'z_c_001', 'bw_c_001', 'gw_c_001', 'r_c_001', 
'b_c_001', 'rg_c_001', 'rgb_c_001', 'b_c_001']
pickle.dump(deck, f)