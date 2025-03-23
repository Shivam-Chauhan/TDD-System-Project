import re

class StringCalculator:
    """
        Main class having the crux of the project.
        Handling various possibility using Regex.
        If negative values are there in input, raising value error.
    """
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        
        delimiters = [',', '\n']
        
        if numbers.startswith("//"):
            header, numbers = numbers.split("\n", 1)
            delimiters.extend(re.findall(r"\[(.*?)\]", header) or [header[2:]])
        
        numbers = re.split("|".join(map(re.escape, delimiters)), numbers)
        
        num_list = [int(num) for num in numbers if num and int(num) <= 1000]
        negatives = [num for num in num_list if num < 0]
        
        if negatives:
            raise ValueError(f"Negatives not allowed: {negatives}")
        
        return sum(num_list)
    
