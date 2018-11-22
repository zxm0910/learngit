import orm
import asyncio
from models import User, Blog, Comment

'''
def test():
    yield from orm.create_pool(1, user='www-data', password='www-data', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()
'''


async def test(loop):
    await orm.create_pool(loop=loop, user='www-data', password='www-data', database='awesome')
    u = User(name='张晓旻', email='17916603@qq.com', passwd='123456', image='about:blank')
    await u.save()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
#   loop.run_forever()

