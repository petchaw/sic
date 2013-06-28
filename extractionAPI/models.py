from django.db import models

# Create your models here.

class Tag_Type(models.Model):
	tagname = models.CharField(max_length=15, primary_key=True, verbose_name = "Tag")	#	The tag is a unique element, attributed to a story (Many-To-Many)

	def __unicode__(self):
		return self.tagname

class Story(models.Model):
	story_id = models.AutoField(primary_key=True)
	headline = models.CharField(max_length=100, verbose_name="Headline")
	author_firstname = models.CharField(max_length=30, verbose_name="First Name")
	author_lastname = models.CharField(max_length=30, verbose_name="Last Name")
	timecreated = models.DateTimeField(auto_now_add=True, editable=False)
	coverphoto = models.ImageField(verbose_name="Cover Photo", upload_to="CoverPhotos")				#	This is just a placeholder field-type for now, look up the file upload field
	storytags = models.ManyToManyField(Tag_Type, db_table="Tags_In_Story", verbose_name="Tags")		# 	The relationship table between a story and tags associated with it

	def __unicode__(self):
		return self.headline


class Slide_Types(models.Model):
	type_name = models.CharField(max_length=30, primary_key=True, verbose_name="Type of Slide")

	def __unicode__(self):
		return self.type_name


class Slide(models.Model):
	slide_id = models.AutoField(primary_key=True)
	typeofslide = models.ForeignKey(Slide_Types, verbose_name="Type of Slide")				#	Each slide must be designated a type existing in the Slide_Types table
	story = models.ForeignKey(Story, verbose_name="Belonging to Story")
	summary = models.CharField(max_length=500, verbose_name="Description", null=True)
	#memberImages = models.ManyToManyField(Image, db_table="Images_In_Slide", verbose_name="Member Images")


class Image(models.Model):
	image_id = models.AutoField(primary_key=True)
	slide = models.ForeignKey(Slide, verbose_name="Belonging to Slide")
	width = models.PositiveIntegerField(verbose_name="Width (pixels)")
	height = models.PositiveIntegerField(verbose_name="Height (pixels)")
	image = models.ImageField(upload_to="Images", height_field="height", width_field="width", verbose_name="Photo")
	photo_credit = models.CharField(max_length=50, verbose_name="Photo Credit")
	caption = models.CharField(max_length=150, verbose_name="Image Caption")
	datetaken = models.DateField(auto_now=False, null=True, verbose_name="Date Photo Taken")			#	They input when the photo was taken? this is an optional value