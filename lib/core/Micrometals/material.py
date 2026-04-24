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
#=== FILE       : material                                        ===#
#=== AUTHORS    : Alberto Delgado, Alberto Vital                  ===#
#=== CONTACT    : a.delgado@upm.es / www.magnetisim.com           ===#
#=== DESCRIPTION: Micrometals Materials                           ===#
#=== CREATED    : 30/03/2026                                      ===#
#=== UPDATED    : 17/04/2026                                      ===#
#====================================================================#
#====================================================================#
# https://www.micrometals.com
# Material fitting
# x = MHz
# Eq real= y0 + A / ( 1 + exp(k*(log10(x*1e-6)-xc)))
# Eq imag= a1*exp(-(log10(x*1e-6)-b1)/c1)^2 + a2*exp(-(log10(x*1e-6)-b2)/c2)^2
# Steinmetz = k * f(kHz)^alpha * B(mT)^beta  kW/m3
# Source: Micrometals CurveFit Coefficients (mmcurvefitcoefficientsall_New.xlsx)
#         Cross-referenced with Micrometals online catalog
#=====================================================================

base_return = {"muR": 0, "muI": 0, "Cond": 0,
               "DebyeParameter": {"Real": {"y0":0,"A":0,"k":0,"xc":0},
                                  "Imag": {"a1":0,"b1":0,"c1":0,"a2":0,"b2":0,"c2":0}},
               "Phi": 0, "Bmax": 380e-3,
               "Steinmetz": {"k": 0, "alpha": 0, "beta": 0}}

_NO_IMAG = {"a1":0,"b1":0,"c1":0,"a2":0,"b2":0,"c2":0}

#=====================================================================
#===  Materials ======================================================
#=====================================================================

