### Phylogenomic_workflow
A complete and easy phylogenomic pipeline using translatorX and iqtree2 with a partitioned dataset for green macrophytes


1. optional: install Entrez Direct, if you want to download files directly from NCBI.
   head to docs -> Entrez_Direct.md and follow instructions

2. Extract every gene sequence of every taxa (.gb file) into one fasta file
   Example: gene name: accD
   all accD sequences from every taxa in one accD.fasta file ect..

3. Apply the script `python extract_gene_fasta.py ` 

4. Installing translatorX and mafft

   a) if you prefer, create a new environment before installing and activate it (e.g. phylogenomic)
   
   b) ``` wget http://translatorx.co.uk/http/translatorx_vLocal.pl ``` or
      ``` curl -O http://translatorx.co.uk/http/translatorx_vLocal.pl ```
      check with ``` perl translatorx_vLocal.pl ```
   
   c) ``` conda install -c bioconda mafft ```
      check with ``` mafft --version ```
   
5. If working with a large set of genome, connect to a HPC cluster and organize your files and folders
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


