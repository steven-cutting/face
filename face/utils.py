
def format_invocation(name='', args=(), kwargs=None):
    kwargs = kwargs or {}
    a_text = ', '.join([repr(a) for a in args])
    kw_text = ', '.join(['%s=%r' % (k, v) for k, v in kwargs.items()])

    star_args_text = a_text
    if star_args_text and kw_text:
        star_args_text += ', '
    star_args_text += kw_text

    return '%s(%s)' % (name, star_args_text)