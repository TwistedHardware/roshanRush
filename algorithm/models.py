import sys
import StringIO
import contextlib
import pandas as pd
import datetime
from sklearn.externals import joblib
#
from django.db import models
from django.utils.timezone import utc
from django.conf import settings
#
from data_set.models import DataSet, Record, Feature, DateFeature, NumberFeature, BooleanFeature, TextFeature, FileFeature, RecordLinkFeature


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


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
    training_percentage = models.FloatField(default=0.5)
    status = models.CharField(max_length=20, choices=status_options, default="not-ready")
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
    
    def save(self, *args, **kwargs):
        """
        Overrides the default save method to add parameters to the model and prepare code
        """
        # Check if it is a new model
        if self.pk is None:
            # Add codes to the model
            self.reset_code()
            
            # Call parent save
            super(TrainedModel, self).save(*args, **kwargs)
            
            # Add parameters
            self.reset_parameters()
        else:
            # Check if algorithm is changed
            old_instance = TrainedModel.objects.get(pk=self.pk)
            if old_instance.algorithm <> self.algorithm:
                self.reset_parameters()
                self.reset_code()
            
            # Call parent save
            super(TrainedModel, self).save(*args, **kwargs)
    
    def reset_parameters(self):
        """
        Deletes and recreates parameters
        """
        # Delete all parameters
        self.trainedmodelparameter_set.all().delete()
        
        # Add parameter to trained model and assign default values to them 
        for parameter in self.algorithm.algorithmparameter_set.all():
            self.trainedmodelparameter_set.all().create(
                                                        parameter=parameter,
                                                        trained_model=self,
                                                        value=parameter.default_value,
                                                        )
    
    def reset_code(self):
        """
        Resets the code the the original code in the algorithm
        """
        self.import_code = self.algorithm.import_code
        self.feature_loader = self.algorithm.feature_loader
        self.feature_preparation = self.algorithm.feature_preparation
        self.result_preparation = self.algorithm.result_preparation
        self.training = self.algorithm.training
        self.prediction = self.algorithm.prediction
        self.test_accuracy = self.algorithm.test_accuracy
    
    def prepare_import_code(self):
        """
        Returns code to import required libraries
        """
        return self.import_code
    
    def prepare_feature_loader(self, dataset="dataset"):
        """
        Returns code to load Features
        """
        return self.feature_loader.format(dataset=dataset, training_percentage=self.training_percentage)
    
    def prepare_feature_preparation(self):
        """
        Returns code to prepare features
        """
        return self.feature_preparation.format(feature_set=",".join(["'%s'" % item[0]  for item in self.trainedmodelfeature_set.all().values_list("feature__name")]))
    
    def prepare_result_preparation(self):
        """
        Returns code to prepare results
        """
        return self.result_preparation.format(result="'%s'" % self.result.name)
    
    def prepare_training(self):
        """
        Returns code to train a model
        """
        return self.training.format(parameters=",".join(["=".join(item) for item in self.trainedmodelparameter_set.all().values_list("parameter__name", "value")]))
    
    def prepare_prediction(self):
        """
        Returns code to predict using this model
        """
        return self.prediction
    
    def prepare_test_accuracy(self):
        """
        Returns code to test accuracy of this model
        """
        return self.test_accuracy
    
    def load_dataset(self):
        """
        Returns a DataFrame object representing the dataset
        """
        # Load all features
        records = [item[0] for item in self.dataset.record_set.all().values_list("id")]
        date_features = list(DateFeature.objects.all().filter(record__id__in=records).values("record__id", "feature__name", "value"))
        numerical_features = list(NumberFeature.objects.all().filter(record__id__in=records).values("record__id", "feature__name", "value"))
        boolean_features = list(BooleanFeature.objects.all().filter(record__id__in=records).values("record__id", "feature__name", "value"))
        text_features = list(TextFeature.objects.all().filter(record__id__in=records).values("record__id", "feature__name", "value"))
        file_features = list(FileFeature.objects.all().filter(record__id__in=records).values("record__id", "feature__name", "value"))
        record_link_features = list(RecordLinkFeature.objects.all().filter(record__id__in=records).values("record__id", "feature__name", "value", "data_set__id"))
        
        # Create dataset with record__id as index
        dataset = pd.DataFrame({"record__id": records})
        dataset.set_index("record__id", inplace=True)
        
        # Process date features
        if len(date_features) <> 0:
            date_df = pd.DataFrame(date_features).pivot(index="record__id", columns="feature__name", values="value")
        else:
            date_df = pd.DataFrame()
        
        # Process number features
        if len(numerical_features) <> 0:
            numerical_df = pd.DataFrame(numerical_features).pivot(index="record__id", columns="feature__name", values="value")
        else:
            numerical_df = pd.DataFrame()
        
        # Process boolean features
        if len(boolean_features) <> 0:
            boolean_df = pd.DataFrame(boolean_features).pivot(index="record__id", columns="feature__name", values="value")
        else:
            boolean_df = pd.DataFrame()
        
        # Process text features
        if len(text_features) <> 0:
            text_df = pd.DataFrame(text_features).pivot(index="record__id", columns="feature__name", values="value")
        else:
            text_df = pd.DataFrame()
        
        # Process file features
        if len(file_features) <> 0:
            file_df = pd.DataFrame(file_features).pivot(index="record__id", columns="feature__name", values="value")
        else:
            file_df = pd.DataFrame()
        
        # Process record link features
        if len(record_link_features) <> 0:
            record_link_df = pd.DataFrame(record_link_features).pivot(index="record__id", columns="feature__name", values="value")
        else:
            record_link_df = pd.DataFrame()
        
        # Concatenate all features DataFrames to the Main IDs DataFrame and return it
        return pd.concat([dataset, date_df, numerical_df, boolean_df, text_df, file_df, record_link_df], axis=1)
    
    def execute_code(self, dataset, exec_import_code=True, exec_feature_loader=True, exec_feature_preparation=True, exec_result_preparation=True,
                     exec_training=True, exec_prediction=True, prepare_test_accuracy=True):
        """
        Executes model's code and returns (error_text, output, trained_model, prediction, accuracy)
        dataset should be a pandas DataFrame
        """
        # Define trained_model, prediction, accuracy
        trained_model = None
        prediction =None
        accuracy = None
        error_text = None
        
        
        # Try to executes all requested code
        try:
            with stdoutIO() as s:
                if exec_import_code:
                    exec self.prepare_import_code()
                
                if exec_feature_loader:
                    exec self.prepare_feature_loader()
                
                if exec_feature_preparation:
                    exec self.prepare_feature_preparation()
                
                if exec_result_preparation:
                    exec self.prepare_result_preparation()
                
                if exec_training:
                    exec self.prepare_training()
                
                if exec_prediction:
                    exec self.prepare_prediction()
                
                if prepare_test_accuracy:
                    exec self.prepare_test_accuracy()
            
            # Retrieve the output of code executed
            output=s.getvalue()
        except Exception as ex:
            try:
                error_text = ex.strerror
            except:
                error_text = str(ex)
        
        # Returns error_text, output, trained_model, prediction, accuracy
        # if error_text is not None then an error happened during code execution
        return (error_text, output, trained_model, prediction, accuracy)
    
    def train_model(self):
        """
        Trains model and stored the trained model pickle file
        Returns predictions of test_set
        """
        # Create a Session
        session = self.trainedmodelsession_set.all().create(
                                                  trained_model = self,
                                                  parameters = "\n".join(["=".join(item) for item in self.trainedmodelparameter_set.all().values_list("parameter__name", "value")]),
                                                  features = "\n".join(["%s" % item[0]  for item in self.trainedmodelfeature_set.all().values_list("feature__name")]),
                                                  start_time = datetime.datetime.utcnow().replace(tzinfo=utc),
                                                  finish_time = None,
                                                  output = None,
                                                  accuracy_score = None,
                                                  accuracy_report = None
                                                  )
        # Load dataset
        dataset = self.load_dataset()
        
        # Execute all code
        error_text, output, trained_model, prediction, accuracy = self.execute_code(dataset)
        
        # Check for error
        if error_text in None:
            # Store Output
            session.output = output
            
            # Store Accuracy score and report
            session.accuracy_report = accuracy
            if self.algorithm.type.name == "Classifier":
                session.accuracy_score = accuracy["accuracy"]
            elif  self.algorithm.type.name == "Regression":
                session.accuracy_score = 1 - accuracy["mean_squared_error"]
        else:
            # Store Output
            session.output = error_text
        
        # Store Trained Model as a pickle file
        joblib.dump(trained_model, "%s/trained_models/%s.pkl" % (settings.MEDIA_ROOT, self.pk))
        
        # Store Finish Time and save Session
        session.finish_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        session.save()
        
        return prediction
    
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
    pre_process = models.ForeignKey(DataProcess, null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return "%s" % self.feature.name
    
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
    accuracy_report = models.TextField(null=True, blank=True)
    
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