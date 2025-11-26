import shutil

from refedez.common.config import get_refedez_config_from_yaml
from refedez.common.errors import InvalidStateError
from refedez.common.project import ReFedEzProject
from refedez.common.state import Dirty


def clean(path: str):
    configuration = get_refedez_config_from_yaml(path=path)
    refedez_project = ReFedEzProject(config=configuration)
    refedez_state = refedez_project.project_state
    match refedez_state.state:
        case Dirty():
            shutil.rmtree(refedez_project.project_folder)
            pass
        case _:
            raise InvalidStateError()
