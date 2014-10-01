import nltk
import mods_article

article = mods_article.get_mods_article_text('sample_data.mods.xml')
tokens = nltk.word_tokenize(article)
tagged = nltk.pos_tag(tokens)
entities = nltk.chunk.ne_chunk(tagged)

for entity in entities:
    if isinstance(entity, nltk.tree.Tree):
        label = entity.label()
        if label == 'PERSON':
            print entity
