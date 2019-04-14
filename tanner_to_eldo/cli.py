import click


@click.command()
@click.argument("input", type=click.File("r"))
@click.argument("output", type=click.File("w"))
def cli(input, output):
    """
    This script converts from tanner to eldo spice format.

    `tanner_to_eldo input_file.spc output_file.spc`
    """
    output.write(f"{80 * '*'}\n")
    output.write("* Converted using tanner_to_eldo.\n")
    output.write(f"{80 * '*'}\n")

    for line in input.readlines():
        if "$" in line:
            line = f"{line.split('$')[0]}\n"

        elif ".probe" in line:
            line = ".option probe\n.option post\n"
        elif ".option probe" in line:
            line = ""

        output.write(line)


if __name__ == "__main__":
    cli()
