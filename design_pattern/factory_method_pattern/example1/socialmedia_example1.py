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

class SocialMediaFactory:
    def create_platform(self,name):
        if name == 'facebook':
            return Facebook("Welcome to FB")
        elif name == 'instagram':
            return Instagram("Welcome to Instagram")


def main():
    factory = SocialMediaFactory()
    platform_name = input("Enter the platform: ")

    platform = factory.create_platform(platform_name)

    print(f"The type of platform created: {type(platform)}")
    print(f"{platform.message}")
    print(f"From {platform_name} , you get many  {platform.like()}")


if __name__ == "__main__":
    main()