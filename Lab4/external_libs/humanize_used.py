import humanize

def humanize_used():  # Розділяє велике число комами для зручного читання
    return humanize.intcomma(1000000)
