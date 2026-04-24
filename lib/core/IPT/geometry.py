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
#=== DESCRIPTION: WPT Geometries                                  ===#
#=== CREATED    : 15/03/2026                                      ===#
#=== UPDATED    : 15/03/2026                                      ===#
#====================================================================#
#====================================================================#
# TODO: En el futuro meter otra variable para el hueco en medio y la bobina central pero en la distancia de F
#=====================================================================
#=== IMPORTS =========================================================
#=====================================================================

base_return = {"A": 0, "B": 0, "Bp": 0, "C": 0, "Cp": 0, "D": 0, "E": 0, "F": 0, "G": 0, "I": 0, "Gap": 0, "Ae": 0, "Ve": 0, "Mass": 0}



#=====================================================================
#===  RZ Geometry ====================================================
#=====================================================================

def IPTRZGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "RZ":     {"A": 0, "C": 0, "Cp": 0, "I": 0, "Gap": 0, "Ae": 0,   "Ve": 0, "Mass": 0},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(IPTRZGeometry("RZ").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('RZ', '1LEG', 'WITH_I')



#=====================================================================
#===  XY Geometry ====================================================
#=====================================================================

def IPTXYGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "XY":      {"A": 0, "C": 0, "Cp": 0, "I": 0, "F": 0, "G": 0, "Gap": 0,  "Ae": 0,   "Ve": 0, "Mass": 0},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(IPTXYGeometry("XY").keys())[:-3]
        else: return tuple(core_geometries.keys()) if ReferenceCores is None else core_geometries.get(ReferenceCores, base_return)
    return ('XY', '1LEG', 'WITH_I')
