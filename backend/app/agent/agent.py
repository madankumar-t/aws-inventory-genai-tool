from app.agent.intent import extract_intent
from app.aws.router import route_request
from app.analysis.topology import build_topology
from app.agent.summarizer import summarize
from app.agent.views import build_view

def run_agent(prompt: str, view: str = "filtered"):

    intent = extract_intent(prompt)
    raw_data = route_request(intent)

    return {
        "summary": summarize(raw_data),
        "topology": build_topology(raw_data),
        "data": build_view(raw_data, view)
    }
