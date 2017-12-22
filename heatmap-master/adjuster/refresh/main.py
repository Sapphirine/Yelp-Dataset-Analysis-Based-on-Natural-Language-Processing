import json
import sys  
#sys.setdefaultencoding('utf8')


def refresh():
    content = json.load(open(('chinese cuisine.json'), encoding="utf-8"))
    refresh_content = []
    refreshed_content = {}
    locations = []
    for i in range(len(content)):
        lat = content[i].pop(u'latitude',None)
        lng = content[i].pop(u'longitude',None)
        locations.append({u'lng':lng,u'lat':lat})
    refresh_content = content[0]
    print (refresh_content)
    refresh_content[u'locations'] = locations
    #print (refresh_content)
    refreshed_content = {"events":[refresh_content]}
    print (refreshed_content)
    json.dump(refreshed_content, open('updated.json', 'w'))
    #refresh_content.append
    '''
    for item in content:
        new_item = dict(item)
        lat = new_item[u'latitude']
        lng = new_item[u'longitude']
        new_item.pop(u'latitude', None)
        new_item.pop(u'longitude', None)
        new_item[u'locations'] = [{u'lng': lng}, {u'lat': lat}]
        refresh_content.append(new_item)
        refreshed_content = {"events":refresh_content}
    json.dump(refreshed_content, open('updated.json', 'w'))'''
    return


if __name__ == '__main__':
    refresh()
