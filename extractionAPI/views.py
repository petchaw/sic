from django.http import HttpResponse
import MySQLdb, json, collections

def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def getStory(request, story_id):
    # db connection
    #db = MySQLdb.connect(host="localhost", user="nytimes", passwd="nytimes", db="StoryDB")
    #cursor = db.cursor()
	
    #getStories = "SELECT xyz FROM xyz WHERE xyz = '%s'" % story_id
    #cursor.execute(getStories)

    #cid = cursor.fetchone()

    #db.close()
    return HttpResponse("You are getting story id %s here!" % story_id)
    #return HttpResponse(j, mimetype='application/json')


def getStories(request, last):
	# db connection
    db = MySQLdb.connect(host="localhost", user="nytimes", passwd="nytimes", db="StoryDB")
    cursor = db.cursor()

    getStory = "SELECT * FROM extractionAPI_story LIMIT %s" % (last)
    cursor.execute(getStory)

    rows = cursor.fetchall()
    objects_list = []

    for row in rows:
        d = collections.OrderedDict()
        d['story_id'] = row[0]
        d['headline'] = row[1]
        d['author_name'] = row[2] + " " + row[3]
        d['timecreated'] = "1674957692458"
        d['coverphoto'] = row[5]
        
        objects_list.append(d)

    j = json.dumps(objects_list)

    db.close()
    return HttpResponse(j, mimetype='application/json')