#!/usr/bin/env python
"""Operate on the taskgraph."""


def get_decision_task_id(task):
    """Given a task dict, return the decision `taskId`.

    This also accepts the return status dict from both `claimTask` and
    `reclaimTask`.

    Args:
        task (dict): the task dict.

    Returns:
        str: the decision `taskId`.

    """
    return task['taskGroupId']
