from django.db import models

# Create your models here.
class Persona(models.Model):
	name  =  models.CharField(max_length=100)
	email =  models.EmailField(max_length=70,blank=True)
	phone =   models.CharField(max_length=50)
	owner = models.ForeignKey('auth.User', related_name='usuario')
	def __str__(self):
		return self.name

class Deuda(models.Model):
	name = models.CharField(max_length=100)
	Persona = models.ForeignKey(Persona)
	create =  models.DateTimeField(auto_now_add=True)
	price  = models.DecimalField(max_digits=10, decimal_places=2)
	paid = models.BooleanField("Pagado", default=False)
	paiddate = models.DateTimeField()
	status = (
		('DEUDA','DEUDA'),
		('PRESTAMO','PRESTAMO')
	)
	state = models.CharField(max_length=8,choices=status,default='DEUDA')
	
	owner = models.ForeignKey('auth.User', related_name='usuario_deuda')

	def __str__(self):
		return self.name + ' - ' + self.price


