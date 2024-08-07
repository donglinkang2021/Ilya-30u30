#!/bin/bash
# pip install arxiv-downloader
mkdir downloads
cd downloads
mkdir papers
cd papers

arxiv-downloader 1409.2329
arxiv-downloader 1506.03134
arxiv-downloader 1511.06391
arxiv-downloader 1811.06965
arxiv-downloader 1512.03385
arxiv-downloader 1511.07122
arxiv-downloader 1704.01212
arxiv-downloader 1706.03762
arxiv-downloader 1409.0473
arxiv-downloader 1603.05027
arxiv-downloader 1706.01427
arxiv-downloader 1611.02731
arxiv-downloader 1806.01822
arxiv-downloader 1405.6903
arxiv-downloader 1410.5401
arxiv-downloader 1512.02595
arxiv-downloader 2001.08361

wget -O "Keeping_Neural_Networks_Simple.pdf" "https://www.cs.toronto.edu/~hinton/absps/colt93.pdf"
wget -O "ImageNet_Classification_with_Deep_CNNs.pdf" "https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf"

cd ..
mkdir books
cd books

wget -O "A_Tutorial_Introduction_to_the_Minimum_Description_Length_Principle.pdf" "https://arxiv.org/pdf/math/0406077.pdf"
wget -O "Machine_Super_Intelligence_Dissertation.pdf" "https://www.vetta.org/documents/Machine_Super_Intelligence.pdf"
wget -O "Komogrov_Complexity.pdf" "https://www.lirmm.fr/~ashen/kolmbook-eng-scan.pdf"

echo "Done!"


