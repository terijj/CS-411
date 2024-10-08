from wildlife_tracker.migration_tracking.migration import Migration
from wildlife_tracker.migration_tracking.migration_path import MigrationPath

class MigrationManager:
    def __init__(self) -> None:
        self.migrations: Dict[int, Migration] = {}
        self.paths: Dict[int, MigrationPath] = {}

    def register_migration(self, migration: Migration) -> None:
        self.migrations[migration.migration_id] = migration

    def get_migration_by_id(self, migration_id: int) -> Optional[Migration]:
        return self.migrations.get(migration_id)

    def remove_migration(self, migration_id: int) -> None:
        if migration_id in self.migrations:
            del self.migrations[migration_id]

    def schedule_migration(self, migration_id: int, path_id: int) -> None:
        migration = self.get_migration_by_id(migration_id)
        path = self.paths.get(path_id)
        if migration and path:
            migration.schedule(path)

    def cancel_migration(self, migration_id: int) -> None:
        migration = self.get_migration_by_id(migration_id)
        if migration:
            migration.cancel()

    def register_migration_path(self, path: MigrationPath) -> None:
        self.paths[path.path_id] = path

    def get_migration_path_by_id(self, path_id: int) -> Optional[MigrationPath]:
        return self.paths.get(path_id)

    def update_migration_details(self, migration_id: int, **kwargs) -> None:
        migration = self.get_migration_by_id(migration_id)
        if migration:
            migration.update_migration_details(**kwargs)
