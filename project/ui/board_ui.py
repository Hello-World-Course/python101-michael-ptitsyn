def parse_cmd(command: str):
    cmd, *args = command.split(" ")
    return cmd, args