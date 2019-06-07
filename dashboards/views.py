from controlcenter import Dashboard, widgets


# class ModelItemList(widgets.ItemList):
#     model = Model
#     list_display = ('pk', 'field')

class MyDashboard(Dashboard):
    widgets = (
        # ModelItemList,
    )