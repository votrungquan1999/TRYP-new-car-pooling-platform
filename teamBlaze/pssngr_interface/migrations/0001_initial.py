<<<<<<< HEAD
# Generated by Django 2.1.1 on 2018-11-10 00:45
=======
# Generated by Django 2.1.3 on 2018-11-15 00:19
>>>>>>> 3021a4c382a24e281ddf0acdf9a0d24073cfae80

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        ('driver_interface', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
=======
        ('driver_interface', '0002_carpoolpost_passengers'),
>>>>>>> 3021a4c382a24e281ddf0acdf9a0d24073cfae80
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NeedRidePost',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='driver_interface.Post')),
                ('driver', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('my_user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.MyUser')),
            ],
            bases=('driver_interface.post',),
        ),
    ]
