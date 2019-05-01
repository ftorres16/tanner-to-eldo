import click


@click.command()
@click.argument("input", type=click.File("r"))
@click.argument("output", type=click.File("w"))
@click.option("--pdk", type=click.Path(), envvar="CONVERTER_PDK")
@click.option("--pdk-options", envvar="CONVERTER_PDK_OPTIONS")
def cli(input, output, pdk, pdk_options):
    """
    This script converts from tanner to eldo spice format.

    `tanner_to_eldo input_file.spc output_file.spc`
    """
    output.write(f"{80 * '*'}\n")
    output.write("* Converted using tanner_to_eldo.\n")
    output.write(f"{80 * '*'}\n")

    if pdk:
        output.write(f".lib \"{pdk}\" {pdk_options or ''}\n")

    # Short 0 node with gnd node
    output.write("v_gnd 0 gnd 0")

    for line in input.readlines():
        if line[0] == "*":
            # Don't process commented lines
            pass

        elif "$" in line:
            # remove unsupported comments
            line = f"{line.split('$')[0]}\n"

        elif ".probe" in line:
            line = ".option probe\n.option post\n"
        elif ".option probe" in line:
            line = ""

        output.write(line)


if __name__ == "__main__":
    cli()
