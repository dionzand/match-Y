## Installation

1. Install python
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python main.py`

## Usage

### Set mutation rate
Load a csv file containing the mutation rates:
`marker_set.read_marker_set_from_file(r"manuscript/mutationrates/1.csv")`

Load a tgf file containing the pedigree:
`pedigree.read_pedigree_from_file("manuscript/basepedigreeA.tgf")`

Load at least one csv file containing the known haplotypes of individuals present in your pedigree file:
`pedigree.read_known_haplotype_from_file("suspect", "manuscript/haplotypes/suspect.csv", marker_set)
pedigree.read_known_haplotype_from_file("known1", "manuscript/haplotypes/known_plus1.csv", marker_set)`

Set the suspect by entering the same identifyer that is used in the pedigree and known haplotype files:
`suspect = "suspect"`

Set the simultation parameters (number of iterations):
`simulation = run_simulation(pedigree, marker_set, suspect, number_of_iterations=100000)`
