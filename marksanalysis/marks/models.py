from django.db import models


class Marksheet(models.Model):
    Roll_No = models.IntegerField()
    Div = models.CharField(max_length=50)
    Mentor= models.CharField(max_length=50)
    Branch= models.CharField(max_length=50)
    Enrollment= models.IntegerField()
    Name= models.CharField(max_length=50)
    DM_T1= models.FloatField()
    DM_T2= models.FloatField()
    DM_T3= models.FloatField()
    DM_T4= models.FloatField()
    FSD_2_T1= models.FloatField()
    FSD_2_T2= models.FloatField()
    FSD_2_T3= models.FloatField()
    FSD_2_T4= models.FloatField()
    TOC_T1=models.FloatField()
    TOC_T2= models.FloatField()
    TOC_T3=models.FloatField()
    TOC_T4= models.FloatField()
    FCSP_2_T1= models.FloatField()
    FCSP_2_T2= models.FloatField()
    FCSP_2_T3= models.FloatField()
    FCSP_2_T4= models.FloatField()
    COA_T1= models.FloatField()
    COA_T2= models.FloatField()
    COA_T3= models.FloatField()
    COA_T4= models.FloatField()

    def __str__(self):
        return self.Name