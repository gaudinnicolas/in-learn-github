import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

    rss_elt = xml_tree.Element('rss', {
        'version': '2.0',
        'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
        'xmlns:content': 'http://purl.org/rss/1.0/modlules/content'
    })

link_prefix = yaml_data['link']

channel = xml_tree.SubElement(rss_elt, 'channel')
xml_tree.SubElement(channel, 'title').text = yaml_data['title']
xml_tree.SubElement(channel, 'format').text = yaml_data['format']
xml_tree.SubElement(channel, 'subtitle').text = yaml_data['subtitle']
xml_tree.SubElement(channel, 'itunes:author').text = yaml_data['author']
xml_tree.SubElement(channel, 'itunes:image', {
    'href': link_prefix + yaml_data['image']
})
xml_tree.SubElement(channel, 'description').text = yaml_data['description']
xml_tree.SubElement(channel, 'language').text = yaml_data['language']
xml_tree.SubElement(channel, 'link').text = link_prefix

for item in yaml_data['item']:
    item_element = xml_tree.SubElement(channel, 'item')
    xml_tree.SubElement(item_element, 'title').text = item['title']
    xml_tree.SubElement(
        item_element, 'itunes:author').text = yaml_data['title']

    enclosure = xml_tree.SubElement(item_element, 'enclosure', {
        'url': link_prefix + item['file'],
        'type': 'audio/mpeg',
        'length': item['length']
    })

output_tree = xml_tree.ElementTree(rss_elt)
output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)
