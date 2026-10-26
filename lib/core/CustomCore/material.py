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
# === FILE       : material                                        ===#
# === AUTHORS    : Alberto Delgado, Alberto Vital                  ===#
# === CONTACT    : a.delgado@upm.es / www.magnetisim.com           ===#
# === DESCRIPTION: CustomCore core materials                       ===#
# ====================================================================#
# ====================================================================#

# ==============================================================================
# MAGNETISiM
# Copyright (c) 2026 Universidad Politécnica de Madrid (UPM).
# Licensed under CC BY-NC-SA 4.0 (see LICENSE). Free for non-commercial use;
# the MAGNETISiM application itself is distributed under its own EULA.
#
# NOTE: Placeholder materials for users to replace with their own parameters
#       (Air and Ferrite with muR = 1000 and Bmax = 0.38 T). They are not
#       manufacturer data. Units: Cond in S/m, Phi in degrees, Bmax in T;
#       Steinmetz with Pv in kW/m³, f in kHz and B in mT; DebyeParameter fitted
#       against x = log10(f[Hz]·1e-6).
# ==============================================================================

base_return = {
    "muR": 0,
    "muI": 0,
    "Cond": 0,
    "DebyeParameter": {
        "Real": {"y0": 0, "A": 0, "k": 0, "xc": 0},
        "Imag": {"a1": 0, "b1": 0, "c1": 0, "a2": 0, "b2": 0, "c2": 0},
    },
    "Phi": 0,
    "Bmax": 380e-3,
    "Steinmetz": {"k": 0, "alpha": 0, "beta": 0},
}

_NO_IMAG = {"a1": 0, "b1": 0, "c1": 0, "a2": 0, "b2": 0, "c2": 0}


# =====================================================================
# ===  Materials ======================================================
# =====================================================================


def Material(Reference=None):
    material_properties = {
        "Air": {
            "muR": 1,
            "muI": 0,
            "Cond": 0,
            "DebyeParameter": {
                "Real": {"y0": 0, "A": 0, "k": 0, "xc": 0},
                "Imag": {"a1": 0, "b1": 0, "c1": 0, "a2": 0, "b2": 0, "c2": 0},
            },
            "Phi": 0,
            "Bmax": 100000e-3,
            "Steinmetz": {"k": 0, "alpha": 0, "beta": 0},
            "epsR": 1.0006,
            "tanDelta": 0.0,
        },
        "Ferrite": {
            "muR": 1000,
            "muI": 0,
            "Cond": 0,
            "DebyeParameter": {
                "Real": {"y0": 0, "A": 0, "k": 0, "xc": 0},
                "Imag": {"a1": 0, "b1": 0, "c1": 0, "a2": 0, "b2": 0, "c2": 0},
            },
            "Phi": 0,
            "Bmax": 380e-3,
            "Steinmetz": {"k": 0, "alpha": 0, "beta": 0},
            "epsR": 12,
            "tanDelta": 0.02,
        },
    }
    if Reference is None:
        return tuple(material_properties.keys())
    else:
        dictaux = dict(material_properties.get(Reference, base_return))
        dictaux["Material"] = Reference
        return dictaux
