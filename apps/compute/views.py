import time

from rest_framework.response import Response
from rest_framework.views import APIView

from fibonacci_rust import fibonacci_rust


class ComputeFibonacci(APIView):

    supported_languages = ["Python", "Rust"]

    def fibonacci(self, number: int) -> int:
        if number <= 0:
            raise ValueError("The number should be a non-null positive integer")
        if number in range(1, 3):
            return 1
        return self.fibonacci(number - 1) + self.fibonacci(number - 2)

    def get(self, request, *args, **kwargs):

        number = int(self.request.query_params.get("number"))
        context = []
        for lang in self.supported_languages:
            match lang:
                case "Python":
                    start_time = time.time()
                    result = self.fibonacci(number)
                    end_time = time.time()
                case "Rust":
                    start_time = time.time()
                    result = fibonacci_rust.fibonacci(number)
                    end_time = time.time()

            context.append(
                dict(
                    language=lang,
                    result=result,
                    computing_time=f"{end_time - start_time:0.4f} s",
                )
            )

        return Response(context)


compute_fibonacci = ComputeFibonacci.as_view()
