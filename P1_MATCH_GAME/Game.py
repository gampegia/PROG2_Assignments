stack = 13 # Lediglich zu Testzweck






def get_bot_choice(stack_size: int):
    """
    get_bot_choice gives back the best possible bot choice

    :param stack_size: Value of current Match Stack
    :return: Bot choice which needs to be subtracted form the stack
    """
    diff_target = (stack_size - 1) % 4
    if diff_target == 0:
        return 1
    else:
        return diff_target

