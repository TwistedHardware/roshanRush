import datetime
#
#from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.utils.timezone import utc
#
from models import API, APIUsage, APIToken


class ProcessAPI(View):
    """
    Processes API requests and return results
    """
    
    """
    Methods
    """
    def dispatch(self, request, *args, **kwargs):
    # Try to dispatch to the right method; if a method doesn't exist,
    # defer to the error handler. Also defer to the error handler if the
    # request method isn't on the approved list.
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Over for HTTP request type=GET to process API requests of that type
        """
        return self.process_api_request(request, *args, **kwargs)
       
    
    def post(self, request, *args, **kwargs):
        """
        Over for HTTP request type=POST to process API requests of that type
        """
        return self.process_api_request(request, *args, **kwargs)
    
    def process_api_request(self, request, *args, **kwargs):
        """
        Process an API request and returns a response
        """
        # Get the API name passed from url.py
        api_name = kwargs['api_name']
        # Check is the API exists
        try:
            api_model = API.objects.all().get(name=api_name)
        except:
            return HttpResponse("API (%s): Doesn't exist. " % api_name, content_type='text/plain')
        
        # Record API Usage
        api_usage = api_model.apiusage_set.all().create(api=api_model)
        api_usage.parameters = ",\n".join(["%s: %s" % (key, value) for key, value in kwargs.iteritems()])
        api_usage.save()
        api_usage.id
        
        # Check Token
        token = request.REQUEST.get('token',None)
        if api_model.require_token and token is None:
            # Update API Usage TODO: Make it a task call
            update_api_usage(api_usage.id, response_code="decline")
            
            # Return HTTPResponse 
            return HttpResponse("API (%s): Requires token authentication. Please provide a valid token." % api_name, content_type='text/plain')
        elif api_model.require_token:
            # Check if the token is valid and associated to this API
            token_model = api_model.apitoken_set.all().filter(token=token)
            if not token_model.exists():
                # Update API Usage TODO: Make it a task call
                update_api_usage(api_usage.id, response_code="decline", token=token)
                
                # Return HTTPResponse 
                return HttpResponse("API (%s): The provided token is invalid or doesn't have access to this API." % api_name, content_type='text/plain')
            elif not token_model[0].active:
                # Update API Usage TODO: Make it a task call
                update_api_usage(api_usage.id, response_code="decline", token=token)
                
                # Return HTTPResponse 
                return HttpResponse("API (%s): The provided token is deactivated. Please activate the token." % api_name, content_type='text/plain')
            elif token_model[0].expiry_date > datetime.datetime.utcnow().replace(tzinfo=utc):
                # Update API Usage TODO: Make it a task call
                update_api_usage(api_usage.id, response_code="decline", token=token)
                
                # Return HTTPResponse 
                return HttpResponse("API (%s): The provided token has expired. Please renew your token or create a new one." % api_name, content_type='text/plain')
            
        # Update API Usage TODO: Make it a task call
        update_api_usage(api_usage.id, response_code="success", token=token)
        
        # TODO: Execute linked process and return the results
        if api_model.process_set.all().exists():
            output, content_type = api_model.process_set.all()[0].execute_process()
            return HttpResponse(output, content_type)
        # Return HTTPResponse
        return HttpResponse("No process is linked to this API", content_type='text/plain')


#TODO Make this into a task
def update_api_usage(api_usage__id, response_code="decline", token=None, response_time=datetime.datetime.utcnow().replace(tzinfo=utc)):
    """
    Updates an existing API Usage record
    """
    api_usage = APIUsage.objects.all().get(id=api_usage__id)
    running_time = (response_time - api_usage.request_time).seconds
    if not token is None:
        api_usage.token = APIToken.objects.all().get(token=token)
    api_usage.response_code = response_code
    api_usage.response_time = response_time
    api_usage.running_time = running_time
    api_usage.save()