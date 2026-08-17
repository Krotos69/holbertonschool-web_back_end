#!/usr/bin/env python3
""" moduele for finding schools by topic."""


def schools_by_topic(mongo_collection, topic):
    """Return list of schools having the given topic."""
    return list(mongo_collection.find({"topics": topic}))

