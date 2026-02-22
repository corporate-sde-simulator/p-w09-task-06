import pytest, os, re

class TestDockerConfig:
    @pytest.fixture
    def dockerfile(self):
        path = os.path.join(os.path.dirname(__file__), '..', 'src', 'Dockerfile')
        with open(path) as f: return f.read()

    @pytest.fixture
    def compose(self):
        path = os.path.join(os.path.dirname(__file__), '..', 'src', 'docker-compose.yml')
        with open(path) as f: return f.read()

    def test_no_latest_tag(self, dockerfile):
        assert 'python:latest' not in dockerfile, "Don't use :latest tag"

    def test_non_root_user(self, dockerfile):
        assert 'USER' in dockerfile, "Should run as non-root user"

    def test_healthcheck(self, dockerfile):
        assert 'HEALTHCHECK' in dockerfile, "Missing health check"

    def test_port_mapping(self, compose):
        assert '3000:8080' in compose or '8080:8080' in compose, "Port mapping incorrect"
