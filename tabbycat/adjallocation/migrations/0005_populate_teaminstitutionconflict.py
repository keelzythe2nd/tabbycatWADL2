# Generated by Django 2.0.8 on 2018-09-20 04:11

from django.db import migrations


def populate_teaminstitutionconflict(apps, schema_editor):

    TeamInstitutionConflict = apps.get_model('adjallocation', 'TeamInstitutionConflict')  # noqa: N806
    Team = apps.get_model('participants', 'Team')  # noqa: N806

    for team in Team.objects.all():
        if team.institution_id is not None:
            TeamInstitutionConflict.objects.get_or_create(team=team, institution_id=team.institution_id)


class Migration(migrations.Migration):

    dependencies = [
        ('adjallocation', '0004_add_teaminstitutionconflict'),
    ]

    operations = [
        migrations.RunPython(populate_teaminstitutionconflict,
            migrations.RunPython.noop,
            elidable=True)
    ]
