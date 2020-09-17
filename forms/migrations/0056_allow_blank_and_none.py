# Generated by Django 2.2.16 on 2020-09-17 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0055_remove_defaults'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internetnewsperson',
            name='family_role',
            field=models.CharField(blank=True, choices=[('Y', '(1) Yes'), ('N', '(2) No')], help_text="Code yes only if the word 'wife', 'husband' etc is actually used to describe the person.", max_length=1, null=True, verbose_name='(16) Family Role Given?'),
        ),
        migrations.AlterField(
            model_name='internetnewsperson',
            name='is_photograph',
            field=models.PositiveIntegerField(blank=True, choices=[(1, '(1) Yes'), (2, '(2) No'), (3, '(3) Do not know')], null=True, verbose_name='(21) Is there a photograph of the person in the story?'),
        ),
        migrations.AlterField(
            model_name='internetnewsperson',
            name='is_quoted',
            field=models.CharField(blank=True, choices=[('Y', '(1) Yes'), ('N', '(2) No')], help_text='A person is <strong>directly quoted</strong> if their own words are printed, e.g. "The war against terror is our first priority" said President Bush.<br/>If the story paraphrases what the person said, that is not a direct quote, e.g. President Bush said that top priority would be given to fighting the war against terror.', max_length=1, null=True, verbose_name='(20) Is the person directly quoted'),
        ),
        migrations.AlterField(
            model_name='internetnewsperson',
            name='victim_or_survivor',
            field=models.CharField(blank=True, choices=[('Y', '(1) Yes'), ('N', '(2) No')], help_text="You should code a person as a victim <strong>either</strong> if the word 'victim' is used to describe her/him, <strong>or</strong> if the story Implies that the person is a victim - e.g. by using language or images that evoke particular emotions such as shock, horror, pity for the person.<br/>You should code a person as a survivor <strong>either</strong> if the word 'survivor' is used to describe her/him, <strong>or</strong> if the story implies that the person is a survivor - e.g. by using language or images that evoke particular emotions such as admiration or respect for the person.", max_length=1, null=True, verbose_name='(17) Does the story identify the person as either a victim or survivor?'),
        ),
        migrations.AlterField(
            model_name='newspaperperson',
            name='family_role',
            field=models.CharField(blank=True, choices=[('Y', '(1) Yes'), ('N', '(2) No')], help_text="Code yes only if the word 'wife', 'husband' etc is actually used to describe the person.", max_length=1, null=True, verbose_name='(14) Family Role Given?'),
        ),
        migrations.AlterField(
            model_name='newspaperperson',
            name='is_photograph',
            field=models.PositiveIntegerField(blank=True, choices=[(1, '(1) Yes'), (2, '(2) No'), (3, '(3) Do not know')], null=True, verbose_name='(19) Is there a photograph of the person in the story?'),
        ),
        migrations.AlterField(
            model_name='newspaperperson',
            name='is_quoted',
            field=models.CharField(blank=True, choices=[('Y', '(1) Yes'), ('N', '(2) No')], help_text='A person is <strong>directly quoted</strong> if their own words are printed, e.g. "The war against terror is our first priority" said President Bush.<br/>If the story paraphrases what the person said, that is not a direct quote, e.g. President Bush said that top priority would be given to fighting the war against terror.', max_length=1, null=True, verbose_name='(18) Is the person directly quoted'),
        ),
        migrations.AlterField(
            model_name='newspaperperson',
            name='victim_or_survivor',
            field=models.CharField(blank=True, choices=[('Y', '(1) Yes'), ('N', '(2) No')], help_text="You should code a person as a victim <strong>either</strong> if the word 'victim' is used to describe her/him, <strong>or</strong> if the story Implies that the person is a victim - e.g. by using language or images that evoke particular emotions such as shock, horror, pity for the person.<br/>You should code a person as a survivor <strong>either</strong> if the word 'survivor' is used to describe her/him, <strong>or</strong> if the story implies that the person is a survivor - e.g. by using language or images that evoke particular emotions such as admiration or respect for the person.", max_length=1, null=True, verbose_name='(15) Does the story identify the person as either a victim or survivor?'),
        ),
        migrations.AlterField(
            model_name='radioperson',
            name='family_role',
            field=models.CharField(blank=True, choices=[('Y', '(1) Yes'), ('N', '(2) No')], help_text="Code yes only if the word 'wife', 'husband' etc is actually used to describe the person.", max_length=1, null=True, verbose_name='(13) Family Role Given?'),
        ),
        migrations.AlterField(
            model_name='radioperson',
            name='victim_or_survivor',
            field=models.CharField(blank=True, choices=[('Y', '(1) Yes'), ('N', '(2) No')], help_text="You should code a person as a victim <strong>either</strong> if the word 'victim' is used to describe her/him, <strong>or</strong> if the story Implies that the person is a victim - e.g. by using language or images that evoke particular emotions such as shock, horror, pity for the person.<br/>You should code a person as a survivor <strong>either</strong> if the word 'survivor' is used to describe her/him, <strong>or</strong> if the story implies that the person is a survivor - e.g. by using language or images that evoke particular emotions such as admiration or respect for the person.", max_length=1, null=True, verbose_name='(14) Does the story identify the person as either a victim or survivor?'),
        ),
        migrations.AlterField(
            model_name='televisionperson',
            name='family_role',
            field=models.CharField(blank=True, choices=[('Y', '(1) Yes'), ('N', '(2) No')], help_text="Code yes only if the word 'wife', 'husband' etc is actually used to describe the person.", max_length=1, null=True, verbose_name='(15) Family Role Given?'),
        ),
        migrations.AlterField(
            model_name='televisionperson',
            name='victim_or_survivor',
            field=models.CharField(blank=True, choices=[('Y', '(1) Yes'), ('N', '(2) No')], help_text="You should code a person as a victim <strong>either</strong> if the word 'victim' is used to describe her/him, <strong>or</strong> if the story Implies that the person is a victim - e.g. by using language or images that evoke particular emotions such as shock, horror, pity for the person.<br/>You should code a person as a survivor <strong>either</strong> if the word 'survivor' is used to describe her/him, <strong>or</strong> if the story implies that the person is a survivor - e.g. by using language or images that evoke particular emotions such as admiration or respect for the person.", max_length=1, null=True, verbose_name='(16) Does the story identify the person as either a victim or survivor?'),
        ),
        migrations.AlterField(
            model_name='twitterperson',
            name='is_photograph',
            field=models.PositiveIntegerField(blank=True, choices=[(1, '(1) Yes'), (2, '(2) No'), (3, '(3) Do not know')], null=True, verbose_name='(13) Is there a photograph of the person in the story?'),
        ),
    ]
