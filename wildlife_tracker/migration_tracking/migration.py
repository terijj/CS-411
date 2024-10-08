from wildlife_tracker.migration_tracking.migration_path import MigrationPath

class Migration:
    def __init__(self, migration_id: int, details: Any = None) -> None:
        self.migration_id = migration_id
        self.details = details

    def schedule(self, path: 'MigrationPath') -> None:
        pass

    def cancel(self) -> None:
        pass

    def update_migration_details(self, **kwargs: Any) -> None:
        pass
