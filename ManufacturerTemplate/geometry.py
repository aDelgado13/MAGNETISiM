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
#=== DESCRIPTION: Ferroxcube Geometries                           ===#
#=== CREATED    : 30/03/2026                                      ===#
#=== UPDATED    : 30/03/2026                                      ===#
#====================================================================#
#====================================================================#

#=====================================================================
#=== IMPORTS =========================================================
#=====================================================================

base_return = {"A": 0, "B": 0, "Bp": 0, "C": 0, "Cp": 0, "D": 0, "E": 0, "F": 0, "G": 0, "I": 0, "Gap": 0, "Ae": 0, "Ve": 0, "Mass": 0}



#=====================================================================
#===  Layout =========================================================
#=====================================================================

# Cores:
# 



#=====================================================================
#===  XY Geometry ====================================================
#=====================================================================

#=== [1] E Geometry =========================================================
def EGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "EXX":     {"A" : 5.25,    "B": 3.80,   "C": 1.40,   "D": 2.65,   "E": 1.90,   "F": 2.00,   "Gap": 0,  "Ae": 2.66,   "Ve": 33.3,       "Mass": 0.08},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(EGeometry("EXX").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY', '3LEG', 'SET')

#=== [2] EI Geometry =========================================================
def EIGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "EIXX":      {"A" : 16.0,    "B": 12.00,    "C": 4.00,   "D": 12.25,  "E": 10.25,  "F": 4.85, "I": 2.40, "Gap": 0.0, "Ae": 19.4, "Ve": 701, "Mass": 2.7},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(EIGeometry("EIXX").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY', '3LEG', 'WITH_I')



#=====================================================================
#===  RZ Geometry ====================================================
#=====================================================================

#=== [1] EQ Geometry =========================================================
def EQGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "EQXX":        {"A" : 12.8,  "B": 9.05,   "Bp": 11.2,  "C": 5.0,  "Cp": 0,  "D": 2.85, "E": 1.75, "F": 8.7, "Gap": 0,  "Ae": 19.9, "Ve": 0, "Mass": 0},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(EQGeometry("EQXX").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('RZ', '1LEG', 'SET')

#=== [2] RM Geometry =========================================================
def RMGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "RMXX":        {"A": 11.0, "B":  5.8, "Bp":  7.95, "C":  3.9,  "Cp": 2.04,  "D":  5.2,  "E": 3.5,  "F":  4.6, "G":  9.8, "Gap": 0,  "Ae":  11.0, "Ve":   230, "Mass":  1.5},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(RMGeometry("RMXX").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('RZ', '1LEG', 'SET')


