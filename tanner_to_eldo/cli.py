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
    output.write("v_gnd 0 gnd 0\n")
    params = []

    for line in input.readlines():
        if line.sartswith("*"):
            # Don't process commented lines
            pass

        elif "$" in line:
            # remove unsupported comments
            line = f"{line.split('$')[0]}\n"

        elif line.startswith(".probe"):
            line = ".option probe\n.option post\n"

        elif line.startswith(".option probe"):
            line = ""

        elif line.startswith(".param"):
            params.append(line.split()[1])

        elif line.startswith(".dc"):
            _, sweep_object, start, end, n_points = line.split()
            if sweep_object in params:
                sweep_object = f"param {sweep_object}"
            step = (float(end) - float(start)) / (float(n_points) - 1)
            line = f".dc {sweep_object} {start} {end} {step}"

        output.write(line)


if __name__ == "__main__":
    cli()
