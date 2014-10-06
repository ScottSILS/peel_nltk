import nltk
import mods_article
import os, fnmatch

def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename

def get_ne_persons(mods_xml_article):
    article_text = mods_article.get_mods_article_text(mods_xml_article)
    if article_text:
        tokens = nltk.word_tokenize(article_text)
        tagged = nltk.pos_tag(tokens)
        entities = nltk.chunk.ne_chunk(tagged)

        for entity in entities:
            if isinstance(entity, nltk.tree.Tree):
                label = entity.label()
                if label == 'PERSON':
                    for person in entity.leaves():
                        print person[0]
    else:
        print "No article text found!"

for mods_xml_article in find_files('data', 'Ar*.mods.xml'):
    get_ne_persons(mods_xml_article)
    print mods_xml_article
