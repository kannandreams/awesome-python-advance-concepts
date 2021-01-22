from abc import ABCMeta
from abc import abstractmethod

class SocialMedia:
    """ Social Media Platform Interface """

    @abstractmethod
    def like(self):
        pass

    @abstractmethod
    def comment(self):
        pass

    @abstractmethod
    def post(self):
        pass

    
class Facebook(SocialMedia):
    def __init__(self,messsage):
        self.message = messsage
    
    def like(self):
        return 'Facebook likes'

    def comment(self):
        return 'Facebook comments'

    def post(self):
        return 'Facebook post'

class Instagram(SocialMedia):
    def __init__(self,messsage):
        self.message = messsage
    
    def like(self):
        return 'Instagram likes'

    def comment(self):
        return 'Instagram comments'

    def post(self):
        return 'Instagram Image post'

class PlatformCreator:
    def __init__(self):
        self.platform = self._factory_method()

    @abstractmethod
    def _factory_method(self):
        pass

class FacebookCreator(PlatformCreator):
    def _factory_method(self):
        return Facebook('Welcome to FB')

class InstagramCreator(PlatformCreator):
    def _factory_method(self):
        return Instagram('Welcome to Instagram')

# class SocialMediaFactory:
#     def create_platform(self,name):
#         if name == 'facebook':
#             return Facebook("Welcome to FB")
#         elif name == 'instagram':
#             return Instagram("Welcome to Instagram")


def main():
    name = input("Enter the platform: ")
    if name == 'facebook':
        creator = FacebookCreator()
    elif name == 'instagram':
        creator = InstagramCreator()   
    print(f"The type of platform created: {type(creator.platform)}")
    print(f"{creator.platform.message}")
    print(f"From {name} , you get many  {creator.platform.like()}")


if __name__ == "__main__":
    main()