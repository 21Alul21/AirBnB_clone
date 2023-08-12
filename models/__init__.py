#!/usr/bin/python3
"""
constructor for the models package
is serves as default module initialiser
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
