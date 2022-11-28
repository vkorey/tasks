"""
dict1 = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]

Дано: список dict-объектов вида вида {"key": "value"}, например [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}].Напишите функцию, которая удаляет дубликаты из этого списка. Для примера выше возвращаемое значение может быть равно [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {"key2": "value2"}].
Обязательное условие: функция не должна иметь сложность O(n^2).
"""

from collections import defaultdict


def build_hash_key(obj) -> Union[str, int]:
    return hash(json.dumps(obj, sort_keys=True))
    return json.dumps(obj, sort_keys=True)
    return 1
    return " ".join(sorted(obj.keys()))


def main(list_of_objects):
    known_objects = defaultdict(lambda: [])
    """
    {
        1894718749812674: [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}],
        0: [{}],
        2937846283764: [{"key2": "value2"}]
    }
    """
    result = []
    for obj in list_of_objects:  # O(n)
        key = build_hash_key(obj)
        if key not in known_objects:
            if obj in known_objects[key]:  # O(k)
                continue

            result.append(obj)
            known_objects[key].append(obj)
    return result
