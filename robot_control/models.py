from django.db import models
from django.forms import ModelForm

# Create your models here.
class Category(models.Model):
	RFID_id = models.CharField(max_length=24, blank=True, null=True, help_text = "Put here the 12 Hexadecimal ID that appears when you read the RFID")
	description = models.TextField(blank=True, help_text = "This is the description of the category")
	name = models.CharField(max_length=255, help_text = "This is the name of the category. Try to put very different names to each category")

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Categories"

class Question(models.Model):
	category = models.ForeignKey(Category, help_text = "This is the category that will contain this question") # REQUIRED
	title = models.CharField(max_length=100, help_text = "This is the main title for the question, i.e. How old are you...")
	explanation = models.TextField(blank=True, null=True, help_text = "This is a explanation if you need to clarify the question")
	difficulty = models.PositiveIntegerField(help_text = "This is number between 1 to 10 that represents the difficulty of the question. 10 is the biggest difficulty") # REQUIRED
	# TODO: Insert an image per Question
	image = models.ImageField(upload_to = 'question_images', help_text = "This is the image that will be appear near your question")

	def __unicode__(self):
		return self.title

class Response(models.Model):
	question = models.ForeignKey(Question, help_text = "This is the question that will contain this response") # REQUIRED
	body = models.CharField(max_length=255, help_text = "This is the response itself") # REQUIRED
	true = models.BooleanField(help_text = "Mark this if the response is the valid one. Only one valid response for question is allowed") # REQUIRED

	def __unicode__(self):
		return self.question

class CategoryForm(ModelForm):
	class Meta:
		model = Category

class QuestionForm(ModelForm):
	class Meta:
		model = Question

class ResponseForm(ModelForm):
	class Meta:
		model = Response
