# Generated by Django 3.2.8 on 2021-10-28 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_web', '0002_alter_paciente_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paciente',
            options={'verbose_name': 'Paciente', 'verbose_name_plural': 'Pacientes'},
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null='true', verbose_name='Fecha Nacimiento (dd/mm/aaaa)'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='foto',
            field=models.ImageField(blank='True', default='profile_default.jpg', null=True, upload_to='fotos', verbose_name='Fotografia (Opcional)'),
        ),
    ]