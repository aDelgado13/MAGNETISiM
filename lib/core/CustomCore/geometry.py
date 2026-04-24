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
#=== DESCRIPTION: CustomCore Geometries                           ===#
#=== CREATED    : 15/03/2026                                      ===#
#=== UPDATED    : 15/03/2026                                      ===#
#====================================================================#
#====================================================================#


#=====================================================================
#=== IMPORTS =========================================================
#=====================================================================

base_return = {"A": 0, "B": 0, "Bp": 0, "C": 0, "Cp": 0, "D": 0, "E": 0, "F": 0, "G": 0, "I": 0, "Gap": 0, "Ae": 0, "Ve": 0, "Mass": 0}



#=====================================================================
#===  XY Geometry ====================================================
#=====================================================================

#=== [1] E Geometry =========================================================
def EGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "E5.3/2.7/2":     {"A" : 5.25,    "B": 3.80,   "C": 1.40,   "D": 2.65,   "E": 1.90,   "F": 2.00,   "Gap": 0,  "Ae": 2.66,   "Ve": 33.3,       "Mass": 0.08},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(EGeometry("E5.3/2.7/2").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY', '3LEG', 'SET')

#=== [2] EI Geometry =========================================================
def EIGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "EI16/12/5":      {"A" : 16.0,    "B": 12.00,    "C": 4.00,   "D": 12.25,  "E": 10.25,  "F": 4.85,   "I": 2.40,   "Gap": 0.0,    "Ae": 19.4,   "Ve": 701,     "Mass": 2.7+0.9},
   }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(EIGeometry("EI16/12/5").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY', '3LEG', 'WITH_I')

#=== [3] EPlanar Geometry =========================================================
def EPlanarGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "E14/3.5/5":   {"A" : 14,    "B": 11,    "C": 3,    "D": 3.5,  "E": 2,    "F": 5,     "Gap": 0, "Ae": 14.3, "Ve": 300,    "Mass": 1.2},
        }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(EPlanarGeometry("E14/3.5/5").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY', '3LEG', 'SET')

#=== [4] EIPlanar Geometry =========================================================
def EIPlanarGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "EI14/3.5/5":   {"A" : 14,    "B": 11,    "C": 3,    "D": 3.5,  "E": 2,    "F": 5,     "I": 1.5,  "Gap": 0,  "Ae": 14.3, "Ve": 240,   "Mass": 1.1},
        }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(EIPlanarGeometry("EI14/3.5/5").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY', '3LEG', 'WITH_I')

#=== [5] EC Geometry =========================================================
def ECGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "EC35":      {"A" : 35.3, "B": 22.75, "C": 9.5,  "D": 17.7, "E": 12.3, "F": 9.5,  "Gap": 0, "Ae": 84.3,  "Ve": 6530,  "Mass": 19},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(ECGeometry("EC35").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY', '1LEG', 'SET')

#=== [6] ER Geometry =========================================================
def ERGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "ER28/14/11":      {"A": 28.55,  "B": 21.75,  "C": 9.9,    "D": 14.0,  "E": 9.75,   "F": 11.40,  "Gap": 0,  "Ae": 81.4,   "Ve": 5260,   "Mass": 14},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(ERGeometry("ER54/18/18").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY', '1LEG', 'SET')

#=== [7] ERPlanar Geometry =========================================================
def ERPlanarGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "ER9.5/2.5/5":      {"A": 9.5,  "B": 7.5,  "C": 3.5,    "D": 2.45,  "E": 1.6,   "F": 5,  "Gap": 0,  "Ae": 8.47,   "Ve": 120,   "Mass": 0.7},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(ERPlanarGeometry("ER9.5/2.5/5").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY', '1LEG', 'SET')

#=== [8] ETD Geometry =========================================================
def ETDGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "ETD29/16/10":    {"A": 30.60,  "B": 22.00, "C": 9.80,   "D": 15.80,  "E": 11.00,  "F": 9.80,   "Gap": 0,  "Ae": 76,   "Ve": 5470,  "Mass": 14},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(ETDGeometry("ETD59/31/22").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY', '1LEG', 'SET')

#=== [9] U Geometry =========================================================
def UGeometry(ReferenceCores: str = None, type: bool = False): 
    core_geometries = {
        "U10/8/3":       {"A":  9.9,  "B": 4.35,  "C": 0, "D": 8.2,  "E": 5.0,  "F": 2.85, "Gap": 0, "Ae":  8.07, "Ve":  309,   "Mass": 0.9},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(UGeometry("U10/8/3").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY', '2LEG', 'SET')

#=== [10] UI Geometry =========================================================
def UIGeometry(ReferenceCores: str = None, type: bool = False): 
    core_geometries = {
        "U25/16/6/I25/6/6*":    {"A": 25.4,  "B": 12.7, "C": 0, "D": 15.9, "E": 9.5, "F": 6.4,  "I": 6.4,  "Gap": 0, "Ae": 40.3, "Ve": 3380 + 2590,    "Mass": 8 + 4.5},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(UIGeometry("U25/16/6/I25/6/6*").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY', '2LEG', 'WITH_I')



#=====================================================================
#===  RZ Geometry ====================================================
#=====================================================================

#=== [1] EQ Geometry =========================================================
def EQGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "EQ13":        {"A" : 12.8,  "B": 9.05,   "Bp": 11.2,  "C": 5.0,  "Cp": 0,  "D": 2.85, "E": 1.75, "F": 8.7,   "Gap": 0,  "Ae": 19.9, "Ve": 0, "Mass": 0},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(EQGeometry("EQ38/8/25").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('RZ', '1LEG', 'SET')

#=== [2] EQPLT Geometry =========================================================    
def EQPLTGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "EQ13PLT13":               {"A" : 12.8,   "B" : 9.05,   "Bp": 11.2,  "C": 5.0,  "Cp": 0,     "D": 2.85,  "E": 1.75, "F": 8.7,  "I": 1.1,  "Gap": 0,  "Ae": 19.9, "Ve": 0,  "Mass": 0},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(EQPLTGeometry("EQ13PLT13").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('RZ', '1LEG', 'WITH_I')

#=== [3] P Geometry =========================================================
def PGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "P9/5":        {"A": 9.3,    "B": 2.0,   "Bp": 7.5,   "C": 3.9,   "Cp": 2.1,    "D": 5.4,     "E": 3.6,   "F": 0,    "Gap": 0, "Ae": 10.1,   "Ve": 126,    "Mass": 0.8},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(PGeometry("P66/56").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('RZ', '1LEG', 'SET')

#=== [4] PT Geometry =========================================================
def PTGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "PT14/8":        {"A": 14.05, "B": 3.3,  "Bp": 11.8,  "C": 5.9,   "Cp": 3.1, "D": 4.15,  "E": 2.90, "F": 0.0, "Gap": 0, "Ae": 23.3,  "Ve": 492,   "Mass": 2.8},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(PTGeometry("PTS40/27/I").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('RZ', '1LEG', 'SET')

#=== [5] PH Geometry =========================================================
def PHGeometry(ReferenceCores: str = None, type: bool = False): 
    core_geometries = {
        "PH5.6/3.6": {"A":  5.75, "B": 1.5, "Bp":  4.5, "C":  2.5, "Cp": 0.95, "D":  7.2, "E":  5.6, "F": 0.0, "Gap": 0, "Ae": 0, "Ve": 0, "Mass":  0.2},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(PHGeometry("PH5.6/3.6").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('RZ', '1LEG', 'SET')

#=== [6] PM Geometry =========================================================
def PMGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "PM74/59":   {"A":  74.0, "B": 34.0, "Bp": 57.5, "C": 29.5, "Cp": 5.4, "D": 59.0, "E": 40.7, "F": 32.4, "Gap": 0, "Ae":  790, "Ve": 101000, "Mass":  460},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(PMGeometry("PM74/59").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('RZ', '1LEG', 'SET')

#=== [7] PQ Geometry =========================================================
def PQGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "PQ20/16":   {"A": 21.3, "B": 12.0, "Bp": 18.0, "C":  8.8, "Cp": 0, "D":  8.10, "E":  5.15, "F":  7.9, "G": 13.6, "Gap": 0, "Ae":  2330, "Ve":  61.9, "Mass": 13},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(PQGeometry("PQ20/16").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('RZ', '1LEG', 'SET')

#=== [8] RM Geometry =========================================================
def RMGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "RM4":        {"A": 11.0, "B":  5.8, "Bp":  7.95, "C":  3.9,  "Cp": 2.04,  "D":  5.2,  "E": 3.5,  "F":  4.6,  "G":  9.8, "Gap": 0,  "Ae":  11.0, "Ve":   230, "Mass":  1.5},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(RMGeometry("RM14/ILP").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('RZ', '1LEG', 'SET')

