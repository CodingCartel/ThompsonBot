

class Post:
    def __init__(self, url: str):
        self.url = url

    def get(self) -> tuple[str, str]:
        """
        TO DO.
        Send a request to self.url to get the contents of the post.
        """
        # return "<post contents>", "https://.../img.png"


# return True upon success, False upon failure. Set last error depending on the nature of the error:

def send_message(msg: str) -> bool: ...


# return the post's url upon success, None upon failure. Set last error depending on the nature of the error:

def get_last_post() -> Post | None:
    # return Post('https://.../post')
    ...

