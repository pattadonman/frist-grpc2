import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    # Connect to the gRPC server
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        # Call the Add method
        response = stub.Add(calculator_pb2.AddRequest(num1=5, num2=7))
        print(f"Result: {response.result}")

if __name__ == "__main__":
    run()
