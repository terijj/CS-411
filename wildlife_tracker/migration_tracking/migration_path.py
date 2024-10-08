from typing import Any

class MigrationPath:
    def __init__(self, path_id: int, species: str, start_habitat_id: int, end_habitat_id: int, duration: int) -> None:
        self.path_id = path_id
        self.species = species
        self.start_habitat_id = start_habitat_id
        self.end_habitat_id = end_habitat_id
        self.duration = duration

    def update_migration_path_details(self, **kwargs: Any) -> None:
        pass
