from typing import List, Tuple

from src.core.interfaces.repository.enum.interface import IEnumRepository
from src.repository.base_repository.cache.repository import CacheRepository
from src.repository.base_repository.oracle.repository import OracleBaseRepository


class EnumRepository(IEnumRepository):

    database = OracleBaseRepository
    cache_database = CacheRepository

    enum_query = """
            SELECT SG_PAIS as initials, NM_PAIS as description
            FROM CORRWIN.TSCPAIS
        """
    enum_key = "EnumCountry"

    @classmethod
    def get_enums(cls) -> List[Tuple]:
        sql = cls.enum_query
        result = cls._get_cached_enum(sql)
        return result

    @classmethod
    def _get_cached_enum(cls, query: str) -> List[Tuple]:
        if cached_enum := cls.cache_database.get_from_cache(cls.enum_key):
            return cached_enum

        enum_values = cls.database.query(sql=query)
        cls.cache_database.save_in_cache(cls.enum_key, enum_values)
        return enum_values
