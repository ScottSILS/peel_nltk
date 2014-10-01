import nltk
import mods_article

def get_ne_persons(mods_xml_article):
    article_text = mods_article.get_mods_article_text(mods_xml_article)
    tokens = nltk.word_tokenize(article_text)
    tagged = nltk.pos_tag(tokens)
    entities = nltk.chunk.ne_chunk(tagged)

    for entity in entities:
        if isinstance(entity, nltk.tree.Tree):
            label = entity.label()
            if label == 'PERSON':
                for person in entity.leaves():
                    print person[0]

get_ne_persons('sample_data.mods.xml')
