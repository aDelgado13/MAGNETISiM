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
# === DESCRIPTION: MagInc core materials                           ===#
# ====================================================================#
# ====================================================================#

# ==============================================================================
# MAGNETISiM
# Copyright (c) 2026 Universidad Politécnica de Madrid (UPM).
# Licensed under CC BY-NC-SA 4.0 (see LICENSE). Free for non-commercial use;
# the MAGNETISiM application itself is distributed under its own EULA.
#
# NOTE: Material parameters fitted by the MAGNETISiM team from the public curves
#       in the manufacturer's datasheets. Units: Cond in S/m, Phi in degrees,
#       Bmax in T; Steinmetz with Pv in kW/m³, f in kHz and B in mT;
#       DebyeParameter fitted against x = log10(f[Hz]·1e-6).
#       Sources:
#       https://www.mag-inc.com/Media/Magnetics/File-Library/Product%20Literature/Ferrite%20Literature/FC-S7.pdf?ext=.pdf
#       https://www.mag-inc.com/products/powder-cores/mpp-cores/mpp-material-curves
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
    "epsR": 12,
    "tanDelta": 0.02,
}

_NO_IMAG = {"a1": 0, "b1": 0, "c1": 0, "a2": 0, "b2": 0, "c2": 0}


# =====================================================================
# ===  Materials ======================================================
# =====================================================================


