from concurrent import futures
import grpc
import calculator_pb2
import calculator_pb2_grpc

# Implement the Calculator service
class CalculatorService(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        # Perform addition
        result = request.num1 + request.num2
        return calculator_pb2.AddResponse(result=result)

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorService(), server)
    server.add_insecure_port('[::]:50051')
    print("Server running on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
