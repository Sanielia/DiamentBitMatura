import queue


class TooFewNumbersError(Exception):
    pass


class TooMuchNumbersError(Exception):
    pass


class ExpressionNotEndedWithEqualSign(Exception):
    pass


def eval_rnp(expression: str) -> float:
    stack = queue.LifoQueue()
    char_list = expression.split(" ")

    for char in char_list:
        if char not in ["+", "-", "/", "*", "="]:
            try:
                stack.put(float(char))
                continue
            except ValueError:
                raise ValueError(f"Cannot evaluate the expression with operator {char}")

        if char == "=":
            if stack.qsize() > 1:
                raise TooMuchNumbersError("More numbers than needed to evaluate the expression provided.")

            return stack.get(block=False)

        try:
            num2 = stack.get(block=False)
            num1 = stack.get(block=False)
        except queue.Empty:
            raise TooFewNumbersError("Less numbers than needed to evaluate the expression provided")

        result = 0

        # Można użyć po prostu eval(num1 + char + num2), tho jest to prawdopodobnie wolniejsze
        match char:
            case "+":
                result = num1 + num2
            case "-":
                result = num1 - num2
            case "*":
                result = num1 * num2
            case "/":
                # Nie handluje ZeroDivisionError, ponieważ zwracanie po prostu None nic nie mówi użytkownikowi,
                # zwracanie random stringa jest bardzo złą praktyką. Nie jest to Rust, żeby używać Result enuma,
                # nie ma po co tworzyć nowego exception będącego 1:1 ZeroDivisionErrorem, więc handleowanie errora
                # jest po stronie użytkownika.
                result = num1 / num2

        stack.put(result)

    raise ExpressionNotEndedWithEqualSign



if __name__ == "__main__":
    print(eval_rnp("0.5 0.5 + 3 4 + * 7 * 1 + 5 5 + / ="))
    try:
        eval_rnp("3 + + =")
    except TooFewNumbersError:
        print("yay")
    try:
        eval_rnp("3asd4+")
    except ValueError:
        print("yay2")
    try:
        eval_rnp("3 3 3 + =")
    except TooMuchNumbersError:
        print("yay3")
    try:
        eval_rnp("3 3 +")
    except ExpressionNotEndedWithEqualSign:
        print("yay4")