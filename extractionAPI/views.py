from django.http import HttpResponse
import MySQLdb, json, collections

def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def getStory(request, story_id):
    # db connection
    db = MySQLdb.connect(host="localhost", user="root", passwd="Danger0534", db="sic")
    cursor = db.cursor()
	
    getStory = "SELECT xyz FROM xyz WHERE xyz = '%s'" % story_id
    cursor.execute(getStory)
    cid = cursor.fetchone()
    db.close()

    return HttpResponse("There you go")


def getStories(request, last):
    getStory = """
				SELECT stories_story.story_id, stories_story.author, stories_story.time_created, 
				stories_story.headline, stories_photo.photo_url FROM stories_story, stories_photo 
				WHERE stories_story.cover_photo_id = stories_photo.photo_id LIMIT %i
				""" % (last)

    cursor.execute(getStory)

    rows = cursor.fetchall()
    rowarray_list = []
    for row in rows:
        t = (row.story_id, row.author, row.time_created, row.headline, row.photo_url)
        rowarray_list.append(t)

    j = json.dumps(rowarray_list)

    return HttpResponse(j)


# ex: /story?id=1     			OR     /story/1
# ex: /stories?getlast=10     	OR     /stories/10
# ex: /