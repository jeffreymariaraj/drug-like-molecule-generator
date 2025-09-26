# 🧬 Drug-Like Molecule Generator

[![Streamlit App](https://img.shields.io/badge/Streamlit-1.28.1-red.svg)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![RDKit](https://img.shields.io/badge/RDKit-2023.9.1-green.svg)](https://rdkit.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful **Streamlit web application** for generating drug-like molecules using combinatorial chemistry. This MVP demonstrates how to create diverse molecular libraries by combining chemical fragments and linkers, with real-time property calculation and visualization.

![Demo](https://via.placeholder.com/800x400/4f46e5/ffffff?text=🧬+Drug-Like+Molecule+Generator)

## ✨ Features

### 🔬 **Smart Molecule Generation**
- **Combinatorial Assembly**: Combines 10+ chemical fragments with 12+ linkers
- **Chemical Validation**: Uses RDKit for structure validation and sanitization
- **Drug-Like Filtering**: Only generates molecules with MW 150-500 Da
- **Diverse Chemistry**: Supports heterocycles, aromatics, and functional groups

### 📊 **Comprehensive Property Analysis**
- **Molecular Weight (MW)**: Calculated using RDKit
- **LogP**: Octanol-water partition coefficient
- **TPSA**: Topological Polar Surface Area
- **H-Bond Donors/Acceptors**: Hydrogen bonding capacity
- **2D Visualization**: Interactive molecule structure display

### 🎨 **User-Friendly Interface**
- **Interactive Controls**: Slider for molecule count (1-50)
- **Real-Time Generation**: One-click molecule creation
- **Data Export**: Download results as CSV
- **Responsive Design**: Works on desktop and mobile

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/drug-like-molecule-generator.git
   cd drug-like-molecule-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

## 📋 Requirements

```
streamlit==1.28.1
rdkit==2023.9.1
pandas==2.1.1
pillow==10.0.1
```

## 🎯 Usage

1. **Configure Parameters**
   - Use the sidebar slider to select number of molecules (1-50)
   - Click "🔬 Generate Molecules" to start

2. **View Results**
   - Browse the generated molecules in the interactive table
   - View 2D molecular structures in the grid layout
   - Analyze calculated properties (MW, LogP, TPSA, etc.)

3. **Export Data**
   - Click "📥 Download Results as CSV" to save your data

## 🔧 Chemical Components

### Fragments (Building Blocks)
- **Aromatics**: Benzene, Pyridine, Pyrimidine, Pyrazine
- **Heterocycles**: Furan, Pyrrole, Thiophene, Isoxazole
- **Azoles**: Pyrazole, Imidazole

### Linkers (Connectors)
- **Alkanes**: Methane, Ethane, Cyclopropane, Cyclobutane
- **Functional Groups**: Carbonyl, Oxygen, Sulfur, Nitrogen
- **Unsaturated**: Alkenes, Alkynes
- **Cyclic**: Oxirane

## 🌐 Deployment

### Streamlit Cloud (Recommended)
1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy automatically!

### Other Platforms
- **Heroku**: Add a `Procfile` and deploy
- **Railway**: Connect GitHub repo for automatic deployment
- **AWS/Azure/GCP**: Use containerized deployment

## 📊 Example Output

| Molecule ID | SMILES | MW (Da) | LogP | TPSA | H-Acceptors | H-Donors |
|-------------|--------|---------|------|------|-------------|----------|
| MOL_1 | c1ccccc1CCc1cnccc1 | 234.32 | 2.45 | 28.68 | 2 | 0 |
| MOL_2 | c1cnccc1C=O | 145.16 | 1.23 | 32.86 | 3 | 0 |
| MOL_3 | c1cocc1C1CC1 | 178.22 | 1.89 | 22.12 | 2 | 0 |

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **RDKit** for cheminformatics functionality
- **Streamlit** for the amazing web framework
- **OpenSMILES** for chemical structure standards

## 📞 Support

If you have any questions or issues:
- Open an issue on GitHub
- Check the [Streamlit documentation](https://docs.streamlit.io/)
- Review [RDKit documentation](https://rdkit.readthedocs.io/)

---

**Made with ❤️ for computational chemistry enthusiasts**

[⭐ Star this repo](https://github.com/yourusername/drug-like-molecule-generator) | [🐛 Report Bug](https://github.com/yourusername/drug-like-molecule-generator/issues) | [💡 Request Feature](https://github.com/yourusername/drug-like-molecule-generator/issues)
