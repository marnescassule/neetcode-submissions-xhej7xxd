from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict(list) cria automaticamente uma lista vazia se a chave não existir
        hash_result = defaultdict(list)
        
        for s in strs:
            # Ordena a string atual. Ex: "tea" -> ['a', 'e', 't']
            # Precisamos converter para tuple, pois listas não podem ser chaves de dicionário
            sorted_s = tuple(sorted(s))
            
            # Adiciona a string original na lista correspondente à chave ordenada
            hash_result[sorted_s].append(s)
            
        # Retorna apenas os valores (as listas de anagramas agrupados)
        return list(hash_result.values())