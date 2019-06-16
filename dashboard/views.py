# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse

from .tables import DashboardTable



def dashboard(request):
    context = dict(
        table_coins=DashboardTable(
            id='table_coins',
            url=reverse('api:coin-list', kwargs={'format': 'json'}),
            columns=['code', 'name']
        ),
        table_markets=DashboardTable(
            id='table_markets',
            url=reverse('api:market-list', kwargs={'format': 'json'}),
            columns=['code', 'coin', 'unit']
        ),
    )
    return render(request, 'index.html', context)


def check_queries(request):
    context = dict(
        table_check_queries=DashboardTable(
            id='table_check_queries',
            url=reverse('api:querytest-list', kwargs={'format': 'json'}),
            columns=['name', 'params', 'result', 'expect', 'created_at', 'passed']
        )
    )
    return render(request, 'check.html', context)
