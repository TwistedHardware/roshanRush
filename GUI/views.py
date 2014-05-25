from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
#
from data_set.models import DataSet

class GetPage(View):
    """
    Return an HTML page for the GUI
    """
    template_name = "gui/home.html"
    
    def get(self, request, *args, **kwargs):
        # Retrieve requested page
        page = request.REQUEST.get("page", None)
        
        # Define Context
        context = {}
        # Check if the user is logged in
        if request.user.is_authenticated():
            context["username"] = request.user.username
        else:
            context["username"] = None
            #Render and return the page
            return render(request, self.template_name, context)
        
        # check if there is no page requested
        if page is None:
            # Render and return the Home page
            return render(request, self.template_name, context)
        elif page == "dataset":
            # Build context for DataSets Page and assign template
            context["dataset_list"] = []
            for dataset in DataSet.objects.all():
                context["dataset_list"].append({"id": dataset.id,
                                                "name": dataset.name,
                                                "type": dataset.type.name,
                                                "group": dataset.data_group.name,
                                                "count": dataset.record_set.all().count()})
            self.template_name = "gui/dataset.html"
            
            # Render and return the DataSets page
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, context)
        
        