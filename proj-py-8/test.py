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
            print(predict_number) 
            if predict_number < number:
                print('число попыток: ', count) 
                continue
            elif predict_number > number:    
                count += 1
                predict_number = i-10
                print(predict_number) 
                if predict_number < number:
                    while True:
                        count += 1
                        predict_number += 1
                        print('число попыток: ', count)
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
                                                                       
    
    

print(random_predict(1))