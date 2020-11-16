# Generated by Django 2.1.15 on 2020-11-11 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmrifAib',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('pid', models.CharField(db_column='PID', max_length=10)),
                ('rstseqno', models.IntegerField(db_column='RSTSEQNO')),
                ('rstdate', models.CharField(db_column='RSTDATE', max_length=8)),
                ('state_flag', models.CharField(blank=True, db_column='STATEFLAG', max_length=50, null=True)),
                ('created', models.DateTimeField(db_column='created')),
            ],
            options={
                'db_table': 'EMRIFAIB',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EmrifDept',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, db_column='created')),
                ('updated', models.DateTimeField(auto_now=True, db_column='updated')),
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='NAME', max_length=50, null=True)),
            ],
            options={
                'db_table': 'EMRIF_DEPT',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EmrifEquip',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, db_column='created')),
                ('updated', models.DateTimeField(auto_now=True, db_column='updated')),
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='NAME', max_length=50, null=True)),
                ('equip_company', models.CharField(blank=True, db_column='EQUIP_COMPANY', max_length=50, null=True)),
                ('equip_name', models.CharField(blank=True, db_column='EQUIP_NAME', max_length=50, null=True)),
                ('equip_number', models.CharField(blank=True, db_column='EQUIP_NUMBER', max_length=50, null=True)),
            ],
            options={
                'db_table': 'EMRIF_EQUIP',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EmrifError',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, db_column='created')),
                ('updated', models.DateTimeField(auto_now=True, db_column='updated')),
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, db_column='TITLE', max_length=500, null=True)),
                ('content', models.CharField(blank=True, db_column='CONTENT', max_length=2000, null=True)),
                ('state_flag', models.CharField(blank=True, db_column='STATE_FLAG', max_length=50, null=True)),
            ],
            options={
                'db_table': 'EMRIF_ERROR',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EmrifLab',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, db_column='created')),
                ('updated', models.DateTimeField(auto_now=True, db_column='updated')),
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='NAME', max_length=50, null=True)),
                ('call_number', models.CharField(blank=True, db_column='CALL_NUMBER', max_length=50, null=True)),
                ('bg_image', models.ImageField(blank=True, db_column='BG_IMAGE', null=True, upload_to='')),
                ('floor', models.CharField(blank=True, db_column='FLOOR', max_length=50, null=True)),
                ('dept', models.ForeignKey(blank=True, db_column='DEPT_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='emriflab', to='emrif.EmrifDept')),
            ],
            options={
                'db_table': 'EMRIF_LAB',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EmrifPc',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, db_column='created')),
                ('updated', models.DateTimeField(auto_now=True, db_column='updated')),
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('ip', models.CharField(blank=True, db_column='IP', max_length=50, null=True)),
                ('status', models.CharField(blank=True, db_column='STATUS', max_length=50, null=True)),
                ('position_left', models.IntegerField(blank=True, db_column='POSITION_LEFT', null=True)),
                ('position_top', models.IntegerField(blank=True, db_column='POSITION_TOP', null=True)),
                ('equip', models.ForeignKey(blank=True, db_column='EQUP_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='emrifpc', to='emrif.EmrifEquip')),
            ],
            options={
                'db_table': 'EMRIF_PC',
                'ordering': ['status'],
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='emriferror',
            name='emrifpc',
            field=models.ForeignKey(blank=True, db_column='PC_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='emriferror', to='emrif.EmrifPc'),
        ),
        migrations.AddField(
            model_name='emrifequip',
            name='lab',
            field=models.ForeignKey(blank=True, db_column='LAB_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='emrifequip', to='emrif.EmrifLab'),
        ),
        migrations.AddField(
            model_name='emrifaib',
            name='emrifpc',
            field=models.ForeignKey(db_column='emrifpc', on_delete=django.db.models.deletion.DO_NOTHING, related_name='emrifaib', to='emrif.EmrifPc'),
        ),
    ]
