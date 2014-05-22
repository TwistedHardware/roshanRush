from django.db import models
from data_set.models import DataSet, Feature

class AlgorithmType(models.Model):
    """
    Represents a type of Machine Learning Algorithms
    """
    
    """
    Fields
    """
    name = models.CharField(max_length=200)
    feature_loader = models.TextField(null=True, blank=True)
    feature_preparation = models.TextField(null=True, blank=True)
    result_preparation = models.TextField(null=True, blank=True)
    training = models.TextField(null=True, blank=True)
    predection = models.TextField(null=True, blank=True)
    test_accuracy = models.TextField(null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return self.name
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Algorithm Type"
        verbose_name_plural = "Algorithm Types"


class ProgrammingLanguage(models.Model):
    """
    Represents a programming language
    """
    
    """
    Fields
    """
    name = models.CharField(max_length=200)
    
    """
    Methods
    """
    def __unicode__(self):
        return self.name
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Programming Language"
        verbose_name_plural = "Programming Languages"


class Library(models.Model):
    """
    Represents a machine Learning Library
    """
    
    """
    Fields
    """
    name = models.CharField(max_length=200)
    language = models.ForeignKey(ProgrammingLanguage)
    
    """
    Methods
    """
    def __unicode__(self):
        return self.name
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Library"
        verbose_name_plural = "Libraries"


class DataProcess(models.Model):
    """
    Represents a process that can be implemented on data
    """
    
    """
    Fields
    """
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    process_code = models.TextField(null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return self.name
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Data Process"
        verbose_name_plural = "Data Processes"


class Algorithm(models.Model):
    """
    Represents an algorithms from a library
    """
    
    """
    Fields
    """
    name = models.CharField(max_length=200)
    type = models.ForeignKey(AlgorithmType)
    library = models.ForeignKey(Library, null=True, blank=True)
    import_code = models.TextField(null=True, blank=True)
    feature_loader = models.TextField(null=True, blank=True)
    feature_preparation = models.TextField(null=True, blank=True)
    result_preparation = models.TextField(null=True, blank=True)
    training = models.TextField(null=True, blank=True)
    prediction = models.TextField(null=True, blank=True)
    test_accuracy = models.TextField(null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return self.name
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Algorithm"
        verbose_name_plural = "Algorithms"


class AlgorithmParameter(models.Model):
    """
    Represents a parameter from an algorithm
    """
    
    """
    Fields
    """
    algorithm = models.ForeignKey(Algorithm)
    name = models.CharField(max_length=200)
    default_value = models.CharField(max_length=200)
    help = models.TextField(null=True, blank=True)
    min_value = models.FloatField(null=True, blank=True)
    max_value = models.FloatField(null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return self.name
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Algorithm Parameter"
        verbose_name_plural = "Algorithm Parameters"


class ParameterValue(models.Model):
    """
    Represents a possible value for a parameters
    """
    
    """
    Fields
    """
    parameter = models.ForeignKey(AlgorithmParameter)
    value = models.CharField(max_length=200)
    help = models.CharField(max_length=200, null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return "%s:%s" % (self.parameter.name, self.value)
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Parameter Value"
        verbose_name_plural = "Parameter Values"


class TrainedModel(models.Model):
    """
    Represents a trained model
    """
    status_options = (
                      ("not-ready","Not Ready"),
                      ("training","Training"),
                      ("ready","Ready"),
                      ("failed","Failed"),
                      )
    
    """
    Fields
    """
    name = models.CharField(max_length=200)
    algorithm = models.ForeignKey(Algorithm)
    dataset = models.ForeignKey(DataSet)
    accumulative_training = models.BooleanField(default=False)
    result = models.ForeignKey(Feature, null=True, blank=True)
    result_offest = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=status_options)
    import_code = models.TextField(null=True, blank=True)
    feature_loader = models.TextField(null=True, blank=True)
    feature_preparation = models.TextField(null=True, blank=True)
    result_preparation = models.TextField(null=True, blank=True)
    training = models.TextField(null=True, blank=True)
    prediction = models.TextField(null=True, blank=True)
    test_accuracy = models.TextField(null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return self.name
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Trained Model"
        verbose_name_plural = "Trained Models"


class TrainedModelParameter(models.Model):
    """
    Represents a parameter for a trained model
    """
    
    """
    Fields
    """
    parameter = models.ForeignKey(AlgorithmParameter)
    trained_model = models.ForeignKey(TrainedModel)
    value = models.CharField(max_length=200)
    
    """
    Methods
    """
    def __unicode__(self):
        return "%s: %s" % (self.parameter.name, self.value)
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Trained Model Parameter"
        verbose_name_plural = "Trained Model Parameters"


class TrainedModelFeature(models.Model):
    """
    Represents a feature for a trained model
    """
    
    """
    Fields
    """
    feature = models.ForeignKey(Feature)
    trained_model = models.ForeignKey(TrainedModel)
    normalize = models.BooleanField(default=False)
    pre_process = models.ForeignKey(DataProcess)
    
    """
    Methods
    """
    def __unicode__(self):
        return "%s: %s" % (self.parameter.name, self.value)
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Trained Model Feature"
        verbose_name_plural = "Trained Model Features"

class TrainedModelSession(models.Model):
    """
    Represents a session for a trained model
    """
    
    """
    Fields
    """
    trained_model = models.ForeignKey(TrainedModel)
    parameters = models.TextField(null=True, blank=True)
    features = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField(auto_now_add=True)
    finish_time = models.DateTimeField(null=True, blank=True)
    output = models.TextField(null=True, blank=True)
    accuracy_score = models.FloatField(null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return "%s" % (self.start_time)
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Trained Model Session"
        verbose_name_plural = "Trained Model Sessions"


class TrainedModelProcess(models.Model):
    """
    Represents a Pre-process or a Post-process for a trained model
    """
    
    """
    Options
    """
    type_options =(
                   ("preprocess", "Pre-Process"),
                   ("postprocess", "Post-Process"),
                   ) 
    
    """
    Fields
    """
    trained_model = models.ForeignKey(TrainedModel)
    process = models.ForeignKey(DataProcess)
    type = models.CharField(max_length =20, choices=type_options)
    
    """
    Methods
    """
    def __unicode__(self):
        return self.process.name
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Trained Model Process"
        verbose_name_plural = "Trained Model Processes"