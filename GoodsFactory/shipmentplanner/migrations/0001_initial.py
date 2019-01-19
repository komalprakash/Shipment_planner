from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DPA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsetno', models.IntegerField()),
                ('vertexno', models.IntegerField()),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DPB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsetno', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('slno', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shipments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=30)),
                ('weight', models.IntegerField()),
                ('slno', models.IntegerField()),
            ],
        ),
    ]
