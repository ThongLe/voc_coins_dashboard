# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.shortcuts import render


def dashboard(request):
    context = {}
    return render(request, 'index.html', context)