def Material(Reference=None):
    material_properties = {

        # ══════════════════════════════════════════════════════════════
        # STANDARD IRON POWDER MIXES  (High Bsat, moderate loss)
        # Best for: boost inductors, PFC, low-frequency chokes
        # ══════════════════════════════════════════════════════════════
        "1":   {"muR":  20, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0":15.43,"A": 4.57,"k":1.529,"xc":3.101},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.730,"Steinmetz":{"k":1.7316e-02,"alpha":1.0221,"beta":2.0739},"epsR":8,"tanDelta":0.04},
        "2":   {"muR":  10, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0": 1.00,"A": 9.00,"k":2.072,"xc":4.222},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.481,"Steinmetz":{"k":1.4463e-02,"alpha":1.0106,"beta":1.9762},"epsR":8,"tanDelta":0.04},
        "3":   {"muR":  35, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0":27.04,"A": 7.90,"k":1.528,"xc":2.751},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.764,"Steinmetz":{"k":1.7316e-02,"alpha":1.0221,"beta":2.0739},"epsR":8,"tanDelta":0.04},
        "5":   {"muR":   5, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0": 1.00,"A": 4.00,"k":2.072,"xc":4.613},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.481,"Steinmetz":{"k":1.1295e-02,"alpha":1.0790,"beta":1.9783},"epsR":8,"tanDelta":0.04},
        "6.5": {"muR": 8.5, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0": 1.00,"A": 7.50,"k":2.072,"xc":4.310},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.440,"Steinmetz":{"k":1.4504e-02,"alpha":1.0098,"beta":1.9761},"epsR":8,"tanDelta":0.04},
        "7":   {"muR":   9, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0": 1.00,"A": 8.00,"k":2.072,"xc":4.279},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.460,"Steinmetz":{"k":1.4463e-02,"alpha":1.0106,"beta":1.9762},"epsR":8,"tanDelta":0.04},
        "8":   {"muR":  35, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0":27.04,"A": 7.90,"k":1.528,"xc":2.751},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.764,"Steinmetz":{"k":1.7142e-02,"alpha":1.0256,"beta":2.0735},"epsR":8,"tanDelta":0.04},
        "10":  {"muR":   6, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0": 1.00,"A": 5.00,"k":2.072,"xc":4.506},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.380,"Steinmetz":{"k":1.4556e-02,"alpha":1.0089,"beta":1.9761},"epsR":8,"tanDelta":0.04},
        "14":  {"muR":  14, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0": 2.47,"A":11.53,"k":3.503,"xc":3.055},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.520,"Steinmetz":{"k":1.3931e-02,"alpha":1.0208,"beta":1.9765},"epsR":8,"tanDelta":0.04},
        "15":  {"muR":  25, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0":19.29,"A": 5.71,"k":1.529,"xc":2.955},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.745,"Steinmetz":{"k":1.7142e-02,"alpha":1.0256,"beta":2.0735},"epsR":8,"tanDelta":0.04},
        "17":  {"muR":   4, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0": 1.00,"A": 3.00,"k":2.072,"xc":4.752},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.280,"Steinmetz":{"k":1.4769e-02,"alpha":1.0049,"beta":1.9760},"epsR":8,"tanDelta":0.04},
        "18":  {"muR":  55, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0": 0.00,"A":55.00,"k":2.556,"xc":2.134},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.782,"Steinmetz":{"k":1.7430e-02,"alpha":1.1209,"beta":2.0309},"epsR":8,"tanDelta":0.04},
        "19":  {"muR":  55, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0": 0.00,"A":55.00,"k":2.556,"xc":1.754},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.817,"Steinmetz":{"k":2.1762e-02,"alpha":1.2173,"beta":1.8806},"epsR":8,"tanDelta":0.04},
        "26":  {"muR":  75, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0": 7.15,"A":68.39,"k":1.951,"xc":0.548},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.853,"Steinmetz":{"k":8.0258e-03,"alpha":1.4708,"beta":1.9333},"epsR":8,"tanDelta":0.04},
        "30":  {"muR":  22, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0": 6.93,"A":15.08,"k":2.198,"xc":1.540},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.672,"Steinmetz":{"k":3.1885e-02,"alpha":1.3086,"beta":1.8076},"epsR":8,"tanDelta":0.04},
        "34":  {"muR":  33, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0":11.82,"A":21.19,"k":2.265,"xc":1.416},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.709,"Steinmetz":{"k":2.3957e-02,"alpha":1.2903,"beta":1.8225},"epsR":8,"tanDelta":0.04},
        "35":  {"muR":  33, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0": 9.13,"A":23.92,"k":2.167,"xc":1.194},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.727,"Steinmetz":{"k":2.6677e-02,"alpha":1.3268,"beta":1.8130},"epsR":8,"tanDelta":0.04},
        "38":  {"muR":  85, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0": 7.71,"A":78.21,"k":1.776,"xc":0.597},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.870,"Steinmetz":{"k":5.0254e-03,"alpha":1.5954,"beta":1.9578},"epsR":8,"tanDelta":0.04},
        "40":  {"muR":  60, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0": 6.64,"A":53.80,"k":1.894,"xc":0.677},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.835,"Steinmetz":{"k":7.6845e-03,"alpha":1.5795,"beta":1.8937},"epsR":8,"tanDelta":0.04},
        "45":  {"muR": 100, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0": 8.43,"A":91.87,"k":2.050,"xc":0.990},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.888,"Steinmetz":{"k":7.9230e-03,"alpha":1.4179,"beta":1.9218},"epsR":8,"tanDelta":0.04},
        "52":  {"muR":  75, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0": 8.58,"A":66.58,"k":2.118,"xc":1.007},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.853,"Steinmetz":{"k":1.5429e-02,"alpha":1.2794,"beta":1.8993},"epsR":8,"tanDelta":0.04},
        "60":  {"muR":  55, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0": 1.00,"A":53.90,"k":2.305,"xc":1.789},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.438,"Steinmetz":{"k":2.4700e-02,"alpha":1.1116,"beta":1.9642},"epsR":8,"tanDelta":0.04},
        "61":  {"muR":  38, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0": 1.00,"A":34.00,"k":2.305,"xc":1.989},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.438,"Steinmetz":{"k":3.1604e-02,"alpha":1.0628,"beta":2.0489},"epsR":8,"tanDelta":0.04},
        "63":  {"muR":  35, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0":27.04,"A": 7.90,"k":1.528,"xc":2.751},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.406,"Steinmetz":{"k":7.0297e-03,"alpha":1.0132,"beta":2.3053},"epsR":8,"tanDelta":0.04},
        "65":  {"muR":  42, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0": 9.13,"A":32.89,"k":2.167,"xc":1.047},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.598,"Steinmetz":{"k":2.3630e-02,"alpha":1.0899,"beta":2.0189},"epsR":8,"tanDelta":0.04},
        "66":  {"muR":  66, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0": 4.20,"A":61.82,"k":2.927,"xc":1.725},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.615,"Steinmetz":{"k":1.0123e-02,"alpha":1.0811,"beta":2.1376},"epsR":8,"tanDelta":0.04},
        "70":  {"muR": 100, "muI": 0, "Cond": 1e3, "DebyeParameter": {"Real": {"y0": 1.00,"A":99.00,"k":1.907,"xc":1.436},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.859,"Steinmetz":{"k":6.9277e-04,"alpha":1.5461,"beta":2.0101},"epsR":8,"tanDelta":0.04},

        # ══════════════════════════════════════════════════════════════
        # SENDUST (FS) — Fe-Si-Al alloy, lower loss than iron powder
        # Best for: PFC, output inductors, moderate-HF chokes
        # ══════════════════════════════════════════════════════════════
        # FS bulk toroid (standard sizes)
        "FS_14":  {"muR": 14, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":14.0,"k":2.481,"xc":2.207},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.532,"Steinmetz":{"k":3.0640e-02,"alpha":1.2302,"beta":1.8323},"epsR":8,"tanDelta":0.04},
        "FS_26":  {"muR": 26, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":26.0,"k":2.481,"xc":1.957},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.677,"Steinmetz":{"k":8.1885e-03,"alpha":1.3407,"beta":1.9017},"epsR":8,"tanDelta":0.04},
        "FS_40":  {"muR": 40, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":40.0,"k":2.481,"xc":1.784},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.729,"Steinmetz":{"k":4.8047e-03,"alpha":1.3686,"beta":1.9431},"epsR":8,"tanDelta":0.04},
        "FS_60":  {"muR": 60, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":60.0,"k":2.481,"xc":1.620},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.764,"Steinmetz":{"k":3.7019e-03,"alpha":1.3817,"beta":1.9589},"epsR":8,"tanDelta":0.04},
        "FS_75":  {"muR": 75, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":75.0,"k":2.481,"xc":1.534},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.814,"Steinmetz":{"k":3.4357e-03,"alpha":1.3543,"beta":1.9837},"epsR":8,"tanDelta":0.04},
        "FS_90":  {"muR": 90, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":90.0,"k":2.481,"xc":1.456},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.781,"Steinmetz":{"k":2.4626e-03,"alpha":1.3727,"beta":2.0228},"epsR":8,"tanDelta":0.04},
        "FS_125": {"muR":125, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":125.0,"k":2.481,"xc":1.324},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.781,"Steinmetz":{"k":4.0993e-03,"alpha":1.2820,"beta":2.0045},"epsR":8,"tanDelta":0.04},

        # ══════════════════════════════════════════════════════════════
        # HIGH FLUX (HF) — Fe-Ni alloy, high Bsat, moderate loss
        # Best for: output inductors, energy storage at moderate freq
        # ══════════════════════════════════════════════════════════════
        "HF_14":  {"muR": 14, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":14.0,"k":2.212,"xc":1.739},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.285,"Steinmetz":{"k":2.2056e-02,"alpha":1.1196,"beta":1.9077},"epsR":8,"tanDelta":0.04},
        "HF_26":  {"muR": 26, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":26.0,"k":2.212,"xc":1.459},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.345,"Steinmetz":{"k":7.6691e-03,"alpha":1.1030,"beta":2.0239},"epsR":8,"tanDelta":0.04},
        "HF_40":  {"muR": 40, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":40.0,"k":2.212,"xc":1.264},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.345,"Steinmetz":{"k":2.7940e-03,"alpha":1.1344,"beta":2.1318},"epsR":8,"tanDelta":0.04},
        "HF_60":  {"muR": 60, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":60.0,"k":2.212,"xc":1.081},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.350,"Steinmetz":{"k":1.9187e-03,"alpha":1.1734,"beta":2.1040},"epsR":8,"tanDelta":0.04},
        "HF_75":  {"muR": 75, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":75.0,"k":2.212,"xc":0.980},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.420,"Steinmetz":{"k":1.9187e-03,"alpha":1.1734,"beta":2.1040},"epsR":8,"tanDelta":0.04},
        "HF_90":  {"muR": 90, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":90.0,"k":2.212,"xc":0.898},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.520,"Steinmetz":{"k":5.4312e-04,"alpha":1.4245,"beta":2.1826},"epsR":8,"tanDelta":0.04},
        "HF_125": {"muR":125, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":125.0,"k":2.212,"xc":0.749},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.524,"Steinmetz":{"k":1.2081e-03,"alpha":1.3048,"beta":2.1060},"epsR":8,"tanDelta":0.04},
        "HF_147": {"muR":147, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":147.0,"k":2.212,"xc":0.676},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.531,"Steinmetz":{"k":8.4587e-04,"alpha":1.5537,"beta":2.0834},"epsR":8,"tanDelta":0.04},
        "HF_160": {"muR":160, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":160.0,"k":2.212,"xc":0.637},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.539,"Steinmetz":{"k":8.4587e-04,"alpha":1.5537,"beta":2.0834},"epsR":8,"tanDelta":0.04},

        # ══════════════════════════════════════════════════════════════
        # HIGH FLUX PLUS (HFP) — improved HF, lower loss
        # ══════════════════════════════════════════════════════════════
        "HFP_40":  {"muR": 40,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":40.0,"k":2.164,"xc":2.239},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.520,"Steinmetz":{"k":1.1743e-03,"alpha":1.3090,"beta":2.0758},"epsR":8,"tanDelta":0.04},
        "HFP_60":  {"muR": 60,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":60.0,"k":2.303,"xc":1.979},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.533,"Steinmetz":{"k":4.8797e-04,"alpha":1.3679,"beta":2.1563},"epsR":8,"tanDelta":0.04},
        "HFP_75":  {"muR": 75,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":75.0,"k":2.533,"xc":1.588},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.520,"Steinmetz":{"k":3.6484e-04,"alpha":1.3951,"beta":2.1695},"epsR":8,"tanDelta":0.04},
        "HFP_90":  {"muR": 90,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":90.0,"k":3.224,"xc":1.606},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.530,"Steinmetz":{"k":4.0960e-04,"alpha":1.4040,"beta":2.1772},"epsR":8,"tanDelta":0.04},
        "HFP_125": {"muR":125,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":125.0,"k":2.510,"xc":1.393},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.570,"Steinmetz":{"k":2.7391e-04,"alpha":1.5195,"beta":2.1404},"epsR":8,"tanDelta":0.04},

        # ══════════════════════════════════════════════════════════════
        # MPP (MP) — Molypermalloy Powder, Fe-Ni-Mo, lowest loss
        # Best for: resonant inductors, precision filters, telecom
        # ══════════════════════════════════════════════════════════════
        "MP_14":  {"muR":  14,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":14.0,"k":2.054,"xc":1.956},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.786,"Steinmetz":{"k":1.4417e-02,"alpha":1.1819,"beta":1.8776},"epsR":8,"tanDelta":0.04},
        "MP_26":  {"muR":  26,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":26.0,"k":2.054,"xc":1.655},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.804,"Steinmetz":{"k":4.0399e-03,"alpha":1.2549,"beta":1.9196},"epsR":8,"tanDelta":0.04},
        "MP_40":  {"muR":  40,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":40.0,"k":2.054,"xc":1.445},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.804,"Steinmetz":{"k":2.8861e-03,"alpha":1.2407,"beta":1.9607},"epsR":8,"tanDelta":0.04},
        "MP_60":  {"muR":  60,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":60.0,"k":2.054,"xc":1.248},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.863,"Steinmetz":{"k":1.5977e-03,"alpha":1.2644,"beta":2.0046},"epsR":8,"tanDelta":0.04},
        "MP_125": {"muR": 125,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":125.0,"k":2.054,"xc":0.890},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.886,"Steinmetz":{"k":6.7209e-04,"alpha":1.3946,"beta":2.0854},"epsR":8,"tanDelta":0.04},
        "MP_147": {"muR": 147,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":147.0,"k":2.054,"xc":0.811},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.905,"Steinmetz":{"k":8.3765e-04,"alpha":1.3586,"beta":2.0937},"epsR":8,"tanDelta":0.04},
        "MP_160": {"muR": 160,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":160.0,"k":2.054,"xc":0.770},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.898,"Steinmetz":{"k":3.2872e-04,"alpha":1.6226,"beta":2.0388},"epsR":8,"tanDelta":0.04},
        "MP_173": {"muR": 173,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":173.0,"k":2.054,"xc":0.732},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.898,"Steinmetz":{"k":5.2238e-04,"alpha":1.6330,"beta":2.0093},"epsR":8,"tanDelta":0.04},
        "MP_205": {"muR": 205,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":205.0,"k":2.054,"xc":0.649},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.898,"Steinmetz":{"k":3.4493e-04,"alpha":1.7732,"beta":2.0064},"epsR":8,"tanDelta":0.04},

        # ══════════════════════════════════════════════════════════════
        # KOOL Mµ (OC) — Fe-Si-Al sendust type, very low loss
        # Best for: output filter inductors, 100kHz–1MHz
        # ══════════════════════════════════════════════════════════════
        "OC_14":  {"muR": 14,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":14.0,"k":2.326,"xc":1.992},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.140,"Steinmetz":{"k":1.0650e-02,"alpha":1.2203,"beta":1.9004},"epsR":8,"tanDelta":0.04},
        "OC_26":  {"muR": 26,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":26.0,"k":2.326,"xc":1.725},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.124,"Steinmetz":{"k":5.1162e-03,"alpha":1.2700,"beta":1.9229},"epsR":8,"tanDelta":0.04},
        "OC_40":  {"muR": 40,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":40.0,"k":2.326,"xc":1.540},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.230,"Steinmetz":{"k":2.1765e-03,"alpha":1.2881,"beta":2.0617},"epsR":8,"tanDelta":0.04},
        "OC_60":  {"muR": 60,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":60.0,"k":2.326,"xc":1.366},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.195,"Steinmetz":{"k":1.0494e-03,"alpha":1.3136,"beta":2.0929},"epsR":8,"tanDelta":0.04},
        "OC_75":  {"muR": 75,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":75.0,"k":2.326,"xc":1.270},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.268,"Steinmetz":{"k":1.2365e-03,"alpha":1.2567,"beta":2.1407},"epsR":8,"tanDelta":0.04},
        "OC_90":  {"muR": 90,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":90.0,"k":2.326,"xc":1.191},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.207,"Steinmetz":{"k":7.4322e-04,"alpha":1.3524,"beta":2.0889},"epsR":8,"tanDelta":0.04},
        "OC_125": {"muR":125,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":125.0,"k":2.326,"xc":1.050},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.212,"Steinmetz":{"k":5.0515e-04,"alpha":1.4126,"beta":2.1338},"epsR":8,"tanDelta":0.04},

        # ══════════════════════════════════════════════════════════════
        # KOOL Mµ MAX (OD) — Fe-Si-Al, higher Bsat (~1.6T)
        # ══════════════════════════════════════════════════════════════
        "OD_14":  {"muR": 14,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":14.0,"k":2.326,"xc":1.992},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.473,"Steinmetz":{"k":1.1905e-02,"alpha":1.2099,"beta":1.9453},"epsR":8,"tanDelta":0.04},
        "OD_26":  {"muR": 26,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":26.0,"k":2.326,"xc":1.725},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.535,"Steinmetz":{"k":9.7448e-03,"alpha":1.2221,"beta":1.9084},"epsR":8,"tanDelta":0.04},
        "OD_40":  {"muR": 40,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":40.0,"k":2.326,"xc":1.540},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.595,"Steinmetz":{"k":4.1342e-03,"alpha":1.2737,"beta":1.9913},"epsR":8,"tanDelta":0.04},
        "OD_60":  {"muR": 60,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":60.0,"k":2.326,"xc":1.366},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.637,"Steinmetz":{"k":1.9625e-03,"alpha":1.3429,"beta":2.0465},"epsR":8,"tanDelta":0.04},
        "OD_75":  {"muR": 75,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":75.0,"k":2.326,"xc":1.270},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.690,"Steinmetz":{"k":1.3815e-03,"alpha":1.3100,"beta":2.1384},"epsR":8,"tanDelta":0.04},
        "OD_90":  {"muR": 90,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":90.0,"k":2.326,"xc":1.191},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.692,"Steinmetz":{"k":1.7031e-03,"alpha":1.4292,"beta":1.9994},"epsR":8,"tanDelta":0.04},

        # ══════════════════════════════════════════════════════════════
        # KOOL Mµ ULTRA (OE) — lowest loss of sendust family
        # ══════════════════════════════════════════════════════════════
        "OE_14":  {"muR": 14,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":14.0,"k":2.326,"xc":1.992},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.290,"Steinmetz":{"k":1.4596e-02,"alpha":1.1707,"beta":1.9030},"epsR":8,"tanDelta":0.04},
        "OE_26":  {"muR": 26,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":26.0,"k":2.326,"xc":1.725},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.243,"Steinmetz":{"k":9.7531e-03,"alpha":1.1892,"beta":1.9416},"epsR":8,"tanDelta":0.04},
        "OE_40":  {"muR": 40,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":40.0,"k":2.326,"xc":1.540},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.400,"Steinmetz":{"k":2.6040e-03,"alpha":1.2574,"beta":2.0307},"epsR":8,"tanDelta":0.04},
        "OE_60":  {"muR": 60,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":60.0,"k":2.326,"xc":1.366},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.322,"Steinmetz":{"k":2.7215e-03,"alpha":1.3029,"beta":2.0090},"epsR":8,"tanDelta":0.04},
        "OE_75":  {"muR": 75,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":75.0,"k":2.326,"xc":1.270},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.198,"Steinmetz":{"k":2.1498e-03,"alpha":1.2511,"beta":2.1337},"epsR":8,"tanDelta":0.04},
        "OE_90":  {"muR": 90,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":90.0,"k":2.326,"xc":1.191},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.322,"Steinmetz":{"k":2.5189e-03,"alpha":1.3047,"beta":2.0115},"epsR":8,"tanDelta":0.04},

        # ══════════════════════════════════════════════════════════════
        # XFlux (FX) — Fe-Si, very high Bsat (~1.8T), low loss
        # Best for: DC bias inductors, energy storage
        # ══════════════════════════════════════════════════════════════
        "FX_14":  {"muR": 14,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":14.0,"k":2.481,"xc":2.207},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.638,"Steinmetz":{"k":1.2160e-02,"alpha":1.1408,"beta":2.0685},"epsR":8,"tanDelta":0.04},
        "FX_26":  {"muR": 26,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":26.0,"k":2.481,"xc":1.957},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.706,"Steinmetz":{"k":3.0946e-03,"alpha":1.1684,"beta":2.1674},"epsR":8,"tanDelta":0.04},
        "FX_40":  {"muR": 40,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":40.0,"k":2.481,"xc":1.784},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.760,"Steinmetz":{"k":3.7299e-03,"alpha":1.1817,"beta":2.1102},"epsR":8,"tanDelta":0.04},
        "FX_60":  {"muR": 60,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":60.0,"k":2.481,"xc":1.620},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.799,"Steinmetz":{"k":2.3763e-03,"alpha":1.2716,"beta":2.0792},"epsR":8,"tanDelta":0.04},
        "FX_75":  {"muR": 75,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":75.0,"k":2.481,"xc":1.534},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.816,"Steinmetz":{"k":2.1712e-03,"alpha":1.1969,"beta":2.1606},"epsR":8,"tanDelta":0.04},
        "FX_90":  {"muR": 90,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":90.0,"k":2.481,"xc":1.456},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.816,"Steinmetz":{"k":2.8835e-03,"alpha":1.2129,"beta":2.1021},"epsR":8,"tanDelta":0.04},
        "FX_125": {"muR":125,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":125.0,"k":2.481,"xc":1.324},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.840,"Steinmetz":{"k":3.3422e-03,"alpha":1.1972,"beta":2.0720},"epsR":8,"tanDelta":0.04},

        # ══════════════════════════════════════════════════════════════
        # GreenX (GX) — Fe-Si, high Bsat, very low core loss at low freq
        # Best for: low-frequency (<100kHz) high-power inductors
        # ══════════════════════════════════════════════════════════════
        "GX_40":  {"muR": 40,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":40.0,"k":1.980,"xc":2.656},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.500,"Steinmetz":{"k":1.2141e-03,"alpha":1.2123,"beta":2.1199},"epsR":8,"tanDelta":0.04},
        "GX_60":  {"muR": 60,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":60.0,"k":2.418,"xc":2.161},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.510,"Steinmetz":{"k":5.5338e-04,"alpha":1.2574,"beta":2.1822},"epsR":8,"tanDelta":0.04},
        "GX_75":  {"muR": 75,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":75.0,"k":3.454,"xc":1.966},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.530,"Steinmetz":{"k":5.3065e-04,"alpha":1.2372,"beta":2.2261},"epsR":8,"tanDelta":0.04},

        # ══════════════════════════════════════════════════════════════
        # SUPER-PERM (SP) / SUPER MIX (SM) — Fe-Ni high perm cores
        # Best for: EMI chokes, current transformers, wide-band
        # ══════════════════════════════════════════════════════════════
        "SP_14":  {"muR": 14,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":14.0,"k":2.994,"xc":2.408},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.805,"Steinmetz":{"k":2.2251e-02,"alpha":1.1145,"beta":1.8320},"epsR":8,"tanDelta":0.04},
        "SP_26":  {"muR": 26,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":26.0,"k":2.994,"xc":2.130},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.865,"Steinmetz":{"k":6.9703e-03,"alpha":1.1564,"beta":1.8869},"epsR":8,"tanDelta":0.04},
        "SP_40":  {"muR": 40,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":40.0,"k":2.994,"xc":1.957},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.903,"Steinmetz":{"k":2.1372e-03,"alpha":1.2695,"beta":1.9228},"epsR":8,"tanDelta":0.04},
        "SP_60":  {"muR": 60,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":60.0,"k":2.994,"xc":1.806},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.897,"Steinmetz":{"k":1.7952e-03,"alpha":1.2477,"beta":1.9470},"epsR":8,"tanDelta":0.04},
        "SP_75":  {"muR": 75,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":75.0,"k":2.994,"xc":1.713},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.924,"Steinmetz":{"k":1.4287e-03,"alpha":1.2182,"beta":1.9827},"epsR":8,"tanDelta":0.04},
        "SP_90":  {"muR": 90,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":90.0,"k":2.994,"xc":1.638},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.901,"Steinmetz":{"k":1.7155e-03,"alpha":1.2312,"beta":1.9636},"epsR":8,"tanDelta":0.04},
        "SM_14":  {"muR": 14,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":14.0,"k":2.994,"xc":2.408},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.862,"Steinmetz":{"k":1.3559e-02,"alpha":1.2077,"beta":1.8587},"epsR":8,"tanDelta":0.04},
        "SM_26":  {"muR": 26,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":26.0,"k":2.994,"xc":2.130},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.887,"Steinmetz":{"k":6.0866e-03,"alpha":1.2435,"beta":1.8935},"epsR":8,"tanDelta":0.04},
        "SM_40":  {"muR": 40,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":40.0,"k":2.994,"xc":1.957},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.920,"Steinmetz":{"k":2.0552e-03,"alpha":1.3018,"beta":1.9564},"epsR":8,"tanDelta":0.04},
        "SM_60":  {"muR": 60,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":60.0,"k":2.994,"xc":1.806},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.962,"Steinmetz":{"k":2.1579e-03,"alpha":1.2813,"beta":1.9196},"epsR":8,"tanDelta":0.04},
        "SM_75":  {"muR": 75,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":75.0,"k":2.994,"xc":1.713},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.938,"Steinmetz":{"k":8.5790e-04,"alpha":1.3436,"beta":2.0315},"epsR":8,"tanDelta":0.04},
        "SM_90":  {"muR": 90,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":90.0,"k":2.994,"xc":1.638},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.914,"Steinmetz":{"k":1.2865e-03,"alpha":1.2653,"beta":2.0037},"epsR":8,"tanDelta":0.04},
        "SM_125": {"muR":125,"muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":125.0,"k":2.994,"xc":1.507},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.923,"Steinmetz":{"k":8.8046e-04,"alpha":1.3047,"beta":1.9808},"epsR":8,"tanDelta":0.04},
    }

    if Reference is None:
        return tuple(material_properties.keys())
    else:
        dictaux = material_properties.get(Reference, base_return)
        dictaux["Material"] = Reference
        return dictaux
