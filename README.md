# Domain Adaptability

Measure the similarity between two corpora (text datasets). The measures work best when each corpus is at least 10k words. This package support 74 languages.

    from domain_adaptability import Adaptability
    cs = Adaptability(language = "eng")

    result = cs.calculate(corpus1, corpus2)

The package contains all preprocessing and training. Only the language needs to be specified. A list of supported languages is provided below.

# Authors

Dainis Boumber @ ReDAS Laboratory

# Attributions 

Domain Adaptability module is derived from the [Corpus Similarity repository](https://github.com/jonathandunn/corpus_similarity.git), 
a project by Jonathan Dunn, Haipeng Li, Damian Sastre.

Corpus Similarity builds on top of the corpus similarity measure is a simple character n-gram comparison, with the best performance coming with using Spearman's Rho as a measure of correlation. The original idea for this kind of corpus comparison comes from Adam Kilgarriff (https://kilgarriff.co.uk/Publications/2001-K-CompCorpIJCL.pdf). 

Recent work in *Lingua* has evaluated the measures used in this package extensively in a multi-lingual setting (https://arxiv.org/abs/2206.04332). These measures have since been used to model the relationship between registers in a multi-lingual setting (https://arxiv.org/abs/2209.09813) and to validate geo-referenced corpus collections (https://arxiv.org/abs/2104.01294). Other work has modelled the relationship between corpus similarity (upstream) and embedding similarity (downstream) (https://arxiv.org/abs/2206.04330). These papers provide further details for the theory and evaluation behind this package.

# Input

The **Adaptability.calculate** method requires two input corpora. These can be:
    
    - a list of strings
    - a filename of one of the following formats:
        - .txt
        - .gz
        - .json
        - .jsonl
        - .csv
    - a dataset of the huggingface/datasets library

# Output

The output is a scalar measure of how adaptable the two corpora are. The values fall between 0 (very different) and 1 (very adaptable). The values are consistent within languages, but not across languages. For example, Swedish has higher relative adaptability than Estonian.

# Installation

    pip install domain_adaptability

    pip install git+https://github.com/dainis-boumber/domain_adaptability.git
    
# Languages

amh, Amharic

ara, Arabic

aze, Azerbaijani

ben, Bengali

bul, Bulgarian

cat, Catalan

ceb, Cebuano

ces, Czech

cha, Chamorro

dan, Danish

deu, German

ell, Greek

eng, English

est, Estonian

eus, Basque

fas, Farsi

fij, Fijian

fin, Finnish

fra, French

gle, Gaelic

glg, Galician

guj, Gujarati

hat, Hatian

haw, Hawaiian

heb, Hebrew

hin, Hindi

hmo, Hiri Motu

hun, Hungarian

ilo, Ilocano

ind, Indonesian

isl, Icelandic

ita, Italian

jav, Javanese

jpn, Japanese

kan, Kannada

kat, Georgian

kor, Korean

lav, Latvian

lit, Lithuanian

mal, Malayalam

mar, Marathi

mkd, Macedonian

mlg, Malagasy

mon, Mongolian

mri, te reo Māori

msa, Malay

nld, Dutch

nor, Norwegian

pan, Punjabi

pol, Polish

por, Portuguese

ron, Romanian

rus, Russian

sin, Sinhala

slk, Slovak

slv, Slovenian

smo, Samoan

som, Somali

spa, Spanish

sqi, Albanian

swe, Swedish

tah, Tahitian

tam, Tamil

tel, Telugu

tgl, Tagalog

tha, Thai

ton, Tongan

tur, Turkish

tvl, Tuvaluan

ukr, Ukrainian

urd, Urdu

uzb, Uzbek

vie, Vietnamese

zho, Chinese
