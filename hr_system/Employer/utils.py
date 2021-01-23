import redis
import json

from django.http import JsonResponse

from hr_system import settings

redis = redis.StrictRedis(port=settings.REDIS_PORT, host=settings.REDIS_HOST, db=0)


class Redis:
    def set(cache_key, data):
        # data = list(data)
        data = json.dumps(data)
        # data = str(data)
        print('inside set')
        redis.set(cache_key, data)
        return True

    def get(cache_key):
        print('before get')
        cache_data = redis.get(cache_key)
        print('after get')
        if cache_data:
            print('inside cached data')
            #cache_data = cache_data.decode("utf-8")
            #cache_data = cache_data.decode("'", "\"")
            cache_data = json.loads(cache_data)
            return JsonResponse(cache_data, safe=False)

        return None
