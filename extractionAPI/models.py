from django.db import models

# Create your models here.
class Story(models.Model):
	story_id = models.AutoField(primary_key=True)
	headline = models.CharField(max_length=30)
	author_firstName = models.CharField(max_length=30)
	author_lastName = models.CharField(max_length=30)
	timeCreated = models.DateTimeField(auto_now_add=True, editable=False)
	numberSlides = models.IntegerField()
	coverPhoto = models.CharField(max_length=500)						#	This is just a placeholder field-type for now, look up the file upload field
	#storyTags = models.ManyToManyField(Tags, db_table="Story_Tags")	# 	The relationship table between a story and tags associated with it
	#memberSlides = models.ManyToManyField(Slide, through="Slide_In_Story")

class Tags(models.Model):
	tag_name = models.CharField(max_length=15, primary_key=True)	#	The tag is a unique element, attributed to a story (Many-To-Many)

class Story_Tags(models.Model):
	story_id = models.ForeignKey(Story)
	tag_name = models.ForeignKey(Tags)

class Slide_Types(models.Model):
	type_name = models.CharField(max_length=15, primary_key=True)

class Slide(models.Model):
	slide_id = models.AutoField(primary_key=True)
	typeOfSlide = models.ForeignKey(Slide_Types)				#	Each slide must be designated a type existing in the Slide_Types table
	story_id = models.ForeignKey(Story)

class Slide_In_Story(models.Model):
	story_id = models.ForeignKey(Story)
	slide_id = models.ForeignKey(Slide)
	slideNumber = models.IntegerField()							#	The slide ordering number as it exists in a story

class Image(models.Model):
	image_id = models.AutoField(primary_key=True)
	url = models.CharField(max_length=100)						#	Future: Maybe there's a URL field
	width = models.IntegerField()
	height = models.IntegerField()
	timeTaken = models.DateTimeField(auto_now=False, null=True)			#	They input when the photo was taken? this is an optional value
	photographer_firstName = models.CharField(max_length=30)
	photographer_lastName = models.CharField(max_length=30)


class Image_In_Slide(models.Model):
	slide_id = models.ForeignKey(Slide, unique=True)			#	This enforces that each slide can only be associated with one image (but images can be related to multiple slides)
	image_id = models.ForeignKey(Image)

