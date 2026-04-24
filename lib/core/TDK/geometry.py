#====================================================================#
#====================================================================#
#===   __  __    _    ____ _   _ _____ _____ ___ ____  _ __  __   ===#
#===  |  \/  |  / \  / ___| \ | | ____|_   _|_ _/ ___|(_)  \/  |  ===#
#===  | |\/| | / _ \| |  _|  \| |  _|   | |  | |\___ \| | |\/| |  ===#
#===  | |  | |/ ___ \ |_| | |\  | |___  | |  | | ___) | | |  | |  ===#
#===  |_|  |_/_/   \_\____|_| \_|_____| |_| |___|____/|_|_|  |_|  ===#
#===                                                              ===#
#====================================================================#
#====================================================================#
#=== FILE       : geometry                                        ===#
#=== AUTHORS    : Alberto Delgado, Alberto Vital                  ===#
#=== CONTACT    : a.delgado@upm.es / www.magnetisim.com           ===#
#=== DESCRIPTION: TDK Geometries                                  ===#
#=== CREATED    : 17/03/2026                                      ===#
#=== UPDATED    : 28/03/2026                                      ===#
#====================================================================#
#====================================================================#
# TDK → MAGNETISiM (XY):
# A = A  
# B = D  
# C = G  
# D = E  
# E = B  
# F1 = C 
# F2 = F 
# https://www.tdk-electronics.tdk.com/en/ferrites
# https://product.tdk.com/en/search/ferrite/ferrite/ferrite-core/catalog#title_group2_100012_1000000158821
#=====================================================================
#=== IMPORTS =========================================================
#=====================================================================

base_return = {"A": 0, "B": 0, "Bp": 0, "C": 0, "Cp": 0, "D": 0, "E": 0, "F": 0, "G": 0, "I": 0, "Gap": 0, "Ae": 0, "Ve": 0, "Mass": 0}



#=====================================================================
#===  Layout =========================================================
#=====================================================================

# Cores:
# E, EI, EPlanar, EIPlanar, EL, ELT, EC, EIC, U
# PQ, PQI, P, PH, PM, RM, ER, ERPlanar, EIRPlanar, ETD



#=====================================================================
#===  XY Geometry ====================================================
#=====================================================================

