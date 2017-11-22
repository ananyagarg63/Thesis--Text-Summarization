#!/bin/python

"""
  Deep Learning Models for Sequence to Sequence Modelling
"""
import tensorflow as tf
import abc

class Model(object):
  """ Abstract class for models, this will be inherited by different models"""
  def __init__(self):
      pass
  
  @abc.abstractmethod
  def processor(self):
      pass
      
  @abc.abstractmethod
  def predict(self):
      pass
  
  @abc.abstractmethod
  def fit(self):
      pass
  
  @abc.abstractmethod
  def save(self, path):
      pass
   
  @abc.abstractmethod 
  def load(self, path):
      pass
      
class NeuralModel(Model):
    def __init__(self):
        pass
        
    @abc.abstractmethod     
    def __add_forward_path(self):
        pass
    
    @abc.abstractmethod 
    def __add_loss_graph(self):
        pass
    
    @abc.abstractmethod     
    def __add_train_graph(self):
        pass
    
    @abc.abstractmethod     
    def __add_eval_graph(self):
        pass
