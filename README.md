### Phylogenomic_workflow
A complete and easy phylogenomic pipeline using translatorX and iqtree2 with a partitioned dataset for green macrophytes


1. optional: install Entrez Direct, if you want to download files directly from NCBI.
```bash
sh -c "$(curl -fsSL https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh)"
```
Then add it to your PATH (the installer tells you the exact line to put in your ~/.bashrc or ~/.zshrc).
In case of working with chloroplast genomes of the genus Caulerpa, you want all complete Caulerpa chloroplast genomes from NCBI, each one as its own separate .gb file.

Create a list so you can download each genome one by one and name the files properly.
```bash
esearch -db nuccore -query "Caulerpa[Organism] AND chloroplast[filter] AND complete genome[Title]" | efetch -format acc > accessions.txt
```
After this, open the file to check, you should see one accession per line:
```bash
cat accessions.txt
```
Now download each genome as its own file
```bash
while read acc; do
  efetch -db nuccore -id "$acc" -format gb > "${acc}.gb"
done < accessions.txt
```
