### Phylogenomic_workflow
A complete and easy phylogenomic pipeline using translatorX and iqtree2 with a partitioned dataset for green macrophytes


1. optional: install Entrez Direct, if you want to download files directly from NCBI.
   Go to docs -> Entrez_Direct.md and follow instructions

3. Extract every gene sequence of every taxa (.gb file) into one fasta file
   Example: gene name: accD
   all accD sequences from every taxa in one accD.fasta file ect..

4. Apply the script `python extract_gene_fasta.py ` 

5. Installing translatorX and mafft

   a) if you prefer, create a new environment before installing and activate it (e.g. phylogenomic)
   
   b) ``` wget http://translatorx.co.uk/http/translatorx_vLocal.pl ``` or
      ``` curl -O http://translatorx.co.uk/http/translatorx_vLocal.pl ```
      check with ``` perl translatorx_vLocal.pl ```
   
   c) ``` conda install -c bioconda mafft ```
      check with ``` mafft --version ```
   
6. If working with a large set of genome, connect to a HPC cluster and organize your files and folders
   a) mkdir Phylo_tree: in that folder load all of your fasta files
   b) within Phylo_tree also do mkdir translatorX_results
  
7. Go to "translatorX_results" and run following command: 
   ```bash
   parallel --jobs 5 translatorx -i {} -o {/.}_tx.fasta -p F -c 11 -g -b5=n ::: ../*fasta
   ```
   - here it will use 5 cores 
   - -i input {} is looking for fasta files in the directory "above".
   - -c 1 change code to 11 (bacterial and plant one)
   - -b5=n decide parameters for GBlocks

8. If Alignments are ready move all `nt.cleanali.fasta` in one folder and all `aa.cleanali.fasta` in one folder
```
├── Phylo_tree
│   ├── fasta files
│   └── translatorX_results/ #here you run the command for translatorX
├── nucleotide_tree
│   ├── all nt.cleanali.fasta
│   └── iqtree_nt_results #here you run iqtree for nucleotide sequences
├── amino_tree
│   ├── all aa.cleanali.fasta
│   └── iqtree_aa_results #here you run iqtree for amino acid sequences
```

9. Check the models in IQ TREE, here you can use a standard TEST model, finding the best fitting model for each alignment. Use 1000 bootstrap support and give it an output name of your choice (--prefix name)
10. head to `iqtree_nt_results` for the nucleotide tree and run
   ```bash
   nohup bash -c 'iqtree -p ../ --seqtype DNA -m TEST --prefix iqtree1 -B 1000 -T 5' &
   ```

11. head to `iqtree_nt_results` for the amino acid tree and run
```bash
   nohup bash -c 'iqtree -p ../ --seqtype AA -m TEST --prefix iqtree1 -B 1000 -T 5' &
   ```

12. Use the .treefile to visualize the tree. Download Figtree or go to https://itol.embl.de/



Source:
* Abascal F, Zardoya R, Telford MJ (2010)
  TranslatorX: multiple alignment of nucleotide sequences guided by amino acid translations
  Nucleic Acids Res. doi:10.1093/nar/gkq291
* https://mafft.cbrc.jp/alignment/software/
* https://iqtree.github.io/doc/Tutorial#input-data
  




