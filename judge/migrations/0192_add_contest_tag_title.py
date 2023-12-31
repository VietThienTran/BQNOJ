# Generated by Django 3.2.20 on 2023-07-10 04:53

from django.db import migrations, models


def populate_tag_title(apps, schema_editor):
    ContestTag = apps.get_model('judge', 'ContestTag')
    for tag in ContestTag.objects.all():
        tag.name = tag.slug
        tag.save()


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0191_submission_index_cleanup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contesttag',
            old_name='name',
            new_name='slug',
        ),
        migrations.AlterField(
            model_name='contesttag',
            name='slug',
            field=models.SlugField(help_text='Tag name shown in URLs.', max_length=20, unique=True, verbose_name='tag slug'),
        ),
        migrations.AddField(
            model_name='contesttag',
            name='name',
            field=models.CharField(null=True, max_length=128, verbose_name='tag title'),
        ),
        migrations.RunPython(populate_tag_title, reverse_code=migrations.RunPython.noop, atomic=True),
        migrations.AlterField(
            model_name='contesttag',
            name='name',
            field=models.CharField(null=False, max_length=128, verbose_name='tag title'),
        ),
    ]
