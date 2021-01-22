#Simple Factory Pattern

from abc import ABCMeta
from abc import abstractmethod

class SocialMedia:
    """ Social Media Platform Interface """

    @abstractmethod
    def like(self):
        raise NotImplementedError()

    @abstractmethod
    def comment(self):
        raise NotImplementedError()

    @abstractmethod
    def post(self):
        raise NotImplementedError()

    
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
    platforms = dict(facebook=Facebook('Welcome to FB'),
    instagram=Instagram('Welcome to Instagram')
    )

    @classmethod
    def get_platform(cls,name):
        if name not in cls.platforms:
            raise AssertionError('Invalid input')
        return cls.platforms.get(name)


def main():
    
    platform_name = input("Enter the platform: ")
    platform = SocialMediaFactory.get_platform(platform_name)

    print(f"The type of platform created: {type(platform)}")
    print(f"{platform.message}")
    print(f"From {platform_name} , you get many  {platform.like()}")


if __name__ == "__main__":
    main()