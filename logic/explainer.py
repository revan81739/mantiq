from logic.ast import Identifier, Not, Binary

class Explainer:
    def explain_argument(self, argument, valid, counterexample):
        lines=[]

        lines.append("Reasoning analysis:")
        lines.append("---------------------")
        lines.append("")
        if valid:
            lines.append(
                "The argument is valid because no possible "
                "assignment of truth values makes all premises "
                "true while making the conclusion false"
            )
            lines.append("")
            lines.append(
                "This means that if the premises are true, "
                "the conclusion must also be true"
            )
        else:
            lines.append(
                "The argument is invalid because a counterexample "
                "was found."
            )
            lines.append("")
            lines.append(
                "A counterexample is a situation where all "
                "premises are true but the conclusion is false"
            )
            lines.append("")
            lines.append("The counterexample is:")

            for variable, value in counterexample.items():
                lines.append(f"{variable}={value}")
                lines.append("")
                lines.append(
                    "Since this situation is possible, the premises "
                    "do not guarantee the truth of the conclusion"
                )

        return "\n".join(lines)
                