def Material(Reference=None):
    material_properties = {
        "F": {
            "muR": 3000,
            "muI": 0,
            "Cond": 1 / 5,
            "DebyeParameter": {
                "Real": {
                    "y0": -11255504.1459,
                    "A": 8150856833137.3789,
                    "k": -18.0478,
                    "xc": 1.1747,
                },
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 470e-3,
            "Steinmetz": {"k": 9.283e-07, "alpha": 1.436, "beta": 2.671},
            "epsR": 12,
            "tanDelta": 0.02,
        },
        "P": {
            "muR": 2500,
            "muI": 0,
            "Cond": 1 / 5,
            "DebyeParameter": {
                "Real": {"y0": -7.9787, "A": 2727.1311, "k": 20.6496, "xc": 0.1202},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 470e-3,
            "Steinmetz": {"k": 2.563e-07, "alpha": 1.540, "beta": 2.730},
            "epsR": 12,
            "tanDelta": 0.02,
        },
        "R": {
            "muR": 2300,
            "muI": 0,
            "Cond": 1 / 5,
            "DebyeParameter": {
                "Real": {"y0": -7.9787, "A": 2727.1311, "k": 20.6496, "xc": 0.1202},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 470e-3,
            "Steinmetz": {"k": 7.660e-08, "alpha": 1.706, "beta": 2.758},
            "epsR": 12,
            "tanDelta": 0.02,
        },
        "K": {
            "muR": 2300,
            "muI": 0,
            "Cond": 1 / 5,
            "DebyeParameter": {
                "Real": {"y0": -90.7144, "A": 2583.9055, "k": 14.1168, "xc": 0.2706},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 470e-3,
            "Steinmetz": {"k": 2.656e-08, "alpha": 1.600, "beta": 3.150},
            "epsR": 12,
            "tanDelta": 0.02,
        },
        "J": {
            "muR": 2300,
            "muI": 0,
            "Cond": 1 / 5,
            "DebyeParameter": {
                "Real": {"y0": 241140.3333, "A": -237082.1749, "k": 10.0926, "xc": 0.9789},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 470e-3,
            "Steinmetz": {"k": 4.580e-08, "alpha": 2.420, "beta": 2.500},
            "epsR": 12,
            "tanDelta": 0.02,
        },
        "W": {
            "muR": 2300,
            "muI": 0,
            "Cond": 1 / 5,
            "DebyeParameter": {
                "Real": {"y0": 554888.2171, "A": -548671.9189, "k": 8.1900, "xc": 1.0159},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 470e-3,
            "Steinmetz": {"k": 2.198e-08, "alpha": 2.320, "beta": 2.620},
            "epsR": 12,
            "tanDelta": 0.02,
        },
        "H": {
            "muR": 2300,
            "muI": 0,
            "Cond": 1 / 5,
            "DebyeParameter": {
                "Real": {"y0": -109.1768, "A": 15372.9530, "k": 4.4790, "xc": -0.7634},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 470e-3,
            "Steinmetz": {"k": 6.766e-06, "alpha": 1.620, "beta": 2.150},
            "epsR": 12,
            "tanDelta": 0.02,
        },
        "MPP_14": {
            "muR": 14,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 9.6767, "A": 4.3155, "k": 6.0680, "xc": 1.0300},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 0.720,
            "Steinmetz": {"k": 1.30689e-04, "alpha": 1.3160, "beta": 2.1030},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "MPP_26": {
            "muR": 26,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 25.9191, "k": 4.2097, "xc": 1.3663},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 0.740,
            "Steinmetz": {"k": 7.21340e-05, "alpha": 1.3570, "beta": 2.1030},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "MPP_40": {
            "muR": 40,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0, "A": 40.0, "k": 2.054, "xc": 1.445},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 0.760,
            "Steinmetz": {"k": 7.21340e-05, "alpha": 1.3570, "beta": 2.1030},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "MPP_60": {
            "muR": 60,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 59.8220, "k": 3.5475, "xc": 1.4066},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 0.750,
            "Steinmetz": {"k": 3.54190e-05, "alpha": 1.4490, "beta": 2.1030},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "MPP_125": {
            "muR": 125,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 124.4425, "k": 2.4563, "xc": 1.1368},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 0.700,
            "Steinmetz": {"k": 3.05443e-05, "alpha": 1.5610, "beta": 2.1030},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "MPP_147": {
            "muR": 147,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 145.9336, "k": 2.6403, "xc": 0.9575},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 0.700,
            "Steinmetz": {"k": 2.77412e-05, "alpha": 1.5980, "beta": 2.1030},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "MPP_160": {
            "muR": 160,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 159.2945, "k": 2.4026, "xc": 0.9359},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 0.680,
            "Steinmetz": {"k": 2.77412e-05, "alpha": 1.5980, "beta": 2.1030},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "MPP_173": {
            "muR": 173,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 172.2372, "k": 2.4026, "xc": 0.9359},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 0.680,
            "Steinmetz": {"k": 2.77412e-05, "alpha": 1.5980, "beta": 2.1030},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "MPP_200": {
            "muR": 200,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 197.0133, "k": 2.8503, "xc": 0.8241},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 0.650,
            "Steinmetz": {"k": 2.63667e-05, "alpha": 1.6240, "beta": 2.1030},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "MPP_300": {
            "muR": 300,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 299.1684, "k": 2.3634, "xc": 0.5832},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 0.600,
            "Steinmetz": {"k": 2.63667e-05, "alpha": 1.6240, "beta": 2.1030},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "MPP_550": {
            "muR": 550,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 526.0861, "k": 6.1634, "xc": -0.2547},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 0.550,
            "Steinmetz": {"k": 3.67003e-05, "alpha": 1.6450, "beta": 2.1030},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "HighFlux_14": {
            "muR": 14,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 13.9499, "k": 4.1251, "xc": 1.2900},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.500,
            "Steinmetz": {"k": 2.14846e-04, "alpha": 1.1890, "beta": 2.2180},
            "epsR": 8,
            "tanDelta": 0.04,
        },
        "HighFlux_26": {
            "muR": 26,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 25.8422, "k": 3.1716, "xc": 1.3611},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.500,
            "Steinmetz": {"k": 1.09204e-04, "alpha": 1.2400, "beta": 2.2180},
            "epsR": 8,
            "tanDelta": 0.04,
        },
        "HighFlux_40": {
            "muR": 40,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 40.0000, "k": 2.2120, "xc": 1.2640},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.500,
            "Steinmetz": {"k": 4.10411e-05, "alpha": 1.3980, "beta": 2.2180},
            "epsR": 8,
            "tanDelta": 0.04,
        },
        "HighFlux_60": {
            "muR": 60,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 59.5136, "k": 3.0696, "xc": 1.2152},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.500,
            "Steinmetz": {"k": 5.46874e-05, "alpha": 1.3110, "beta": 2.2180},
            "epsR": 8,
            "tanDelta": 0.04,
        },
        "HighFlux_75": {
            "muR": 75,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 75.0000, "k": 2.2120, "xc": 1.0000},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.500,
            "Steinmetz": {"k": 9.76184e-05, "alpha": 1.2100, "beta": 2.2180},
            "epsR": 8,
            "tanDelta": 0.04,
        },
        "HighFlux_90": {
            "muR": 90,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 90.0000, "k": 2.2120, "xc": 1.0000},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.500,
            "Steinmetz": {"k": 9.76184e-05, "alpha": 1.2100, "beta": 2.2180},
            "epsR": 8,
            "tanDelta": 0.04,
        },
        "HighFlux_125": {
            "muR": 125,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 123.8628, "k": 2.5645, "xc": 1.0615},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.500,
            "Steinmetz": {"k": 4.09124e-05, "alpha": 1.4280, "beta": 2.2180},
            "epsR": 8,
            "tanDelta": 0.04,
        },
        "HighFlux_147": {
            "muR": 147,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 146.1858, "k": 2.5091, "xc": 1.0514},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.500,
            "Steinmetz": {"k": 4.09124e-05, "alpha": 1.4280, "beta": 2.2180},
            "epsR": 8,
            "tanDelta": 0.04,
        },
        "HighFlux_160": {
            "muR": 160,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 159.1799, "k": 2.5036, "xc": 1.0225},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.500,
            "Steinmetz": {"k": 4.09124e-05, "alpha": 1.4280, "beta": 2.2180},
            "epsR": 8,
            "tanDelta": 0.04,
        },
        "KoolMu_14": {
            "muR": 14,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 10.4031, "A": 3.5988, "k": 2.3991, "xc": 1.7001},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.000,
            "Steinmetz": {"k": 6.99984e-05, "alpha": 1.5410, "beta": 1.9880},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "KoolMu_26": {
            "muR": 26,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 13.6124, "A": 12.3943, "k": 2.3992, "xc": 1.6994},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.000,
            "Steinmetz": {"k": 5.68852e-05, "alpha": 1.5410, "beta": 1.9880},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "KoolMu_40": {
            "muR": 40,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 10.6734, "A": 29.3424, "k": 2.3992, "xc": 1.6995},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.000,
            "Steinmetz": {"k": 5.68852e-05, "alpha": 1.5410, "beta": 1.9880},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "KoolMu_60": {
            "muR": 60,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 60.0281, "k": 2.4242, "xc": 1.6464},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.000,
            "Steinmetz": {"k": 4.81287e-05, "alpha": 1.5410, "beta": 1.9880},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "KoolMu_75": {
            "muR": 75,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 75.0111, "k": 2.4952, "xc": 1.5200},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.000,
            "Steinmetz": {"k": 4.81287e-05, "alpha": 1.5410, "beta": 1.9880},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "KoolMu_90": {
            "muR": 90,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 89.9691, "k": 2.5694, "xc": 1.4154},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.000,
            "Steinmetz": {"k": 4.81287e-05, "alpha": 1.5410, "beta": 1.9880},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "KoolMu_125": {
            "muR": 125,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 124.7305, "k": 2.7571, "xc": 1.2240},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.000,
            "Steinmetz": {"k": 4.81287e-05, "alpha": 1.5410, "beta": 1.9880},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "XFlux_26": {
            "muR": 26,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 13.0438, "A": 12.9492, "k": 2.9840, "xc": 1.2030},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.500,
            "Steinmetz": {"k": 5.24300e-04, "alpha": 1.1940, "beta": 2.0150},
            "epsR": 8,
            "tanDelta": 0.04,
        },
        "XFlux_40": {
            "muR": 40,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.6748, "A": 39.3702, "k": 2.3843, "xc": 1.5052},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.500,
            "Steinmetz": {"k": 5.67990e-04, "alpha": 1.1940, "beta": 2.0150},
            "epsR": 8,
            "tanDelta": 0.04,
        },
        "XFlux_60": {
            "muR": 60,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 1.0121, "A": 59.0553, "k": 2.3843, "xc": 1.5052},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.500,
            "Steinmetz": {"k": 5.02455e-04, "alpha": 1.1940, "beta": 2.0150},
            "epsR": 8,
            "tanDelta": 0.04,
        },
        "XFlux_75": {
            "muR": 75,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 75.1631, "k": 2.2220, "xc": 1.4021},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.500,
            "Steinmetz": {"k": 4.89346e-04, "alpha": 1.1940, "beta": 2.0150},
            "epsR": 8,
            "tanDelta": 0.04,
        },
        "XFlux_125": {
            "muR": 125,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 125.4163, "k": 2.1759, "xc": 1.2393},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.500,
            "Steinmetz": {"k": 4.80610e-04, "alpha": 1.1940, "beta": 2.0150},
            "epsR": 8,
            "tanDelta": 0.04,
        },
        "Edge_14": {
            "muR": 14,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 14.0000, "k": 2.3260, "xc": 1.9920},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.000,
            "Steinmetz": {"k": 3.46177e-05, "alpha": 1.3900, "beta": 2.2630},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "Edge_26": {
            "muR": 26,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 23.6642, "A": 2.3409, "k": 2.0935, "xc": 1.4157},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.000,
            "Steinmetz": {"k": 3.37952e-05, "alpha": 1.3220, "beta": 2.2630},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "Edge_40": {
            "muR": 40,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 40.0000, "k": 2.3260, "xc": 1.5400},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.000,
            "Steinmetz": {"k": 2.44483e-05, "alpha": 1.3690, "beta": 2.2630},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "Edge_60": {
            "muR": 60,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 47.5560, "A": 12.4710, "k": 2.0936, "xc": 1.4157},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.000,
            "Steinmetz": {"k": 2.53878e-05, "alpha": 1.3210, "beta": 2.2630},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "Edge_75": {
            "muR": 75,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 57.3158, "A": 17.6488, "k": 2.4967, "xc": 1.1078},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.000,
            "Steinmetz": {"k": 1.97455e-05, "alpha": 1.4030, "beta": 2.2630},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "Edge_90": {
            "muR": 90,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 0.0000, "A": 89.8105, "k": 2.6525, "xc": 1.4695},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.000,
            "Steinmetz": {"k": 7.83141e-05, "alpha": 1.1390, "beta": 2.2630},
            "epsR": 7,
            "tanDelta": 0.03,
        },
        "Edge_125": {
            "muR": 125,
            "muI": 0,
            "Cond": 200,
            "DebyeParameter": {
                "Real": {"y0": 63.8005, "A": 125.4217, "k": 0.0000, "xc": 1.0929},
                "Imag": _NO_IMAG,
            },
            "Phi": 0,
            "Bmax": 1.000,
            "Steinmetz": {"k": 7.83141e-05, "alpha": 1.1390, "beta": 2.2630},
            "epsR": 7,
            "tanDelta": 0.03,
        },
    }

    if Reference is None:
        return tuple(material_properties.keys())
    else:
        dictaux = dict(material_properties.get(Reference, base_return))
        dictaux["Material"] = Reference
        return dictaux
