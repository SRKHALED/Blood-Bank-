from django.db import models
import datetime
BT = (('','Blood Group'),('A+','A+'),('B+','B+'),('O+','O+'),('AB+','AB+'),
	 ('A-','A-'),('B-','B-'),('O-','O-'),('AB-','AB-'))
GD = (('','Choos Gender'),('Male','Male'),('Female','Female'),('Others','Others'))
class Donor(models.Model):
	name  = models.CharField(max_length = 50)
	email = models.EmailField()
	contact = models.CharField(max_length = 15)
	division = models.CharField(max_length = 15)
	city = models.CharField(max_length = 15)
	address = models.CharField(max_length = 50)
	blood = models.CharField(max_length = 20,choices = BT,default = 'Blood Group')
	date_of_birth = models.DateField()
	gender = models.CharField(max_length = 20,choices = GD,default = 'Choos Gender')
	height = models.CharField(max_length = 4,default = '')
	weight = models.CharField(max_length = 5)
	password = models.CharField(max_length = 20)

	def save(self, force_insert = False, force_update = False):
		self.city = self.city.upper()
		self.division = self.division.upper()
		return super(Donor,self).save(force_insert,force_update)