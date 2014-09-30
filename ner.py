import nltk
import xml.etree.ElementTree as etree

def get_mods_article_text(xml_article):
        tree = etree.parse(xml_article)
        find_article = tree.findall('{http://www.loc.gov/mods/v3}note')
        article_content = find_article[0].text
        return article_content

article = get_mods_article_text('Ar00123.mods.xml')
tokens = nltk.word_tokenize(article)
tagged = nltk.pos_tag(tokens)
entities = nltk.chunk.ne_chunk(tagged)

print entities

