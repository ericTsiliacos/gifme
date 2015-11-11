def build_gif_url(search):
    if search is not None:
        return "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=%s" % search
    else:
        return "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC"
