choice = input('Menu\n1. Con una semilla\n2. Con dos semillas')


if choice == '1':
    amount = int(input('Ingrese la cantidad de numeros que quiere: '))

    seed = int(input('Ingrese la semilla de cuatro digitos: '))

    numbers = []

    if amount > 0 and len(str(seed)) == 4:
        for i in range(amount):
            powered_seed = pow(seed, 2)
            if len(str(powered_seed)) < 8:
                powered_seed = f"0{powered_seed}"

            seed = str(powered_seed)[2:]

            n_seed = ''
            for e, n in enumerate(str(seed)):
                if e == 4:
                    break

                n_seed += n

            if n_seed == '0000':
                raise Exception('Invalid seed!')

            seed = int(n_seed)

            numbers.append(float(f"0.{seed}"))

    print(numbers)

elif choice == '2':
    amount = int(input('Ingrese la cantidad de numeros que desea generar: '))+1

    seed1 = int(input('Ingrese la primera semilla: '))
    seed2 = int(input('Ingrese la segunda semilla: '))

    if len(str(seed1)) == len(str(seed2)):
        numbers = []

        for i in range(amount):
            mult_result = str(seed1*seed2)

            eliminated_nums = len(mult_result) - len(str(seed1))
            while eliminated_nums % 2 != 0:
                mult_result = mult_result[::-1]
                mult_result += '0'
                mult_result = mult_result[::-1]
                eliminated_nums = len(mult_result) - len(str(seed1))

            edges = eliminated_nums/2

            n_seed = ''
            for e, n in enumerate(mult_result):

                if e == len(str(seed1))+edges:
                    break

                if e < edges:
                    continue

                n_seed += n

            seed1 = seed2
            seed2 = int(n_seed)

            numbers.append(float(f"0.{seed1}"))

        numbers.reverse()
        numbers.pop()
        numbers.reverse()

        print(numbers)

    else:
        raise Exception('Seed lens must be equal')

elif choice == '3':
    amount = int(input('Ingrese la cantidad que desea obtener: '))


    seed = int(input('Ingrese la semilla: '))

    constant = int(input('Ingrese la constante: '))

    if len(str(constant)) > 3 and len(str(seed)) > 3:
        if len(str(constant)) == len(str(seed)):
            numbers = []

            for i in range(amount):
                mult_result = str(constant * seed)

                eliminated_nums = len(mult_result) - len(str(seed))
                while eliminated_nums % 2 != 0:
                    mult_result = mult_result[::-1]
                    mult_result += '0'
                    mult_result = mult_result[::-1]
                    eliminated_nums = len(mult_result) - len(str(seed))

                edges = eliminated_nums / 2

                n_seed = ''
                for e, n in enumerate(mult_result):

                    if e == len(str(seed)) + edges:
                        break

                    if e < edges:
                        continue

                    n_seed += n

                constant = seed
                seed = int(n_seed)

                numbers.append(float(f"0.{seed}"))

            numbers.reverse()
            numbers.pop()
            numbers.reverse()

            print(numbers)

        else:
            raise Exception('Seed lens must be equal')

