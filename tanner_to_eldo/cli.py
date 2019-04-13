import click


@click.command()
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
def cli(input, output):
    """
    This script converts from tanner to mentor spice format.

    `tanner_to_mentor input_file.spc output_file.spc`
    """
    for line in input.readlines():
        output.write(line)


if __name__ == "__main__":
    cli()
