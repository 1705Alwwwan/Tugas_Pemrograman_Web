from django.db import models

class ProgramStudi (models.Model):
    kode_programstudi = models.CharField(max_length=3)
    nama_programstudi = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_programstudi
    

class Mahasiswa (models.Model):
    JENIS_KELAMIN_CHOICES = (
        ('Laki-laki', 'Laki-laki'),
        ('Perempuan', 'Perempuan'), 
        ('Lainnya', 'Lainnya'), 
    )

    nama = models.CharField(max_length=50)
    nim = models.CharField(max_length=10)
    jenis_kelamin = models.CharField(max_length=10, choices=JENIS_KELAMIN_CHOICES)
    alamat = models.TextField()
    programstudi =  models.ForeignKey(ProgramStudi, on_delete=models.CASCADE, null=True)
    telephone = models.CharField(max_length=12) 

    def __str__(self):
        return self.nama
