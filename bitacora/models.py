# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BitacoraSoc(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    cliente = models.ForeignKey('Clientes', models.DO_NOTHING)
    proyecto = models.ForeignKey('Proyectos', models.DO_NOTHING)
    tecnico = models.ForeignKey('Tecnicos', models.DO_NOTHING)
    modalidad = models.ForeignKey('Modalidades', models.DO_NOTHING)
    evento = models.ForeignKey('Eventos', models.DO_NOTHING)
    reportando = models.CharField(max_length=15)
    duracion = models.CharField(max_length=15)
    asistencia_tecnica = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=150)
    resultados = models.CharField(max_length=150)
    enlace = models.CharField(max_length=150)
    creado_en = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bitacora_soc'


class Clientes(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=120)
    activo = models.BooleanField()
    creado_en = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'clientes'


class Eventos(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=120)
    activo = models.BooleanField()
    creado_en = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'eventos'


class Modalidades(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=80)
    activo = models.BooleanField()
    creado_en = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'modalidades'


class Proyectos(models.Model):
    id = models.BigAutoField(primary_key=True)
    cliente = models.ForeignKey(Clientes, models.DO_NOTHING)
    nombre = models.CharField(max_length=120)
    activo = models.BooleanField()
    creado_en = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'proyectos'
        unique_together = (('cliente', 'nombre'), ('id', 'cliente'),)


class Tecnicos(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=120)
    activo = models.BooleanField()
    creado_en = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tecnicos'
