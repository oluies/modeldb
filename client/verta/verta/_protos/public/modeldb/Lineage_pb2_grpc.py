# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from ..modeldb import Lineage_pb2 as modeldb_dot_Lineage__pb2


class LineageServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.addLineage = channel.unary_unary(
        '/ai.verta.modeldb.LineageService/addLineage',
        request_serializer=modeldb_dot_Lineage__pb2.AddLineage.SerializeToString,
        response_deserializer=modeldb_dot_Lineage__pb2.AddLineage.Response.FromString,
        )
    self.deleteLineage = channel.unary_unary(
        '/ai.verta.modeldb.LineageService/deleteLineage',
        request_serializer=modeldb_dot_Lineage__pb2.DeleteLineage.SerializeToString,
        response_deserializer=modeldb_dot_Lineage__pb2.DeleteLineage.Response.FromString,
        )
    self.findAllInputs = channel.unary_unary(
        '/ai.verta.modeldb.LineageService/findAllInputs',
        request_serializer=modeldb_dot_Lineage__pb2.FindAllInputs.SerializeToString,
        response_deserializer=modeldb_dot_Lineage__pb2.FindAllInputs.Response.FromString,
        )
    self.findAllOutputs = channel.unary_unary(
        '/ai.verta.modeldb.LineageService/findAllOutputs',
        request_serializer=modeldb_dot_Lineage__pb2.FindAllOutputs.SerializeToString,
        response_deserializer=modeldb_dot_Lineage__pb2.FindAllOutputs.Response.FromString,
        )
    self.findAllInputsOutputs = channel.unary_unary(
        '/ai.verta.modeldb.LineageService/findAllInputsOutputs',
        request_serializer=modeldb_dot_Lineage__pb2.FindAllInputsOutputs.SerializeToString,
        response_deserializer=modeldb_dot_Lineage__pb2.FindAllInputsOutputs.Response.FromString,
        )


class LineageServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def addLineage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteLineage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def findAllInputs(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def findAllOutputs(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def findAllInputsOutputs(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LineageServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'addLineage': grpc.unary_unary_rpc_method_handler(
          servicer.addLineage,
          request_deserializer=modeldb_dot_Lineage__pb2.AddLineage.FromString,
          response_serializer=modeldb_dot_Lineage__pb2.AddLineage.Response.SerializeToString,
      ),
      'deleteLineage': grpc.unary_unary_rpc_method_handler(
          servicer.deleteLineage,
          request_deserializer=modeldb_dot_Lineage__pb2.DeleteLineage.FromString,
          response_serializer=modeldb_dot_Lineage__pb2.DeleteLineage.Response.SerializeToString,
      ),
      'findAllInputs': grpc.unary_unary_rpc_method_handler(
          servicer.findAllInputs,
          request_deserializer=modeldb_dot_Lineage__pb2.FindAllInputs.FromString,
          response_serializer=modeldb_dot_Lineage__pb2.FindAllInputs.Response.SerializeToString,
      ),
      'findAllOutputs': grpc.unary_unary_rpc_method_handler(
          servicer.findAllOutputs,
          request_deserializer=modeldb_dot_Lineage__pb2.FindAllOutputs.FromString,
          response_serializer=modeldb_dot_Lineage__pb2.FindAllOutputs.Response.SerializeToString,
      ),
      'findAllInputsOutputs': grpc.unary_unary_rpc_method_handler(
          servicer.findAllInputsOutputs,
          request_deserializer=modeldb_dot_Lineage__pb2.FindAllInputsOutputs.FromString,
          response_serializer=modeldb_dot_Lineage__pb2.FindAllInputsOutputs.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ai.verta.modeldb.LineageService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))