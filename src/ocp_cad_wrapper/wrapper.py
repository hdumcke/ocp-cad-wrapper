import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import click
from build123d import *
from ocp_vscode import *
from importlib import reload


class SingleFileEventHandler(FileSystemEventHandler):
    def __init__(self, filepath):
        self.filepath = os.path.abspath(filepath)

    def on_modified(self, event):
        global is_modified
        if os.path.abspath(event.src_path) == self.filepath:
            is_modified = True


def watch_file(file_path):
    directory = os.path.dirname(os.path.abspath(file_path))
    event_handler = SingleFileEventHandler(file_path)
    observer = Observer()
    observer.schedule(event_handler, path=directory, recursive=False)
    observer.start()

    try:
        while True:
            global is_modified
            global b123d
            if is_modified:
                is_modified = False
                try:
                    b123d = reload(b123d)
                except Exception as e: print(e)
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


@click.command()
@click.argument('filename')
def run(filename):
    global is_modified
    global b123d
    is_modified = False
    dir_name = os.path.dirname(os.path.expanduser(filename))
    sys.path.insert(0, dir_name)
    file_name = os.path.splitext(os.path.basename(filename))[0]
    b123d = __import__(file_name)
    watch_file(filename)
