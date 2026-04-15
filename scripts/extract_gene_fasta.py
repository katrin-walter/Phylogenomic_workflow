import os
from Bio import SeqIO
from collections import defaultdict

# Folder with the .gb-files
input_folder = "genbank_files"  # <--- here insert the folder name which contains the .gb files
output_folder = "gene_fastas"   # <--- give it an output name
os.makedirs(output_folder, exist_ok=True)

# Dictionary for saving gene sequences
genes = defaultdict(list)

# checks all .gb-files in the input_folder
for filename in os.listdir(input_folder):
    if filename.endswith(".gb") or filename.endswith(".gbk"):
        filepath = os.path.join(input_folder, filename)
        for record in SeqIO.parse(filepath, "genbank"):
            base_name = os.path.splitext(filename)[0]
            organism = record.annotations.get("organism", "Unknown_organism").replace(" ", "_")
            species_id = f"{organism}_{base_name}"

            for feature in record.features:
                if feature.type == "CDS":
                    gene_name = feature.qualifiers.get("gene", [None])[0]
                    if gene_name and not gene_name.lower().startswith(("orf", "trna", "rrna")):
                        try:
                            sequence = feature.extract(record.seq)
                            genes[gene_name].append(f">{species_id}\n{sequence}")
                        except:
                            print(f"Fehler beim Extrahieren von {gene_name} in {filename}")

# creates a FASTA file for each gene
for gene, seqs in genes.items():
    output_path = os.path.join(output_folder, f"{gene}.fasta")
    with open(output_path, "w") as f:
        f.write("\n".join(seqs) + "\n")
