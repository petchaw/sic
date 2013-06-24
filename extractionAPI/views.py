from django.http import HttpResponse
import MySQLdb, json, collections

def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def getStory(request, story_id):
    # db connection
    db = MySQLdb.connect(host="localhost", user="nytimes", passwd="nytimes", db="StoryDB")
    cursor = db.cursor()
	
    getStory = "SELECT xyz FROM xyz WHERE xyz = '%s'" % story_id
    cursor.execute(getStory)
    cid = cursor.fetchone()
    db.close()

    return HttpResponse("There you go")


def getStories(request, last):
	# db connection
    db = MySQLdb.connect(host="localhost", user="nytimes", passwd="nytimes", db="StoryDB")
    cursor = db.cursor()

    getStory = "SELECT * FROM extractionAPI_story LIMIT %s" % (last)

    cursor.execute(getStory)

    rows = cursor.fetchall()
    rowarray_list = []
    for row in rows:
        t = (row[0], row[1], row[2] + " " + row[3], "1427364927", row[5])
        rowarray_list.append(t)

    j = json.dumps(rowarray_list)

    db.close()

    return HttpResponse(j)


# ex: /story?id=1     			OR     /story/1
# ex: /stories?getlast=10     	OR     /stories/10
# ex: /