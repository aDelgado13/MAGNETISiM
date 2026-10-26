# ====================================================================#
# ====================================================================#
# ===   __  __    _    ____ _   _ _____ _____ ___ ____  _ __  __   ===#
# ===  |  \/  |  / \  / ___| \ | | ____|_   _|_ _/ ___|(_)  \/  |  ===#
# ===  | |\/| | / _ \| |  _|  \| |  _|   | |  | |\___ \| | |\/| |  ===#
# ===  | |  | |/ ___ \ |_| | |\  | |___  | |  | | ___) | | |  | |  ===#
# ===  |_|  |_/_/   \_\____|_| \_|_____| |_| |___|____/|_|_|  |_|  ===#
# ===                                                              ===#
# ====================================================================#
# ====================================================================#
# === FILE       : geometry                                        ===#
# === AUTHORS    : Alberto Delgado, Alberto Vital                  ===#
# === CONTACT    : a.delgado@upm.es / www.magnetisim.com           ===#
# === DESCRIPTION: IPT core geometries                             ===#
# ====================================================================#
# ====================================================================#

# ==============================================================================
# MAGNETISiM
# Copyright (c) 2026 Universidad Politécnica de Madrid (UPM).
# Licensed under CC BY-NC-SA 4.0 (see LICENSE). Free for non-commercial use;
# the MAGNETISiM application itself is distributed under its own EULA.
#
# NOTE: Pair of flat plates of magnetic material for inductive power transfer
#       (IPT/WPT), as discs (RZ) or rectangular plates (XY). The only reference
#       of each family has all dimensions at 0, to be set by the user. All
#       dimensions in mm.
# ==============================================================================

# =====================================================================
# === IMPORTS =========================================================
# =====================================================================

base_return = {
    "A": 0,
    "B": 0,
    "Bp": 0,
    "C": 0,
    "Cp": 0,
    "D": 0,
    "E": 0,
    "F": 0,
    "G": 0,
    "I": 0,
    "Gap": 0,
    "Ae": 0,
    "Ve": 0,
    "Mass": 0,
}


# =====================================================================
# ===  RZ Geometry ====================================================
# =====================================================================


def IPTRZGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "RZ": {"A": 0, "C": 0, "Cp": 0, "I": 0, "Gap": 0, "Ae": 0, "Ve": 0, "Mass": 0},
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(IPTRZGeometry("RZ").keys())[:-3]
        else:
            return (
                tuple(core_geometries.keys())
                if ReferenceCores is None
                else core_geometries.get(ReferenceCores, base_return)
            )
    return ("RZ", "1LEG", "WITH_I")


# =====================================================================
# ===  XY Geometry ====================================================
# =====================================================================


def IPTXYGeometry(ReferenceCores: str = None, type: bool = False):
    core_geometries = {
        "XY": {
            "A": 0,
            "C": 0,
            "Cp": 0,
            "I": 0,
            "F": 0,
            "G": 0,
            "Gap": 0,
            "Ae": 0,
            "Ve": 0,
            "Mass": 0,
        },
    }
    if not type:
        if ReferenceCores == "GeoParam":
            return tuple(IPTXYGeometry("XY").keys())[:-3]
        else:
            return (
                tuple(core_geometries.keys())
                if ReferenceCores is None
                else core_geometries.get(ReferenceCores, base_return)
            )
    return ("XY", "1LEG", "WITH_I")
