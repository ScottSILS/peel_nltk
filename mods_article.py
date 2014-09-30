import xml.etree.ElementTree as etree

def get_mods_article_text(xml_article):
        tree = etree.parse(xml_article)
        find_article = tree.findall('{http://www.loc.gov/mods/v3}note')
        article_content = find_article[0].text
        return article_content


