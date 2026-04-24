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
#=== DESCRIPTION: AirCore Geometries                              ===#
#=== CREATED    : 15/03/2026                                      ===#
#=== UPDATED    : 15/03/2026                                      ===#
#====================================================================#
#====================================================================#


#=====================================================================
#=== IMPORTS =========================================================
#=====================================================================

base_return = {"A": 0, "B": 0, "Bp": 0, "C": 0, "Cp": 0, "D": 0, "E": 0, "F": 0, "G": 0, "I": 0, "Gap": 0, "Ae": 0, "Ve": 0, "Mass": 0}



#=====================================================================
#===  RZ Geometry ====================================================
#=====================================================================

def AIRRZGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "RZ":     {"C": 0,  "Ae": 0,   "Ve": 0, "Mass": 0},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(AIRRZGeometry("RZ").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('RZ', '1LEG', 'SET')



#=====================================================================
#===  XY Geometry ====================================================
#=====================================================================

def AIRXYGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "XY":      {"C": 0,   "F": 0,  "Ae": 0,   "Ve": 0, "Mass": 0},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(AIRXYGeometry("XY").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY', '1LEG', 'SET')


