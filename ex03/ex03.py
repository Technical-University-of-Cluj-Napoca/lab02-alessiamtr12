import os
from _datetime import datetime

COLORS = {
    "info": "\033[94m",    # blue
    "debug": "\033[90m",   # gray
    "warning": "\033[93m", # yellow
    "error": "\033[91m",   # red
    "reset": "\033[0m"      # reset
}
def smart_log(*args, **kwargs) -> None:

    level = kwargs.get("level", "info")
    show_timestamp = kwargs.get("timestamp", True)
    show_date = kwargs.get("date", False)
    save_to_file = kwargs.get("save_to", None)
    color = kwargs.get("color", True)

    message = " ".join(str(arg) for arg in args)

    time_now = datetime.now()
    prefix = []
    if show_timestamp:
        prefix.append(time_now.strftime("%H:%M:%S"))
    if show_date:
        prefix.append(time_now.strftime("%Y-%m-%d"))

    prefix_str = " ".join(prefix)
    if prefix_str:
        prefix_str += " "
    level_str = f"[{level.upper()}]"
    color_start = ""
    color_end = ""
    if color:
        color_start = COLORS.get(level, "")
        if color_start:
            color_end = COLORS["reset"]
    output = f"{color_start}{prefix_str}{level_str} {message}{color_end}"
    print(output)

    file_output = f"{prefix_str}{level_str} {message}"

    if save_to_file:
        dir = os.path.dirname(save_to_file)
        if dir:
            os.makedirs(dir, exist_ok=True)
            with open(save_to_file, "a") as f:
                f.write(file_output + "\n")




if __name__ == "__main__":
    smart_log("System started successfully.", level="info")
    smart_log("User", "alice", "logged in", level="debug")
    smart_log("Low disk space detected!", level="warning")
    smart_log("Model training failed!", level="error", save_to="logs/errors.log")
    smart_log("Process end", level="info", color=False, save_to="logs/errors.log")