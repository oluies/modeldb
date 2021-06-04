# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from ..modeldb import CommonService_pb2 as modeldb_dot_CommonService__pb2
from ..modeldb import ExperimentService_pb2 as modeldb_dot_ExperimentService__pb2


class ExperimentServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.createExperiment = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/createExperiment',
        request_serializer=modeldb_dot_ExperimentService__pb2.CreateExperiment.SerializeToString,
        response_deserializer=modeldb_dot_ExperimentService__pb2.CreateExperiment.Response.FromString,
        )
    self.updateExperimentNameOrDescription = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/updateExperimentNameOrDescription',
        request_serializer=modeldb_dot_ExperimentService__pb2.UpdateExperimentNameOrDescription.SerializeToString,
        response_deserializer=modeldb_dot_ExperimentService__pb2.UpdateExperimentNameOrDescription.Response.FromString,
        )
    self.updateExperimentName = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/updateExperimentName',
        request_serializer=modeldb_dot_ExperimentService__pb2.UpdateExperimentName.SerializeToString,
        response_deserializer=modeldb_dot_ExperimentService__pb2.UpdateExperimentName.Response.FromString,
        )
    self.updateExperimentDescription = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/updateExperimentDescription',
        request_serializer=modeldb_dot_ExperimentService__pb2.UpdateExperimentDescription.SerializeToString,
        response_deserializer=modeldb_dot_ExperimentService__pb2.UpdateExperimentDescription.Response.FromString,
        )
    self.addExperimentTags = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/addExperimentTags',
        request_serializer=modeldb_dot_ExperimentService__pb2.AddExperimentTags.SerializeToString,
        response_deserializer=modeldb_dot_ExperimentService__pb2.AddExperimentTags.Response.FromString,
        )
    self.getExperimentTags = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/getExperimentTags',
        request_serializer=modeldb_dot_CommonService__pb2.GetTags.SerializeToString,
        response_deserializer=modeldb_dot_CommonService__pb2.GetTags.Response.FromString,
        )
    self.deleteExperimentTags = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/deleteExperimentTags',
        request_serializer=modeldb_dot_ExperimentService__pb2.DeleteExperimentTags.SerializeToString,
        response_deserializer=modeldb_dot_ExperimentService__pb2.DeleteExperimentTags.Response.FromString,
        )
    self.addExperimentTag = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/addExperimentTag',
        request_serializer=modeldb_dot_ExperimentService__pb2.AddExperimentTag.SerializeToString,
        response_deserializer=modeldb_dot_ExperimentService__pb2.AddExperimentTag.Response.FromString,
        )
    self.deleteExperimentTag = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/deleteExperimentTag',
        request_serializer=modeldb_dot_ExperimentService__pb2.DeleteExperimentTag.SerializeToString,
        response_deserializer=modeldb_dot_ExperimentService__pb2.DeleteExperimentTag.Response.FromString,
        )
    self.addAttribute = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/addAttribute',
        request_serializer=modeldb_dot_CommonService__pb2.AddAttributes.SerializeToString,
        response_deserializer=modeldb_dot_CommonService__pb2.AddAttributes.Response.FromString,
        )
    self.addExperimentAttributes = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/addExperimentAttributes',
        request_serializer=modeldb_dot_ExperimentService__pb2.AddExperimentAttributes.SerializeToString,
        response_deserializer=modeldb_dot_ExperimentService__pb2.AddExperimentAttributes.Response.FromString,
        )
    self.getExperimentAttributes = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/getExperimentAttributes',
        request_serializer=modeldb_dot_CommonService__pb2.GetAttributes.SerializeToString,
        response_deserializer=modeldb_dot_CommonService__pb2.GetAttributes.Response.FromString,
        )
    self.deleteExperimentAttributes = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/deleteExperimentAttributes',
        request_serializer=modeldb_dot_ExperimentService__pb2.DeleteExperimentAttributes.SerializeToString,
        response_deserializer=modeldb_dot_ExperimentService__pb2.DeleteExperimentAttributes.Response.FromString,
        )
    self.logExperimentCodeVersion = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/logExperimentCodeVersion',
        request_serializer=modeldb_dot_ExperimentService__pb2.LogExperimentCodeVersion.SerializeToString,
        response_deserializer=modeldb_dot_ExperimentService__pb2.LogExperimentCodeVersion.Response.FromString,
        )
    self.getExperimentCodeVersion = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/getExperimentCodeVersion',
        request_serializer=modeldb_dot_ExperimentService__pb2.GetExperimentCodeVersion.SerializeToString,
        response_deserializer=modeldb_dot_ExperimentService__pb2.GetExperimentCodeVersion.Response.FromString,
        )
    self.getExperimentsInProject = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/getExperimentsInProject',
        request_serializer=modeldb_dot_ExperimentService__pb2.GetExperimentsInProject.SerializeToString,
        response_deserializer=modeldb_dot_ExperimentService__pb2.GetExperimentsInProject.Response.FromString,
        )
    self.getExperimentById = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/getExperimentById',
        request_serializer=modeldb_dot_ExperimentService__pb2.GetExperimentById.SerializeToString,
        response_deserializer=modeldb_dot_ExperimentService__pb2.GetExperimentById.Response.FromString,
        )
    self.getExperimentByName = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/getExperimentByName',
        request_serializer=modeldb_dot_ExperimentService__pb2.GetExperimentByName.SerializeToString,
        response_deserializer=modeldb_dot_ExperimentService__pb2.GetExperimentByName.Response.FromString,
        )
    self.deleteExperiment = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/deleteExperiment',
        request_serializer=modeldb_dot_ExperimentService__pb2.DeleteExperiment.SerializeToString,
        response_deserializer=modeldb_dot_ExperimentService__pb2.DeleteExperiment.Response.FromString,
        )
    self.getUrlForArtifact = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/getUrlForArtifact',
        request_serializer=modeldb_dot_CommonService__pb2.GetUrlForArtifact.SerializeToString,
        response_deserializer=modeldb_dot_CommonService__pb2.GetUrlForArtifact.Response.FromString,
        )
    self.findExperiments = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/findExperiments',
        request_serializer=modeldb_dot_ExperimentService__pb2.FindExperiments.SerializeToString,
        response_deserializer=modeldb_dot_ExperimentService__pb2.FindExperiments.Response.FromString,
        )
    self.logArtifacts = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/logArtifacts',
        request_serializer=modeldb_dot_ExperimentService__pb2.LogExperimentArtifacts.SerializeToString,
        response_deserializer=modeldb_dot_ExperimentService__pb2.LogExperimentArtifacts.Response.FromString,
        )
    self.getArtifacts = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/getArtifacts',
        request_serializer=modeldb_dot_CommonService__pb2.GetArtifacts.SerializeToString,
        response_deserializer=modeldb_dot_CommonService__pb2.GetArtifacts.Response.FromString,
        )
    self.deleteArtifact = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/deleteArtifact',
        request_serializer=modeldb_dot_ExperimentService__pb2.DeleteExperimentArtifact.SerializeToString,
        response_deserializer=modeldb_dot_ExperimentService__pb2.DeleteExperimentArtifact.Response.FromString,
        )
    self.deleteExperiments = channel.unary_unary(
        '/ai.verta.modeldb.ExperimentService/deleteExperiments',
        request_serializer=modeldb_dot_ExperimentService__pb2.DeleteExperiments.SerializeToString,
        response_deserializer=modeldb_dot_ExperimentService__pb2.DeleteExperiments.Response.FromString,
        )


class ExperimentServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def createExperiment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def updateExperimentNameOrDescription(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def updateExperimentName(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def updateExperimentDescription(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def addExperimentTags(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getExperimentTags(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteExperimentTags(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def addExperimentTag(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteExperimentTag(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def addAttribute(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def addExperimentAttributes(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getExperimentAttributes(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteExperimentAttributes(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def logExperimentCodeVersion(self, request, context):
    """code version
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getExperimentCodeVersion(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getExperimentsInProject(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getExperimentById(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getExperimentByName(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteExperiment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getUrlForArtifact(self, request, context):
    """artifacts
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def findExperiments(self, request, context):
    """queries
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def logArtifacts(self, request, context):
    """artifacts
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getArtifacts(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteArtifact(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteExperiments(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ExperimentServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'createExperiment': grpc.unary_unary_rpc_method_handler(
          servicer.createExperiment,
          request_deserializer=modeldb_dot_ExperimentService__pb2.CreateExperiment.FromString,
          response_serializer=modeldb_dot_ExperimentService__pb2.CreateExperiment.Response.SerializeToString,
      ),
      'updateExperimentNameOrDescription': grpc.unary_unary_rpc_method_handler(
          servicer.updateExperimentNameOrDescription,
          request_deserializer=modeldb_dot_ExperimentService__pb2.UpdateExperimentNameOrDescription.FromString,
          response_serializer=modeldb_dot_ExperimentService__pb2.UpdateExperimentNameOrDescription.Response.SerializeToString,
      ),
      'updateExperimentName': grpc.unary_unary_rpc_method_handler(
          servicer.updateExperimentName,
          request_deserializer=modeldb_dot_ExperimentService__pb2.UpdateExperimentName.FromString,
          response_serializer=modeldb_dot_ExperimentService__pb2.UpdateExperimentName.Response.SerializeToString,
      ),
      'updateExperimentDescription': grpc.unary_unary_rpc_method_handler(
          servicer.updateExperimentDescription,
          request_deserializer=modeldb_dot_ExperimentService__pb2.UpdateExperimentDescription.FromString,
          response_serializer=modeldb_dot_ExperimentService__pb2.UpdateExperimentDescription.Response.SerializeToString,
      ),
      'addExperimentTags': grpc.unary_unary_rpc_method_handler(
          servicer.addExperimentTags,
          request_deserializer=modeldb_dot_ExperimentService__pb2.AddExperimentTags.FromString,
          response_serializer=modeldb_dot_ExperimentService__pb2.AddExperimentTags.Response.SerializeToString,
      ),
      'getExperimentTags': grpc.unary_unary_rpc_method_handler(
          servicer.getExperimentTags,
          request_deserializer=modeldb_dot_CommonService__pb2.GetTags.FromString,
          response_serializer=modeldb_dot_CommonService__pb2.GetTags.Response.SerializeToString,
      ),
      'deleteExperimentTags': grpc.unary_unary_rpc_method_handler(
          servicer.deleteExperimentTags,
          request_deserializer=modeldb_dot_ExperimentService__pb2.DeleteExperimentTags.FromString,
          response_serializer=modeldb_dot_ExperimentService__pb2.DeleteExperimentTags.Response.SerializeToString,
      ),
      'addExperimentTag': grpc.unary_unary_rpc_method_handler(
          servicer.addExperimentTag,
          request_deserializer=modeldb_dot_ExperimentService__pb2.AddExperimentTag.FromString,
          response_serializer=modeldb_dot_ExperimentService__pb2.AddExperimentTag.Response.SerializeToString,
      ),
      'deleteExperimentTag': grpc.unary_unary_rpc_method_handler(
          servicer.deleteExperimentTag,
          request_deserializer=modeldb_dot_ExperimentService__pb2.DeleteExperimentTag.FromString,
          response_serializer=modeldb_dot_ExperimentService__pb2.DeleteExperimentTag.Response.SerializeToString,
      ),
      'addAttribute': grpc.unary_unary_rpc_method_handler(
          servicer.addAttribute,
          request_deserializer=modeldb_dot_CommonService__pb2.AddAttributes.FromString,
          response_serializer=modeldb_dot_CommonService__pb2.AddAttributes.Response.SerializeToString,
      ),
      'addExperimentAttributes': grpc.unary_unary_rpc_method_handler(
          servicer.addExperimentAttributes,
          request_deserializer=modeldb_dot_ExperimentService__pb2.AddExperimentAttributes.FromString,
          response_serializer=modeldb_dot_ExperimentService__pb2.AddExperimentAttributes.Response.SerializeToString,
      ),
      'getExperimentAttributes': grpc.unary_unary_rpc_method_handler(
          servicer.getExperimentAttributes,
          request_deserializer=modeldb_dot_CommonService__pb2.GetAttributes.FromString,
          response_serializer=modeldb_dot_CommonService__pb2.GetAttributes.Response.SerializeToString,
      ),
      'deleteExperimentAttributes': grpc.unary_unary_rpc_method_handler(
          servicer.deleteExperimentAttributes,
          request_deserializer=modeldb_dot_ExperimentService__pb2.DeleteExperimentAttributes.FromString,
          response_serializer=modeldb_dot_ExperimentService__pb2.DeleteExperimentAttributes.Response.SerializeToString,
      ),
      'logExperimentCodeVersion': grpc.unary_unary_rpc_method_handler(
          servicer.logExperimentCodeVersion,
          request_deserializer=modeldb_dot_ExperimentService__pb2.LogExperimentCodeVersion.FromString,
          response_serializer=modeldb_dot_ExperimentService__pb2.LogExperimentCodeVersion.Response.SerializeToString,
      ),
      'getExperimentCodeVersion': grpc.unary_unary_rpc_method_handler(
          servicer.getExperimentCodeVersion,
          request_deserializer=modeldb_dot_ExperimentService__pb2.GetExperimentCodeVersion.FromString,
          response_serializer=modeldb_dot_ExperimentService__pb2.GetExperimentCodeVersion.Response.SerializeToString,
      ),
      'getExperimentsInProject': grpc.unary_unary_rpc_method_handler(
          servicer.getExperimentsInProject,
          request_deserializer=modeldb_dot_ExperimentService__pb2.GetExperimentsInProject.FromString,
          response_serializer=modeldb_dot_ExperimentService__pb2.GetExperimentsInProject.Response.SerializeToString,
      ),
      'getExperimentById': grpc.unary_unary_rpc_method_handler(
          servicer.getExperimentById,
          request_deserializer=modeldb_dot_ExperimentService__pb2.GetExperimentById.FromString,
          response_serializer=modeldb_dot_ExperimentService__pb2.GetExperimentById.Response.SerializeToString,
      ),
      'getExperimentByName': grpc.unary_unary_rpc_method_handler(
          servicer.getExperimentByName,
          request_deserializer=modeldb_dot_ExperimentService__pb2.GetExperimentByName.FromString,
          response_serializer=modeldb_dot_ExperimentService__pb2.GetExperimentByName.Response.SerializeToString,
      ),
      'deleteExperiment': grpc.unary_unary_rpc_method_handler(
          servicer.deleteExperiment,
          request_deserializer=modeldb_dot_ExperimentService__pb2.DeleteExperiment.FromString,
          response_serializer=modeldb_dot_ExperimentService__pb2.DeleteExperiment.Response.SerializeToString,
      ),
      'getUrlForArtifact': grpc.unary_unary_rpc_method_handler(
          servicer.getUrlForArtifact,
          request_deserializer=modeldb_dot_CommonService__pb2.GetUrlForArtifact.FromString,
          response_serializer=modeldb_dot_CommonService__pb2.GetUrlForArtifact.Response.SerializeToString,
      ),
      'findExperiments': grpc.unary_unary_rpc_method_handler(
          servicer.findExperiments,
          request_deserializer=modeldb_dot_ExperimentService__pb2.FindExperiments.FromString,
          response_serializer=modeldb_dot_ExperimentService__pb2.FindExperiments.Response.SerializeToString,
      ),
      'logArtifacts': grpc.unary_unary_rpc_method_handler(
          servicer.logArtifacts,
          request_deserializer=modeldb_dot_ExperimentService__pb2.LogExperimentArtifacts.FromString,
          response_serializer=modeldb_dot_ExperimentService__pb2.LogExperimentArtifacts.Response.SerializeToString,
      ),
      'getArtifacts': grpc.unary_unary_rpc_method_handler(
          servicer.getArtifacts,
          request_deserializer=modeldb_dot_CommonService__pb2.GetArtifacts.FromString,
          response_serializer=modeldb_dot_CommonService__pb2.GetArtifacts.Response.SerializeToString,
      ),
      'deleteArtifact': grpc.unary_unary_rpc_method_handler(
          servicer.deleteArtifact,
          request_deserializer=modeldb_dot_ExperimentService__pb2.DeleteExperimentArtifact.FromString,
          response_serializer=modeldb_dot_ExperimentService__pb2.DeleteExperimentArtifact.Response.SerializeToString,
      ),
      'deleteExperiments': grpc.unary_unary_rpc_method_handler(
          servicer.deleteExperiments,
          request_deserializer=modeldb_dot_ExperimentService__pb2.DeleteExperiments.FromString,
          response_serializer=modeldb_dot_ExperimentService__pb2.DeleteExperiments.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ai.verta.modeldb.ExperimentService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))