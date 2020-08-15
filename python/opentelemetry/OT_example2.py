
""" OT_example.py

Run with the following:

CMD : pip install opentelemetry-api
CMD : pip install opentelemetry-sdk
CMD : docker run --name jaeger -d --rm -p 16686:16686 -p 6831:6831/udp jaegertracing/all-in-one
In browser : http://localhost:16686/
CMD : pip install opentelemetry-ext-jaeger
CMD : python example2.py
"""
from opentelemetry import trace
from opentelemetry.ext import jaeger
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor

trace.set_tracer_provider(TracerProvider())

jaeger_exporter = jaeger.JaegerSpanExporter(
    service_name="example2-service",
    agent_host_name="localhost",
    agent_port=6831,
)

trace.get_tracer_provider().add_span_processor(
    BatchExportSpanProcessor(jaeger_exporter)
)

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("foo"):
    with tracer.start_as_current_span("bar"):
        with tracer.start_as_current_span("baz"):
            print("Hello world from OpenTelemetry Python!")