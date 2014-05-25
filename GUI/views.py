from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth import authenticate, logout, login
#
from data_set.models import DataSet, DataSetType, DataGroup

class GetPage(View):
    """
    Return an HTML page for the GUI
    """
    template_name = "gui/home.html"
    
    def get(self, request, *args, **kwargs):
        # Retrieve requested page
        page = request.REQUEST.get("page", None)
        action = request.REQUEST.get("action", None)
        instance_id = request.REQUEST.get("id", None)
        order = request.REQUEST.get("order", "-id")
        
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
            # Process actions first
            if action == "delete":
                DataSet.objects.all().get(id=instance_id).delete()
            # Build context for DataSets Page and assign template
            context["dataset_list"] = []
            for dataset in DataSet.objects.all().order_by(order):
                context["dataset_list"].append({"id": dataset.id,
                                                "name": dataset.name,
                                                "type": dataset.type.name,
                                                "group": dataset.data_group.name,
                                                "count": dataset.record_set.all().count()})
                context["type_list"] = [{"id":item.id, "name":item.name} for item in DataSetType.objects.all()]
                context["group_list"] = [{"id":item.id, "name":item.name} for item in DataGroup.objects.all()]
                context["order"] = order
            self.template_name = "gui/dataset.html"
            
            # Render and return the DataSets page
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        # Retrieve requested page
        page = request.REQUEST.get("page", None)
        action = request.REQUEST.get("action", None)
        instance_id = request.REQUEST.get("id", None)
        
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
            if action == "new":
                name = request.REQUEST.get("name", None)
                schema = request.REQUEST.get("schema", None)
                group = request.REQUEST.get("group", None)
                DataSet.objects.all().create(name=name,
                                             type=DataSetType.objects.all().get(id=schema),
                                             data_group=DataGroup.objects.all().get(id=group),
                                             )
                return self.get(request, args, kwargs)

class UserControl(View):
    """
    Processes requests related to user control like login, logout, password recovery ... etc
    """
    
    def post(self, request, *args, **kwargs):
        
        action = request.REQUEST.get("action", None)
        
        if action == "login":
            username = request.REQUEST.get("username", None)
            password = request.REQUEST.get("password", None)
            user = authenticate(username=username, password=password)
            if user is not None:
                # the password verified for the user
                if not user.is_active:
                    logout(request)
                else:
                    login(request, user)
            return redirect("/")

            
    def get(self, request, *args, **kwargs):
        
        action = request.REQUEST.get("action", None)
        
        if action == "logout":
            logout(request)
            return redirect("/")