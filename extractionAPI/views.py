from django.http import HttpResponse
import MySQLdb, json, collections

def index(request):
    return HttpResponse("You're at the index.")


def getStoriesByTag(request, tag, cnt):
    # db connection
    db = MySQLdb.connect(host="localhost", user="nytimes", passwd="nytimes", db="StoryDB")
    cursor = db.cursor()

    getStories = "SELECT extractionAPI_story.story_id, extractionAPI_story.headline, extractionAPI_story.author_firstName, extractionAPI_story.author_lastName, unix_timestamp(extractionAPI_story.timecreated), extractionAPI_story.coverphoto FROM extractionAPI_story, extractionAPI_story_tags WHERE extractionAPI_story_tags.tag_name_id = \"%s\" AND extractionAPI_story.story_id = extractionAPI_story_tags.story_id  LIMIT %s" % (tag, cnt)
    cursor.execute(getStories)

    rows = cursor.fetchall()
    objects_list = []

    for row in rows:
        d = collections.OrderedDict()
        d['story_id'] = row[0]
        d['headline'] = row[1]
        d['author'] = row[2] + " " + row[3]
        d['timecreated'] = row[4]
        d['coverphoto'] = row[5]
        
        objects_list.append(d)

    j = json.dumps(objects_list)

    db.close()
    return HttpResponse(j, mimetype='application/json')


def getStory(request, story_id):
    # db connection
    db = MySQLdb.connect(host="localhost", user="nytimes", passwd="nytimes", db="StoryDB")
    cursor = db.cursor()
	
    getStory = "SELECT headline, author_firstName, author_lastName, unix_timestamp(timecreated), coverphoto FROM extractionAPI_story WHERE story_id = %s" % story_id
    cursor.execute(getStory)

    row = cursor.fetchone()
    story_obj = []

    s = collections.OrderedDict()
    s['author'] = row[1] + " " + row[2]
    s['timecreated'] = row[3]
    s['headline'] = row[0]
    s['coverphoto'] = row[4]
    s['tags'] = []
    s['slide'] = []

    getTags = "SELECT tag_type_id FROM Tags_In_Story WHERE story_id = %s" % story_id
    cursor.execute(getTags)

    stags = cursor.fetchall()
    t = []

    for tag in stags:
        t.append(tag[0])

    s['tags'].append(t)

    getSlides = "SELECT slide_id, typeofslide_id, summary FROM extractionAPI_slide WHERE story_id = %s" % story_id
    cursor.execute(getSlides)

    rows = cursor.fetchall()

    for row in rows:
        s1 = collections.OrderedDict()
        s1['type'] = row[1]
        s1['summary'] = row[2]
        s['slide'].append(s1)
        s1['images'] = []

        #getImages = "SELECT extractionAPI_image.image_id, extractionAPI_image.image, extractionAPI_image.width, extractionAPI_image.height, unix_timestamp(extractionAPI_image.timetaken), extractionAPI_image.photo_credit, extractionAPI_image.caption FROM extractionAPI_image, extractionAPI_image_in_slide WHERE extractionAPI_image_in_slide.slide_id = %s AND extractionAPI_image_in_slide.image_id = extractionAPI_image.image_id" % row[0]
        getImages = "SELECT image, width, height, unix_timestamp(extractionAPI_image.datetaken), photo_credit, caption FROM extractionAPI_image WHERE slide_id = %s" % row[0]
        cursor.execute(getImages)

        imgrows = cursor.fetchall()

        for imgrow in imgrows:
            i = collections.OrderedDict()
            i['url'] = imgrow[0]
            i['caption'] = imgrow[5]
            i['width'] = imgrow[1]
            i['height'] = imgrow[2]
            i['timetaken'] = imgrow[3]
            i['credit'] = imgrow[4]
            s1['images'].append(i)

    story_obj.append(s)
    sty = json.dumps(story_obj)

    db.close()
    return HttpResponse(sty, mimetype='application/json')


def getStories(request, last):
	# db connection
    db = MySQLdb.connect(host="localhost", user="nytimes", passwd="nytimes", db="StoryDB")
    cursor = db.cursor()

    getStories = "SELECT story_id, headline, author_firstName, author_lastName, unix_timestamp(timecreated), coverphoto FROM extractionAPI_story LIMIT %s" % (last)
    cursor.execute(getStories)

    rows = cursor.fetchall()
    objects_list = []

    for row in rows:
        d = collections.OrderedDict()
        d['story_id'] = row[0]
        d['headline'] = row[1]
        d['author'] = row[2] + " " + row[3]
        d['timecreated'] = row[4]
        d['coverphoto'] = row[5]
        
        objects_list.append(d)

    j = json.dumps(objects_list)

    db.close()
    return HttpResponse(j, mimetype='application/json')