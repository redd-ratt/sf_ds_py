"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict_number = 0
    while count < 21:        
        try_lst = [20, 40, 60, 80, 100]
        for i in try_lst:
            count += 1
            predict_number = i
            
            if predict_number < number:
                
                continue
            elif predict_number > number:    
                count += 1
                predict_number = i-10
                 
                if predict_number < number:
                    while True:
                        count += 1
                        predict_number += 1
                        
                        if predict_number == number:
                            return count
                if predict_number > number:
                    while True:
                        count += 1
                        predict_number -= 1
                        if predict_number == number:
                            return count
            else:
                 return count
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    

    for number in random_array:
        
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return None 


