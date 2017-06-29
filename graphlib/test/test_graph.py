import graphlib.graph as graph

def test_get_decision_task_id():
    assert graph.get_decision_task_id({"taskGroupId": "asdf"}) == "asdf"
