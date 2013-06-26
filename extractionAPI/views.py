from django.http import HttpResponse
import MySQLdb, json, collections

def index(request):
    return HttpResponse("You're at the index.")


def getStoriesByTag(request, tag, cnt):
    # db connection
    db = MySQLdb.connect(host="localhost", user="nytimes", passwd="nytimes", db="StoryDB")
    cursor = db.cursor()

    getStories = "SELECT extractionAPI_story.story_id, extractionAPI_story.headline, extractionAPI_story.author_firstName, extractionAPI_story.author_lastName, extractionAPI_story.timecreated, extractionAPI_story.coverphoto FROM extractionAPI_story, extractionAPI_story_tags WHERE extractionAPI_story_tags.tag_name_id = \"%s\" AND extractionAPI_story.story_id = extractionAPI_story_tags.story_id  LIMIT %s" % (tag, cnt)
    cursor.execute(getStories)

    rows = cursor.fetchall()
    objects_list = []

    for row in rows:
        d = collections.OrderedDict()
        d['story_id'] = row[0]
        d['headline'] = row[1]
        d['author'] = row[2] + " " + row[3]
        d['timecreated'] = "1674957692458"
        d['coverphoto'] = row[5]
        
        objects_list.append(d)

    j = json.dumps(objects_list)

    db.close()
    return HttpResponse(j, mimetype='application/json')


def getStory(request, story_id):
    # db connection
    db = MySQLdb.connect(host="localhost", user="nytimes", passwd="nytimes", db="StoryDB")
    cursor = db.cursor()
	
    getStory = "SELECT headline, author_firstName, author_lastName, timecreated, coverphoto FROM extractionAPI_story WHERE story_id = %s" % story_id
    cursor.execute(getStory)

    row = cursor.fetchone()
    story_obj = []

    s = collections.OrderedDict()
    s['author'] = row[1] + " " + row[2]
    s['timecreated'] = "1625339234453"
    s['headline'] = row[0]
    s['coverphoto'] = row[4]
    s['tags'] = []
    s['slide'] = []

    getTags = "SELECT tag_name_id FROM extractionAPI_story_tags WHERE story_id = %s" % story_id
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

        getImages = "SELECT extractionAPI_image.image_id, extractionAPI_image.image, extractionAPI_image.width, extractionAPI_image.height, extractionAPI_image.timetaken, extractionAPI_image.photo_credit, extractionAPI_image.caption FROM extractionAPI_image, extractionAPI_image_in_slide WHERE extractionAPI_image_in_slide.slide_id = %s AND extractionAPI_image_in_slide.image_id = extractionAPI_image.image_id" % row[0]
        cursor.execute(getImages)

        imgrows = cursor.fetchall()

        for imgrow in imgrows:
            i = collections.OrderedDict()
            i['url'] = imgrow[1]
            i['caption'] = imgrow[6]
            i['width'] = imgrow[2]
            i['height'] = imgrow[3]
            i['timetaken'] = "17364529455673"
            i['credit'] = imgrow[5]
            s1['images'].append(i)

    story_obj.append(s)
    sty = json.dumps(story_obj)

    db.close()
    return HttpResponse(sty, mimetype='application/json')


def getStories(request, last):
	# db connection
    db = MySQLdb.connect(host="localhost", user="nytimes", passwd="nytimes", db="StoryDB")
    cursor = db.cursor()

    getStories = "SELECT * FROM extractionAPI_story LIMIT %s" % (last)
    cursor.execute(getStories)

    rows = cursor.fetchall()
    objects_list = []

    for row in rows:
        d = collections.OrderedDict()
        d['story_id'] = row[0]
        d['headline'] = row[1]
        d['author'] = row[2] + " " + row[3]
        d['timecreated'] = "1674957692458"
        d['coverphoto'] = row[5]
        
        objects_list.append(d)

    j = json.dumps(objects_list)

    db.close()
    return HttpResponse(j, mimetype='application/json')