#Сортировка массива методом Шелла

import numpy as np


# Заполняем массив случайными числами

arr = np.random.randint(0, 20, 10)

print("Array before Shell sort: ")
print(arr)



# /* shellsort: сортируются v[0] ... v[n-1] в возрастающем порядке */
# void shellsort (int v[], int n)
# {
# int gap, i, j, temp;
# for (gap = n/2; gap > 0; gap /= 2)
# for (i = gap; i < n; i++)
# for (j = i - gap; j >= 0 && v[j] > v[j + gap]; j -= gap) {
# temp = v[j];
# v[j] = v[j + gap];
# v[j + gap] = temp;
# }
# }

lenArray = (len(arr))

for gap in arr:
    print(gap)



print("Array after:")
print(arr)