#=== [1] E Geometry =========================================================
def EGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "E8-Z":             {"A": 8.3,    "B": 6.0,    "C": 1.85,   "D": 4.0,    "E": 3.0,    "F": 3.6,    "Gap": 0, "Ae": 7.0,   "Ve": 134,    "Mass": 0.7},
        "E10/11-Z":         {"A": 10.2,   "B": 7.7,    "C": 2.45,   "D": 5.5,    "E": 4.2,    "F": 4.75,   "Gap": 0, "Ae": 12.1,  "Ve": 315,    "Mass": 1.5},
        "F12.6-Z":          {"A": 12.7,   "B": 8.8,    "C": 3.65,   "D": 6.4,    "E": 4.65,   "F": 3.6,    "Gap": 0, "Ae": 13.0,  "Ve": 385,    "Mass": 2.0},
        "E13-Z":            {"A": 13.0,   "B": 10.0,   "C": 2.75,   "D": 6.0,    "E": 4.6,    "F": 6.15,   "Gap": 0, "Ae": 17.1,  "Ve": 517,    "Mass": 2.7},
        "E16-Z":            {"A": 16.0,   "B": 11.7,   "C": 4.0,    "D": 7.15,   "E": 5.0,    "F": 4.8,    "Gap": 0, "Ae": 19.0,  "Ve": 656,    "Mass": 3.3},
        "EE16-Z":           {"A": 16.0,   "B": 12.5,   "C": 3.18,   "D": 7.15,   "E": 5.5,    "F": 6.8,    "Gap": 0, "Ae": 21.7,  "Ve": 795,    "Mass": 4.1},
        "F16-Z":            {"A": 16.1,   "B": 11.3,   "C": 4.55,   "D": 8.05,   "E": 5.9,    "F": 4.5,    "Gap": 0, "Ae": 20.1,  "Ve": 754,    "Mass": 3.9},
        "E19-Z":            {"A": 19.1,   "B": 14.2,   "C": 4.55,   "D": 7.95,   "E": 5.6,    "F": 5.0,    "Gap": 0, "Ae": 23.0,  "Ve": 906,    "Mass": 4.8},
        "E19/16-Z":         {"A": 19.29,  "B": 14.05,  "C": 4.75,   "D": 8.1,    "E": 5.715,  "F": 4.75,   "Gap": 0, "Ae": 22.4,  "Ve": 876,    "Mass": 4.8},
        "E20/20/5-Z":       {"A": 20.15,  "B": 12.8,   "C": 5.0,    "D": 10.0,   "E": 6.5,    "F": 5.1,    "Gap": 0, "Ae": 31.0,  "Ve": 1340,   "Mass": 7.5},
        "F20-Z":            {"A": 20.0,   "B": 14.1,   "C": 5.7,    "D": 9.9,    "E": 7.2,    "F": 5.65,   "Gap": 0, "Ae": 33.5,  "Ve": 1500,   "Mass": 7.4},
        "E22-Z":            {"A": 22.0,   "B": 13.0,   "C": 5.75,   "D": 9.35,   "E": 5.35,   "F": 5.75,   "Gap": 0, "Ae": 41.0,  "Ve": 1620,   "Mass": 8.8},
        "E25/19-Z":         {"A": 25.4,   "B": 18.55,  "C": 6.35,   "D": 9.46,   "E": 6.41,   "F": 6.29,   "Gap": 0, "Ae": 40.0,  "Ve": 1950,   "Mass": 9.1},
        "F25-Z":            {"A": 25.05,  "B": 17.5,   "C": 7.25,   "D": 12.55,  "E": 8.95,   "F": 7.2,    "Gap": 0, "Ae": 51.8,  "Ve": 2990,   "Mass": 15.0},
        "E25.4-Z":          {"A": 25.4,   "B": 18.5,   "C": 6.35,   "D": 9.66,   "E": 6.48,   "F": 6.35,   "Gap": 0, "Ae": 40.3,  "Ve": 1963,   "Mass": 10.0},
        "E30-Z":            {"A": 30.0,   "B": 19.7,   "C": 10.7,   "D": 13.15,  "E": 8.15,   "F": 10.7,   "Gap": 0, "Ae": 109.0, "Ve": 6290,   "Mass": 32.0},
        "E30/30/7-Z":       {"A": 30.1,   "B": 19.5,   "C": 6.95,   "D": 15.0,   "E": 9.95,   "F": 7.05,   "Gap": 0, "Ae": 59.7,  "Ve": 4000,   "Mass": 22.0},
        "F32-Z":            {"A": 32.1,   "B": 22.7,   "C": 9.2,    "D": 16.1,   "E": 11.6,   "F": 9.15,   "Gap": 0, "Ae": 83.2,  "Ve": 6180,   "Mass": 32.0},
        "E35/28B-Z":        {"A": 34.6,   "B": 25.0,   "C": 9.4,    "D": 14.27,  "E": 9.78,   "F": 9.31,   "Gap": 0, "Ae": 84.9,  "Ve": 5907,   "Mass": 28.0},
        "E35-Z":            {"A": 34.54,  "B": 24.89,  "C": 9.39,   "D": 14.35,  "E": 9.71,   "F": 9.53,   "Gap": 0, "Ae": 89.3,  "Ve": 6179,   "Mass": 57.0},
        "E40-Z":            {"A": 40.0,   "B": 27.4,   "C": 10.7,   "D": 17.0,   "E": 10.25,  "F": 10.7,   "Gap": 0, "Ae": 128.0, "Ve": 9890,   "Mass": 50.0},
        "E41/33C-Z":        {"A": 41.07,  "B": 28.55,  "C": 12.64,  "D": 16.78,  "E": 10.38,  "F": 12.57,  "Gap": 0, "Ae": 157.0, "Ve": 12200,  "Mass": 64.0},
        "E42/42/15-Z":      {"A": 42.15,  "B": 29.5,   "C": 11.95,  "D": 21.0,   "E": 15.15,  "F": 14.95,  "Gap": 0, "Ae": 182.0, "Ve": 17600,  "Mass": 80.0},
        "E42/42/20-Z":      {"A": 42.15,  "B": 29.5,   "C": 11.95,  "D": 21.0,   "E": 15.15,  "F": 19.7,   "Gap": 0, "Ae": 235.0, "Ve": 22900,  "Mass": 116.0},
        "E47/39-Z":         {"A": 47.12,  "B": 31.72,  "C": 15.62,  "D": 19.63,  "E": 12.2,   "F": 15.62,  "Gap": 0, "Ae": 242.0, "Ve": 21930,  "Mass": 108.0},
        "E50-Z":            {"A": 50.0,   "B": 34.2,   "C": 14.6,   "D": 21.3,   "E": 12.75,  "F": 14.6,   "Gap": 0, "Ae": 226.0, "Ve": 21600,  "Mass": 116.0},
        "E55/55/21-Z":      {"A": 55.15,  "B": 37.5,   "C": 16.95,  "D": 27.5,   "E": 18.8,   "F": 20.7,   "Gap": 0, "Ae": 354.0, "Ve": 43700,  "Mass": 234.0},
        "E57/47-Z":         {"A": 56.57,  "B": 38.1,   "C": 18.8,   "D": 23.6,   "E": 14.63,  "F": 18.8,   "Gap": 0, "Ae": 344.0, "Ve": 35100,  "Mass": 190.0},
        "E60-Z":            {"A": 60.0,   "B": 43.8,   "C": 15.6,   "D": 22.3,   "E": 14.05,  "F": 15.6,   "Gap": 0, "Ae": 247.0, "Ve": 27100,  "Mass": 135.0}
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(EGeometry("E60-Z").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY','3LEG','SET')

#=== [2] EI Geometry =========================================================
def EIGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "EI12.5-Z":        {"A": 12.4,  "B": 8.8,   "C": 2.4,   "D": 7.4,   "E": 5.1,   "F": 4.85,  "I": 1.5, "Gap": 0, "Ae": 14.4,  "Ve": 308,   "Mass": 1.9},
        "EI16-Z":          {"A": 16.0,  "B": 11.6,  "C": 4.0,   "D": 12.2,  "E": 10.2,  "F": 4.8,   "I": 2.0, "Gap": 0, "Ae": 19.8,  "Ve": 685,   "Mass": 3.3},
        "EI19-Z":          {"A": 20.0,  "B": 14.3,  "C": 4.55,  "D": 13.55, "E": 11.15, "F": 5.0,   "I": 2.3, "Gap": 0, "Ae": 24.0,  "Ve": 950,   "Mass": 5.1},
        "EI22-Z":          {"A": 22.0,  "B": 13.0,  "C": 5.75,  "D": 14.55, "E": 10.55, "F": 5.75,  "I": 4.5, "Gap": 0, "Ae": 42.0,  "Ve": 1650,  "Mass": 9.8},
        "EI22/19/6-Z":     {"A": 22.0,  "B": 15.75, "C": 5.75,  "D": 14.7,  "E": 10.7,  "F": 5.75,  "I": 4.0, "Gap": 0, "Ae": 37.0,  "Ve": 1550,  "Mass": 8.5},
        "EI25-Z":          {"A": 25.3,  "B": 19.0,  "C": 6.5,   "D": 15.55, "E": 12.35, "F": 6.75,  "I": 2.7, "Gap": 0, "Ae": 41.0,  "Ve": 1930,  "Mass": 9.8},
        "EI28-Z":          {"A": 28.0,  "B": 18.4,  "C": 7.2,   "D": 16.75, "E": 12.25, "F": 10.6,  "I": 3.5, "Gap": 0, "Ae": 86.0,  "Ve": 4150,  "Mass": 22.0},
        "EI30-Z":          {"A": 30.0,  "B": 19.7,  "C": 10.7,  "D": 21.25, "E": 16.25, "F": 10.7,  "I": 5.5, "Gap": 0, "Ae": 111.0, "Ve": 6440,  "Mass": 34.0},
        "EI33/29/13-Z":    {"A": 33.0,  "B": 23.4,  "C": 9.7,   "D": 23.75, "E": 19.25, "F": 12.7,  "I": 5.0, "Gap": 0, "Ae": 119.0, "Ve": 8030,  "Mass": 41.0},
        "EI35-Z":          {"A": 35.0,  "B": 24.5,  "C": 10.0,  "D": 24.35, "E": 18.25, "F": 10.0,  "I": 4.6, "Gap": 0, "Ae": 101.0, "Ve": 6780,  "Mass": 36.0},
        "EI40-Z":          {"A": 40.0,  "B": 27.2,  "C": 11.65, "D": 27.25, "E": 20.25, "F": 11.65, "I": 7.5, "Gap": 0, "Ae": 148.0, "Ve": 11400, "Mass": 60.0},
        "EI50-Z":          {"A": 50.0,  "B": 33.5,  "C": 14.6,  "D": 33.35, "E": 24.75, "F": 14.6,  "I": 9.0, "Gap": 0, "Ae": 230.0, "Ve": 21620, "Mass": 115.0},
        "EI60-Z":          {"A": 60.0,  "B": 43.6,  "C": 15.6,  "D": 35.85, "E": 27.85, "F": 15.6,  "I": 8.5, "Gap": 0, "Ae": 247.0, "Ve": 26900, "Mass": 139.0}
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(EIGeometry("EI12.5-Z").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY','3LEG','WITH_I')

#=== [3] EPlanar Geometry =========================================================
def EPlanarGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "E14/5/5-Z":      {"A": 14.0,  "B": 11.0,  "C": 3.0,   "D": 3.50,  "E": 2.00,  "F": 5.0,   "Gap": 0, "Ae": 15.0,  "Ve": 251,   "Mass": 1.3},
        "E18/6/10-Z":     {"A": 18.0,  "B": 14.0,  "C": 4.0,   "D": 4.00,  "E": 2.00,  "F": 10.0,  "Gap": 0, "Ae": 40.0, "Ve": 811,    "Mass": 4.4},
        "E22/8/16-Z":     {"A": 21.8,  "B": 16.8,  "C": 5.0,   "D": 5.70,  "E": 3.20,  "F": 15.8,  "Gap": 0, "Ae": 79.0, "Ve": 2060,   "Mass": 11.0},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(EPlanarGeometry("E22/8/16-Z").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY','3LEG','SET')

#=== [4] EIPlanar Geometry =========================================================
def EIPlanarGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "EI14/5/5-Z":      {"A": 14.0,  "B": 11.0,  "C": 3.0,   "D": 3.50,  "E": 2.00,  "F": 5.0,   "I": 1.5, "Gap": 0, "Ae": 15.0,  "Ve": 251,   "Mass": 1.3},
        "EI18/6/10-Z":     {"A": 18.0,  "B": 14.0,  "C": 4.0,   "D": 4.00,  "E": 2.00,  "F": 10.0,  "I": 2.0, "Gap": 0, "Ae": 40.0, "Ve": 811,    "Mass": 4.4},
        "EI22/8/16-Z":     {"A": 21.8,  "B": 16.8,  "C": 5.0,   "D": 5.70,  "E": 3.20,  "F": 15.8,  "I": 2.5, "Gap": 0, "Ae": 79.0, "Ve": 2060,   "Mass": 11.0},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(EIPlanarGeometry("EI22/8/16-Z").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY','3LEG','WITH_I')

#=== [5] EL Geometry =========================================================
def ELGeometry(ReferenceCores: str = None, type: bool = False): 
    core_geometries = {
        "EL11X4-Z":      {"A": 11.00,  "B":  9.17,  "C": 2.78, "D": 2.01,  "E": 1.00, "F": 6.40,   "G": 8.80,   "Gap": 0, "Ae": 16.5, "Ve":  226, "Mass": 1.3},
        "EL13X4.4-Z":    {"A": 13.00,  "B": 10.83,  "C": 3.29, "D": 2.19,  "E": 1.00, "F": 7.56,   "G": 10.40,  "Gap": 0, "Ae": 23.1, "Ve":  357, "Mass": 2.0},
        "EL15.5X5.8-Z":  {"A": 15.50,  "B": 12.92,  "C": 3.92, "D": 2.92,  "E": 1.50, "F": 9.01,   "G": 12.40,  "Gap": 0, "Ae": 32.9, "Ve":  646, "Mass": 3.5},
        "EL18X7.3-Z":    {"A": 18.00,  "B": 15.00,  "C": 4.55, "D": 3.65,  "E": 2.00, "F": 10.47,  "G": 14.40,  "Gap": 0, "Ae": 44.3, "Ve": 1050, "Mass": 6.0},
        "EL20X7.7-Z":    {"A": 20.00,  "B": 16.67,  "C": 5.06, "D": 3.83,  "E": 2.00, "F": 11.63,  "G": 16.00,  "Gap": 0, "Ae": 54.6, "Ve": 1400, "Mass": 7.8},
        "EL22X8-Z":      {"A": 22.00,  "B": 18.33,  "C": 5.56, "D": 4.02,  "E": 2.00, "F": 12.79,  "G": 17.60,  "Gap": 0, "Ae": 66.2, "Ve": 1810, "Mass": 10},
        "EL25X8.6-Z":    {"A": 25.00,  "B": 20.83,  "C": 6.32, "D": 4.29,  "E": 2.00, "F": 14.54,  "G": 20.00,  "Gap": 0, "Ae": 85.6, "Ve": 2570, "Mass": 15},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(ELGeometry("EL25X8.6-Z").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY','1LEG','SET')

#=== [6] ELT Geometry =========================================================
def ELTGeometry(ReferenceCores: str = None, type: bool = False): 
    core_geometries = {
        "ELT11X3-Z":      {"A": 11.00,  "B": 9.17,   "C": 2.78,  "D": 2.01,  "E": 1.00,  "F": 6.4,   "G": 8.80,  "I": 1.01, "Gap": 0, "Ae": 16.6,  "Ve": 194,  "Mass": 1.1},
        "ELT11X4-Z":      {"A": 11.00,  "B": 9.17,   "C": 2.78,  "D": 3.01,  "E": 2.00,  "F": 6.4,   "G": 8.80,  "I": 1.01, "Gap": 0, "Ae": 16.5,  "Ve": 226,  "Mass": 1.3},
        "ELT13X3.4-Z":    {"A": 13.00,  "B": 10.83,  "C": 3.29,  "D": 2.19,  "E": 1.00,  "F": 7.56,  "G": 10.40, "I": 1.19, "Gap": 0, "Ae": 23.2,  "Ve": 312,  "Mass": 1.8},
        "ELT13X4.4-Z":    {"A": 13.00,  "B": 10.83,  "C": 3.29,  "D": 3.19,  "E": 2.00,  "F": 7.56,  "G": 10.40, "I": 1.19, "Gap": 0, "Ae": 23.1,  "Ve": 357,  "Mass": 2.0},
        "ELT15.5X4.3-Z":  {"A": 15.50,  "B": 12.92,  "C": 3.92,  "D": 2.92,  "E": 1.50,  "F": 9.01,  "G": 12.40, "I": 1.42, "Gap": 0, "Ae": 33.1,  "Ve": 550,  "Mass": 3.0},
        "ELT15.5X5.8-Z":  {"A": 15.50,  "B": 12.92,  "C": 3.92,  "D": 4.42,  "E": 3.00,  "F": 9.01,  "G": 12.40, "I": 1.42, "Gap": 0, "Ae": 32.9,  "Ve": 646,  "Mass": 3.5},
        "ELT18X5.3-Z":    {"A": 18.00,  "B": 15.00,  "C": 4.55,  "D": 3.65,  "E": 2.00,  "F": 10.47, "G": 14.40, "I": 1.65, "Gap": 0, "Ae": 44.5,  "Ve": 882,  "Mass": 5.0},
        "ELT18X7.3-Z":    {"A": 18.00,  "B": 15.00,  "C": 4.55,  "D": 5.65,  "E": 4.00,  "F": 10.47, "G": 14.40, "I": 1.65, "Gap": 0, "Ae": 44.3,  "Ve": 1050, "Mass": 6.0},
        "ELT20X5.7-Z":    {"A": 20.00,  "B": 16.67,  "C": 5.06,  "D": 3.83,  "E": 2.00,  "F": 11.63, "G": 16.00, "I": 1.83, "Gap": 0, "Ae": 54.9,  "Ve": 1180, "Mass": 6.7},
        "ELT20X7.7-Z":    {"A": 20.00,  "B": 16.67,  "C": 5.06,  "D": 5.83,  "E": 4.00,  "F": 11.63, "G": 16.00, "I": 1.83, "Gap": 0, "Ae": 54.6,  "Ve": 1400, "Mass": 7.8},
        "ELT22X6-Z":      {"A": 22.00,  "B": 18.33,  "C": 5.56,  "D": 4.02,  "E": 2.00,  "F": 12.79, "G": 17.60, "I": 2.02, "Gap": 0, "Ae": 66.6,  "Ve": 1560, "Mass": 9.0},
        "ELT22X8-Z":      {"A": 22.00,  "B": 18.33,  "C": 5.56,  "D": 6.02,  "E": 4.00,  "F": 12.79, "G": 17.60, "I": 2.02, "Gap": 0, "Ae": 66.2,  "Ve": 1810, "Mass": 10.0},
        "ELT25X6.6-Z":    {"A": 25.00,  "B": 20.83,  "C": 6.32,  "D": 4.29,  "E": 2.00,  "F": 14.54, "G": 20.00, "I": 2.29, "Gap": 0, "Ae": 86.0,  "Ve": 2230, "Mass": 13.0},
        "ELT25X8.6-Z":    {"A": 25.00,  "B": 20.83,  "C": 6.32,  "D": 6.29,  "E": 4.00,  "F": 14.54, "G": 20.00, "I": 2.29, "Gap": 0, "Ae": 85.6,  "Ve": 2570, "Mass": 15.0}
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(ELTGeometry("ELT25X8.6-Z").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY','1LEG','WITH_I')

#=== [7] EC Geometry =========================================================
def ECGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "EC70X69X16-Z":   {"A": 70.0,  "B": 43.3,  "Bp": 43.3,  "C": 16.4,  "Cp": 0, "D": 34.5,  "E": 22.75, "F": 16.4,  "G": 16.4,  "Gap": 0, "Ae": 280.0,  "Ve": 40420,  "Mass": 250},
        "EC90X90X30-Z":   {"A": 90.0,  "B": 68.5,  "Bp": 68.5,  "C": 30.0,  "Cp": 0, "D": 45.0,  "E": 35.5,  "F": 30.0,  "G": 30.0,  "Gap": 0, "Ae": 626.0,  "Ve": 138270, "Mass": 635},
        "EC120X101X30-Z": {"A": 120.0, "B": 93.3,  "Bp": 93.3,  "C": 30.0,  "Cp": 0, "D": 50.5,  "E": 35.5,  "F": 30.0,  "G": 30.0,  "Gap": 0, "Ae": 773.0,  "Ve": 196490, "Mass": 986},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(ECGeometry("EC70X69X16-Z").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY','1LEG','SET')

#=== [8] EIC Geometry =========================================================
def EICGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "EIC70X46X16-Z":   {"A": 70.0,  "B": 43.3,  "Bp": 43.3,  "C": 16.4,  "Cp": 0, "D": 23.125, "E": 11.375, "F": 22.75, "G": 22.75, "I": 11.75, "Gap": 0, "Ae": 297.0,  "Ve": 30601,  "Mass": 188},
        "EIC90X55X30-Z":   {"A": 90.0,  "B": 68.5,  "Bp": 68.5,  "C": 30.0,  "Cp": 0, "D": 27.5,   "E": 17.525, "F": 35.5,  "G": 35.5,  "I": 10.0,  "Gap": 0, "Ae": 624.0,  "Ve": 94432,  "Mass": 469},
        "EIC120X65X30-Z":  {"A": 120.0, "B": 93.3,  "Bp": 93.3,  "C": 30.0,  "Cp": 0, "D": 32.75,  "E": 17.525, "F": 25.5,  "G": 25.5,  "I": 15.0,  "Gap": 0, "Ae": 794.0,  "Ve": 146310, "Mass": 747},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(EICGeometry("EIC70X46X16-Z").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY','1LEG','WITH_I')

#=== [9] U Geometry =========================================================
def UGeometry(ReferenceCores: str = None, type: bool = False): 
    core_geometries = {
    "U79x129x31" : {"A": 79.0,  "B": 34.0, "D": 64.5,  "E": 42.5, "F": 31.5, "Gap": 0, "Ae": 693, "Ve": 214220, "Mass": 1080},
    "U80x150x30N": {"A": 80.0,  "B": 39.0, "D": 75.0,  "E": 55.0, "F": 30.0, "Gap": 0, "Ae": 600, "Ve": 217700, "Mass": 1095},
    "U100x151x30": {"A": 100.0, "B": 39.0, "D": 75.5,  "E": 45.0, "F": 30.0, "Gap": 0, "Ae": 915, "Ve": 324860, "Mass": 1630},
    "U101x115x25": {"A": 101.0, "B": 50.0, "D": 57.5,  "E": 32.0, "F": 25.4, "Gap": 0, "Ae": 648, "Ve": 200350, "Mass": 1000},
    "U120x160x20": {"A": 120.0, "B": 59.0, "D": 80.0,  "E": 50.0, "F": 20.0, "Gap": 0, "Ae": 600, "Ve": 248550, "Mass": 1240},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(UGeometry("U120x160x20").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY', '2LEG', 'SET')

#=== [10] UI Geometry =========================================================
def UIGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "U79x129x31/I79-Z":  {"A": 79.0,  "B": 34.0, "D": 64.5,  "E": 42.5,  "F": 31.5, "I": 22.0, "Gap": 0, "Ae": 693,  "Ve": 214220*0.5 + 153000, "Mass": 1080*0.5 + 540},
        "U100x151x30/I100-Z":{"A": 100.0, "B": 39.0, "D": 75.5,  "E": 45.0,  "F": 30.0, "I": 30.0, "Gap": 0, "Ae": 915,  "Ve": 324860*0.5 + 275000, "Mass": 1630*0.5 + 815},
        "U101x115x25/I101-Z":{"A": 101.0, "B": 50.0, "D": 57.5,  "E": 32.0,  "F": 25.4, "I": 25.0, "Gap": 0, "Ae": 648,  "Ve": 200350*0.5 + 162000, "Mass": 1000*0.5 + 500},
        "U120x160x20/I120-Z":{"A": 120.0, "B": 59.0, "D": 80.0,  "E": 50.0,  "F": 20.0, "I": 30.0, "Gap": 0, "Ae": 600,  "Ve": 248550*0.5 + 180000, "Mass": 1240*0.5 + 620},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(UIGeometry("U79x129x31/I79-Z").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY', '2LEG', 'WITH_I')

#=====================================================================
#===  RZ Geometry ====================================================
#=====================================================================

#=== [1] EQ Geometry =========================================================
def EQGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "EQ20/6.3/14-Z": {"A": 20.0,  "B": 12.86, "Bp": 18.0,  "C": 8.8,  "Cp": 0, "D": 3.15, "E": 2.05, "F": 14.0, "Gap": 0, "Ae": 59.0,  "Ve": 1960,  "Mass": 5.5},
        "EQ25/5.6/18-Z": {"A": 25.0,  "B": 15.2,  "Bp": 22.0,  "C": 11.0, "Cp": 0, "D": 2.80, "E": 1.60, "F": 18.0, "Gap": 0, "Ae": 93.5,  "Ve": 3082,  "Mass": 9.5},
        "EQ30/8/20-Z":   {"A": 30.0,  "B": 19.45, "Bp": 26.0,  "C": 11.0, "Cp": 0, "D": 4.00, "E": 2.65, "F": 20.0, "Gap": 0, "Ae": 108.0, "Ve": 4970,  "Mass": 11.5},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(EQGeometry("EQ20/6.3/14-Z").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('RZ', '1LEG', 'SET')

#=== [2] EQPLT Geometry =========================================================
def EQPLTGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "EIQ20/6.3/14-Z": {"A": 20.0,  "B": 12.86, "Bp": 18.0,  "C": 8.8,  "Cp": 0, "D": 3.15, "E": 2.05, "F": 14.0, "I": 2.3, "Gap": 0, "Ae":  59.8, "Ve": 1500,  "Mass": 4.25},
        "EIQ25/5.6/18-Z": {"A": 25.0,  "B": 15.2,  "Bp": 22.0,  "C": 11.0, "Cp": 0, "D": 2.80, "E": 1.60, "F": 18.0, "I": 2.3, "Gap": 0, "Ae":  89.7, "Ve": 2370,  "Mass": 7.3},
        "EIQ30/8/20-Z":   {"A": 30.0,  "B": 19.45, "Bp": 26.0,  "C": 11.0, "Cp": 0, "D": 4.00, "E": 2.65, "F": 20.0, "I": 2.7, "Gap": 0, "Ae": 108.0, "Ve": 3400,  "Mass": 10.75},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(EQPLTGeometry("EIQ20/6.3/14-Z").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('RZ', '1LEG', 'WITH_I')

#=== [3] PQ Geometry =========================================================
def PQGeometry(ReferenceCores: str = None, type: bool = False): # TODO: Falta meter los PQ de large power
    # https://product.tdk.com/system/files/dam/doc/product/ferrite/ferrite/ferrite-core/catalog/ferrite_mz_large_pq_en.pdf 
    core_geometries = {
        "PQ20/16Z-12": {"A": 20.5,  "B": 12,   "Bp": 18.0,  "C": 8.8,   "Cp": 0, "D": 8.1,    "E": 5.15,  "F": 0.9*8.8,   "G": 14.0, "Gap": 0, "Ae": 62,  "Ve": 2310,  "Mass": 13},
        "PQ20/20Z-12": {"A": 20.5,  "B": 12,   "Bp": 18.0,  "C": 8.8,   "Cp": 0, "D": 10.1,   "E": 7.15,  "F": 0.9*8.8,   "G": 14.0, "Gap": 0, "Ae": 62,  "Ve": 2790,  "Mass": 15},
        "PQ26/20Z-12": {"A": 26.5,  "B": 15.5, "Bp": 22.5,  "C": 12.0,  "Cp": 0, "D": 10.075, "E": 5.75,  "F": 0.9*12.0,  "G": 19.0, "Gap": 0, "Ae": 119, "Ve": 5490,  "Mass": 31},
        "PQ26/25Z-12": {"A": 26.5,  "B": 15.5, "Bp": 22.5,  "C": 12.0,  "Cp": 0, "D": 12.375, "E": 8.05,  "F": 0.9*12.0,  "G": 19.0, "Gap": 0, "Ae": 118, "Ve": 6530,  "Mass": 36},
        "PQ32/20Z-12": {"A": 32.0,  "B": 19,   "Bp": 27.5,  "C": 13.45, "Cp": 0, "D": 10.275, "E": 5.75,  "F": 0.9*13.45, "G": 22.0, "Gap": 0, "Ae": 170, "Ve": 9420,  "Mass": 42},
        "PQ32/30Z-12": {"A": 32.0,  "B": 19,   "Bp": 27.5,  "C": 13.45, "Cp": 0, "D": 15.175, "E": 10.65, "F": 0.9*13.45, "G": 22.0, "Gap": 0, "Ae": 161, "Ve": 12000, "Mass": 55},
        "PQ35/35Z-12": {"A": 35.1,  "B": 23.5, "Bp": 32.0,  "C": 14.35, "Cp": 0, "D": 17.375, "E": 12.5,  "F": 0.9*14.35, "G": 26.0, "Gap": 0, "Ae": 196, "Ve": 17300, "Mass": 73},
        "PQ40/40Z-12": {"A": 40.5,  "B": 28,   "Bp": 37.0,  "C": 14.9,  "Cp": 0, "D": 19.875, "E": 14.75, "F": 0.9*14.9,  "G": 28.0, "Gap": 0, "Ae": 201, "Ve": 20500, "Mass": 95},
        "PQ50/50Z-12": {"A": 50.0,  "B": 31.5, "Bp": 44.0,  "C": 20.0,  "Cp": 0, "D": 24.975, "E": 18.05, "F": 0.9*20.0,  "G": 32.0, "Gap": 0, "Ae": 328, "Ve": 37200, "Mass": 195}
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(PQGeometry("PQ50/50Z-12").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('RZ','1LEG','SET')

#=== [4] PQI Geometry =========================================================
def PQIGeometry(ReferenceCores: str = None, type: bool = False):
	core_geometries = {
		"PQI16/7.8Z-12": {"A": 16.40, "B": 9.6,  "C": 7.00, "Cp": 0, "D": 5.40, "E": 3.05, "F": 7.00, "G": 11.20, "Bp": 14.40, "I": 2.35, "Gap": 0, "Ae": 41.8, "Ve": 815,  "Mass": 5},
		"PQI20/9Z-12":   {"A": 20.50, "B": 12,   "C": 8.80, "Cp": 0, "D": 6.00, "E": 3.05, "F": 8.80, "G": 14.00, "Bp": 18.00, "I": 2.95, "Gap": 0, "Ae": 66,   "Ve": 1510, "Mass": 9},
		"PQI26/12Z-12":  {"A": 26.50, "B": 15.5, "C": 12.00,"Cp": 0, "D": 7.30, "E": 3.10, "F": 12.00,"G": 19.00, "Bp": 22.50, "I": 4.20, "Gap": 0, "Ae": 123,  "Ve": 3410, "Mass": 21}
	}
	if not type:
		if ReferenceCores == "GeoParam":
			return tuple(PQIGeometry("PQI16/7.8Z-12").keys())[:-3]
		else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
	return ('RZ','1LEG','WITH_I')

#=== [5] P Geometry =========================================================
def PGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "P9/5-Z":       {"A":  9.3,  "B": 2.0,  "Bp":  7.5,  "C":  3.9,  "Cp": 2.1, "D": 2.70, "E": 1.80,  "F":  7.5,  "Gap": 0, "Ae": 10.1,  "Ve":  126,   "Mass":  0.8},
        "P11/7-Z":      {"A": 11.1,  "B": 2.2,  "Bp":  9.0,  "C":  4.7,  "Cp": 2.1, "D": 3.25, "E": 2.20,  "F":  9.0,  "Gap": 0, "Ae": 16.2,  "Ve":  251,   "Mass":  1.8},
        "P14/8-Z":      {"A": 14.3,  "B": 2.7,  "Bp": 11.6,  "C":  6.0,  "Cp": 3.1, "D": 4.20, "E": 2.80,  "F": 11.6,  "Gap": 0, "Ae": 25.1,  "Ve":  495,   "Mass":  3.2},
        "P18/11-Z":     {"A": 18.4,  "B": 3.8,  "Bp": 14.9,  "C":  7.6,  "Cp": 3.1, "D": 5.30, "E": 3.60,  "F": 14.9,  "Gap": 0, "Ae": 43.3,  "Ve": 1120,   "Mass":  6.0},
        "P22/13-Z":     {"A": 22.0,  "B": 3.8,  "Bp": 17.9,  "C":  9.4,  "Cp": 4.4, "D": 6.70, "E": 4.60,  "F": 17.9,  "Gap": 0, "Ae": 63.4,  "Ve": 2000,   "Mass": 12.0},
        "P26/16-Z":     {"A": 25.5,  "B": 3.8,  "Bp": 21.2,  "C": 11.5,  "Cp": 5.4, "D": 8.05, "E": 5.50,  "F": 21.2,  "Gap": 0, "Ae": 93.3,  "Ve": 3530,   "Mass": 20.0},
        "P30/19-Z":     {"A": 30.0,  "B": 4.3,  "Bp": 25.0,  "C": 13.5,  "Cp": 5.4, "D": 9.40, "E": 6.50,  "F": 25.0,  "Gap": 0, "Ae": 137.0, "Ve": 6190,   "Mass": 34.0},
        "P36/22-Z":     {"A": 36.2,  "B": 4.9,  "Bp": 29.9,  "C": 16.2,  "Cp": 5.4, "D": 10.85,"E": 7.30,  "F": 29.9,  "Gap": 0, "Ae": 202.0, "Ve": 10700,  "Mass": 54.0},
        "P42/29-Z":     {"A": 42.4,  "B": 5.1,  "Bp": 35.6,  "C": 17.7,  "Cp": 5.4, "D": 14.70,"E": 10.15, "F": 35.6,  "Gap": 0, "Ae": 265.0, "Ve": 18200,  "Mass": 104.0},
        "P47/28-Z":     {"A": 47.0,  "B": 6.0,  "Bp": 39.0,  "C": 19.5,  "Cp": 6.5, "D": 14.0, "E": 9.5,   "F": 39.0,  "Gap": 0, "Ae": 308.0, "Ve": 21800,  "Mass": 130.0},
        "P66/56-Z":     {"A": 66.29, "B": 7.26, "Bp": 54.51, "C": 28.19, "Cp": 6.5, "D": 28.65,"E": 21.64, "F": 54.51, "Gap": 0, "Ae": 717.0, "Ve": 88200,  "Mass": 550.0}
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(PGeometry("P66/56-Z").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('RZ','1LEG','SET')

#=== [6] PH Geometry =========================================================
def PHGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "PH5.6/3.6-Z":  {"A":  5.75, "B": 1.5, "Bp":  4.5, "C":  2.5,  "Cp": 0.95, "D": 3.60,  "E": 2.80,  "F":  4.5,  "Gap": 0, "Ae":  0,  "Ve":    0,   "Mass":  0.2},
        "PH7.4/3.9-Z":  {"A":  7.4,  "B": 1.6, "Bp":  5.8, "C":  3.0,  "Cp": 1.38, "D": 3.95,  "E": 2.80,  "F":  5.8,  "Gap": 0, "Ae":  0,  "Ve":    0,   "Mass":  0.4},
        "PH9.4/4.8-Z":  {"A":  9.4,  "B": 2.0, "Bp":  7.5, "C":  3.9,  "Cp": 2.0,  "D": 4.80,  "E": 3.55,  "F":  7.5,  "Gap": 0, "Ae":  0,  "Ve":    0,   "Mass":  0.7},
        "PH14/7.5-Z":   {"A": 14.4,  "B": 3.3, "Bp": 11.6, "C":  6.0,  "Cp": 3.0,  "D": 7.50,  "E": 5.60,  "F": 11.6,  "Gap": 0, "Ae":  0,  "Ve":    0,   "Mass":  3.0},
        "PH26/9.2-Z":   {"A": 25.5,  "B": 3.8, "Bp": 21.2, "C": 11.5,  "Cp": 5.4,  "D": 9.20,  "E": 5.90,  "F": 21.2,  "Gap": 0, "Ae":  0,  "Ve":    0,   "Mass": 12.0}
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(PHGeometry("PH5.6/3.6-Z").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('RZ','1LEG','SET')

#=== [7] PM Geometry =========================================================
def PMGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "PM74/59-Z":   {"A":  74.0, "B": 34.0, "Bp": 57.5, "C": 29.5, "Cp": 5.4, "D": 29.5,  "E": 20.35, "F": 57.5,  "Gap": 0, "Ae":  790, "Ve": 101000, "Mass":  537},
        "PM87/70-Z":   {"A":  87.0, "B": 41.0, "Bp": 67.0, "C": 31.7, "Cp": 8.5, "D": 35.0,  "E": 24.0,  "F": 67.0,  "Gap": 0, "Ae":  910, "Ve": 133000, "Mass":  770},
        "PM114/93-Z":  {"A": 114.0, "B": 53.5, "Bp": 88.0, "C": 43.0, "Cp": 5.4, "D": 46.5,  "E": 31.5,  "F": 88.0,  "Gap": 0, "Ae": 1720, "Ve": 344000, "Mass": 1940}
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(PMGeometry("PM74/59-Z").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('RZ','1LEG','SET')

#=== [8] RM Geometry =========================================================
def RMGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "RM4Z-12":  {"A": 10.8,  "B": 5.8,  "Bp": 8.15,  "C": 3.8,  "Cp": 0, "D": 5.2,   "E": 3.6,   "F": 4.45,  "G": 9.63,  "Gap": 0, "Ae": 14,  "Ve": 318,   "Mass": 1.7},
        "RM5Z-12":  {"A": 14.3,  "B": 6.0,  "Bp": 10.4,  "C": 4.8,  "Cp": 0, "D": 5.2,   "E": 3.25,  "F": 6.6,   "G": 12.05, "Gap": 0, "Ae": 23.7, "Ve": 530,   "Mass": 3.0},
        "RM6Z-12":  {"A": 17.6,  "B": 8.4,  "Bp": 12.65, "C": 6.3,  "Cp": 0, "D": 6.2,   "E": 4.1,   "F": 8.0,   "G": 14.4,  "Gap": 0, "Ae": 36.6, "Ve": 1050,  "Mass": 5.5},
        "RM8Z-12":  {"A": 22.75, "B": 9.8,  "Bp": 17.3,  "C": 8.4,  "Cp": 0, "D": 8.2,   "E": 5.5,   "F": 10.8,  "G": 19.35, "Gap": 0, "Ae": 64.0, "Ve": 2430,  "Mass": 13.0},
        "RM10Z-12": {"A": 27.85, "B": 11.3, "Bp": 21.65, "C": 10.7, "Cp": 0, "D": 9.3,   "E": 6.35,  "F": 13.25, "G": 24.15, "Gap": 0, "Ae": 98.0, "Ve": 4310,  "Mass": 23.0},
        "RM12Z-12": {"A": 36.75, "B": 12.9, "Bp": 25.5,  "C": 12.6, "Cp": 0, "D": 11.75, "E": 8.55,  "F": 16.0,  "G": 29.25, "Gap": 0, "Ae": 140.0, "Ve": 7970,  "Mass": 42.0},
        "RM14Z-12": {"A": 41.6,  "B": 17.0, "Bp": 29.5,  "C": 14.75, "Cp": 0, "D": 14.4, "E": 10.55, "F": 18.7,  "G": 34.2,  "Gap": 0, "Ae": 178.0, "Ve": 12500, "Mass": 70.0}
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(RMGeometry("RM14Z-12").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('RZ','1LEG','SET')

#=== [9] ER Geometry =========================================================
def ERGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "ER25.5-Z":     {"A": 25.5,  "B": 19.8, "Bp": 19.8,  "C":  7.5,  "D": 12.75, "E":  6.2,  "F":  7.5,  "Gap": 0, "Ae":  44.8, "Ve":  2160,  "Mass": 11},
        "ER28-Z":       {"A": 28.55, "B": 21.75,"Bp": 21.75, "C":  9.9,  "D": 14.0,  "E":  9.65, "F":  9.9,  "Gap": 0, "Ae":  82.1, "Ve":  5250,  "Mass": 28},
        "ER28L-Z":      {"A": 28.55, "B": 21.75,"Bp": 21.75, "C":  9.9,  "D": 16.9,  "E": 12.53, "F":  9.9,  "Gap": 0, "Ae":  81.4, "Ve":  6150,  "Mass": 33},
        "ER35-Z":       {"A": 35.0,  "B": 26.15,"Bp": 26.15, "C": 11.3,  "D": 20.7,  "E": 14.7,  "F": 11.3,  "Gap": 0, "Ae": 107.0, "Ve":  9720,  "Mass": 52},
        "ER40-Z":       {"A": 40.0,  "B": 29.6, "Bp": 29.6,  "C": 13.3,  "D": 22.4,  "E": 15.4,  "F": 13.3,  "Gap": 0, "Ae": 149.0, "Ve": 14600,  "Mass": 78},
        "ER42-Z":       {"A": 42.0,  "B": 30.05,"Bp": 30.05, "C": 15.5,  "D": 22.4,  "E": 15.4,  "F": 15.5,  "Gap": 0, "Ae": 194.0, "Ve": 19200,  "Mass": 102},
        "ER42/42/20-Z": {"A": 42.15, "B": 31.8, "Bp": 31.8,  "C": 19.60, "D": 21.8,  "E": 15.25, "F": 17.3,  "Gap": 0, "Ae": 240.0, "Ve": 23700,  "Mass": 116},
        "ER49-Z":       {"A": 49.0,  "B": 36.4, "Bp": 36.4,  "C": 17.2,  "D": 18.0,  "E": 12.4,  "F": 17.2,  "Gap": 0, "Ae": 231.0, "Ve": 21100,  "Mass": 110}
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(ERGeometry("ER49-Z").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('RZ','1LEG','SET')

#=== [10] ERPlanar Geometry =========================================================
def ERPlanarGeometry(ReferenceCores: str = None, type: bool = False): 
    core_geometries = {
        "ER9.5/5-Z":        {"A": 9.5,   "B": 7.0,   "Bp": 7.0,   "C": 3.5,  "Cp": 0,  "D": 2.5,   "E": 1.6,   "F": 5.0,   "Gap": 0, "Ae": 8.47,  "Ve": 120,   "Mass": 0.7},
        "ER11/5-Z":         {"A": 11.0,  "B": 7.9,   "Bp": 7.9,   "C": 4.25, "Cp": 0,  "D": 2.5,   "E": 1.5,   "F": 6.0,   "Gap": 0, "Ae": 11.9,  "Ve": 174,   "Mass": 1.1},
        "ER14/4.5/9-Z":     {"A": 13.85, "B": 11.35, "Bp": 11.35, "C": 5.20, "Cp": 0,  "D": 2.25,  "E": 0.95,  "F": 9.0,   "Gap": 0, "Ae": 22.7,  "Ve": 349,   "Mass": 2.0},
        "ER14.5/6-Z":       {"A": 14.5,  "B": 11.8,  "Bp": 11.8,  "C": 4.7,  "Cp": 0,  "D": 3.0,   "E": 1.65,  "F": 6.7,   "Gap": 0, "Ae": 17.6,  "Ve": 333,   "Mass": 2.0},
        "ER18/5/12-Z":      {"A": 18.15, "B": 15.75, "Bp": 15.75, "C": 6.0,  "Cp": 0,  "D": 2.5,   "E": 1.0,   "F": 12.0,  "Gap": 0, "Ae": 32.8,  "Ve": 645,   "Mass": 3.8},
        "ER22/5.5/15-Z":    {"A": 22.1,  "B": 19.7,  "Bp": 19.7,  "C": 6.8,  "Cp": 0,  "D": 2.75,  "E": 1.0,   "F": 15.25, "Gap": 0, "Ae": 46.1,  "Ve": 1070,  "Mass": 6.5},
        "ER25/5.5/18-Z":    {"A": 25.3,  "B": 22.9,  "Bp": 22.9,  "C": 7.0,  "Cp": 0,  "D": 2.75,  "E": 1.0,   "F": 18.0,  "Gap": 0, "Ae": 53.7,  "Ve": 1400,  "Mass": 8.5}
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(ERPlanarGeometry("ER25/5.5/18-Z").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('RZ','1LEG','SET')

#=== [11] EIRPlanar Geometry =========================================================
def EIRPlanarGeometry(ReferenceCores: str = None, type: bool = False): 
    core_geometries = {
        "EIR14/4.5/9-Z":    {"A": 13.85, "B": 11.35, "Bp": 11.35, "C": 5.20, "Cp": 0, "D": 3.20, "E": 1.90, "F": 9.00,  "I": 1.30, "Gap": 0, "Ae": 22.7,  "Ve": 349,   "Mass": 2},
        "EIR18/5/12-Z":     {"A": 18.15, "B": 15.75, "Bp": 15.75, "C": 6.00, "Cp": 0, "D": 3.50, "E": 2.00, "F": 12.00, "I": 1.50, "Gap": 0, "Ae": 32.8,  "Ve": 645,   "Mass": 3.8},
        "EIR22/5.5/15-Z":   {"A": 22.10, "B": 19.70, "Bp": 19.70, "C": 6.80, "Cp": 0, "D": 3.75, "E": 2.00, "F": 15.25, "I": 1.75, "Gap": 0, "Ae": 46.1,  "Ve": 1070,  "Mass": 6.5}
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(EIRPlanarGeometry("EIR22/5.5/15-Z").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('RZ','1LEG','WITH_I')

#=== [12] ETD Geometry =========================================================
def ETDGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "ETD19-Z": {"A": 19.6,  "B": 14.9, "Bp": 14.9, "C": 7.4,  "Cp": 0, "D": 13.65, "E": 9.4,  "F": 7.4,   "Gap": 0, "Ae": 41.3,  "Ve": 2260,  "Mass": 14},
        "ETD24-Z": {"A": 24.4,  "B": 18.6, "Bp": 18.6, "C": 8.5,  "Cp": 0, "D": 14.45, "E": 10.1, "F": 8.5,   "Gap": 0, "Ae": 56.3,  "Ve": 3480,  "Mass": 20},
        "ETD29-Z": {"A": 29.8,  "B": 22.7, "Bp": 22.7, "C": 9.5,  "Cp": 0, "D": 15.80, "E": 11.0, "F": 9.5,   "Gap": 0, "Ae": 73.6,  "Ve": 5200,  "Mass": 28},
        "ETD34-Z": {"A": 34.2,  "B": 26.3, "Bp": 26.3, "C": 10.8, "Cp": 0, "D": 17.3,  "E": 12.1, "F": 10.88, "Gap": 0, "Ae": 97.1,  "Ve": 7630,  "Mass": 40},
        "ETD39-Z": {"A": 39.1,  "B": 30.1, "Bp": 30.1, "C": 12.5, "Cp": 0, "D": 19.8,  "E": 14.6, "F": 12.58, "Gap": 0, "Ae": 125.0, "Ve": 11500, "Mass": 60},
        "ETD44-Z": {"A": 44.0,  "B": 33.3, "Bp": 33.3, "C": 14.8, "Cp": 0, "D": 22.3,  "E": 16.5, "F": 14.9,  "Gap": 0, "Ae": 175.0, "Ve": 18000, "Mass": 94},
        "ETD49-Z": {"A": 48.7,  "B": 37.0, "Bp": 37.0, "C": 16.3, "Cp": 0, "D": 24.7,  "E": 18.1, "F": 16.4,  "Gap": 0, "Ae": 213.0, "Ve": 24300, "Mass": 124}
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(ETDGeometry("ETD49-Z").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('RZ','1LEG','SET')

