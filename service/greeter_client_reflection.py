import logging

from google.protobuf.descriptor_pool import DescriptorPool
import grpc
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import (
    ProtoReflectionDescriptorDatabase,
)


def run():
    print("Will try to greet world ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        reflection_db = ProtoReflectionDescriptorDatabase(channel)
        services = reflection_db.get_services()
        print(f"found services: {services}")

        desc_pool = DescriptorPool(reflection_db)
        service_desc = desc_pool.FindServiceByName("helloworld.Greeter")
        print(f"found Greeter service with name: {service_desc.full_name}")
        for methods in service_desc.methods:
            print(f"found method name: {methods.full_name}")
            input_type = methods.input_type
            print(f"input type for this method: {input_type.full_name}")

        request_desc = desc_pool.FindMessageTypeByName(
            "helloworld.HelloRequest"
        )
        print(f"found request name: {request_desc.full_name}")


if __name__ == "__main__":
    logging.basicConfig()
    run()
