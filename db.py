import redis


class RedisConnector:
    conn = redis.StrictRedis(host='0.0.0.0',
                             decode_responses=True)

    def write_role(self, role):
        self.conn.rpush("roles", role)

    def get_all_roles(self):
        return self.conn.lrange("roles", 0, -1)
