# DEVTOOLS-104: Fix Broken Docker Configuration

**Status:** In Progress · **Priority:** High
**Sprint:** Sprint 30 · **Story Points:** 5
**Reporter:** Mike Chen (DevOps) · **Assignee:** You (Intern)
**Labels:** `docker`, `devops`, `containers`, `maintenance`
**Task Type:** Maintenance

---

## Description

Our microservice Docker setup stopped working after a base image update. The app
builds but fails at runtime. The `Dockerfile` and `docker-compose.yml` have
several issues flagged with `# TODO (code review):` markers.

## Issues Found in Code Review

1. Using `latest` tag (non-reproducible builds)
2. Running as root (security risk)
3. Not using multi-stage build (image is 1.2GB instead of ~200MB)
4. Missing health check
5. docker-compose port mappings and volume mounts are wrong

## Acceptance Criteria

- [ ] Dockerfile uses specific base image version
- [ ] App runs as non-root user
- [ ] Multi-stage build reduces image size
- [ ] Health check is configured
- [ ] docker-compose ports and volumes are correct
- [ ] All tests pass
