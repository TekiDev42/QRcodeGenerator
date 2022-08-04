def validate_input(user_inputs: list[tuple[str, str]]) -> bool:
    for user_input in user_inputs:
        if user_input[0] == 'url':
            if len(user_input[1]) < 0:
                print("Erreur 'url': Veuillez saisir une URL")
                return False

        if user_input[0] == 'size_input':
            if len(user_input[1]) > 0 and not user_input[1].isnumeric():
                print("Erreur 'taille': Veuillez saisir une valeur numérique")
                return False

            if user_input[1].isnumeric():
                size = int(user_input[1])

                if size < 0 or size > 100:
                    print("Erreur 'taille': Veuillez saisir une valuer comprise en 1 et 100")
                    return False
    return True
