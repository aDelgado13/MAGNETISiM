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
#=== DESCRIPTION: Magnetics Inc. Materials                        ===#
#=== CREATED    : 17/04/2026                                      ===#
#=== UPDATED    : 17/04/2026                                      ===#
#====================================================================#
#====================================================================#
# https://www.mag-inc.com
# Material fitting
# x = MHz
# Eq real= y0 + A / ( 1 + exp(k*(log10(x*1e-6)-xc)))
# Eq imag= a1*exp(-(log10(x*1e-6)-b1)/c1)^2 + a2*exp(-(log10(x*1e-6)-b2)/c2)^2
# Steinmetz = k * f(kHz)^alpha * B(mT)^beta  kW/m3 @ 100C
# Sources:
#   - Magnetics Ferrite Catalog (2022): https://www.mag-inc.com
#   - Magnetics Core Loss Calculator: https://www.mag-inc.com/Design/Design-Tools
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
        # MAGNETICS SOFT FERRITES (MnZn)
        # ══════════════════════════════════════════════════════════════
        "F": {
            # muR=3000, Tc>210C, Bsat=470mT
            "muR": 3000, "muI": 0, "Cond": 1/3,
            "DebyeParameter": {
                "Real": {"y0":11.1741,"A":2977.9909,"k":6.1899,"xc":0.2538},
                "Imag": {"a1":2069.6572,"b1":0.3603,"c1":0.2717,"a2":256.7777,"b2":0.7580,"c2":1.0044}},
            "Phi": 0, "Bmax": 470e-3,
            "Steinmetz": {"k": 6.5e-06, "alpha": 1.32, "beta": 2.10},"epsR":12,"tanDelta":0.02},

        "P": {
            # muR=2500, Tc>215C, Bsat=470mT 
            "muR": 2500, "muI": 0, "Cond": 1/5,
            "DebyeParameter": {
                "Real": {"y0":11.1741,"A":1977.9909,"k":6.1899,"xc":0.2538},
                "Imag": {"a1":2069.6572,"b1":0.3603,"c1":0.2717,"a2":256.7777,"b2":0.7580,"c2":1.0044}},
            "Phi": 0, "Bmax": 470e-3,
            "Steinmetz": {"k": 9.5e-06, "alpha": 1.30, "beta": 2.05},"epsR":12,"tanDelta":0.02},

        "R": {
            # muR=2300, Tc>210C, Bsat=470mT
            "muR": 2300, "muI": 0, "Cond": 1/5,
            "DebyeParameter": {
                "Real": {"y0":-90.7144,"A":2583.9055,"k":14.1168,"xc":0.2706},
                "Imag": {"a1":1430.9021,"b1":0.1911,"c1":0.2135,"a2":763.9520,"b2":0.4517,"c2":0.5188}},
            "Phi": 0, "Bmax": 470e-3,
            "Steinmetz": {"k": 5.5e-08, "alpha": 1.62, "beta": 2.85},"epsR":12,"tanDelta":0.02},

        "T": {
            # muR=3000, Tc>215C, Bsat=530mT
            "muR": 3000, "muI": 0, "Cond": 1/3,
            "DebyeParameter": {
                "Real": {"y0":20.3595,"A":2519.7145,"k":35.7137,"xc":0.2008},
                "Imag": {"a1":1763.7515,"b1":0.1510,"c1":0.1374,"a2":1016.5035,"b2":0.4071,"c2":0.4650}},
            "Phi": 0, "Bmax": 530e-3,
            "Steinmetz": {"k": 3.5e-08, "alpha": 1.68, "beta": 2.90},"epsR":12,"tanDelta":0.02},

        "L": {
            # muR=750, Tc>280C, Bsat=520mT 
            "muR": 750, "muI": 0, "Cond": 1/20,
            "DebyeParameter": {
                "Real": {"y0":20.0,"A":730.0,"k":4.5,"xc":0.8},
                "Imag": {"a1":600.0,"b1":0.5,"c1":0.35,"a2":150.0,"b2":1.0,"c2":0.5}},
            "Phi": 0, "Bmax": 520e-3,
            "Steinmetz": {"k": 1.2e-09, "alpha": 2.20, "beta": 2.60},"epsR":10,"tanDelta":0.01},

        # ══════════════════════════════════════════════════════════════
        # MPP (Molypermalloy Powder) 
        # ══════════════════════════════════════════════════════════════
        "MPP_14":  {"muR": 14, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 14.0,"k":2.054,"xc":1.956},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.720,"Steinmetz":{"k":1.4417e-02,"alpha":1.1819,"beta":1.8776},"epsR":7,"tanDelta":0.03},
        "MPP_26":  {"muR": 26, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 26.0,"k":2.054,"xc":1.655},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.740,"Steinmetz":{"k":4.0399e-03,"alpha":1.2549,"beta":1.9196},"epsR":7,"tanDelta":0.03},
        "MPP_40":  {"muR": 40, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 40.0,"k":2.054,"xc":1.445},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.760,"Steinmetz":{"k":2.8861e-03,"alpha":1.2407,"beta":1.9607},"epsR":7,"tanDelta":0.03},
        "MPP_60":  {"muR": 60, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 60.0,"k":2.054,"xc":1.248},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.750,"Steinmetz":{"k":1.5977e-03,"alpha":1.2644,"beta":2.0046},"epsR":7,"tanDelta":0.03},
        "MPP_125": {"muR":125, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":125.0,"k":2.054,"xc":0.890},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.700,"Steinmetz":{"k":6.7209e-04,"alpha":1.3946,"beta":2.0854},"epsR":7,"tanDelta":0.03},
        "MPP_160": {"muR":160, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":160.0,"k":2.054,"xc":0.770},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.680,"Steinmetz":{"k":3.2872e-04,"alpha":1.6226,"beta":2.0388},"epsR":7,"tanDelta":0.03},
        "MPP_200": {"muR":200, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":200.0,"k":2.054,"xc":0.649},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.650,"Steinmetz":{"k":2.5e-04,  "alpha":1.750, "beta":2.020},"epsR":7,"tanDelta":0.03},
        "MPP_300": {"muR":300, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":300.0,"k":2.054,"xc":0.500},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.600,"Steinmetz":{"k":1.5e-04,  "alpha":1.900, "beta":2.050},"epsR":7,"tanDelta":0.03},
        "MPP_550": {"muR":550, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":550.0,"k":2.054,"xc":0.340},"Imag":_NO_IMAG},"Phi":0,"Bmax":0.550,"Steinmetz":{"k":8.0e-05,  "alpha":2.000, "beta":2.100},"epsR":7,"tanDelta":0.03},

        # ══════════════════════════════════════════════════════════════
        # HIGH FLUX 
        # ══════════════════════════════════════════════════════════════
        "HighFlux_14":  {"muR": 14, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 14.0,"k":2.212,"xc":1.739},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.500,"Steinmetz":{"k":2.2056e-02,"alpha":1.1196,"beta":1.9077},"epsR":8,"tanDelta":0.04},
        "HighFlux_26":  {"muR": 26, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 26.0,"k":2.212,"xc":1.459},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.500,"Steinmetz":{"k":7.6691e-03,"alpha":1.1030,"beta":2.0239},"epsR":8,"tanDelta":0.04},
        "HighFlux_40":  {"muR": 40, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 40.0,"k":2.212,"xc":1.264},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.500,"Steinmetz":{"k":2.7940e-03,"alpha":1.1344,"beta":2.1318},"epsR":8,"tanDelta":0.04},
        "HighFlux_60":  {"muR": 60, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 60.0,"k":2.212,"xc":1.081},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.500,"Steinmetz":{"k":1.9187e-03,"alpha":1.1734,"beta":2.1040},"epsR":8,"tanDelta":0.04},
        "HighFlux_125": {"muR":125, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":125.0,"k":2.212,"xc":0.749},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.500,"Steinmetz":{"k":1.2081e-03,"alpha":1.3048,"beta":2.1060},"epsR":8,"tanDelta":0.04},
        "HighFlux_160": {"muR":160, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":160.0,"k":2.212,"xc":0.637},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.500,"Steinmetz":{"k":8.4587e-04,"alpha":1.5537,"beta":2.0834},"epsR":8,"tanDelta":0.04},

        # ══════════════════════════════════════════════════════════════
        # KOOL Mµ 
        # ══════════════════════════════════════════════════════════════
        "KoolMu_14":  {"muR": 14, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 14.0,"k":2.326,"xc":1.992},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.000,"Steinmetz":{"k":1.0650e-02,"alpha":1.2203,"beta":1.9004},"epsR":7,"tanDelta":0.03},
        "KoolMu_26":  {"muR": 26, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 26.0,"k":2.326,"xc":1.725},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.000,"Steinmetz":{"k":5.1162e-03,"alpha":1.2700,"beta":1.9229},"epsR":7,"tanDelta":0.03},
        "KoolMu_40":  {"muR": 40, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 40.0,"k":2.326,"xc":1.540},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.000,"Steinmetz":{"k":2.1765e-03,"alpha":1.2881,"beta":2.0617},"epsR":7,"tanDelta":0.03},
        "KoolMu_60":  {"muR": 60, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 60.0,"k":2.326,"xc":1.366},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.000,"Steinmetz":{"k":1.0494e-03,"alpha":1.3136,"beta":2.0929},"epsR":7,"tanDelta":0.03},
        "KoolMu_75":  {"muR": 75, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 75.0,"k":2.326,"xc":1.270},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.000,"Steinmetz":{"k":1.2365e-03,"alpha":1.2567,"beta":2.1407},"epsR":7,"tanDelta":0.03},
        "KoolMu_90":  {"muR": 90, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 90.0,"k":2.326,"xc":1.191},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.000,"Steinmetz":{"k":7.4322e-04,"alpha":1.3524,"beta":2.0889},"epsR":7,"tanDelta":0.03},
        "KoolMu_125": {"muR":125, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":125.0,"k":2.326,"xc":1.050},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.000,"Steinmetz":{"k":5.0515e-04,"alpha":1.4126,"beta":2.1338},"epsR":7,"tanDelta":0.03},

        # ══════════════════════════════════════════════════════════════
        # XFLUX 
        # ══════════════════════════════════════════════════════════════
        "XFlux_26":  {"muR": 26, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 26.0,"k":2.481,"xc":1.957},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.500,"Steinmetz":{"k":3.0946e-03,"alpha":1.1684,"beta":2.1674},"epsR":8,"tanDelta":0.04},
        "XFlux_40":  {"muR": 40, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 40.0,"k":2.481,"xc":1.784},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.500,"Steinmetz":{"k":3.7299e-03,"alpha":1.1817,"beta":2.1102},"epsR":8,"tanDelta":0.04},
        "XFlux_60":  {"muR": 60, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 60.0,"k":2.481,"xc":1.620},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.500,"Steinmetz":{"k":2.3763e-03,"alpha":1.2716,"beta":2.0792},"epsR":8,"tanDelta":0.04},
        "XFlux_75":  {"muR": 75, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 75.0,"k":2.481,"xc":1.534},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.500,"Steinmetz":{"k":2.1712e-03,"alpha":1.1969,"beta":2.1606},"epsR":8,"tanDelta":0.04},
        "XFlux_125": {"muR":125, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A":125.0,"k":2.481,"xc":1.324},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.500,"Steinmetz":{"k":3.3422e-03,"alpha":1.1972,"beta":2.0720},"epsR":8,"tanDelta":0.04},

        # ══════════════════════════════════════════════════════════════
        # EDGE
        # ══════════════════════════════════════════════════════════════
        "Edge_14":  {"muR": 14, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 14.0,"k":2.326,"xc":1.992},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.000,"Steinmetz":{"k":8.0e-03,"alpha":1.2000,"beta":1.9500},"epsR":7,"tanDelta":0.03},
        "Edge_26":  {"muR": 26, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 26.0,"k":2.326,"xc":1.725},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.000,"Steinmetz":{"k":3.5e-03,"alpha":1.2500,"beta":1.9800},"epsR":7,"tanDelta":0.03},
        "Edge_40":  {"muR": 40, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 40.0,"k":2.326,"xc":1.540},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.000,"Steinmetz":{"k":1.5e-03,"alpha":1.2700,"beta":2.0400},"epsR":7,"tanDelta":0.03},
        "Edge_60":  {"muR": 60, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 60.0,"k":2.326,"xc":1.366},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.000,"Steinmetz":{"k":8.0e-04,"alpha":1.3000,"beta":2.0800},"epsR":7,"tanDelta":0.03},
        "Edge_75":  {"muR": 75, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 75.0,"k":2.326,"xc":1.270},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.000,"Steinmetz":{"k":9.5e-04,"alpha":1.2800,"beta":2.1000},"epsR":7,"tanDelta":0.03},
        "Edge_90":  {"muR": 90, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 90.0,"k":2.326,"xc":1.191},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.000,"Steinmetz":{"k":6.0e-04,"alpha":1.3200,"beta":2.0800},"epsR":7,"tanDelta":0.03},

        # ══════════════════════════════════════════════════════════════
        # 75-SERIES
        # ══════════════════════════════════════════════════════════════
        "75_26":  {"muR": 26, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 26.0,"k":2.200,"xc":1.700},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.000,"Steinmetz":{"k":1.2e-02,"alpha":1.1500,"beta":1.9000},"epsR":7,"tanDelta":0.03},
        "75_40":  {"muR": 40, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 40.0,"k":2.200,"xc":1.500},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.000,"Steinmetz":{"k":6.0e-03,"alpha":1.1800,"beta":1.9500},"epsR":7,"tanDelta":0.03},
        "75_60":  {"muR": 60, "muI":0,"Cond":200,"DebyeParameter":{"Real":{"y0":0.0,"A": 60.0,"k":2.200,"xc":1.330},"Imag":_NO_IMAG},"Phi":0,"Bmax":1.000,"Steinmetz":{"k":2.5e-03,"alpha":1.2200,"beta":2.0200},"epsR":7,"tanDelta":0.03},
    }

    if Reference is None:
        return tuple(material_properties.keys())
    else:
        dictaux = material_properties.get(Reference, base_return)
        dictaux["Material"] = Reference
        return dictaux
