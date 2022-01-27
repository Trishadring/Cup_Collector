from django.db import models
from django.urls import reverse
# Create your models here.
CONTENTS = (
    ('T', 'Tea'),
    ('C', 'Coffee'),
    ('M', 'Milk'),
		('W', 'Water'),
		('A', 'Alcohol'),
)


class Cup(models.Model):
  color = models.CharField(max_length=100)
  brand = models.CharField(max_length=100)
  type = models.TextField(max_length=250)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.color

  # Add this method
  def get_absolute_url(self):
    return reverse('detail', kwargs={'cup_id': self.id})


class Using(models.Model):
	date = models.DateField('used date')
	content = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=CONTENTS,
    # set the default value for meal to be 'B'
    default=CONTENTS[0][0]
  )

	cup = models.ForeignKey(Cup, on_delete=models.CASCADE)

	def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
		return f"{self.get_content_display()} on {self.date}"