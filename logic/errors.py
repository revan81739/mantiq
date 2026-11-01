class MantiqError(Exception):
    pass

def format_error(error):
    message=str(error)
    return f"""
ERROR
-----
{message}
-----
Please check your punch card format

You can try an example from the Punch Card Library
or refer to the project README.
"""
