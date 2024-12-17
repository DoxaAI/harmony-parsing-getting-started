import pathlib
import re
import sys
from random import choice
from typing import Any, Generator, Literal, Tuple

directory = pathlib.Path(__file__).parent
sys.path.insert(0, str(directory.resolve()))


from competition import BaseEvaluator

#################################################################################
#                                                                               #
#   This file gets run when you submit your work for evaluation on the DOXA     #
#   AI platform. Modify the predict() method to implement your own strategy!    #
#                                                                               #
#################################################################################


class Evaluator(BaseEvaluator):
    def predict(
        self, text: str
    ) -> Generator[Tuple[int, int, Literal["Q", "A"]], Any, None]:
        """Write all the code you need to generate predictions for the test set here!

        You only need to classify sections of text as being questions ("Q") or potential
        question answers ("A"). We will assume everything else does not match. See the
        competition page for more on how your submission is evaluated.

        Args:
            text (str): This is the plain-text test set

        Yields:
            Tuple[int, int, Literal["Q", "A"]: A starting index (inclusive), an ending index (exclusive)
                                                and a categorisation ("Q" or "A").
        """

        # Implement your own strategy here!

        regex = re.compile(r"\w+", re.UNICODE)
        for match in regex.finditer(text):
            category = choice(["Q", "A", "O"])
            if category in ("Q", "A"):
                a, b = match.span()
                yield (a, b, category)


if __name__ == "__main__":
    Evaluator().run()
