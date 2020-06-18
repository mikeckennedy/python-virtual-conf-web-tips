

#################################################################
# See the documentation on secure.py here.
# This is their suggested integration
# https://secure.readthedocs.io/en/latest/frameworks.html#pyramid
#
def set_secure_headers(handler, registry):
    import secure
    secure_headers = secure.SecureHeaders()

    def tween(request):
        response = handler(request)
        secure_headers.pyramid(response)
        return response

    return tween
