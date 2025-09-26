import streamlit as st
import pandas as pd
import random
import io
from PIL import Image

# Try to import RDKit with error handling
try:
    from rdkit import Chem
    from rdkit.Chem import Draw, Descriptors, Crippen, rdMolDescriptors
    RDKIT_AVAILABLE = True
except ImportError as e:
    st.error(f"RDKit not available: {e}")
    st.error("This app requires RDKit for molecule generation. Please check the deployment configuration.")
    st.info("💡 **Troubleshooting tips:**")
    st.info("1. Try using Streamlit Cloud instead of Community Cloud")
    st.info("2. Consider Railway.app or Render.com for deployment")
    st.info("3. Check if your Python version is compatible (3.8+)")
    RDKIT_AVAILABLE = False
    # Create dummy functions for when RDKit is not available
    Chem = None
    Draw = None
    Descriptors = None
    Crippen = None
    rdMolDescriptors = None

# Set page configuration
st.set_page_config(
    page_title="Drug-like Molecule Generator",
    page_icon="🧬",
    layout="wide"
)

# Title and description
st.title("🧬 Drug-like Molecule Generator")
st.markdown("Generate drug-like molecules using combinatorial fragment assembly")

def main():
    # Fragment and linker definitions
    fragments = [
        "c1ccccc1",      # benzene
        "c1cnccc1",      # pyridine
        "c1cncnc1",      # pyrimidine
        "c1ccncc1",      # pyrazine
        "c1cocc1",       # furan
        "c1c[nH]cc1",    # pyrrole
        "c1cscc1",       # thiophene
        "c1cnoc1",       # isoxazole
        "c1cnnc1",       # pyrazole
        "c1cncc1"        # imidazole
    ]

    linkers = [
        "C",             # methane
        "CC",            # ethane
        "C=O",           # carbonyl
        "C1CC1",         # cyclopropane
        "C1CCC1",        # cyclobutane
        "O",             # oxygen
        "S",             # sulfur
        "N",             # nitrogen
        "NH",            # secondary amine
        "C=C",           # alkene
        "C#C",           # alkyne
        "C1COC1"         # oxirane
    ]

    # User interface
    st.sidebar.header("Generation Parameters")
    num_molecules = st.sidebar.slider(
        "Number of molecules to generate",
        min_value=1,
        max_value=50,
        value=10,
        help="Select how many drug-like molecules to generate"
    )

    generate_button = st.sidebar.button(
        "🔬 Generate Molecules",
        type="primary",
        use_container_width=True
    )

    if generate_button:
        with st.spinner("Generating molecules..."):
            # Generate molecules
            molecules_data = generate_molecules(fragments, linkers, num_molecules)

            if molecules_data:
                # Display results
                display_results(molecules_data)
            else:
                st.warning("No valid drug-like molecules were generated. Try adjusting parameters.")

    # Display instructions if no molecules generated yet
    if not generate_button:
        st.info("👈 Use the sidebar to configure and generate drug-like molecules!")

def generate_molecules(fragments, linkers, num_molecules):
    """
    Generate drug-like molecules by combining fragments and linkers

    Args:
        fragments: List of SMILES strings for core fragments
        linkers: List of SMILES strings for linkers
        num_molecules: Number of molecules to generate

    Returns:
        List of dictionaries containing molecule data
    """
    molecules_data = []

    for i in range(num_molecules):
        # Randomly select fragments and linkers
        frag1 = random.choice(fragments)
        frag2 = random.choice(fragments)
        linker = random.choice(linkers)

        # Try different combination patterns
        combination_patterns = [
            f"{frag1}{linker}{frag2}",
            f"{frag2}{linker}{frag1}",
            f"{frag1}{linker}",
            f"{frag2}{linker}",
            f"{linker}{frag1}{frag2}",
            f"{linker}{frag2}{frag1}"
        ]

        valid_molecule = None

        for pattern in combination_patterns:
            try:
                # Create molecule from SMILES
                mol = Chem.MolFromSmiles(pattern)

                if mol is not None:
                    # Calculate properties
                    mol_wt = Descriptors.MolWt(mol)
                    logp = Crippen.MolLogP(mol)
                    tpsa = rdMolDescriptors.CalcTPSA(mol)
                    h_acceptors = rdMolDescriptors.CalcNumHBA(mol)
                    h_donors = rdMolDescriptors.CalcNumHBD(mol)

                    # Check if molecule meets drug-like criteria
                    if 150 <= mol_wt <= 500:
                        valid_molecule = {
                            'smiles': pattern,
                            'mol_wt': round(mol_wt, 2),
                            'logp': round(logp, 2),
                            'tpsa': round(tpsa, 2),
                            'h_acceptors': h_acceptors,
                            'h_donors': h_donors,
                            'mol': mol
                        }
                        break

            except Exception as e:
                # Skip invalid combinations
                continue

        if valid_molecule:
            molecules_data.append(valid_molecule)

    return molecules_data

def display_results(molecules_data):
    """
    Display the generated molecules and their properties

    Args:
        molecules_data: List of dictionaries containing molecule data
    """
    st.success(f"Generated {len(molecules_data)} valid drug-like molecules!")

    # Create DataFrame for properties
    df_data = []
    images = []

    for i, mol_data in enumerate(molecules_data):
        df_data.append({
            'Molecule ID': f'MOL_{i+1}',
            'SMILES': mol_data['smiles'],
            'MW (Da)': mol_data['mol_wt'],
            'LogP': mol_data['logp'],
            'TPSA': mol_data['tpsa'],
            'H-Acceptors': mol_data['h_acceptors'],
            'H-Donors': mol_data['h_donors']
        })

        # Generate 2D image
        img = Draw.MolToImage(mol_data['mol'], size=(300, 200))
        images.append(img)

    # Create and display DataFrame
    df = pd.DataFrame(df_data)
    st.subheader("📊 Generated Molecules Properties")
    st.dataframe(df, use_container_width=True)

    # Display molecule images in a grid
    st.subheader("🧪 Molecule Structures")

    # Calculate number of columns for grid layout
    num_cols = min(4, len(images))
    cols = st.columns(num_cols)

    for i, img in enumerate(images):
        col_idx = i % num_cols
        with cols[col_idx]:
            st.image(img, caption=f"MOL_{i+1}", use_column_width=True)

    # Add download button for CSV
    csv = df.to_csv(index=False)
    st.download_button(
        label="📥 Download Results as CSV",
        data=csv,
        file_name="generated_molecules.csv",
        mime="text/csv",
        use_container_width=True
    )

if __name__ == "__main__":
    main()
