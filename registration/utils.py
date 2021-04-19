import string
import random

def random_string_generator(size=5,chars=string.ascii_uppercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_entry_pass_generator(instance):
    new_entry_pass = random_string_generator()
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(entry_pass = new_entry_pass).exists()
    if qs_exists:
        return unique_entry_pass_generator(instance)
    return new_entry_pass