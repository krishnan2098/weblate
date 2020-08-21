# Generated by Django 3.0.7 on 2020-08-21 11:59

from django.db import migrations


def set_source_language(apps, schema_editor):
    Glossary = apps.get_model("glossary", "Glossary")
    db_alias = schema_editor.connection.alias
    for glossary in Glossary.objects.using(db_alias).select_related("project"):
        glossary.source_language = glossary.project.source_language
        glossary.save(update_fields=["source_language"])


class Migration(migrations.Migration):

    dependencies = [
        ("glossary", "0004_glossary_source_language"),
    ]

    operations = [
        migrations.RunPython(
            set_source_language, migrations.RunPython.noop, elidable=True
        ),
    ]
