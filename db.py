import redis


class RedisConnector:
    conn = redis.StrictRedis(host='redis',
                             decode_responses=True)

    def write_role(self, role):
        self.conn.rpush("roles", role)

    def get_all_roles(self):
        return self.conn.lrange("roles", 0, -1)

    def add_source(self, role, source: list):
        for el in source:
            self.conn.rpush(f"{role}_source", str({el.get("name"): el.get("url")}))

    def get_source(self, role):
        return self.conn.lrange(f"{role}_source", 0, -1)
