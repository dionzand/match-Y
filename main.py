from models import Pedigree, MarkerSet, Simulation
from simulation import run_simulation

marker_set = MarkerSet()
marker_set.read_marker_set_from_file(r"manuscript/mutationrates/1.csv")

pedigree = Pedigree()
pedigree.read_pedigree_from_file("manuscript/basepedigreeA.tgf")

pedigree.read_known_haplotype_from_file("suspect", "manuscript/haplotypes/suspect.csv", marker_set)
# pedigree.read_known_haplotype_from_file("known1", "manuscript/haplotypes/known_plus1.csv", marker_set)

suspect = "suspect"

pedigree.reroot_pedigree(suspect)

simulation = run_simulation(pedigree, marker_set, suspect, number_of_iterations=100000)