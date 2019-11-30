
#price_with_discount = int(price - (int(price) * int(discount) / 100)


def discounted (price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except (ValueError):
        print ('Введена строка')
        return -1
         
p=discounted (100,"sasdf",30)
print(p)

