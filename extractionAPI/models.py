from django.db import models

# Create your models here.
class Story(models.Model):
	story_id = models.AutoField(primary_key=True)
	headline = models.CharField(max_length=30, verbose_name="Article Headline")
	author_firstName = models.CharField(max_length=30, verbose_name="Author's First Name")
	author_lastName = models.CharField(max_length=30, verbose_name="Author's Last Name")
	timeCreated = models.DateTimeField(auto_now_add=True, editable=False)
	#numberSlides = models.IntegerField(verbose_name="Number of Slides")
	coverPhoto = models.ImageField(verbose_name="Cover Photo", upload_to="CoverPhotos")						#	This is just a placeholder field-type for now, look up the file upload field
	#storyTags = models.ManyToManyField(Tags, db_table="Story_Tags")	# 	The relationship table between a story and tags associated with it
	#memberSlides = models.ManyToManyField(Slide, through="Slide_In_Story")

class Tags(models.Model):
	tag_name = models.CharField(max_length=15, primary_key=True)	#	The tag is a unique element, attributed to a story (Many-To-Many)

class Story_Tags(models.Model):
	story_id = models.ForeignKey(Story)
	tag_name = models.ForeignKey(Tags)

class Slide_Types(models.Model):
	type_name = models.CharField(max_length=15, primary_key=True, verbose_name="Type of Slide")

class Slide(models.Model):
	slide_id = models.AutoField(primary_key=True)
	typeOfSlide = models.ForeignKey(Slide_Types, verbose_name="Type of Slide")				#	Each slide must be designated a type existing in the Slide_Types table
	story_id = models.ForeignKey(Story, verbose_name="Belonging to Story")
	summary = models.CharField(max_length=250, verbose_name="Description", null=True)

class Slide_In_Story(models.Model):
	story_id = models.ForeignKey(Story)
	slide_id = models.ForeignKey(Slide)
	slideNumber = models.IntegerField()							#	The slide ordering number as it exists in a story

class Image(models.Model):
	image_id = models.AutoField(primary_key=True)
	image = models.ImageField(upload_to="Images", verbose_name="Photo")						#	Future: Maybe there's a URL field
	width = models.IntegerField(verbose_name="Width (pixels)")
	height = models.IntegerField(verbose_name="Height (pixels)")
	timeTaken = models.DateTimeField(auto_now=False, null=True, verbose_name="Time Photo Taken")			#	They input when the photo was taken? this is an optional value
	photo_credit = models.CharField(max_length=30, verbose_name="Photo Credit")
	caption = models.CharField(max_length=50, verbose_name="Image Caption")


class Image_In_Slide(models.Model):
	slide_id = models.ForeignKey(Slide, unique=True)			#	This enforces that each slide can only be associated with one image (but images can be related to multiple slides)
	image_id = models.ForeignKey(Image)

