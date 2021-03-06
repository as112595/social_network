

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=1, max_length=100)),
                ('status', models.CharField(choices=[('Married', 'Married'), ('Single', 'Single')], default=1, max_length=10)),
                ('website', models.URLField(blank=True, max_length=283, null=True)),
                ('company', models.CharField(max_length=120)),
                ('profession', models.CharField(choices=[('Student or Learning', 'Student or Learning'), ('Junior Developer', 'Junior Developer'), ('Senior Developer', 'Senior Developer'), ('Developer', 'Developer'), ('Manager', 'Manager'), ('Instructor or Teacher', 'Instructor or Teacher'), ('Intern', 'Intern'), ('ussiness Man', 'Bussiness Man'), ('Digital Marketer', 'Digital Marketer'), ('Data Scientist', 'Data Scientist'), ('Other', 'Other')], default='Web Developer', max_length=120)),
                ('location', models.CharField(default='USA', max_length=100)),
                ('skills', models.CharField(max_length=120)),
                ('bio', models.TextField(blank=True, default='Hello buddies..!')),
                ('image', models.ImageField(blank=True, default='default.jpg', upload_to='profiles/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, max_length=283, null=True)),
                ('youtube', models.URLField(blank=True, max_length=283, null=True)),
                ('twitter', models.URLField(blank=True, max_length=283, null=True)),
                ('instagram', models.URLField(blank=True, max_length=283, null=True)),
                ('linkedin', models.URLField(blank=True, max_length=283, null=True)),
                ('github', models.URLField(blank=True, max_length=283, null=True)),
                ('google_plus', models.URLField(blank=True, max_length=283, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default='IFS', max_length=120, null=True)),
                ('profession', models.CharField(choices=[('Student or Learning', 'Student or Learning'), ('Junior Developer', 'Junior Developer'), ('Senior Developer', 'Senior Developer'), ('Developer', 'Developer'), ('Manager', 'Manager'), ('Instructor or Teacher', 'Instructor or Teacher'), ('Intern', 'Intern'), ('ussiness Man', 'Bussiness Man'), ('Digital Marketer', 'Digital Marketer'), ('Data Scientist', 'Data Scientist'), ('Other', 'Other')], default=1, max_length=120)),
                ('started_at', models.DateField(default=datetime.datetime.now, null=True)),
                ('ended_at', models.DateField(default=datetime.datetime.now, null=True)),
                ('is_currently_working', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(default='Info Tech', max_length=120, null=True)),
                ('degree', models.CharField(choices=[('IT', 'Information Technologies'), ('Bussiness Managment', 'Bussiness Managment'), ('Digital Marketing', 'Digital Marketing'), ('Computer Science', 'Computer Science'), ('Civil Engineering', 'Civil Engineering'), ('AI', 'Artificial & Inteligence'), ('Other', 'Other')], default=1, max_length=120)),
                ('started_at', models.DateField(default=datetime.datetime.now, null=True)),
                ('ended_at', models.DateField(default=datetime.datetime.now, null=True)),
                ('is_currently_studying', models.BooleanField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
        ),
    ]
