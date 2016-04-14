# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=20, verbose_name='IP\u5730\u5740')),
                ('hostname', models.CharField(max_length=30, verbose_name='\u4e3b\u673a\u540d')),
                ('product', models.CharField(max_length=20, verbose_name='\u4ea7\u54c1')),
                ('application', models.CharField(max_length=20, verbose_name='\u5e94\u7528')),
                ('idc_jg', models.CharField(max_length=10, verbose_name='\u673a\u67dc\u7f16\u53f7', blank=True)),
                ('status', models.CharField(default='\u5f85\u88c5\u673a', max_length=10, verbose_name='\u4f7f\u7528\u72b6\u6001')),
                ('remark', models.TextField(max_length=50, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name_plural': '\u4e3b\u673a\u5217\u8868\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('audit_time', models.DateTimeField(auto_now_add=True, verbose_name='\u65f6\u95f4')),
                ('type', models.CharField(max_length=10, verbose_name='\u7c7b\u578b')),
                ('action', models.CharField(max_length=10, verbose_name='\u52a8\u4f5c')),
                ('action_ip', models.CharField(max_length=15, verbose_name='\u6267\u884cIP')),
                ('content', models.CharField(max_length=50, verbose_name='\u5185\u5bb9')),
            ],
            options={
                'verbose_name_plural': '\u5ba1\u8ba1\u4fe1\u606f\u7ba1\u7406',
            },
        ),
    ]
