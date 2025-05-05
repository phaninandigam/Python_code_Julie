def format_name(f_name, l_name):
    """Convert name into Typecase""" #doc string
    converted_f_name = f_name.title()
    converted_l_name = l_name.title()
    print(f"fortma_name function output {converted_f_name, converted_l_name}")
    return f"{converted_f_name} {converted_l_name}"


print(format_name("angela", "yu"))
format_name