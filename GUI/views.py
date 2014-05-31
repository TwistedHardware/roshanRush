import os.path
import Image
import numpy as np
from skimage import img_as_float
from sklearn.externals import joblib

#
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate, logout, login
from django.db.models import Count
#
from data_set.models import DataSet, DataSetType, DataGroup, NumberFeature, TextFeature
from roshanRush import settings

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
            elif action == "showdata":
                df = DataSet.objects.all().get(id=instance_id).to_DataFrame(truncate=True)
                context["columns_list"] = df.columns
                context["record_list"] = df.values[:1000]
                self.template_name = "gui/dataset-showdata.html"
                # Render and return the DataSets page
                return render(request, self.template_name, context)
                
                
            # Build context for DataSets Page and assign template
            context["dataset_list"] = []
            for dataset in DataSet.objects.all().annotate(record_count=Count('record')).order_by(order):
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
            elif action == "edit":
                # TODO add edit code
                pass

class DoctorView(View):
    """
    Process requests for Doctor View
    """
    template_name = "doctor_view/home.html"
    
    def get(self, request, *args, **kwargs):
        studyid = request.REQUEST.get("studyid", None)
        # Define Context
        context = {}
        # Check if the user is logged in
        if request.user.is_authenticated():
            context["username"] = request.user.username
        else:
            context["username"] = None
            #Render and return the page
            return render(request, self.template_name, context)
        
        context["studyid"] = studyid
        
        df = DataSet.objects.all().get(id=7).to_DataFrame(truncate=False, filter_features=("StudyID", studyid))
        
        series_list = np.unique(df["SeriesNumber"]).values
        context["series_list"] = [{"seriesid": int(item), "images":[]} for item in series_list]
        
        for series in context["series_list"]:
            df2 = df[df["SeriesNumber"]==series["seriesid"]]
            for counter in df2.index:
                try:
                    instackid = int(df2["InStackPositionNumber"][counter])
                except:
                    instackid = "nan"
                try:
                    instanceid = int(df2["InstanceNumber"][counter])
                except:
                    instanceid = "nan"
                #try:
                
                window_center = float(df2["WindowCenter"][counter])
                window_width = float(df2["WindowWidth"][counter])
                
                pickle_file_path = "%s/cache/%s_%s_%s_%s.pkl" % (settings.MEDIA_ROOT, studyid, series["seriesid"], instackid, instanceid)
                if os.path.isfile(pickle_file_path):
                    image_pickle = joblib.load(pickle_file_path)
                    image = image_pickle["image"]
                else:
                    image = df2["pixel_array"][counter]
                    image = eval(image)
                    image = np.asarray(image, dtype=np.int16)
                    joblib.dump({"image":image, "WindowCenter":window_center, "WindowWidth":window_width}, pickle_file_path)
                
                
                
                
                max_color = int(np.max(image))
                min_color = int(np.min(image))
                #except:
                    #window_center = "nan"
                    #window_width = "nan"
                    #max_color = "nan"
                    #min_color = "nan"
                
                series["images"].append({
                                         "instanceid":instanceid,
                                         "instackid": instackid,
                                         "window_center":window_center,
                                         "window_width":window_width,
                                         "max_color":max_color,
                                         "min_color":min_color,
                                         })
        
        

        
        
        
        
        return render(request, self.template_name, context)

class GetImage(View):
    """
    Returns an Image from DICOM
    """
    
    def get(self, request, *args, **kwargs):
        studyid = request.REQUEST.get("studyid", None)
        seriesid = request.REQUEST.get("seriesid", None)
        instackid = request.REQUEST.get("instackid", None)
        instanceid = request.REQUEST.get("instanceid", None)
        size = request.REQUEST.get("size", None)
        window_center = request.REQUEST.get("windowcenter", None)
        window_width = request.REQUEST.get("windowwidth", None)
        
        file_path = "%s/cache/%s_%s_%s_%s_%s_%s_%s.jpg" % (settings.MEDIA_ROOT, studyid, seriesid, instackid, instanceid, size, window_center, window_width)
        pickle_file_path = "%s/cache/%s_%s_%s_%s.pkl" % (settings.MEDIA_ROOT, studyid, seriesid, instackid, instanceid)
        
        response = HttpResponse(content_type="image/jpeg")
        if os.path.isfile(file_path):
            image = Image.open(file_path)
        else:
            if os.path.isfile(pickle_file_path):
                image_pkl = joblib.load(pickle_file_path)
                image = image_pkl["image"]
                if window_center and window_width:
                    WindowCenter = float(window_center)
                    WindowWidth = float(window_width)
                else:
                    WindowCenter = float(image_pkl["WindowCenter"])
                    WindowWidth = float(image_pkl["WindowWidth"])
            else:
                #df = DataSet.objects.all().get(id=7).to_DataFrame(truncate=False, filter_features=("StudyID", studyid))
                #df[(df["InStackPositionNumber"]=instackid) & (df["InStackPositionNumber"]=instackid)]
                record_ids = NumberFeature.objects.all().filter(feature__name="StudyID", value=studyid).values_list("record__id")
                record_ids = NumberFeature.objects.all().filter(record__id__in=record_ids, feature__name="SeriesNumber", value=seriesid).values_list("record__id")
                #record_ids = NumberFeature.objects.all().filter(record__id__in=record_ids, feature__name="InStackPositionNumber", value=instackid).values_list("record__id")
                record_ids = NumberFeature.objects.all().filter(record__id__in=record_ids, feature__name="InstanceNumber", value=instanceid).values_list("record__id")
                
                if len(record_ids) == 0:
                    return HttpResponse("NA")
                
                image = TextFeature.objects.all().get(feature__name="pixel_array", record__id__in=record_ids).value
                WindowCenter = NumberFeature.objects.all().get(feature__name="WindowCenter", record__id__in=record_ids).value
                WindowWidth = NumberFeature.objects.all().get(feature__name="WindowWidth", record__id__in=record_ids).value
                image = eval(image)
                image = np.asarray(image, dtype=np.int16)
                # Save Raw image pickle file
                joblib.dump({"image":image, "WindowCenter":WindowCenter, "WindowWidth":WindowWidth}, pickle_file_path)
                
            # WindowWidth,WindowCenter
            #original_image = image / float(np.max(image)) * 255 
            minWindowValue = WindowCenter - (WindowWidth / 2)
            image = 255 * (image - minWindowValue) / WindowWidth
            
            image = Image.fromarray(image).convert("RGB")
            if size:
                size = (int(size), int(size))
                image.thumbnail(size, Image.ANTIALIAS)
                    
            # Final File
            image.save(file_path, "JPEG")

        image.save(response, "JPEG")
        return response
        

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