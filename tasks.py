from invoke import task

@task
def start(ctx):
    ctx.run("poetry run python3 src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("poetry run pytest src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def lint(ctx):
    ctx.run("poetry run pylint src", pty=True)

@task
def format(ctx):
    ctx.run("poetry run autopep8 --in-place --recursive src", pty=True)