<div align="center">
  <img src="./logoabout.png" alt="MAGNETISiM Logo" width="300"/>

  # MAGNETISiM

  *A modular platform for fast, reproducible electromagnetic modeling for education, research, and industry.*

  [![Website](https://img.shields.io/badge/Website-magnetisim.com-blue?style=flat-square)](https://www.magnetisim.com)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
</div>

---

## What is MAGNETISiM?

The ultimate design and simulation platform for magnetic components. MAGNETISiM automates complex electromagnetic and thermal calculations, turning basic inputs into ready-to-use circuit models in seconds.

---

## Why use MAGNETISiM?

As a power electronics engineer or researcher, designing magnetics often involves jumping between different tools, datasheets, and complex physics simulators. MAGNETISiM simplifies this workflow into a single, unified platform:

* 🚀 **Automated FEA Simulation:** Run complex Finite Element Analysis (FEA) in the background. You get the accuracy of advanced numerical methods without needing to be an expert in meshing, boundaries, or solver configurations.
* 📚 **Built-in Materials Database:** Forget about searching through manufacturer PDFs. Access a comprehensive, integrated library of commercial cores, bobbins, and magnetic materials directly within the tool.
* 🧠 **Advanced Analysis Made Simple:** Automatically calculate core losses, winding losses, parasitic capacitances, and reluctance matrices effortlessly. 
* 🌡️ **Multiphysics Extraction:** Obtain a complete picture of your component. MAGNETISiM seamlessly couples and extracts the electrical, magnetic, and thermal profiles of your design.
* ⚡ **Direct to Circuit Simulator:** Stop guessing your component's behavior in a circuit. Export highly accurate models directly to **LTSpice**, bridging the gap between component design and converter simulation.

---

## How it works

Everything you need to design, simulate, and export, unified in one logical workflow:

```text
┌─────────────────────────────────────────────────────────────────┐
│                        MAGNETISiM Workflow                      │
├─────────────────────────────────────────────────────────────────┤
│  INPUTS (Your Design Specs)                                     │
│  ├── Geometry: Core shape (ETD, RM...), Winding shape, Airgap   │
│  ├── Materials: Ferrite, Wire type (PCB, Litz, Round...)        │
│  └── Setup: Frequencies, ambient temperature...                 │
│                                                                 │
│  MAGNETISiM ENGINE (The Magic)                                  │
│  ├── Automated FEA: Background meshing & solving                │
│  ├── Multiphysics: Coupled magnetic & thermal analysis (future) │
│  └── Analytical Engine: Loss models & parasitic extraction      │
│                                                                 │
│  OUTPUTS (Ready to Use)                                         │
│  ├── Circuit Models: Direct export to LTSpice (.asc / .sub)     │
│  ├── Component Data: Inductance matrix, Leakage, and more       │
│  ├── Loss Analysis: Core & Winding power dissipation breakdown  │
│  └── Thermal Profile: Estimated temperature rise (in comming)   │
└─────────────────────────────────────────────────────────────────┘
```

## 🚀 Getting Started & Examples

MAGNETISiM is designed to be intuitive from the get-go. Whether you are a beginner or an advanced user, we provide multiple resources to speed up your workflow:

* **Built-in Examples:** The application includes several pre-configured examples. Load them directly to see how components are defined, meshed, and simulated.
* **Web Tutorials:** Visit our website to find detailed presentations, use-case demonstrations, and step-by-step guides.
* **Quick-Start Templates:** We provide ready-to-use templates in this repository so you don't have to start from scratch. Check them out here: [**MAGNETISiM Templates**](https://github.com/aDelgado13/MAGNETISiM/tree/main/Template)
* **Schemas:** Comprehensive JSON schemas are available to help you understand the underlying data structures and integrate them into your own pipelines.

---

## 🗄️ Component Database: What's Included?

MAGNETISiM comes equipped with a growing database of real-world components, materials, and geometries to streamline your design process. 

| Category | Supported Types & Details |
| :--- | :--- |
| **Manufacturers** | **TDK, FERROXCUBE, MICROMETALS** *(Many more coming soon!)* |
| **Standard Cores** | E, EI, EC, U, UI, P, PT, PH, PM, RM, ETD, EQ, PQ, PQI, ER |
| **Planar Cores** | EPlanar, EIPlanar, EL, ELT, EQPLT, ERPlanar, EIRPlanar |
| **Special / Air Cores** | AIRXY, IPTXY, AIRRZ, IPTRZ |
| **Windings** | *PCB, Round, and 🚧 Litz wire support are in the final stages of development and will be released very soon!* |

**All database entries include:**
* Accurate dimensional information and parameterization.
* Material properties tailored for electromagnetic and thermal simulations.

---

## 📈 Continuous Development & Roadmap

MAGNETISiM is evolving every single day. Maintained by a dedicated team of students and professors at the **Universidad Politécnica de Madrid (UPM)**, we deliver weekly builds based on the latest code. This agile approach allows our community to test bug fixes, provide feedback, and explore new features the moment they are developed.

### 🚀 Upcoming Features
*Currently powered by ongoing thesis projects and research at UPM:*

* 🌡️ **3D Thermal Simulations:** Full integration with Elmer for advanced, three-dimensional thermal modeling.
* 🧲 **3D Electromagnetic Simulations:** Extended capabilities using Elmer to tackle complex 3D FEA scenarios.
* ⚡ **Advanced Circuit Modeling:** Automated symbol creation and frequency-domain circuit modeling for both **QSpice** and **LTspice**.
* 🔌 **Automatic PCB Generation:** Seamless integration with **KiCad** to automatically generate footprints and board layouts for your custom magnetics.
* 🏗️ **Automated CAD Design:** Direct integration with **FreeCAD** for automatic 3D bobbin generation and mechanical design.

---
<div align="center">
  <i>MAGNETISiM</i><br>
  <b><a href="https://www.magnetisim.com">www.magnetisim.com</a></b>
</div>

