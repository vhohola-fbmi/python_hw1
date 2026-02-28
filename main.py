# імпортуємо numpy
import numpy as np

# створюємо випадковий масив 3 х 3
arr = np.random.randint(1, 101, size=(3, 3))

# знаходимо суму всіх елементів
total_arr = np.sum(arr)

# знаходимо максимальний та мінімальний елементи масиву
arr_max = np.max(arr)
arr_min = np.min(arr)

# знаходимо їх індекси
arr_max_ind = np.argmax(arr)
arr_min_ind = np.argmin(arr)

# сортуємо масив по рядках
arr_sort = np.sort(arr, axis=1)

# виводимо знайдені результати
print(f'Випадковий масив: \n{arr}')
print(f'Сума всіх елементів в масиві: {total_arr}')
print(f'Найбільший елемент масиву: {arr_max}, його індекс: {arr_max_ind}')
print(f'Найменший елемент масиву: {arr_min}, його індекс: {arr_min_ind}')
print(f'Відсортований по рядках масив: \n{arr_sort}')