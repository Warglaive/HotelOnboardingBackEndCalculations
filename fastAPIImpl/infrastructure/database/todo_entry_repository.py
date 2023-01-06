from tempfile import TemporaryDirectory

from container import ApplicationContainer
from domain.exampleObj import TodoEntry


class TodoEntryPickleRepository:
    import pytest as pytest
    from infrastructure.database.todo_entry_repository import TodoEntryPickleRepository

    @pytest.fixture()
    def repository(self):
        with TemporaryDirectory() as tmp_dir:
            container = ApplicationContainer()

            container.configuration.storage_dir.from_value(tmp_dir)
            yield container.todo_entry_repository()

    def test_add_and_get(self: TodoEntryPickleRepository):
        entry = TodoEntry.create_from_content("test")
        self.add(entry)
        assert entry == self.get(entry.id)

    def get(self, new_id):
        pass

    def add(self, entry):
        pass
