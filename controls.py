def get_global_variables():
    global_vars = globals().copy()
    exclude_keys = list(__builtins__.__dict__.keys()) + [
        "get_global_variables",
        "main",
        "__builtins__",
    ]
    filtered_globals = {
        k: v
        for k, v in global_vars.items()
        if k not in exclude_keys and not k.startswith("__")
    }
    return filtered_globals


def main():
    # Main function can be used for other logic
    print("Global Variables:")
    global_vars = get_global_variables()
    for name, value in global_vars.items():
        print(f"{name}: {value}")


# Example global variables
global_var1 = 10
global_var2 = "hello"
global_var3 = [1, 2, 3]
global_var4 = {"key": "value"}

if __name__ == "__main__":
    main()
