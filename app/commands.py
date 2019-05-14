import click

from app import app, db
from app.models import TestCase


@app.cli.command()
@click.option('--drop', is_flag=True, help='Drop tables and create.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        click.confirm('This operation will delete the database, \
            do you want to continue?', abort=True)
        db.drop_all()
        click.echo('Drop tables.')
    db.create_all()
    click.echo('Initialized database.')


@app.cli.command()
@click.option('--count', default=20, help='Quantity of data, default is 20.')
def forge(count):
    """Generate fake data."""
    from faker import Faker

    db.drop_all()
    db.create_all()

    fake = Faker()

    click.echo('Create fake data in test_case table...')
    for i in range(count):
        message = TestCase(
            file_name="fakename" + str(i),
            author=fake.name(),
            create_date=fake.date_time(),
            last_update_by=fake.name(),
            last_update_time=fake.date_time_this_year(),
            file_path="filepath" + str(i)
        )
        db.session.add(message)

    db.session.commit()
    click.echo('Created %d fake messages.' % count)
