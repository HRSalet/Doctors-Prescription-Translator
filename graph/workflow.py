from typing import TypedDict
from langgraph.graph import StateGraph, END
from agents.ocr_cleanup_agent import cleanup_prescription
from agents.medicine_agent import extract_medicines

class PrescriptionState(TypedDict):
    raw_text: str
    cleaned_text: str
    medicines: str

def cleanup_node(state):
    cleaned = cleanup_prescription(
        state["raw_text"]
    )

    return {
        "cleaned_text": cleaned
    }

def medicine_node(state):

    meds = extract_medicines(
        state["cleaned_text"]
    )

    return {
        "medicines": meds
    }

workflow = StateGraph(PrescriptionState)

workflow.add_node("cleanup", cleanup_node)
workflow.add_node("medicine", medicine_node)

workflow.set_entry_point("cleanup")
workflow.add_edge("cleanup", "medicine")
workflow.add_edge("medicine", END)

app = workflow.compile()