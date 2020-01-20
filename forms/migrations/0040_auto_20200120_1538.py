# Generated by Django 2.2.9 on 2020-01-20 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0039_auto_20200120_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='televisionperson',
            name='special_qn_1',
            field=models.CharField(blank=True, choices=[('Y', '(1) Yes'), ('N', '(2) No')], max_length=1, verbose_name='(19) Special question 1'),
        ),
        migrations.AlterField(
            model_name='televisionperson',
            name='special_qn_2',
            field=models.CharField(blank=True, choices=[('Y', '(1) Yes'), ('N', '(2) No')], max_length=1, verbose_name='(20) Special question 2'),
        ),
        migrations.AlterField(
            model_name='televisionperson',
            name='special_qn_3',
            field=models.CharField(blank=True, choices=[('Y', '(1) Yes'), ('N', '(2) No')], max_length=1, verbose_name='(21) Special question 3'),
        ),
    ]
